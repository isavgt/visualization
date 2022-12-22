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
                html.H4("Histogram of prices in the same neighborhood", style = {'color':'black'}),
                html.Div(children=
                    [#html.H5(children= 'Selected airbnb:', style={'width': '49%'}),
                     #makes a table. first row of the table
                     html.Table(
                         [html.Tr([html.Td(html.H5(children= 'Selected airbnb:', style={'width': '49%'}))] + [html.Td('t')])] +
                     #second row of the table
                        [html.Tr([html.Td(html.H5(children='Price per night for selected Airbnb in dollars:', style={'width': '49%'}))] + [html.Td('t')])] +
                     #third row
                        [html.Tr([html.Td(html.H5(children='Neighborhood:', style={'width': '49%'}))] + [html.Td('t')])],
                         style = {'width': '80%'})
                    #html.H5(children='Price per night for clicked airbnb : €', style={'width': '49%'})
                    ], id = "info_selected"
                ),
                dcc.Graph(id=self.html_id, figure = self.update(None))
            ],
        )

    #create figure
    def update(self, clicked_id):
        if clicked_id != None:
            neighbourhood = self.df.loc[self.df['id']==clicked_id[0]]['neighbourhood'].to_string(index=False)
            print(self.df.loc[self.df['id']==clicked_id[0]]['price'])
            price = self.df.loc[self.df['id']==clicked_id[0]]['price'].values[0]
            neighbourhood_data = self.df.loc[self.df['neighbourhood']==neighbourhood]
            self.fig= go.Figure(data=[go.Histogram(x=neighbourhood_data['price'])])
            print(clicked_id)
            print(type(price))
            self.fig.add_vline(x=price, line_dash = 'dash', line_color = 'firebrick')
            dcc.Graph(id=self.html_id, figure = self.fig)
        
        else:
            self.fig = go.Figure(data=[go.Histogram(x=self.df['price'])])

        # update axis titles
        self.fig.update_layout(
            xaxis_title='price per night',
            yaxis_title='frequency',
        )
        
        
        return self.fig