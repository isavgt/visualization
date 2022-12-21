from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.scatterplot import Scatterplot
from jbi100_app.views.map import Map

from dash import html, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

if __name__ == '__main__':
    # Create data
    df = px.data.iris()
    df_airbnb = pd.read_csv('Airbnb_Open_Data.csv')

    # Instantiate custom views
    map = Map("Airbnb", "long", "lat", df_airbnb)

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


    app.run_server(debug=False, dev_tools_ui=False)