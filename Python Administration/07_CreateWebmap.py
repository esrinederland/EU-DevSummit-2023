import arcgis
from Settings import PortalUrl,ProfileName, AgolUrl, AgolProfileName, EarthquakeRenderer
import os

print("Getting GIS")
gis = arcgis.GIS(AgolUrl, profile=AgolProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username))

# CREATE WEBMAP
print("Creating a webmap")
wm = arcgis.mapping.WebMap()

# ADD BASEMAP AND LAYER
wm.basemap = "streets-night-vector"
layer = gis.content.get("5da9f6e8810741d7859491c32f1b46be").layers[0]
wm.add_layer(
    layer,
    options= {
        "title": "Earthquakes",
        "renderer": EarthquakeRenderer
    })

# SAVE THE WEBMAP
webmap_item_properties = {
    'title':'DevSummit Earthquakes with magnitude above 5.5 in 2023',
    'snippet':'Map created using Python API',
    'tags':['automation', 'python', "DevSummit2023"]
    }

print("Saving the webmap")
new_wm_item = wm.save(webmap_item_properties, thumbnail=r'D:\Data\WebMap_Icon.jpg')
print(f"Created item with id: {new_wm_item.id}")

print("Script complete")