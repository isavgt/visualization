from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px

class Map(html.Div):
    def __init__(self, name, long, lat, df):
        self.html_id = name.lower().replace(" ", "-")
        #For screenshotting purposes for interim report, we only show the first 300 rows. 
        self.df = df[:300]
        self.long = long
        self.lat = lat

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id, figure=self.update(self.df), style={'height': '40vh'}),
            ],
        )

    def update(self, df_selected):
        self.fig = px.scatter_mapbox(df_selected, lat="lat", lon="long", custom_data=['id'])
        self.fig.update_layout(
            mapbox={
                "style": "open-street-map",
                "zoom": 8,
                "center" : go.layout.mapbox.Center(lat = 40.730610, lon= -73.935242)
            },
            margin={"l": 0, "r": 0, "t": 0, "r": 0}, 
            autosize=True,
            hovermode='closest'
        )
        return self.fig
