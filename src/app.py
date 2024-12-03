import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Initialize Dash app with Cerulean theme
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.CYBORG]
)
app.title = "Embedded Dashboards"
server = app.server

# Profile Section
profile_section = html.Div([
    html.Div([
        html.Img(
            src="https://yajitersoo.github.io/jsonapi/Profile%20picture.jpg",
            style={
                'width': '120px',
                'height': '120px',
                'borderRadius': '50%',
                'marginBottom': '10px'
            }
        ),
        html.H4("Yaji Tersoo", style={'marginBottom': '5px', 'color': 'black'}),
        html.H6("Data Analyst | Information Management Specialist | Data Scientist", style={'marginTop': '0', 'color': 'black'}),
        html.P(
            "Welcome! I'm passionate about data-driven solutions and actionable insights. "
            "Below, you'll find live dashboards showcasing my works.",
            style={'padding': '10px', 'textAlign': 'center', 'color': 'black'}
        ),
    ], style={'textAlign': 'center'})
], style={'marginBottom': '20px', 'textAlign': 'center', 'width': '994px', 'margin': '0 auto'})

# Dashboard definitions
dashboard_definitions = {
    "/": {
        "title": "Nigeria Joint Market Monitoring Initiative (JMMI) Dashboard",
        "description": "This interactive dashboard provides insights into market monitoring initiatives in Nigeria.",
        "iframe_src": "https://app.powerbi.com/view?r=eyJrIjoiODc2ZTc5NTktYzJhNC00NGIyLTgwYjUtZmUyZjU2MWE1ZGQ2IiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9",
    },
    "/service-mapping": {
        "title": "Service Mapping Flood MMC Revised Dashboard",
        "description": "This interactive dashboard provides insights into flood mapping services.",
        "iframe_src": "https://app.powerbi.com/view?r=eyJrIjoiYzI1NmMzZDItMzI3ZS00OGNjLTg5MDAtZWQ5NWRkN2VjOGUyIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9",
    },
    "/gain-nigeria": {
        "title": "Gain Nigeria Country Programme Performance Dashboard",
        "description": "Description for dashboard 3.",
        "iframe_src": "https://app.powerbi.com/view?r=eyJrIjoiMTU1NDY1MzUtYTIyNi00YzA5LWJjZTUtN2Y2YzJlZDA2NWIwIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9",
    },
    "/ingo-matrix": {
        "title": "INGOs Project Matrix Dashboard",
        "description": "Description for dashboard 4.",
        "iframe_src": "https://app.powerbi.com/view?r=eyJrIjoiODk5NDkwNTctZmFjZi00N2E3LThmOWItMTU1MTNhODFlOGMwIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9&pageName=ReportSection4a1f4a02068a4a203203",
    }
}

# Function to generate dashboard layout dynamically
def generate_dashboard_layout(title, description, iframe_src):
    return html.Div([
        html.H5(title, style={'textAlign': 'center', 'color': 'black'}),
        html.P(description, style={'textAlign': 'center', 'color': 'black'}),
        html.Div([
            html.Iframe(
                src=iframe_src,
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ], style={'textAlign': 'center'}),
    ], style={
        'width': '994px', 'margin': '0 auto', 'padding': '20px',
        'backgroundColor': 'white', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'
    })

# Main Layout with Tabs
app.layout = html.Div([
    profile_section,
    dcc.Location(id='url', refresh=False),
    dbc.Card(
        dbc.Tabs(
            [
                dbc.Tab(label='Dashboards', tab_id='dashboards', style={'color': 'black'}),
                dbc.Tab(label='Maps', tab_id='pdfs', style={'color': 'black'}),
            ],
            id='tabs',
            active_tab='dashboards'
        ),
        style={'marginBottom': '20px'}
    ),
    # Dashboard Dropdown
    html.Div([
        dcc.Dropdown(
            id='dashboard-dropdown',
            options=[
                {'label': dashboard['title'], 'value': key} for key, dashboard in dashboard_definitions.items()
            ],
            value='/',
            style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
        ),
    ], id="dashboard-dropdown-container", style={'textAlign': 'center'}),
    # PDF Dropdown (hidden by default)
    html.Div([
        dcc.Dropdown(
            id='pdf-dropdown',
            options=[
                {'label': "3Ws Partner's Operational Presence Map Northeast, Nigeria", 'value': "https://drive.google.com/file/d/1uIxMMlLHR9R8HWk9sulmSJkJJEFFBhuc/preview"},
                {'label': 'Humanitarian Partners Presence in Sokoto State', 'value': "https://drive.google.com/file/d/1VT09guEpfFOhuK4FPgqxfHTjf0V0huNJ/preview"},
                {'label': 'Humanitarian Partners Presence in Zamfara State', 'value': "https://drive.google.com/file/d/1gRLwH9nei35KgMR0sVOhNh7EZQjqvYpI/preview"},
                {'label': 'Wards and LGAs in Jigawa State', 'value': "https://drive.google.com/file/d/1-lu5zsH3vt54gZ6UzEDn_9AnuomMkmBr/preview"},
            ],
            value="https://drive.google.com/file/d/1uIxMMlLHR9R8HWk9sulmSJkJJEFFBhuc/preview",
            style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
        ),
        html.Iframe(
            id='pdf-iframe',
            src="https://drive.google.com/file/d/1uIxMMlLHR9R8HWk9sulmSJkJJEFFBhuc/preview",
            style={'width': '100%', 'height': '800px', 'border': 'none'}
        )
    ], id="pdf-dropdown-container", style={'textAlign': 'center', 'display': 'none'}),  # Hidden by default
    html.Div(id='tab-content', style={'marginTop': '20px'})
], style={'backgroundColor': '#f4f4f4', 'padding': '20px', 'width': '1194px', 'margin': '0 auto', 'color': 'black'})

# Callbacks
@app.callback(
    Output('tab-content', 'children'),
    [Input('tabs', 'active_tab'),
     Input('dashboard-dropdown', 'value')]
)
def render_tab_content(active_tab, selected_dashboard):
    if active_tab == 'dashboards':
        dashboard = dashboard_definitions.get(selected_dashboard, dashboard_definitions['/'])
        return generate_dashboard_layout(dashboard['title'], dashboard['description'], dashboard['iframe_src'])

@app.callback(
    Output('pdf-iframe', 'src'),
    Input('pdf-dropdown', 'value')
)
def update_pdf_src(selected_pdf):
    return selected_pdf

@app.callback(
    [Output('pdf-dropdown-container', 'style'),
     Output('dashboard-dropdown-container', 'style')],
    [Input('tabs', 'active_tab')]
)
def update_dropdown_visibility(active_tab):
    if active_tab == 'pdfs':
        return {'display': 'block'}, {'display': 'none'}
    else:
        return {'display': 'none'}, {'display': 'block'}

if __name__ == '__main__':
    app.run_server(debug=True)
