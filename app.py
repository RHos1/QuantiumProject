import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("formatted_data.csv")
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales: Pre vs Post Price Increase",
    labels={"date": "Date", "sales": "Total Sales (USD)"}
)

fig.add_vline(
    x="2021-01-15", 
    line_dash="dash", 
    line_color="red", 
    annotation_text="Price Increase"
)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser", style={'textAlign': 'center'}),
    dcc.Graph(id='sales-chart', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)