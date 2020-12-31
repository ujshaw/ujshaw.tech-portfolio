import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from webpage.components.stacks import Stacks
from webpage.components.portfolio import Portfolio
from webpage.components.footer import Footer


def Info():
    about = html.Div([
        html.Div([
            html.H4(
                "welcome to ujshaw.tech",
                className="font-xl bold letter_spac8 default_inverse logo"
            ),
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            "Hello, I'm Jaeden Shaw.", html.Br(), html.Br(),
                            "I'm an IT Professional at Bostik Australia, with a passion for Cyber Security."],
                            className="font-about",
                        ),
                        html.Div(className="bottom32 dt_hide"),
                    ], lg=12, sm=12),
                ]),
                dbc.Row(
                    dbc.Col(
                        html.Div([
                            html.Div(
                                html.A(
                                    html.I(className="fab fa-linkedin-in"),
                                    href="https://www.linkedin.com/ujshaw",
                                    target="_blank"
                                )
                            ),
                            html.Div(
                                html.A(
                                    html.I(className="fab fa-kaggle"),
                                    href="https://www.kaggle.com/ujshaw/notebooks",
                                    target="_blank"
                                )
                            ),
                            html.Div(
                                html.A(
                                    html.I(className="fab fa-github "),
                                    href="https://github.com/ujshaw",
                                    target="_blank"
                                )
                            ),
                            html.Div(
                                html.A(
                                    html.I(className="fab fa-medium-m"),
                                    href="https://medium.com/@ujshaw",
                                    target="_blank"
                                )
                            )
                        ], className="about_logos font-lg"),
                        width=12
                    )

                )
            ], className="about_content padding32")
        ], className="terciary_bg radius8 relative about")
    ], className="padding16")
    return about

info = Info()
portfolio = Portfolio()
stacks = Stacks()
footer = Footer()

def Homepage():
    body = dbc.Container([
        info,
        html.Div("WRITEUPS",className="font-about"),
        stacks,
        html.Div("PORTFOLIO",className="font-about"),
        portfolio,
        footer
    ], className="top32")
    return body