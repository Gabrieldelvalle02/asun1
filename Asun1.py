import pandas as pd
import unidecode
import json
import plotly.express as px

df = pd.read_csv('archivoasun.csv', sep=';', header=0)

df[' Barrio '] = df[' Barrio '].str.upper().apply(unidecode.unidecode)
with open('Barrios_Localidades_Asuncion.geojson', 'r') as f:
    geojson_data = json.load(f)

# Crear el mapa de calor
fig = px.choropleth_mapbox(
    df,
    geojson=geojson_data,
    locations=' Barrio ',  # Columna del CSV
    featureidkey='properties.BARLO_DESC',  # Clave del GeoJSON
    color=' Total ',  # Columna para el color
    color_continuous_scale='Plasma',  # Escala de color
    mapbox_style='carto-positron',  # Estilo del mapa
    zoom=14,  # Zoom en Asunción
    center={'lat': -25.3, 'lon': -57.6},  # Centro de Asunción
    title='Mapa de calor: Encuestados por barrio en Asuncion'
)

# Ajustar márgenes
fig.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0})

# Mostrar el gráfico
fig.show()