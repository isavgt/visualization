from dash import dcc, html
from ..config import color_list1, color_list2


def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H3("CompAirbnb", style={"color": "black",'font-size':'54px'}),
            html.H4(
                id="intro",
                children="You can use this to find the perfect Airbnb for your trip to New York City."
            ),
        ],
    )


def generate_control_card(df):
    """

    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[
            html.Label("Select price per night"),
            dcc.RangeSlider(
                id = 'select-price',
                min = min(df.loc[:,'price']), 
                max = max(df.loc[:,'price']),
                tooltip={"placement": "bottom", "always_visible": True},
                value=[min(df.loc[:,'price']), max(df.loc[:,'price'])],
                ),
                
            html.Br(),
            html.Label("Select review score"),
            dcc.RangeSlider(
                id="select-review-score",
                min = 1,
                max = 5,
                step = 1,
                value = [1,5]),
            html.Br(),
            html.Label("Select number of people"),
            dcc.RangeSlider(
                id="select-accommodates",
                min = min(df.loc[:,'accommodates']),
                max = max(df.loc[:,'accommodates']),
                step = 1,
                value = [min(df.loc[:,'accommodates']),max(df.loc[:,'accommodates'])],
            ),
            html.Br(), 
            html.Label("Select the room type"),
            dcc.Dropdown(
                id = "select-roomtype",
                options = ['Private room','Entire home/apt','Hotel room','Shared room'],
                value = ["Private room", "Entire home/apt", "Hotel room", "Shared room"],
                multi = True,
            ), 
            html.Br(), 
            html.Label("Other filters"),
            dcc.Checklist(
                id = "select-other-filters", 
                value = [],
                options = ["Superhost", "Private Bathroom"]
            )
        ], style={"textAlign": "float-left"}
    )


def make_menu_layout(df):
    return [generate_description_card(), generate_control_card(df)]
