from dash import dcc, html
import plotly.graph_objects as go

# This file enholds the plot on the right of the page. It shows a histogram of the price
class Plots(html.Div):
    def __init__(self, name, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df

        # Creates a graph when a plot has been created
        super().__init__(
            className="graph_card",
            # This contains a title, information on the selected airbnb and a histogram with the prices in the area.
            children=[
                html.H4("Prices in the same neighbourhood", style = {'color':'black','font-size':'25px'}),
                html.Div(children=
                    [html.H5(children= 'Selected airbnb:', style={'display':'block','font-size':'14px'}), 
                    html.H5(children='Price per night: €', style={'display':'block','font-size':'14px'}),
                    html.H5(children='Neighbourhood:', style={'display':'block','font-size':'14px'})
                    ], id = "info_selected"
                ),
                dcc.Graph(id=self.html_id, figure = self.update(None),style={'height': '70vh'})
            ],
        )

    #create figure
    def update(self, clicked_id):
        # If an airbnb has been clicked, show histogram of prices of airbnbs in the same neighbourhood
        if clicked_id != None:
            print('id', clicked_id[0])
            print('0',self.df.loc[self.df['index']==clicked_id[0]]['price'])
            print('1',len(self.df.loc[self.df['index']==clicked_id[0]]['price']))
            neighbourhood = self.df.loc[self.df['index']==clicked_id[0]]['neighbourhood'].to_string(index=False)
            price = self.df.loc[self.df['index']==clicked_id[0]]['price'].values[0]
            neighbourhood_data = self.df.loc[self.df['neighbourhood']==neighbourhood]
            self.fig= go.Figure(data=[go.Histogram(x=neighbourhood_data['price'], marker_color='#3567AC')])
            self.fig.add_vline(x=price, line_dash = 'dash', line_color = '#FFAC1E')
            dcc.Graph(id=self.html_id, figure = self.fig)
        # If no airbnb has been clicked, show histogram of prices of all airbnbs
        else:
            self.fig = go.Figure(data=[go.Histogram(x=self.df['price'], marker_color='#3567AC')] )

        # Update axis titles
        self.fig.update_layout(
            xaxis_title='price per night',
            yaxis_title='frequency',
            margin=dict(l=20, r=20, t=20, b=20)
        )
        
        
        return self.fig