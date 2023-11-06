##### ARCGIS ONLINE #####

import arcgis
from Settings import PortalUrl,ProfileName, AgolUrl, AgolProfileName
import os

print("Getting GIS")
gis = arcgis.GIS(AgolUrl, profile=AgolProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

# GET THE LAYER TO UPDATE
layer = gis.content.search("type:'Feature Service' tags:earthquakes,DevSummit2023")[0].layers[0]

# ADD CSV TO USE FOR UPDATE
fileFolder = r"D:\Data"
fileName = "earthquakesHistory.csv"
fileType = "CSV"
filePath = os.path.join(fileFolder, fileName)
title = os.path.splitext(fileName)[0]
itemProperties={'type':fileType,
                'title':title,
                'description':'CSV file with earthquake information',
                'tags':'python, csv, earthquakes, DevSummit2023'}

csvItem = gis.content.add(
    item_properties=itemProperties, 
    data=filePath)
print(f"The item '{fileName}' was added to your portal with itemID: '{csvItem.itemid}'")

csvInfo = gis.content.analyze(
    item=csvItem.itemid, 
    file_type="csv", 
    location_type="coordinates"
    )

# UPDATE FEATURE SERVICE FROM CSV
print(f"BEFORE APPEND: Layer contains {layer.query(return_count_only=True)} features")
layer.append(
    item_id=csvItem.itemid,
    upload_format="csv",
    source_info=csvInfo['publishParameters']
    )
print(f"AFTER APPEND: Layer contains {layer.query(return_count_only=True)} features")

print("Script complete")