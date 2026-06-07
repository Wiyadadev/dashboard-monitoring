from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 150, 120, 180, 200]
})

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Monitoring"),

    dcc.Dropdown(
        id="month-dropdown",
        options=[{"label": m, "value": m} for m in df["Month"]],
        value="Jan"
    ),

    dcc.Graph(id="sales-graph")
])

@app.callback(
    Output("sales-graph", "figure"),
    Input("month-dropdown", "value")
)
def update_graph(selected_month):
    filtered_df = df[df["Month"] == selected_month]
    return px.bar(
        filtered_df,
        x="Month",
        y="Sales",
        title=f"Sales for {selected_month}"
    )

if __name__ == "__main__":
    app.run(debug=True)

    from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# อ่านข้อมูลจาก Excel
df = pd.read_excel("sales.xlsx")

fig = px.line(
    df,
    x="Month",
    y="Sales",
    title="Monthly Sales"
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Monitoring"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
    from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import base64
import io

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Monitoring"),

    dcc.Upload(
        id="upload-data",
        children=html.Button("Upload Excel File")
    ),

    dcc.Graph(id="graph")
])

@app.callback(
    Output("graph", "figure"),
    Input("upload-data", "contents")
)
def update_graph(contents):
    if contents is None:
        return px.line(title="Upload an Excel file")

    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    df = pd.read_excel(io.BytesIO(decoded))

    fig = px.line(
        df,
        x=df.columns[0],
        y=df.columns[1],
        title="Excel Data"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)

    from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://root:password@localhost/dashboard_db"
)

df = pd.read_sql(
    "SELECT month, sales FROM sales_data",
    engine
)
import plotly.express as px

fig = px.bar(
    df,
    x="month",
    y="sales",
    title="Sales from MySQL"
)
from dash import Dash, html, dcc
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px

engine = create_engine(
    "mysql+pymysql://root:password@localhost/dashboard_db"
)

df = pd.read_sql(
    "SELECT month, sales FROM sales_data",
    engine
)

fig = px.bar(df, x="month", y="sales")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Database Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
    from dash import Dash, html, dcc, dash_table
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 150, 120, 180, 200]
})

fig = px.line(df, x="Month", y="Sales")

app = Dash(__name__)

app.layout = html.Div([

    # Sidebar
    html.Div([
        html.H2("Dashboard"),
        html.Hr(),
        html.P("Navigation"),
        html.Ul([
            html.Li("Overview"),
            html.Li("Reports"),
            html.Li("Settings")
        ])
    ], style={
        "width": "20%",
        "height": "100vh",
        "backgroundColor": "#2c3e50",
        "color": "white",
        "padding": "20px",
        "float": "left"
    }),

    # Main Content
    html.Div([

        html.H1("Sales Dashboard"),

        html.Div([
            html.Div([
                html.H3("750"),
                html.P("Total Sales")
            ], style={"border":"1px solid #ddd","padding":"15px","width":"200px"}),

            html.Div([
                html.H3("200"),
                html.P("Best Month")
            ], style={"border":"1px solid #ddd","padding":"15px","width":"200px"})
        ], style={"display":"flex","gap":"20px"}),

        dcc.Graph(figure=fig),

        dash_table.DataTable(
            data=df.to_dict("records"),
            columns=[{"name": c, "id": c} for c in df.columns]
        )

    ], style={
        "width": "75%",
        "float": "right",
        "padding": "20px"
    })

])

if __name__ == "__main__":
    app.run(debug=True)
    total_sales = df["Sales"].sum()
avg_sales = round(df["Sales"].mean(), 2)
max_sales = df["Sales"].max()
min_sales = df["Sales"].min()
fig_bar = px.bar(df, x="Month", y="Sales")

fig_pie = px.pie(
    df,
    names="Month",
    values="Sales"
)