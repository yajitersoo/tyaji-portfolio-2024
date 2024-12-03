import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Initialize Dash app
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

# Layout with Tabs
app.layout = html.Div([
    profile_section,
    dcc.Location(id='url', refresh=False),
    dbc.Card(
        dbc.Tabs(
            [
                dbc.Tab(label='Dashboards', tab_id='dashboards', style={'color': 'black'}),
                dbc.Tab(label='Maps', tab_id='maps', style={'color': 'black'}),
                dbc.Tab(label='Reports', tab_id='reports', style={'color': 'black'}),
                dbc.Tab(label='Static Dashboards', tab_id='static_dashboards', style={'color': 'black'}),
                dbc.Tab(label='Infographics', tab_id='infographics', style={'color': 'black'}),
                dbc.Tab(label='Presentations', tab_id='presentations', style={'color': 'black'}),
                dbc.Tab(label='Videos', tab_id='videos', style={'color': 'black'})
            ],
            id='tabs',
            active_tab='dashboards'
        ),
        style={'marginBottom': '20px'}
    ),
    html.Div(id='tab-content', style={'marginTop': '20px'})  # Content dynamically rendered by the tab
], style={'backgroundColor': '#f4f4f4', 'padding': '20px', 'width': '1194px', 'margin': '0 auto', 'color': 'black'})

