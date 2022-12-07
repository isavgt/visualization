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
                html.H2(name),
                html.Div(children=
                    [html.H5(children= 'Selected airbnb:', id = 'your_price'), 
                    html.H5(children='Price per night for clicked airbnb: ')
                    ], id = "info_selected"
                ),
                dcc.Graph(id=self.html_id, figure = self.update(None))
            ],
        )

    #create figure
    def update(self, clicked_id):
        if clicked_id != None:  
            neighbourhood = self.df.loc[self.df['id']==clicked_id[0]]['neighbourhood'].to_string(index=False)
            neighbourhood_data = self.df.loc[self.df['neighbourhood']==neighbourhood]
            self.fig= go.Figure(data=[go.Histogram(x=neighbourhood_data['price'])])
            dcc.Graph(id=self.html_id, figure = self.fig)
        
        else:
            self.fig = go.Figure(data=[go.Histogram(x=self.df['price'])])

        # update axis titles
        self.fig.update_layout(
            xaxis_title='price per night',
            yaxis_title='frequency',
        )
        
        return self.fig