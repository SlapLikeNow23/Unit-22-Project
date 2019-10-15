import folium, pandas as pd, matplotlib.pyplot as plt, matplotlib as mpl, seaborn as sns, numpy as np, geopandas as gpd, csv, json, requests
from folium import plugins
from shapely.geometry import Point, Polygon
from folium.plugins import TimeSliderChoropleth
from geopandas import GeoSeries, GeoDataFrame

#%matplotlib inline

dfUTC = pd.read_csv('/home/ruhit/Downloads/UTCs.csv')
print("UTCs\n", dfUTC.head())

#Create map objefolium join datact
m = folium.Map(location=[53.381130, -1.470085], zoom_start=5)

for index, row in dfUTC.iterrows():
    #print(row)
    folium.Marker([row['Latitude'], row['Longitude']],
                  popup=row['University Technical College'],
                  icon=folium.Icon(icon='cloud')
                 ).add_to(m)

region_file = '/home/ruhit/Downloads/Local_Authority_Districts_April_2019_Boundaries_UK_BUC.geojson'
#regions = pd.read_csv()
#print("regions", regions.head())

'''
url = 'https://opendata.arcgis.com/datasets'
regions = f'{url}/bbb0e58b0be64cc1a1460aa69e33678f_0.geojson'
'''

fields=[str(y) for y in range(1997, 2017)]
print(fields)

dfProsperity = pd.read_csv('/home/ruhit/Desktop/Unit 22 Map/Unit-22-Project/Prosperity1.csv')

'''
for y in range(1997, 2017):
    folium.Choropleth(
     geo_data = region_file,
     name=str(y),
     data=dfProsperity,
     columns=['LAU1 code', str(y)],
     key_on='feature.properties.lad19cd',
     fill_color='YlGn',
     fill_opacity=0.7,
     line_opacity=0.2,
     show=False,
     overlay=True,
    ).add_to(m)
'''

dfTime = dfProsperity.melt(id_vars=['LAU1 code','LA name'], var_name='year', value_name='prosperity', value_vars=fields)
print("prosperity\n", dfTime.head())


folium.Choropleth(
     geo_data = region_file,
     name='prosperity',
     data=dfTime,
     columns=['LAU1 code', 'prosperity'],
     key_on='feature.properties.lad19cd',
     fill_color='YlGn',
     fill_opacity=0.7,
     line_opacity=0.2,
     #show=False,
     #overlay=True,
    ).add_to(m)


'''
for key in m._children:
    if key.startswith('color_map'):
        del(m._children[key])
'''
'''
styledict = {
    str(record): data.to_dict(orient='index') for
    record, data in styledata.items()
}


g = TimeSliderChoropleth(
    co2_geo_data_table_TS_subset.to_json(),
    styledict=styledict, overlay = True
).add_to(m)

'''

folium.LayerControl().add_to(m)


#in Local_Authority_Districts_April_2019_Boundaries_UK_BUC, join field name






#Generate Map
m.save('map.html')
