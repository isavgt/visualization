from dash import dcc, html
import plotly.graph_objects as go


class Plots(html.Div):
    def __init__(self, name, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H4("Prices in the same neighbourhood", style = {'color':'black','font-size':'25px'}),
                html.Div(children=
                    [html.H5(children= 'Selected airbnb:', style={'display':'block','font-size':'14px'}), 
                    html.H5(children='Price per night: €', style={'display':'block','font-size':'14px'})
                    ], id = "info_selected"
                ),
                dcc.Graph(id=self.html_id, figure = self.update(None),style={'height': '70vh'})
            ],
        )

    #create figure
    def update(self, clicked_id):
        if clicked_id != None:
            neighbourhood = self.df.loc[self.df['id']==clicked_id[0]]['neighbourhood'].to_string(index=False)
            print(self.df.loc[self.df['id']==clicked_id[0]]['price'])
            price = self.df.loc[self.df['id']==clicked_id[0]]['price'].values[0]
            neighbourhood_data = self.df.loc[self.df['neighbourhood']==neighbourhood]
            self.fig= go.Figure(data=[go.Histogram(x=neighbourhood_data['price'], marker_color='#3567AC')])
            print(clicked_id)
            print(type(price))
            self.fig.add_vline(x=price, line_dash = 'dash', line_color = '#FFAC1E')
            dcc.Graph(id=self.html_id, figure = self.fig)
        
        else:
            self.fig = go.Figure(data=[go.Histogram(x=self.df['price'], marker_color='#3567AC')] )

        # update axis titles
        self.fig.update_layout(
            xaxis_title='price per night',
            yaxis_title='frequency',
            margin=dict(l=20, r=20, t=20, b=20)
        )
        
        
        return self.fig