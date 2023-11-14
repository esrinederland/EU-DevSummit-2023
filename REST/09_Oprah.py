import Settings
import requests
import json
#set variables
template_webmapid = "640f37acaf2f49189a514a525220257c"
template_dashboardid = "3ec7a48b8a8a471b9673eb659518659b"

#Generate token
print("Getting token")
token = Settings.GenerateToken()

#get template dashboard and webmap
defaultParams = {"f":"json","token":token}

print("getting template webmap")
webmapDataUrl = "https://www.arcgis.com/sharing/rest/content/items/{}/data".format(template_webmapid)
r = requests.get(webmapDataUrl,defaultParams)
webmapData = r.json()

print("getting template dashboard")
dashboardDataUrl = "https://www.arcgis.com/sharing/rest/content/items/{}/data".format(template_dashboardid)
r = requests.get(dashboardDataUrl,defaultParams)
dashboardData = r.text

#find layerid with locations or tesselations in the title
locationsLayerId = None
locationsLayerUrl = None
tesselationsLayerId = None
tesselationsLayerUrl = None
for layer in webmapData["operationalLayers"]:
    if "locations" in layer["title"].lower():
        locationsLayerId = layer["id"]
        locationsLayerUrl = layer["url"]
        print(f"{locationsLayerId=}")
    if "tessellations" in layer["title"].lower():
        tesselationsLayerId = layer["id"]
        tesselationsLayerUrl = layer["url"]
        print(f"{tesselationsLayerId=}")
        
#query features
print("querying features")
queryUrl = "{}/query".format(locationsLayerUrl)
queryParams = {"f":"json","token":token,"where":"1=1","outFields":"*", "outSR":4326}
r = requests.get(queryUrl,queryParams)
features = r.json()["features"]


print(f"looping through {len(features)} features")
#for each feature
for feature in features:
    oid = feature["attributes"]["objectid"]
    name = feature["attributes"]["name"]
    color = feature["attributes"]["color"]
    comment = feature["attributes"]["comment"]
    geometry = feature["geometry"]
    
    print(f"Parsing feature for {name} ({oid})")
    
    #query the area's service
    print("querying area's service")
    geometry["spatialReference"] = {"wkid":4326}
    areaQueryUrl = "{}/query".format(tesselationsLayerUrl)
    areaQueryParams = {"f":"json","token":token,"where":"1=1","outFields":"*", "outSR":4326, "geometry":json.dumps(geometry),"geometryType":"esriGeometryPoint"}
    r = requests.get(areaQueryUrl,areaQueryParams)
    areaFeatures = r.json()["features"]
    areaOid = -1
    if len(areaFeatures) >0:
        areaFeature = areaFeatures[0]
        areaOid = areaFeature["attributes"]["OBJECTID"]
        print(f"Found area for {name} ({oid}): ({areaOid})")
    
    #generate new webmap
    print("generating new webmap definition")
    newWebmapData = webmapData.copy()
    areaLayer = [layer for layer in newWebmapData["operationalLayers"] if layer["id"] == tesselationsLayerId][0]
    areaLayer["layerDefinition"]["definitionExpression"] = f"objectid = {areaOid}"

    locationsLayer = [layer for layer in newWebmapData["operationalLayers"] if layer["id"] == locationsLayerId][0]
    locationsLayer["layerDefinition"]["definitionExpression"] = f"objectid = {oid}"

    newWebmapInfo = defaultParams.copy()
    newWebmapInfo["title"] = f"Generated webmap for {name}"
    newWebmapInfo["tags"] = f"EUDevSummit23,Demo08,Oprah,{name}"
    newWebmapInfo["description"] = f"Hello {name}, this is a newly created webmap. You said: {comment}"
    newWebmapInfo["type"] = "Web Map"
    newWebmapInfo["text"] = json.dumps(newWebmapData)

    #addItemurl = f"https://www.arcgis.com/sharing/rest/content/users/{Username.Username()}/{folderid}/addItem"
    addItemurl = f"https://www.arcgis.com/sharing/rest/content/users/{Settings.Username}/addItem"

    r = requests.post(addItemurl,newWebmapInfo)

    newWebmapResult = r.json()
    print(f"{newWebmapResult=}")

    newWebmapId = newWebmapResult["id"]
    print(f"{newWebmapId=}")

    #generate a new dashboard
    print("generating new dashboard definition")
    newDashboardData = dashboardData
    newDashboardData = newDashboardData.replace(template_webmapid,newWebmapId)

    newDashboardInfo = defaultParams.copy()
    newDashboardInfo["title"] = f"Generated dashboard for {name}"
    newDashboardInfo["tags"] = f"EUDevSummit23,Demo08,Oprah,{name}"
    newDashboardInfo["description"] = f"Hello {name}, this is a newly created dashboard. You said: {comment}"
    newDashboardInfo["type"] = "Dashboard"
    newDashboardInfo["typeKeywords"] = "ArcGIS Dashboard,Dashboard,Operations Dashboard"
    newDashboardInfo["text"] = newDashboardData

    r = requests.post(addItemurl,newDashboardInfo)

    newDashboardResult = r.json()
    print(f"{newDashboardResult=}")

    newDashboardId = newDashboardResult["id"]
    print(f"{newDashboardId=}")

print("Script complete")

    
        

    
    



    #generate new webmap
    
    #generate a new dashboard

    #generate a group

    #share the dashboard and webmap to the group