import dash
from dash.dependencies import Input, Output, State

from app_layout import define_layout
from driver import *

app = dash.Dash(__name__)
app.layout = define_layout()


@app.callback(
    Output("status-text", "children"),
    [Input("submit-button", "n_clicks")],
    state=[State('day-dropdown', 'value'),
           State('time-input', 'value'),
           State('focus-dropdown', 'value')])
def render_content(n_clicks, day, time, focus):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    if send_to_db(day, time, focus):
        return "Communication Successful"
    return "Communication Unsuccessful"


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)