# Tab Content Render Function
def render_tab_content(active_tab):
    if active_tab == 'dashboards':
        return html.Div([
            dcc.Dropdown(
                id='dashboard-dropdown',
                options=[
                    {'label': "Nigeria JMMI Dashboard", 'value': "https://app.powerbi.com/view?r=eyJrIjoiODc2ZTc5NTktYzJhNC00NGIyLTgwYjUtZmUyZjU2MWE1ZGQ2IiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "Service Mapping Flood MMC", 'value': "https://app.powerbi.com/view?r=eyJrIjoiYzI1NmMzZDItMzI3ZS00OGNjLTg5MDAtZWQ5NWRkN2VjOGUyIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"}
                ],
                value="https://app.powerbi.com/view?r=eyJrIjoiODc2ZTc5NTktYzJhNC00NGIyLTgwYjUtZmUyZjU2MWE1ZGQ2IiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='dashboard-iframe',
                src="https://app.powerbi.com/view?r=eyJrIjoiODc2ZTc5NTktYzJhNC00NGIyLTgwYjUtZmUyZjU2MWE1ZGQ2IiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])
    elif active_tab == 'maps':
        return html.Div([
            dcc.Dropdown(
                id='maps-dropdown',
                options=[
                    {'label': "3Ws Map Northeast Nigeria", 'value': "https://drive.google.com/file/d/1uIxMMlLHR9R8HWk9sulmSJkJJEFFBhuc/preview"},
                    {'label': "Humanitarian Presence Sokoto", 'value': "https://drive.google.com/file/d/1VT09guEpfFOhuK4FPgqxfHTjf0V0huNJ/preview"},
                    {'label': "Humanitarian Presence Zamfara", 'value': "https://drive.google.com/file/d/1gRLwH9nei35KgMR0sVOhNh7EZQjqvYpI/preview"},
                    {'label': "Jigawa Wards and LGAs", 'value': "https://drive.google.com/file/d/1-lu5zsH3vt54gZ6UzEDn_9AnuomMkmBr/preview"}
                ],
                value="https://drive.google.com/file/d/1uIxMMlLHR9R8HWk9sulmSJkJJEFFBhuc/preview",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='maps-iframe',
                src="https://drive.google.com/file/d/1uIxMMlLHR9R8HWk9sulmSJkJJEFFBhuc/preview",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])
    elif active_tab == 'reports':
        return html.Div([
            dcc.Dropdown(
                id='reports-dropdown',
                options=[
                    {'label': "GBV Annual Report 2023", 'value': "https://drive.google.com/file/d/11r8oDc19VH0ALLbt6rWHEoPWU-QETQ4B/view?usp=sharing"},
                    {'label': "Cash Working Group Workshop", 'value': "https://drive.google.com/file/d/1MdjPiTAfLjN58TrN2znWQ4UqQ1owPr2Z/view?usp=sharing"},
                    {'label': "GBV AoR Coordination Workshop 2024", 'value': "https://drive.google.com/file/d/1vgD7LiAlfdwWAAE8Vx2Xe0yNTmEouWDc/view?usp=sharing"},
                    {'label': "GBV SOPs in Humanitarian Settings", 'value': "https://docs.google.com/document/d/1znGcqnmSJaakEhD9rKQ_qx5dsUPYnvlE/edit?usp=sharing"}
                ],
                value="https://drive.google.com/file/d/11r8oDc19VH0ALLbt6rWHEoPWU-QETQ4B/view?usp=sharing",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='reports-iframe',
                src="https://drive.google.com/file/d/11r8oDc19VH0ALLbt6rWHEoPWU-QETQ4B/view?usp=sharing",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])
    elif active_tab == 'static_dashboards':
        return html.Div([
            dcc.Dropdown(
                id='static-dashboards-dropdown',
                options=[
                    {'label': "Static Dashboard 1", 'value': "https://drive.google.com/file/d/1MdjPiTAfLjN58TrN2znWQ4UqQ1owPr2Z/view?usp=sharing"},
                    {'label': "Static Dashboard 2", 'value': "https://drive.google.com/file/d/1vACQEwEr3kaGEIWi9_c7b50UxYVKO8At/view?usp=sharing"},
                    {'label': "Static Dashboard 3", 'value': "https://drive.google.com/file/d/1NuY9X3Rj14F-ADKs-0lQB2jpCBSPWrV9/view?usp=sharing"},
                    {'label': "Static Dashboard 4", 'value': "https://drive.google.com/file/d/1lK0GRxIgQG2vEhnlNN_hyRaLtKPzGc-V/view?usp=sharing"}
                ],
                value="https://drive.google.com/file/d/1MdjPiTAfLjN58TrN2znWQ4UqQ1owPr2Z/view?usp=sharing",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='static-dashboards-iframe',
                src="https://drive.google.com/file/d/1MdjPiTAfLjN58TrN2znWQ4UqQ1owPr2Z/view?usp=sharing",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])
    elif active_tab == 'infographics':
        return html.Div([
            dcc.Dropdown(
                id='infographics-dropdown',
                options=[
                    {'label': "Infographic 1", 'value': "https://drive.google.com/file/d/1ldezmdWXPwuyaIO1q8pQHMka9bKCULij/preview"},
                    {'label': "Infographic 2", 'value': "https://drive.google.com/file/d/1r2WrLgAto9-lZDgjGh9DZ_gQOzoT1I1P/preview"}
                ],
                value="https://drive.google.com/file/d/1ldezmdWXPwuyaIO1q8pQHMka9bKCULij/preview",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='infographics-iframe',
                src="https://drive.google.com/file/d/1ldezmdWXPwuyaIO1q8pQHMka9bKCULij/preview",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])
    elif active_tab == 'presentations':
        return html.Div([
            dcc.Dropdown(
                id='presentations-dropdown',
                options=[
                    {'label': "Presentation 1", 'value': "https://drive.google.com/file/d/1FCykbEBcl07lYgU4F3W2zqij55jJJFqg/preview"},
                    {'label': "Presentation 2", 'value': "https://drive.google.com/file/d/1x5m0lgAsfp7ErxWp_bPpyetH4Ws9wbjE/preview"}
                ],
                value="https://drive.google.com/file/d/1FCykbEBcl07lYgU4F3W2zqij55jJJFqg/preview",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='presentations-iframe',
                src="https://drive.google.com/file/d/1FCykbEBcl07lYgU4F3W2zqij55jJJFqg/preview",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])
    elif active_tab == 'videos':
        return html.Div([
            dcc.Dropdown(
                id='videos-dropdown',
                options=[
                    {'label': "Video 1", 'value': "https://drive.google.com/file/d/18hrklwliDL8tzSzlDeKBVHUycZpOQ0am/preview"},
                    {'label': "Video 2", 'value': "https://www.youtube.com/embed/ZaU-R3T3hXs"}
                ],
                value="https://drive.google.com/file/d/18hrklwliDL8tzSzlDeKBVHUycZpOQ0am/preview",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='videos-iframe',
                src="https://drive.google.com/file/d/18hrklwliDL8tzSzlDeKBVHUycZpOQ0am/preview",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])

# Update content based on active tab
@app.callback(
    Output('tab-content', 'children'),
    [Input('tabs', 'active_tab')]
)
def display_tab_content(active_tab):
    return render_tab_content(active_tab)

if __name__ == '__main__':
    app.run_server(debug=True)
