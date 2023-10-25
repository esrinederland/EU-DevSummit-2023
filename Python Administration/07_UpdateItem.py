import arcgis
from Settings import PortalUrl,ProfileName
import os

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

# UPDATE ITEM
fileFolder = r"D:\Data"
fileName = "earthquakes_year.csv"
fileType = "CSV"

filePath = os.path.join(fileFolder, fileName)
title = os.path.splitext(fileName)[0]
itemProperties={'type':fileType,
                'title':title,
                'description':'CSV file with earthquake information',
                'tags':'python, csv, earthquakes, DevSummit2023'}

# GET THE LAYER TO UPDATE
layer = gis.content.get("96cbbfd990844b78a3150313ea9971d6").layers[0]

addedItem = gis.content.add(item_properties=itemProperties, data=filePath)
print(f"The item '{fileName}' was added to your portal with itemID: '{addedItem.itemid}'")



print("Script complete")