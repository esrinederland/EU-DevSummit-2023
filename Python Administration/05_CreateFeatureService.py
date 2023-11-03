##### ARCGIS ONLINE #####

import arcgis
from Settings import AgolUrl,AgolProfileName
import os

print("Getting GIS")
gis = arcgis.GIS(AgolUrl, profile=AgolProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

# ADD ITEM
fileFolder = r"D:\Data"
fileName = "earthquakes2023.csv"
fileType = "CSV"

filePath = os.path.join(fileFolder, fileName)
title = os.path.splitext(fileName)[0]
itemProperties={'type':fileType,
                'title':title,
                'description':'CSV file with earthquake information',
                'tags':'python, csv, earthquakes, DevSummit2023'}
thumbnailPath = r"D:\Data\EarthQuake_image.png"

addedItem = gis.content.add(
    item_properties=itemProperties, 
    data=filePath,
    thumbnail=thumbnailPath
    )
print(f"The item '{fileName}' was added to your portal with itemID: '{addedItem.itemid}'")

# csvInfo = gis.content.analyze(
#     item=addedItem.itemid, 
#     file_type="csv", 
#     location_type="coordinates"
#     )
# csvInfo["publishParameters"]["layerInfo"]["capabilities"] = "Create,Delete,Query,Update,Editing,Sync"

# PUBLISH AS FEATURE SERVICE
publishedItem = addedItem.publish(
    # publish_parameters=csvInfo['publishParameters'],
    overwrite=True, 
    file_type="csv"
    )
publishedItem.layers[0].manager.add_to_definition({"capabilities": "Create,Delete,Query,Update,Editing,Sync"})
flCollection = arcgis.features.FeatureLayerCollection.fromitem(publishedItem)
flCollection.manager.update_definition({"syncEnabled":True})
print(f"The item was published to your portal with itemID: '{publishedItem.itemid}'")

print("Script complete")