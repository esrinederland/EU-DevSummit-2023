##### ARCGIS ONLINE #####

import arcgis
from Settings import PortalUrl,ProfileName, AgolUrl, AgolProfileName
import os

print("Getting GIS")
gis = arcgis.GIS(AgolUrl, profile=AgolProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

# ADD CSV TO USE FOR UPDATE
print("Adding CSV to your portal")
fileFolder = r"D:\Data"
fileName = "earthquakesHistory.csv"
fileType = "CSV"
filePath = os.path.join(fileFolder, fileName)
title = os.path.splitext(fileName)[0]
itemProperties={'type':fileType,
                'title':title,
                'description':'CSV file with earthquake information',
                'tags':'python, csv, earthquakes, DevSummit2023'}
thumbnailPath = r"D:\Data\EarthQuake_image.png"

csvItem = gis.content.add(
    item_properties=itemProperties, 
    data=filePath,
    thumbnail=thumbnailPath
    )
print(f"The item '{fileName}' was added to your portal with itemID: '{csvItem.itemid}'")

# ANALYZE THE CSV ITEM
csvInfo = gis.content.analyze(
    item=csvItem.itemid, 
    file_type="csv", 
    location_type="coordinates"
    )

# GET THE LAYER TO UPDATE
layer = gis.content.search("type:'Feature Service' tags:earthquakes,DevSummit2023")[0].layers[0]

# UPDATE FEATURE SERVICE FROM CSV
print(f"BEFORE APPEND: Layer contains {layer.query(return_count_only=True)} features")
layer.append(
    item_id=csvItem.itemid,
    upload_format="csv",
    source_info=csvInfo['publishParameters']
    )
print(f"AFTER APPEND: Layer contains {layer.query(return_count_only=True)} features")

print("Script complete")