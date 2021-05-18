import dash
from dash.dependencies import Input, Output

from webapp_layout import define_layout

app = dash.Dash(__name__)
app.layout = define_layout()

if __name__ == '__main__':
    app.run_server(debug=True)
