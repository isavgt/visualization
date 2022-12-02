from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
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
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self):
        self.fig = px.scatter_mapbox(self.df, lat="lat", lon="long", hover_name="NAME", hover_data=[],
                        color_discrete_sequence=["fuchsia"], zoom=3)
        self.fig.update_layout(mapbox_style="open-street-map")
        self.fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        self.fig.update_traces(cluster=dict(enabled=True, size = 10, step = 10))

        return self.fig
