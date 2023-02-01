from jbi100_app.main import app
from jbi100_app.views.menu import make_menu_layout
from jbi100_app.views.map import Map
from jbi100_app.views.plots import Plots

from dash import html
import pandas as pd
from dash.dependencies import Input, Output

if __name__ == '__main__':
    # Import data
    df_airbnb  = pd.read_csv('airbnb_with_crimes_cleaned.csv')
    # Create the two objects: map with airbnbs & plots
    map = Map("airbnbs", "longitude", "latitude", df_airbnb)
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

            # Middle column
            html.Div(
                id="middle-column",
                className="five columns",
                children = map
                ),

            # Right column
            html.Div(
                id="right-column",
                className="four columns",
                children = plots
                ),
            ],
        )

    # Callback for showing the information about the clicked airbnb to the user
    @app.callback(
        Output("info_selected", "children"), 
        Input(map.html_id, 'clickData')
    )
    def update_text(selected_data):
        # Get the specific values of the clicked airbnb
        if selected_data != None:
            selected_index = selected_data['points'][0]['customdata']
            selected_row = df_airbnb.loc[df_airbnb['index']==selected_index[0]]
            selected_name = selected_row['name'].to_string(index=False)
            selected_price = selected_row['price'].to_string(index=False)
            selected_neighbourhood = selected_row['neighbourhood'].to_string(index=False)
            # Return the text as a child of "info_selected (in plots)"
            return [html.H5(children= f'Selected airbnb: {selected_name}', style={ 'display':'block','font-size':'14px'}), 
                    html.H5(children=f'Price per night: €{selected_price}', style={ 'display':'block','font-size':'14px'}),
                    html.H5(children=f'Neighbourhood: {selected_neighbourhood}', style={'display':'block','font-size':'14px'})]

    # Callback for plotting the plots for a clicked airbnb
    @app.callback(
        Output("plots", "figure"), 
        Input(map.html_id, "clickData")
    )
    def update_plots(selected_data):
        # Check if there is click data
        if selected_data != None:
            # Update the plot for the specific point
            selected_index = selected_data['points'][0]['customdata']
            fig = plots.update(selected_index)

        else: 
            fig = plots.update(None)
        return fig

    # Callback for updating the scattermapbox according to the filter values & the dropdown menu for selecting the type of map
    @app.callback(
        Output("airbnbs", "figure"), 
        Input("select-price", "value"),
        Input("select-review-score", "value"),
        Input("select-accommodates", "value"),
        Input("select-roomtype", "value"), 
        Input("select-other-filters", "value"),
        Input("select-color_scale","value")
    )
    def update_map(price_range, review_range, accommodate_range, room_type, other_filters,color_scale):
        # Update the dataframe of airbnbs after filtering for all attributes
        df_selected_airbnbs = df_airbnb[df_airbnb["price"].between(price_range[0], price_range[1])]
        df_selected_airbnbs = df_selected_airbnbs[df_selected_airbnbs["review_scores_value"].between(review_range[0], review_range[1])]
        df_selected_airbnbs = df_selected_airbnbs[df_selected_airbnbs["accommodates"].between(accommodate_range[0], accommodate_range[1])]
        df_selected_airbnbs = df_selected_airbnbs[df_selected_airbnbs["room_type"].isin(room_type)]
        if 'Superhost' in other_filters: 
            df_selected_airbnbs = df_selected_airbnbs[df_selected_airbnbs["host_is_superhost"]==True]
        if 'Private Bathroom' in other_filters: 
            df_selected_airbnbs = df_selected_airbnbs[df_selected_airbnbs["Private/Shared"]=="Private"]
        
        # Update the map according to the new dataframe & type of map 
        fig = map.update(df_selected_airbnbs, color_scale)
        return fig

    df_selected_test = df_airbnb[(df_airbnb['index'] == 639199)]

    print(df_selected_test)

    app.run_server(debug=False, dev_tools_ui=False)
