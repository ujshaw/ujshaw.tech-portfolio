import dash_html_components as html
import dash_trich_components as dtc


def Navbar():
    navbar = html.Div(
        [
            html.Div(
                [
                    html.Div(html.Div(
                        html.A(
                            'ujshaw.tech', className="logo", href="/",
                        ))),
                    html.Div(
                        html.Ul(
                                className="nav-links font-md logo",
                                children=[]
                            ),
                            className="nav"
                    ),

                ], className="container flex_row_btw"
            ),

        ],
        className="navbar"
    )
    return navbar
