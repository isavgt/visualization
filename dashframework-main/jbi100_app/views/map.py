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
                dcc.Graph(id=self.html_id, figure=self.update())
            ],
        )

    def update(self):
        self.fig = px.scatter_mapbox(self.df, lat="lat", lon="long").update_layout(
            mapbox={
                "style": "open-street-map",
                "zoom": 6,
            },
            margin={"l": 0, "r": 0, "t": 0, "r": 0}
        ).update_traces(selected={"marker":{"color":"fuchsia"}})
        #self.fig = go.Figure(go.Scattermapbox(lat=self.df.lat, lon=self.df.long, mode = 'markers', hovertemplate='<b>%{text}</b>', showlegend=False, text=self.df.NAME,marker = go.scattermapbox.Marker(size = 10)))
        #self.fig.update_layout(mapbox_style="open-street-map", hovermode = 'closest', clickmode = 'event+select', mapbox = dict(zoom = 9, style = "open-street-map", center = go.layout.mapbox.Center(lat = 40.730610, lon =  -73.935242)))
        #self.fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        #self.fig.update_traces(cluster=dict(enabled=True, size = 10, step = 10))

        return self.fig
