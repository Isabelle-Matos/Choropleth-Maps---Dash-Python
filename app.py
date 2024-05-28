from urllib.request import urlopen
import json
import plotly.express as px
import pandas as pd

with urlopen("https://raw.githubusercontent.com/codeforamerica/click_that_hood/"
             "master/public/data/brazil-states.geojson") as response:
    Brazil = json.load(response)

state_id_map = {}
for feature in Brazil['features']:
    feature['id'] = feature['properties']['name']
    state_id_map[feature['properties']['sigla']] = feature['id']

brazil_date = pd.read_csv("/home/izzy/Documentos/Choropleth-Maps---Dash-Python/csv_files/br-state-codes.csv")
# print(brazil_date)

fig = px.choropleth_mapbox(
    brazil_date,
    locations="name",  #define the limits on the map/geography
    geojson=Brazil,  #shape information
    color="creation",  #defining the color of the scale through the database
    hover_name="name",  #the information in the box
    hover_data=["creation"],
    title="Criação dos estados brasileiros",  #title of the map
    mapbox_style="carto-positron",  #defining a new map style
    center={"lat": -14, "lon": -55},  #define the limits that will be plotted
    zoom=3,  #map view size
    opacity=0.5,  #opacity of the map color, to appear the background
)
    # animation_frame="creation")  #creating the application based on the year
fig.show()
