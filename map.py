import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import csv
import json
import requests

#%matplotlib inline

df = pd.read_csv('/home/ruhit/Downloads/UTCs.csv')
df.head()

#Create map objefolium join datact
m = folium.Map(location=[53.381130, -1.470085], zoom_start=5)

for index, row in df.iterrows():
    #print(row)
    folium.Marker([row['Latitude'], row['Longitude']],
                  popup=row['University Technical College'],
                  icon=folium.Icon(icon='cloud')
                 ).add_to(m)

'''
shapefile = '/home/ruhit/Downloads/Local_Authority_Districts_April_2019_Boundaries_UK_BUC/Local_Authority_Districts_April_2019_Boundaries_UK_BUC.shp'

#Read shapefile using Geopandas
gdf = gpd.read_file(shapefile)[['LAD19NM', 'LAD19CD', 'st_area(shape)']]

#Rename columns.
gdf.columns = ['country', 'country_code', 'geometry']
gdf.head()
'''

#region_file = 'http:///home/ruhit/Downloads/Local_Authority_Districts_April_2019_Boundaries_UK_BUC.geojson'
#regions = pd.read_csv()
#print("regions", regions.head())


url = 'https://opendata.arcgis.com/datasets'
regions = f'{url}/bbb0e58b0be64cc1a1460aa69e33678f_0.geojson'

geo_json_data = json.loads(requests.get(regions).text)

folium.LayerControl().add_to(m)


df = pd.read_csv('/home/ruhit/Desktop/Unit 22 Map/Unit-22-Project/Prosperity1.csv')
print("prosperity", df.head())

p_data = pd.read_csv('/home/ruhit/Downloads/UTCs.csv')

print("UTCs", p_data.head())



m.choropleth(
 geo_data = regions,
 name='choropleth',
 data=p_data,
 columns=['LAU1 code', '1997'],
 key_on='feature.lad19cd',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.2,
)
folium.LayerControl().add_to(m)


#in Local_Authority_Districts_April_2019_Boundaries_UK_BUC, join field name


#Generate Map
m.save('map.html')
