import dash
from dash import dcc
from dash import html
import plotly.express as px

# Load data and create a figure
df_cnt = px.data.gapminder()
fig1 = px.scatter(df_cnt, x="gdpPercap", y="lifeExp", animation_frame="year", 
           animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])


df = df_cnt[df_cnt['year'] == 2007]
fig2 = px.scatter_geo(df, locations="iso_alpha",
                     color="continent", # which column to use to set the color of markers
                     hover_name="country", # column added to hover information
                     size="pop", # size of markers
                     projection="orthographic")


# Create the app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H3("BME 225 demo: Use the interactive chart below to explore data on population, life expectancy, and GDP for various countries!"),
    html.H5("You can click the arrow at the year bar to show information from different time."),
    dcc.Graph(
        id='example-graph1',
        figure=fig1
    ),
    html.H5("You can rotate the globe to show population from 2007"),
    dcc.Graph(
        id='example-graph2',
        figure=fig2
    )
])

# Run the app
app.run_server(port=10000)
