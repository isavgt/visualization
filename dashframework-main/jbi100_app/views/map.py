from dash import dcc, html
import plotly.graph_objects as go
import plotly.express as px

class Map(html.Div):
    def __init__(self, name, long, lat, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df
        self.long = long
        self.lat = lat

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id, figure=self.update(self.df)),
            ],
        )

    def update(self, df_selected):
        self.fig = px.scatter_mapbox(df_selected, lat="lat", lon="long", custom_data=['id'])
        self.fig.update_layout(
            mapbox={
                "style": "open-street-map",
                "zoom": 6,
            },
            margin={"l": 0, "r": 0, "t": 0, "r": 0}
        )
        return self.fig
