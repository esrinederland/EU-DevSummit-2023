import Settings
import requests
import json

#template webmapid
inputWebMapdata = {
    "operationalLayers": [
        {
            "id": "18b47ee6cd3-layer-1",
            "title": "InputPoints",
            "url": "https://services9.arcgis.com/7e6lF03RcLhwFtm5/arcgis/rest/services/survey123_d4b3ab2513384ea48ae3cb62a9e0e5df_results/FeatureServer/0",
            "layerType": "ArcGISFeatureLayer"
        }
    ],
    "baseMap": {
        "baseMapLayers": [
            {
                "id": "18b484c1391-layer-2",
                "title": "World Topographic Map",
                "itemId": "7dc6cea0b1764a1f9af2e679f642f0f5",
                "layerType": "VectorTileLayer",
                "styleUrl": "https://www.arcgis.com/sharing/rest/content/items/7dc6cea0b1764a1f9af2e679f642f0f5/resources/styles/root.json"
            }
        ],
        "title": "World Topographic Map"
    },
    "authoringApp": "ArcGISMapViewer",
    "authoringAppVersion": "2023.2",
    "initialState": {
        "viewpoint": {
            "targetGeometry": {
                "spatialReference": {
                    "latestWkid": 3857,
                    "wkid": 102100
                },
                "xmin": 1425323.745287461,
                "ymin": 6840074.534306565,
                "xmax": 1548693.1089397825,
                "ymax": 6936538.064002495
            }
        }
    },
    "spatialReference": {
        "latestWkid": 3857,
        "wkid": 102100
    },
    "version": "2.28"
}

webmapInfo = {}
webmapInfo["title"] = f"Generated webmap for EU DevSummit 2023 - REST Session"
webmapInfo["tags"] = f"EUDevSummit23,Demo04"
webmapInfo["description"] = f"Hello all, this is a newly created webmap. You said: "
webmapInfo["type"] = "Web Map"
webmapInfo["text"] = json.dumps(inputWebMapdata)


token = Settings.GenerateToken()
webmapInfo["f"] = "json"
webmapInfo["token"] = token


addItemurl = f"https://www.arcgis.com/sharing/rest/content/users/{Settings.Username}/addItem"

r = requests.post(addItemurl,webmapInfo)

print(r.text)

print("script complete")