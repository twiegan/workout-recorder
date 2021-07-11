import dash_core_components as dcc
import dash_html_components as html

workout_inputs = html.Div(className="workout-inputs",
                          children=[dcc.Dropdown(id='day-dropdown',
                                                 options=[
                                                     {'label': 'Monday', 'value': 'Monday'},
                                                     {'label': 'Tuesday', 'value': 'Tuesday'},
                                                     {'label': 'Wednesday', 'value': 'Wednesday'},
                                                     {'label': 'Thursday', 'value': 'Thursday'},
                                                     {'label': 'Friday', 'value': 'Friday'},
                                                     {'label': 'Saturday', 'value': 'Saturday'},
                                                     {'label': 'Sunday', 'value': 'Sunday'},
                                                 ],
                                                 placeholder="workout day"),
                                    dcc.Input(id="time-input", type="text", placeholder="workout time"),
                                    dcc.Dropdown(id='focus-dropdown',
                                                 options=[
                                                     {'label': 'Chest', 'value': 'Chest'},
                                                     {'label': 'Triceps', 'value': 'Triceps'},
                                                     {'label': 'Biceps', 'value': 'Biceps'},
                                                     {'label': 'Back', 'value': 'Back'},
                                                     {'label': 'Legs', 'value': 'Legs'},
                                                     {'label': 'Core', 'value': 'Core'},
                                                     {'label': 'Cardio', 'value': 'Cardio'}
                                                 ],
                                                 placeholder="workout focus area",
                                                 multi=True),
                                    html.Button('submit', id='submit-button', value='submit')])

status_message = html.Div(className="status-message", children=[html.Plaintext(id="status-text", children="No communication")])


def define_layout():
    return \
        html.Div(children=[
            workout_inputs,
            status_message
        ])
