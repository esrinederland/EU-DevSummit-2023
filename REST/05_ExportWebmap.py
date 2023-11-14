import Settings
import requests
import json

webmapID = "52f017f8cbcd4334a23726fd40aa3064"

# generate token
token = Settings.GenerateToken()

# get webmap json
webmapUrl = f"https://www.arcgis.com/sharing/rest/content/items/{webmapID}/data?f=json&token={token}"

print("Retrieving WebMap data")
r = requests.get(webmapUrl)
webmapData = r.json()

# add token to operational layers
for layer in webmapData["operationalLayers"]:
    layer["token"] = token

# Web_Map_as_JSON
webmapAsJson = {
    "exportOptions": {         
        "outputSize": [800,1100],         
        "dpi": 96     
    }
}
webmapAsJson["operationalLayers"] = webmapData["operationalLayers"]
webmapAsJson["baseMap"] = webmapData["baseMap"]
webmapAsJson["mapOptions"] = {
    "extent": webmapData["initialState"]["viewpoint"]["targetGeometry"]
}

# Export Web Map Task
exportWebMapUrl = "https://utility.arcgisonline.com/arcgis/rest/services/Utilities/PrintingTools/GPServer/Export%20Web%20Map%20Task/execute"
exportWebMapParams = {}
exportWebMapParams["f"] = "json"
exportWebMapParams["Web_Map_as_JSON"] = json.dumps(webmapAsJson)
exportWebMapParams["Format"] = "PNG32"
exportWebMapParams["Layout_Template"] = "MAP_ONLY"

print(f"Exporting WebMap as {exportWebMapParams['Format']}")
r = requests.post(exportWebMapUrl, exportWebMapParams)

print(f"View exported webmap at: '{r.json()['results'][0]['value']['url']}'")
print("Script complete")