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
        html.H6("Data Analyst | Information Management Specialist | Data Scientist",
                style={'marginTop': '0', 'color': 'black'}),
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
                    {'label': "Nigeria JMMI Dashboard",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiODc2ZTc5NTktYzJhNC00NGIyLTgwYjUtZmUyZjU2MWE1ZGQ2IiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "GBV AoR Response Activities Northeast Nigeria 2024",
                     'value': "https://experience.arcgis.com/experience/4166a5bbdd804b0f8a106952999eb7cb/page/Response-Activity-Dashboard/"},
                    {'label': "GBV AoR Reference Maps Northeast Nigeria 2024",
                     'value': "https://experience.arcgis.com/experience/4166a5bbdd804b0f8a106952999eb7cb/page/Reference-Maps/"},
                    {'label': "Service Mapping Flood MMC",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiYzI1NmMzZDItMzI3ZS00OGNjLTg5MDAtZWQ5NWRkN2VjOGUyIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "GBV AoR Response Activities Northeast Nigeria 2023",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiNGRjYjc2ZTEtMGU5MS00N2M2LWFhOTgtMzU4MWI2MDkzNzc1IiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9&pageName=ReportSection"},
                    {'label': "IRC MSNA Dashboard",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiMmExMDIwMWMtOGM0ZS00ZjBmLTkzOTgtY2ZlZjhjZTYzZTQxIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "Northeast Nigeria CVA Dashboard",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiNjRiNTBhYzgtNzIwMS00NDM1LThlMzQtM2Q0YWM1MTQ1YjA2IiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "Protection Monitoring Interactive Dashboard: Northeast Nigeria",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiNjM0YWE5MTUtNmI0ZC00Nzg4LWEyNjUtYWE4Y2ZkZjc4ZTdkIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "GBV AoR - Financial Analysis Dashboard (GPC)",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiZTQ4MjFmNjItMGI3Yy00NDRkLThiMzQtZjBlZjZhOTE3MzNiIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "INGO Forum Power BI Interactive Dashboard",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiNGYzMzVkOTEtN2IwNC00NmU2LWI0YjktODdiZWNhNDZmZWQ1IiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9&pageName=ReportSectiond4052e84529b0d4b048b"},
                    {'label': "Child Protection Sub-Sector Response Monitoring Dashboard",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiYjk5YTIxZTItZGIyZS00NmM2LTgxNDItZGQ4MTFiY2Y3NTkwIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9&pageName=ReportSection5aef375c1153ec70bac1"},

                    {'label': "Market Price Index Interactive Dashboard",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiZGFjYmYzMDUtZWViNC00NDBkLWE4NTEtOGU0NjlmMzU4YjFiIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9&pageName=ReportSection2e5116d592f50302d0cc"},
                    {'label': "Early Recovery and Livelihoods Sector 5Ws Response Dashboard",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiYmYzNDM3NjMtOTI4Zi00ZjBmLTljMzItNWMwMjc5NWQzNDdkIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9&pageName=ReportSection9017b20e3098cc470503"},
                    {'label': "Rate of Service Utilization for Nutrition Sector ",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiMTA4NGVhOTctYmFmZS00ZGMyLThkNDgtYTJiZjU2MGI3MjZmIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},

                    {'label': "Rate of Service Utilization for GBV Sub-Sector",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiYjAxMzM3NDUtOGNhMC00Y2E0LWJlMzMtOTAxZjcyMDEwZGNlIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9&pageName=ReportSectionf73010df95854087e8e5"},
                    {'label': "MDM Knowledge, Attitude and Practices Survey",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiNjViY2UxNmYtMjA5ZS00MTJkLTliZmMtZWZiMmIzNWFlYjc4IiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "Nigeria International Non-Government Organisations (INGOs) Project Matrix – 2021",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiODk5NDkwNTctZmFjZi00N2E3LThmOWItMTU1MTNhODFlOGMwIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9&pageName=ReportSection4a1f4a02068a4a203203"},
                    {'label': "Nigeria International Non-Government Organisations (INGOs) Project Matrix – 2021",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiODk5NDkwNTctZmFjZi00N2E3LThmOWItMTU1MTNhODFlOGMwIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9&pageName=ReportSection4a1f4a02068a4a203203"},
                    {
                        'label': "2023 Status - Anticipatory Actions GBV Sub Sector, Northeast Nigeria (Floods, Malnutrition and Cholera) Contingency Planning Dashboard",
                        'value': "https://app.powerbi.com/view?r=eyJrIjoiZDgyMTgwZTAtZDE5Ni00YWVlLTlmNGYtNzk0YjhmZjk4MmViIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "DTM Nigeria Site Assessment Dashboard Northeast Nigeria",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiNDlkNmYxM2YtNmI3YS00ZmRkLThkN2UtMjRiYzc1MmY5ZmVkIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "Biofortification Beneficiary Enrolment Activity Dashboard",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiM2Q0OTJkZTYtZDE3ZC00ZWZhLWFmYzctMzNlMGJjMTJkMjgzIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "Gain Nigeria Country Programme Performance Dashboard",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiMTU1NDY1MzUtYTIyNi00YzA5LWJjZTUtN2Y2YzJlZDA2NWIwIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "Weekly Consultation Dashboard",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiNGY4YzY5Y2YtOWNmOS00MGQ5LWEzYWEtNDg2OGNlOGNhNjM4IiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "GBViE in Emergencies Capacity Mapping and Development 2023-2025",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiOWZmMWFhZDYtZTBkOS00OWNlLThhNWEtOWU3ZWJlYTg0OWE2IiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "Referral Pathway Dashboard 2024",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiYjQ3ZWRjMjctYzAxMC00MWMyLTkwYTYtYWIzZWViNzczNDRiIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {
                        'label': "GBV AoR Service Mapping 2024 (Ngala, Mungonu, Mafa, Madagali, Michika, Damboa,Geidam,Bade)",
                        'value': "https://app.powerbi.com/view?r=eyJrIjoiNzlhMGZmZDktOGI5Mi00YTM4LWI4NjAtMjM5NWEwMTRjODlkIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},
                    {'label': "GBV AoR: Flood Response Service Mapping in MMC and Jere, Borno State",
                     'value': "https://app.powerbi.com/view?r=eyJrIjoiYzI1NmMzZDItMzI3ZS00OGNjLTg5MDAtZWQ5NWRkN2VjOGUyIiwidCI6ImY2ZjcwZjFiLTJhMmQtNGYzMC04NTJhLTY0YjhjZTBjMTlkNyIsImMiOjF9"},

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
                    {'label': "Nigeria Political Region Map",
                     'value': "https://drive.google.com/file/d/1rUbsFTM5qo9byfLgP0NlMg1JSzly7ab7/preview"},
                    {'label': "Demasak Imagery",
                     'value': "https://drive.google.com/file/d/1EOWxKSP8WxyBqtw1dt_ls4_c6q-uNwCN/preview"},
                    {'label': "NiMet Map 2024",
                     'value': "https://drive.google.com/file/d/1639_ogX_fe7AHALuEJx41SGZjpZLxi2P/preview"},
                    {'label': "Nigeria Administrative Map",
                     'value': "https://drive.google.com/file/d/1BO7AHV7X6BZDCCEchKwVO8jOr809k_hK/preview"},
                    {'label': "BAY States Humanitarian Access Map",
                     'value': "https://drive.google.com/file/d/1s8aOgpz2pBmCzRFbFjCYRYCXkrzbcYJR/preview"},
                    {'label': "BAY States IDP camp sites",
                     'value': "https://drive.google.com/file/d/12QskUyQNpz5Ch9sIPJdtrLGj-uwzA-o1/preview"},
                    {'label': "Rapid Response Mechanism (Borno State)",
                     'value': "https://drive.google.com/file/d/10mri8eT4wqodkDdcys363Iygeg27as3a/preview"},
                    {'label': "Rapid Response Mechanism (Adamawa State)",
                     'value': "https://drive.google.com/file/d/19xfpKbZwgvOVkVyYQ2q6Q9TECJDEP1Qe/preview"},
                    {'label': "Rapid Response Mechanism (Yobe State)",
                     'value': "https://drive.google.com/file/d/1LzqewE4YQaqySDqe13MdzVtjVqQNYHHG/preview"},
                    {'label': "IDPs Relocation Areas (Borno State)",
                     'value': "https://drive.google.com/file/d/10YQYkbKGZcx7TlA8hAVb2L6zUMi-1QjD/preview"},
                    {'label': "3Ws Map Northeast Nigeria",
                     'value': "https://drive.google.com/file/d/1uIxMMlLHR9R8HWk9sulmSJkJJEFFBhuc/preview"},
                    {'label': "Humanitarian Presence Sokoto",
                     'value': "https://drive.google.com/file/d/1VT09guEpfFOhuK4FPgqxfHTjf0V0huNJ/preview"},
                    {'label': "Humanitarian Presence Zamfara",
                     'value': "https://drive.google.com/file/d/1gRLwH9nei35KgMR0sVOhNh7EZQjqvYpI/preview"},
                    {'label': "Jigawa Wards and LGAs",
                     'value': "https://drive.google.com/file/d/1-lu5zsH3vt54gZ6UzEDn_9AnuomMkmBr/preview"},
                    {'label': "IRC Borno State OPM",
                     'value': "https://drive.google.com/file/d/1wyscmWMEpiQ2rEkVMOqAeOIbnQ231q-H/preview"},
                    {'label': "IRC Adamawa State OPM",
                     'value': "https://drive.google.com/file/d/1Jk5PlQDuyAz6F_7Ypi2FRq_v1nZ0lM5T/preview"},
                    {'label': "IRC Katsina State OPM",
                     'value': "https://drive.google.com/file/d/13KCtFbEP4W943w8sok3Z-ACMOBcEFv3P/preview"},
                    {'label': "GBV Flood Response Map",
                     'value': "https://drive.google.com/file/d/1h5XOujDa-DM24ikYu-Cyfh5mwSTZ8Jxe/preview"},
                    {'label': "BAY States IDP camp sites",
                     'value': "https://drive.google.com/file/d/12QskUyQNpz5Ch9sIPJdtrLGj-uwzA-o1/preview"},
                    {'label': "Borno State Administrative Map",
                     'value': "https://drive.google.com/file/d/1T2f9sn_zw4QrMNQAFlV6C4g6xxSCvJdg/preview"},
                    {'label': "Borno State Administrative Map",
                     'value': "https://drive.google.com/file/d/1T2f9sn_zw4QrMNQAFlV6C4g6xxSCvJdg/preview"},
                    {'label': "Humanitarian Partners Presence in Katsina State",
                     'value': "https://drive.google.com/file/d/1yNd3_31r5u9AUSPYBqerVDmEQrjHbKS2/preview"},
                    {'label': "Humanitarian Partners Presence in Sokoto State",
                     'value': "https://drive.google.com/file/d/1UizHeI4cDJE4sgNIJhjPTPGg1R_n3-oV/preview"},
                    {'label': "Humanitarian Partners Presence in Zamfara State",
                     'value': "https://drive.google.com/file/d/19c2A4tq-d85zqi8sj97Gm-TebnvpgO1-/preview"},
                    {'label': "IRC Flood Map",
                     'value': "https://drive.google.com/file/d/1t-wBhE3AX6zGj0URKInH_YL8odML4IOa/preview"},
                    {'label': "Towns and Wards in Katsina State",
                     'value': "https://drive.google.com/file/d/1hM1Y__PswUtIa0LwyoATiZtIxkVe38n0/preview"},
                    {'label': "Project Location Security Incidents Mapping, Borno State",
                     'value': "https://drive.google.com/file/d/1Jjzo2Q-s1LPpWlZgIvDmr0anQms5Jpcx/preview"},
                    {'label': "Major Highways, Towns & Airports in Nigeria",
                     'value': "https://drive.google.com/file/d/1neV-uv_IB7p1QiKxNcxn7G_c_w6X38Ty/preview"},
                    {'label': "Map-WGSS-&-OSC",
                     'value': "https://drive.google.com/file/d/1hFUhGDbVtZeksaxeJQFquFBsOKMIPizP/preview"},
                    {'label': "Flood Impacted LGAs in Adamawa, Anambra, Bayelsa and Benue States",
                     'value': "https://drive.google.com/file/d/100U67liET42S44_XILN-VuvRNqT4SXsw/preview"},
                    {'label': "Humanitarian Access Map, October 2023 - Adamawa, Borno & Yobe States",
                     'value': "https://drive.google.com/file/d/1ifuFte3xiw9nq3RNvp--rqCmai7Cjw9K/preview"},
                    {'label': "NS IPC Malnutrition Project and Warehoses Locations",
                     'value': "https://drive.google.com/file/d/13N_KgtbyMA0ykfyo3CmTp8KEqM1HYNKL/preview"},
                    {'label': "ZOA Operational Presence Map Northeast Nigeria",
                     'value': "https://drive.google.com/file/d/1kW9FzK24uVwhesqFmpWxYjzDvEPtFGhB/preview"},
                    {'label': "Government-Led Relocations and Returns - Conflict, Food Security & Access Borno State",
                     'value': "https://drive.google.com/file/d/1vDIvelNXSnPSqu81ruhE800aHh_SMq0Q/preview"},
                ],
                value="https://drive.google.com/file/d/1Jjzo2Q-s1LPpWlZgIvDmr0anQms5Jpcx/preview",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='maps-iframe',
                src="https://drive.google.com/file/d/1Jjzo2Q-s1LPpWlZgIvDmr0anQms5Jpcx/preview",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])
    elif active_tab == 'reports':
        return html.Div([
            dcc.Dropdown(
                id='reports-dropdown',
                options=[
                    {'label': "GBV Mid-Year Report 2023",
                     'value': "https://drive.google.com/file/d/1Fg7tb6BPGCfJ-DUsvrTRuHubWHHs2_C2/preview"},
                    {'label': "GBV Mid-Year Report 2024",
                     'value': "https://drive.google.com/file/d/1mId3DmWYbBO0fXBRaMZ3QH8dPnMOevk4/preview"},
                    {'label': "Cash Working Group Workshop",
                     'value': "https://drive.google.com/file/d/1MdjPiTAfLjN58TrN2znWQ4UqQ1owPr2Z/preview?usp=sharing"},
                    {'label': "16DoA ANNUAL REPORT  2023",
                     'value': "https://drive.google.com/file/d/1tScc0ditcVQYWaGEHpo-LrethlNEmLKK/preview"},
                    {'label': "GBV Annual Report 2023",
                     'value': "https://drive.google.com/file/d/11r8oDc19VH0ALLbt6rWHEoPWU-QETQ4B/preview"},
                    {'label': "GBV AoR Coordination Workshop Report 2024",
                     'value': "https://drive.google.com/file/d/1vgD7LiAlfdwWAAE8Vx2Xe0yNTmEouWDc/preview"},
                    {'label': "Standard Operating Procedures for GBV Interventions in Humanitarian Settings",
                     'value': "https://drive.google.com/file/d/1Y85nxNtb4EfNpvf7KbM21dVYMUtbhLs9/preview"},
                    {'label': "Guidance Note WGSS",
                     'value': "https://drive.google.com/file/d/1S2c4QM9z7Sbak6OqJl2I2f9WXPTJhz66/preview"},
                    {'label': "Guidance Note PWD",
                     'value': "https://drive.google.com/file/d/1KimGgqmuWAZHTQH3NheMepSEOJcJ5jRz/preview"},
                    {'label': "Guidance Note IPV",
                     'value': "https://drive.google.com/file/d/1aDBR-2_6E1Ft075ixzwp8XXSme_CSV_8/preview"},
                    {'label': "GBV Key Messages for Floods",
                     'value': "https://drive.google.com/file/d/1EzVr5Nn3rVpfbNKigcj1oVVWGsWbZ4UZ/preview"},
                ],
                value="https://drive.google.com/file/d/1Fg7tb6BPGCfJ-DUsvrTRuHubWHHs2_C2/preview",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='reports-iframe',
                src="https://drive.google.com/file/d/1Fg7tb6BPGCfJ-DUsvrTRuHubWHHs2_C2/preview",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])
    elif active_tab == 'static_dashboards':
        return html.Div([
            dcc.Dropdown(
                id='static-dashboards-dropdown',
                options=[
                    {'label': "IDPS 2014 -2020 Northeast Nigeria",
                     'value': "https://drive.google.com/file/d/1I7_pJ11_r8SHWxk_Y5oSwlpa8A5DfSyS/preview"},
                    {'label': "Cash and Voucher Activities & Stakeholders Mapping",
                     'value': "https://drive.google.com/file/d/1vACQEwEr3kaGEIWi9_c7b50UxYVKO8At/preview"},
                    {'label': "DTM Round 35 Site Assessment Dashboard",
                     'value': "https://drive.google.com/file/d/1PgXrRBbtlHFMWrbwMU0nfbI1poiOACLl/preview"},
                    {'label': "First Quarter Dashboard GBV AoR Response Activity Northeast 2024",
                     'value': "https://drive.google.com/file/d/19dXeFBWiTm4FKwQghyB2j0oDFBWvYDvP/preview"},
                    {'label': "DARYA Youth Voices",
                     'value': "https://drive.google.com/file/d/1JwWoEKeEf7-5q4NeJVv4Awksx1l3EG6l/preview"},
                    {'label': "Project Matrix Dashboard NIF 2021",
                     'value': "https://drive.google.com/file/d/1NuY9X3Rj14F-ADKs-0lQB2jpCBSPWrV9/preview"}
                ],
                value="https://drive.google.com/file/d/19dXeFBWiTm4FKwQghyB2j0oDFBWvYDvP/preview",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='static-dashboards-iframe',
                src="https://drive.google.com/file/d/19dXeFBWiTm4FKwQghyB2j0oDFBWvYDvP/preview",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])
    elif active_tab == 'infographics':
        return html.Div([
            dcc.Dropdown(
                id='infographics-dropdown',
                options=[
                    {'label': "16DoA1",
                     'value': "https://drive.google.com/file/d/1ldezmdWXPwuyaIO1q8pQHMka9bKCULij/preview"},
                    {'label': "16DoA2",
                     'value': "https://drive.google.com/file/d/1chSyVpZ3K7k_xVBHh9fP7E86hJjZPg3s/preview"},
                    {'label': "16DoA3",
                     'value': "https://drive.google.com/file/d/12PYwuNG0v4AVKpAFzpLstonyiYTQEnWT/preview"},
                    {'label': "Malaria",
                     'value': "https://drive.google.com/file/d/1mK6WEkpzAowcF6AxYPq6uOQltIcZjnS4/preview"},
                    {'label': "Prevention & Response to Gender-Based Violence",
                     'value': "https://drive.google.com/file/d/11WnA5DNKtUx5M1NLA8XAV5qZ1IxmP-S1/preview"},
                    {'label': "Election Flyer1",
                     'value': "https://drive.google.com/file/d/16CnwRZfacXxuequk0YDv56udK5JCl3c2/preview"},
                    {'label': "Election Flyer2",
                     'value': "https://drive.google.com/file/d/1zo9V6d8oe1KP14OZefrECeKYfCd3Cusk/preview"},
                    {'label': "Election Flyer3",
                     'value': "https://drive.google.com/file/d/1zo9V6d8oe1KP14OZefrECeKYfCd3Cusk/preview"},
                    {'label': "Election Flyer4",
                     'value': "https://drive.google.com/file/d/1B79zmMioNnzNeLxWTqogpLqBXdg68BPl/preview"},
                    {'label': "Election Flyer5",
                     'value': "https://drive.google.com/file/d/1G8KZOezuKgi_3hoTISgY4eDcxDVB1xFi/preview"},
                    {'label': "Election Flyer6",
                     'value': "https://drive.google.com/file/d/1_gcTIK9iCbc6X--f4Hp4ngIJvvbagw3k/preview"},
                    {'label': "Children in Crisis",
                     'value': "https://drive.google.com/file/d/1MvsZcKNsGCL-5SdUCDCoexFceUHULgIQ/preview"},
                    {'label': "Minimum Services for Preventing Maternal Morbidity and Mortality",
                     'value': "https://drive.google.com/file/d/1XqLxLnl0_5qUvMxnFv6P4qKmpHCPgPy4/preview"},
                    {'label': "No Shame in Bleeding during Menstruation",
                     'value': "https://drive.google.com/file/d/1V09zl0JGHavxFt59YdAaqoDMTyD6Nqfj/preview"},

                ],
                value="https://drive.google.com/file/d/1mK6WEkpzAowcF6AxYPq6uOQltIcZjnS4/preview",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='infographics-iframe',
                src="https://drive.google.com/file/d/1mK6WEkpzAowcF6AxYPq6uOQltIcZjnS4/preview",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])
    elif active_tab == 'presentations':
        return html.Div([
            dcc.Dropdown(
                id='presentations-dropdown',
                options=[
                    {'label': "GBV AoR: Responding to Violence through Information Management",
                     'value': "https://drive.google.com/file/d/1q8ad-Ugg8HXbQi-aioTNnbQEyxQHXw7-/preview"},
                    {'label': "GIS Mapping Using ArcGIS Pro",
                     'value': "https://drive.google.com/file/d/1s3po69guW_TutdrRrbIp1DBfFA9yOC1G/preview"},
                    {'label': "Introduction to Basic Data Processing/Visualization Tools - Power BI",
                     'value': "https://drive.google.com/file/d/1vYwS6h7-gDpcT7IjS5ShZKYk5Ft8Fesn/preview"},
                    {'label': "iMMAP Nigeria Presentation HIAU P5",
                     'value': "https://drive.google.com/file/d/1S_Vp3-asUEs4FsUaixRrTIM_dls7vJdm/preview"}
                ],
                value="https://drive.google.com/file/d/1q8ad-Ugg8HXbQi-aioTNnbQEyxQHXw7-/preview",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='presentations-iframe',
                src="https://drive.google.com/file/d/1q8ad-Ugg8HXbQi-aioTNnbQEyxQHXw7-/preview",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])
    elif active_tab == 'videos':
        return html.Div([
            dcc.Dropdown(
                id='videos-dropdown',
                options=[
                    {'label': "End of Year Technical Review Workshop 2023",
                     'value': "https://drive.google.com/file/d/1i0fkkCo-0nVZJ3N17Q4WIeOeqrniwGQZ/preview"},
                    {'label': "Farewell wishes",
                     'value': "https://drive.google.com/file/d/18hrklwliDL8tzSzlDeKBVHUycZpOQ0am/preview"},
                    {'label': "iMMAP Nigeria SDSP Demo",
                     'value': "https://drive.google.com/file/d/1d90s5FcJUuGkwEDpXAUpsaa501jdghdC/preview"},
                    {
                        'label': "Geographical Coverage of Planned JMMI Data Collection LGAs in Northeast Nigeria - Borno State",
                        'value': "https://drive.google.com/file/d/1abs1Zn0T0u3ko3BSJ0qJODhqwYhcE_3i/preview"},
                ],
                value="https://drive.google.com/file/d/1i0fkkCo-0nVZJ3N17Q4WIeOeqrniwGQZ/preview",
                style={'width': '50%', 'margin': '0 auto', 'marginBottom': '20px'}
            ),
            html.Iframe(
                id='videos-iframe',
                src="https://drive.google.com/file/d/1i0fkkCo-0nVZJ3N17Q4WIeOeqrniwGQZ/preview",
                style={'width': '100%', 'height': '800px', 'border': 'none'}
            )
        ])


# # Update content based on active tab
# @app.callback(
#     Output('tab-content', 'children'),
#     [Input('tabs', 'active_tab')]
# )
# def display_tab_content(active_tab):
#     return render_tab_content(active_tab)
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Callback to Update Tab Content
@app.callback(
    Output('tab-content', 'children'),
    [Input('tabs', 'active_tab')]
)
def update_tab_content(active_tab):
    return render_tab_content(active_tab)


# Callback to Update Iframes
@app.callback(
    Output('dashboard-iframe', 'src'),
    [Input('dashboard-dropdown', 'value')]
)
def update_dashboard(selected_value):
    return selected_value


# Callback to Update Iframes
@app.callback(
    Output('maps-iframe', 'src'),
    [Input('maps-dropdown', 'value')]
)
def update_dashboard(selected_value):
    return selected_value


# Callback to Update Iframes
@app.callback(
    Output('reports-iframe', 'src'),
    [Input('reports-dropdown', 'value')]
)
def update_dashboard(selected_value):
    return selected_value


# Callback to Update Iframes
@app.callback(
    Output('static-dashboards-iframe', 'src'),
    [Input('static-dashboards-dropdown', 'value')]
)
def update_dashboard(selected_value):
    return selected_value


# Callback to Update Iframes
@app.callback(
    Output('infographics-iframe', 'src'),
    [Input('infographics-dropdown', 'value')]
)
def update_dashboard(selected_value):
    return selected_value


# Callback to Update Iframes
@app.callback(
    Output('presentations-iframe', 'src'),
    [Input('presentations-dropdown', 'value')]
)
def update_dashboard(selected_value):
    return selected_value


# Callback to Update Iframes
@app.callback(
    Output('videos-iframe', 'src'),
    [Input('videos-dropdown', 'value')]
)
def update_dashboard(selected_value):
    return selected_value


if __name__ == '__main__':
    app.run_server(debug=True, port=7070)
