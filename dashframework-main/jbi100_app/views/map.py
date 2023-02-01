from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px

# This file enholds the map on the page. It has a function update, to reload the map with different filters or map types

class Map(html.Div):
    def __init__(self, name, long, lat, df):
        # Define variables
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.long = long
        self.lat = lat

        # Create an html div when a map is created. 
        super().__init__(
            className="graph_card",
            # This div includes a title, dropdown, the mapbox graph and notes on the mapbox
            children=[
                html.H4("Airbnbs in New York City", style = {'color':'black','font-size':'30px'}),
                dcc.Dropdown(['No color scale', 'Danger Score','Price'], 'No color scale', id='select-color_scale'),
                dcc.Graph(id=self.html_id, figure=self.update(self.df, 'No color scale'), style={'height': '70vh'}),
                html.H6("The danger score is calculated by the amount of arrests in the direct surroundings of the airbnb", style={'color':'black','font-size':'14px'}),
                html.H6("Note: Danger score of the grey markers is unknown.", style={'color':'black','font-size':'14px'})
            ],
        )

    # Function that updates the map with given preferences for which airbnbs to show & what attributes to show on the map using the markers
    def update(self, selected_df, color_scale):

        # Create the mapbox with markers indicating danger score
        if color_scale == 'Danger Score':
            self.fig = go.Figure(px.scatter_mapbox(selected_df,color_continuous_scale=px.colors.sequential.Plasma,lat="latitude",
                lon="longitude", color="Danger Score",hover_data={'latitude':False, 'longitude':False,'price':True,'review_scores_value':True,'neighbourhood':True}, custom_data=['index']))
        
        # Create the mapbox without a color scale for extra attributes
        elif color_scale == 'No color scale':
            self.fig = go.Figure(px.scatter_mapbox(selected_df,color_discrete_sequence=["#3567AC"],lat="latitude",
            hover_data={'latitude':False, 'longitude':False,'price':True,'review_scores_value':True,'neighbourhood':True, 'index': True},lon="longitude", custom_data=['index']))

        # Create the mapbox with markers indicating price
        elif color_scale == 'Price':
            self.fig = go.Figure(px.scatter_mapbox(selected_df,color_continuous_scale=px.colors.sequential.Plasma,lat="latitude",
            hover_data={'latitude':False, 'longitude':False,'price':True,'review_scores_value':True,'neighbourhood':True},lon="longitude", color="price", custom_data=['index']))
        
        # Updat the layout of the map
        self.fig.update_layout(
            mapbox={
                "style": "carto-positron",
                "zoom": 8,
                "center" : go.layout.mapbox.Center(lat = 40.730610, lon= -73.935242)
            },
            margin=dict(l=20, r=20, t=20, b=20), 
            autosize=True,
            hovermode='closest'
            
        )    
        # Create the graph and return it
        dcc.Graph(id=self.html_id, figure = self.fig)
        return self.fig