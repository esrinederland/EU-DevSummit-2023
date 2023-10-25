import arcgis
from Settings import PortalUrl,ProfileName
import os

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username))

# CREATE WEBMAP
print("Creating a webmap")
wm = arcgis.mapping.WebMap()  # new web map

wm.basemap = "streets-night-vector"

layer = gis.content.get("96cbbfd990844b78a3150313ea9971d6").layers[0]
wm.add_layer(layer)  # add some layers


# SAVE THE WEBMAP
webmap_item_properties = {'title':'DevSummit Created Webmap',
             'snippet':'Map created using Python API',
             'tags':['automation', 'python', "DevSummit2023"],
             'extent': {'xmin': -17, 'ymin': 42, 'xmax': 39, 'ymax': 59, 'spatialReference': {'wkid': 4326}}}

print("Saving the webmap")
new_wm_item = wm.save(webmap_item_properties, thumbnail=r'D:\Data\WebMap_Icon.jpg')
print(f"Created item with id: {new_wm_item.id}")

print("Script complete")