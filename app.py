import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("formatted_data.csv")
app = dash.Dash(__name__)

app.layout = html.Div(id="wrapper", children=[
    html.H1("Pink Morsel Visualiser", id="header"),
    
    html.Div(id="control-container", children=[
        html.Label("Select Region:"),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"}
            ],
            value="all",
            inline=True
        ),
    ]),

    dcc.Graph(id="sales-line-chart")
])

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Pink Morsel Sales - {selected_region.capitalize()} Region"
    )
    
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color="#ffffff"
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)