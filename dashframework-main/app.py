from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.scatterplot import Scatterplot
from jbi100_app.views.map import Map
from jbi100_app.views.plots import Plots
#from jbi100_app.data import read_data

from dash import html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

if __name__ == '__main__':
    # Create data
    df = px.data.iris()
    df_airbnb = pd.read_csv('dashframework-main\cleaned_airbnb_data_test.csv')
    df_airbnb_old = pd.read_csv('Airbnb_Open_Data.csv')

    df_airbnb.info()
    print(type(df_airbnb_old.lat[1]))
    print(type(df_airbnb.lat[1]))

    print(df_airbnb.info())

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
                children=make_menu_layout()
            ),

            # Right column
            html.Div(
                id="right-column",
                className="nine columns",
                children = dcc.Graph(figure=map.update())
            ),
        ],
    )
    print()
    @app.callback(
        Output(plots.html_id, "figure"), [
        Input(map.html_id, 'selectedData')
    ])
    def update_plots(selected_data):
        print(selected_data)
        print(type(selected_data))
        return plots.update(selected_data)


    app.run_server(debug=False, dev_tools_ui=False)