from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Create sample dataset
df = px.data.iris()

# Create Dash application
app = Dash(__name__)

# Expose Flask server for Gunicorn
server = app.server

# Design application layout
app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "padding": "30px",
        "backgroundColor": "#f4f6f9"
    },
    children=[
        html.H1(
            "My First Dash Dashboard",
            style={"textAlign": "center", "color": "#17365D"}
        ),

        html.H3("Explore Iris Dataset"),

        html.Label("Select Flower Species:"),

        dcc.Dropdown(
            id="species-dropdown",
            options=[
                {"label": species, "value": species}
                for species in df["species"].unique()
            ],
            value="setosa",
            clearable=False
        ),

        dcc.Graph(id="iris-chart"),

        html.Div(
            "Created using Python Dash and Plotly",
            style={"textAlign": "center", "marginTop": "20px"}
        )
    ]
)


# Create interactive callback
@app.callback(
    Output("iris-chart", "figure"),
    Input("species-dropdown", "value")
)
def update_graph(selected_species):

    filtered_df = df[df["species"] == selected_species]

    fig = px.scatter(
        filtered_df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        title=f"Iris Dataset - {selected_species}"
    )

    return fig


# Run locally
if __name__ == "__main__":
    app.run(debug=True)
