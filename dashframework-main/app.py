from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.scatterplot import Scatterplot
from jbi100_app.views.map import Map
from jbi100_app.views.plots import Plots
#from jbi100_app.data import read_data
#test

from dash import html, dcc
import numpy as np
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go

if __name__ == '__main__':
    # Import data
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

    # Create the two objects: map with airbnbs & plots (for now only price)
    map = Map("airbnbs", "long", "lat", df_airbnb)
    plots = Plots("plots", df_airbnb)

    # Create the layout of the page
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
                    map,
                    plots
                ]
                ),
            ],
        )

    # Callback for showing the clicked data (name & price) to user
    @app.callback(
        Output("info_selected", "children"), 
        #Output(plots.html_id, "children"),
        Input(map.html_id, 'clickData')
    )
    def update_text(selected_data):
        # Get the specific values of the clicked airbnb
        selected_id = selected_data['points'][0]['customdata']
        selected_row = df_airbnb.loc[df_airbnb['id']==selected_id[0]]
        selected_name = selected_row['NAME'].to_string(index=False)
        selected_price = selected_row['price'].to_string(index=False)
        # Return the text as a child of "info_selected (in plots)"
        return [html.H5(children= f'Selected airbnb: {selected_name}', style={'width': '49%', 'display':'inline-block'}), 
                html.H5(children=f'Price per night for clicked airbnb : € {selected_price}', style={'width': '49%', 'display':'inline-block'})]

    # Callback for plotting the plots for a clicked airbnb
    @app.callback(
        Output("plots", "figure"), 
        Input(map.html_id, "clickData")
    )
    def update_plots(selected_data):
        # Check if there is click data
        if selected_data != None:
            # Update the plot for the specific point
            selected_id = selected_data['points'][0]['customdata']
            fig = plots.update(selected_id)

        else: 
            fig = plots.update(None)
        return fig
    app.run_server(debug=False, dev_tools_ui=False)

