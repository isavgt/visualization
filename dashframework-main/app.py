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

if __name__ == '__main__':
    # Create data
    df_airbnb  = pd.read_csv('cleaned_airbnb_data.csv',
        dtype={
            'id': np.int32,
            'name': np.character,
            'host_id': np.int32,
            'host_name': np.character,
            'neighboorhoud_group': np.character,
            'neighboorhooud': np.character,
            'latitude': np.float16,
            'longitude': np.float16,
            'room_type': np.character,
            'price': np.int32,
            'minimum_nights': np.int32,
            'number_of_reviews': np.int32,
            'last_review': np.datetime64,
            'reviews_per_month': np.int32,
            'calculated_host_listing_count': np.int32,
            'availability_365': np.int32
        }
    )
    df_airbnb = df_airbnb[:300]

    # Instantiate custom views
    map = Map("Airbnb", "long", "lat", df_airbnb)
    plots = Plots("plots", df_airbnb)

    app.layout = html.Div(
        id="app-container",
        children=[
            # Left column
            html.Div(
                id="left-column",
                className="three columns",
                children=make_menu_layout(df_airbnb)
            ),

            # Right column
            html.Div(
                id="right-column",
                className="nine columns",
                children = [
                    dcc.Graph(id= 'map', figure = map.update()),
                    dcc.Graph(id='plots', figure = plots.update())
                ]
                ),
            ],
        )

    print(min(df_airbnb.loc[:,'price']))

    # @app.callback(
    #     Output(plots.html_id, "figure"), [
    #     Input(map.html_id, 'selectedData')
    # ])
    # def update_plots(selected_data):
    #     return map.update()


    app.run_server(debug=False, dev_tools_ui=False)