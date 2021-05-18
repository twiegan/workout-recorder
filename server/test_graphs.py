import plotly.graph_objects as go


def create_example_graph():
    labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
    values = [4500, 2500, 1053, 500]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)],
                    layout=go.Layout(width=500, height=500))
    return fig
