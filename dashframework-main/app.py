from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.scatterplot import Scatterplot
from jbi100_app.views.map import Map
from jbi100_app.views.plots import Plots
#from jbi100_app.data import read_data

from dash import html, dcc
import numpy as np
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

from dash import Dash, dcc, html, Input, Output, ctx
import pandas as pd
import plotly.express as px

df_airbnb = pd.read_csv("cleaned_airbnb_data.csv")

app = Dash(__name__)
app.layout = html.Div(
    [
        html.Header(
            "Geographic Distribution Airbnbs in New York",
            style={"font-size": "30px", "textAlign": "center"},
        ),
        html.Div("Maximum price", style={"font-size": "20px"}),
        "Dollars",
        dcc.Input(id="max_price", value=100, type="number", step=1),
        dcc.Graph(id="map"),
    ],
    style={"margin": 10, "maxWidth": 800},
)


@app.callback(
    Output("map", "figure"),
    Input("max_price", "value"),
)
def sync_input(meter, feet):
    fig = px.scatter_geo(
        data_frame=df_airbnb.loc[df_airbnb["price"] <= "max_price"],
        lat="lat",
        lon="long",
        size="price",
        hover_name="NAME",
        projection="natural earth",
    )

app.run_server(debug=False, dev_tools_ui=False)