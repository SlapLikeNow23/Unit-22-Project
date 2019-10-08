import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

#%matplotlib inline

df = pd.read_csv('/home/ruhit/Downloads/UTCs.csv')
df.head()

#Create map object
m = folium.Map(location=[53.381130, -1.470085], zoom_start=12)

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


url = 'https://opendata.arcgis.com/datasets/'
regions = f'{url}/bbb0e58b0be64cc1a1460aa69e33678f_0.geojson'

folium.GeoJson(
    regions,
    name='geojson'
).add_to(m)

folium.LayerControl().add_to(m)




'''
#Global tooltip
tooltip = 'Click for more info'


#Create markers
folium.Marker([53.381130, -1.570085],
              popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(m),
folium.Marker([53.381130, -1.470085],
              popup='<strong>Location Two</strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([53.381130, -1.370085],
              popup='<strong>Location Three</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([53.381130, -1.270085],
              popup='<strong>Location Three</strong>',
              tooltip=tooltip,
              icon=folium.Icon(color='green', icon='leaf')).add_to(m)
'''
#Generate Map
m.save('map.html')
