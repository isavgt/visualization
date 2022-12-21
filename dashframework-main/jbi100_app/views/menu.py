from dash import dcc, html
from ..config import color_list1, color_list2


def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H3("CompAirbnb", style={"color": "#1EAEDB"}),
            html.H4(
                id="intro",
                children="You can use this to select the perfect Airbnb for your trip to New York."
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
                value=[min(df.loc[:,'price']), max(df.loc[:,'price'])]),
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
                value = [min(df.loc[:,'accommodates']),max(df.loc[:,'accommodates'])]
            )
        ], style={"textAlign": "float-left"}
    )


def make_menu_layout(df):
    return [generate_description_card(), generate_control_card(df)]
