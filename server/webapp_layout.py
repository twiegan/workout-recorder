import dash_core_components as dcc
import dash_html_components as html
import test_graphs

example_graph = test_graphs.create_example_graph()


def define_layout():
    return \
        html.Div(className="grid-layout",
                 children=[dcc.Graph(className="graph1", figure=example_graph),
                           dcc.Graph(className="graph2", figure=example_graph),
                           dcc.Graph(className="graph3", figure=example_graph),
                           dcc.Graph(className="graph4", figure=example_graph)])
