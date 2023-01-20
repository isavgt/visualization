from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px

class Map(html.Div):
    def __init__(self, name, long, lat, df):
        self.html_id = name.lower().replace(" ", "-")
        #For screenshotting purposes for interim report, we only show the first 300 rows. 
        self.df = df
        self.long = long
        self.lat = lat

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H4("Airbnbs in New York City", style = {'color':'black','font-size':'30px'}),
                dcc.Dropdown(['No color scale', 'Danger Score','Price'], 'No color scale', id='select-heatmap'),
                dcc.Graph(id=self.html_id, figure=self.update(self.df, 'No color scale'), style={'height': '70vh'}),
                html.H6("The danger score is calculated by the amount of arrests in the direct surroundings of the airbnb", style={'color':'black','font-size':'14px'}),
                html.H6("Note: Danger score of the grey markers is unknown.", style={'color':'black','font-size':'14px'})
            ],
        )

    def update(self, selected_df, heatmap):
        if heatmap == 'Danger Score':
            self.fig = go.Figure(px.scatter_mapbox(selected_df,color_continuous_scale=px.colors.sequential.Plasma,lat="latitude",
                lon="longitude", color="Danger Score",hover_data={'latitude':False, 'longitude':False,'price':True,'review_scores_value':True,'neighbourhood':True}, custom_data=['id']))
        
        elif heatmap == 'No color scale':
            self.fig = go.Figure(px.scatter_mapbox(selected_df,color_discrete_sequence=["#3567AC"],lat="latitude",
            hover_data={'latitude':False, 'longitude':False,'price':True,'review_scores_value':True,'neighbourhood':True},lon="longitude", custom_data=['id']))

        elif heatmap == 'Price':
            self.fig = go.Figure(px.scatter_mapbox(selected_df,color_continuous_scale=px.colors.sequential.Plasma,lat="latitude",
            hover_data={'latitude':False, 'longitude':False,'price':True,'review_scores_value':True,'neighbourhood':True},lon="longitude", color="price", custom_data=['id']))
        
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
     
        dcc.Graph(id=self.html_id, figure = self.fig)
        return self.fig