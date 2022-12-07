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
                html.H6(name),
                dcc.Graph(id=self.html_id)
            ],
        )

    #create figure
    def update(self):
        self.fig = go.Figure(data=[go.Histogram(x=self.df['price'])])

        # update axis titles
        self.fig.update_layout(
            xaxis_title='price',
            yaxis_title='frequency',
        )

        return self.fig
