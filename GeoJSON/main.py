########################################################################################################################
# Data Visualization of The Spread of Corona
# This program will give figure the spread of corona case in an area
# Make sure use the right data source
# Make sure place geojson file in the right directory, put directory of geojson and URL in program
# example for API link : https://covid19-public.digitalservice.id/api/v1/sebaran_v2/jabar
# example for geojson file : E:\GitHub\Python\GeoJSON\map.geojson
########################################################################################################################

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import requests
import json

# From https://www.covid19.go.id
totalCase = 68066

# Using API to access data for mark area
response = requests.get('https://covid19-public.digitalservice.id/api/v1/sebaran_v2/jabar')

# Open json file in read mode for mark area
# with open('E:\GitHub\Python\GeoJSON\case_point.json', 'r') as response:
#     data = json.load(response)

# Show response data
# print(response)

# Show response data in JSON format
# print(response.json()) # show API in JSON format

# Show response data in better JSON format
# print(json.dumps(response.json(), sort_keys=True, indent=4))

# Convert JSON data
jsonDump = json.dumps(response.json())
jsonLoad = json.loads(jsonDump)

# Show jsonDump data
# print(jsonDump)

# Show jsonLoad data
# print(jsonLoad)

# Set figure size
plt.rcParams['figure.figsize'] = (10, 10)

# Open geoJSON for map
cityMap = gpd.read_file('E:\GitHub\Python\GeoJSON\map.geojson')

# Create empty data frame for lon & lat
dataFrame = pd.DataFrame(
    {'Latitude': [],
     'Longitude': []
     })

# Looping for get every lon & lat
for i in range(totalCase):
    # Print lon & lat
    # print('{} lat = {}, lon = {}'
    #       .format(i, jsonLoad['data']['content'][i]['latitude'],
    #       jsonLoad['data']['content'][i]['longitude']))

    # Insert lon & lat to data frame start with index 0
    dataFrame.loc[0] = [jsonLoad['data']['content'][i]['latitude'], jsonLoad['data']['content'][i]['longitude']]
    # Increment index
    dataFrame.index = dataFrame.index + 1
    # Sorting index
    dataFrame = dataFrame.sort_index()

#  Use lon & lat to mark area
geoDataFrame = gpd.GeoDataFrame(dataFrame, geometry=gpd.points_from_xy(dataFrame.Longitude, dataFrame.Latitude))

# Plotting for city map
ax = cityMap.plot(color='green', edgecolor='black')

# Plotting for mark area
geoDataFrame.plot(ax=ax, color='red', markersize=1)

# Save figure
# plt.savefig('figure.png', dpi=300)
plt.savefig('figure.jpg', format='jpg')

# Show result visualisation
plt.show()
