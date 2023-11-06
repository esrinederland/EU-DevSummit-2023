##### ARCGIS ENTERPRISE #####
#TODO: Change extent
import arcgis
from Settings import PortalUrl,ProfileName,EarthquakeRenderer
import os

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username))

# SYNC COLLABORATION
print("Syncing collaboration")
collaboration = [collab for collab in gis.admin.collaborations.list() if "EsriNL Events + EsriNL DevTeam" in collab.name][0]
syncresult = collaboration.sync(
    workspace_id=collaboration.workspaces[0]["id"]
)
print(f"Sync result is: {syncresult}")

# CREATE WEBMAP
print("Creating a webmap")
wm = arcgis.mapping.WebMap()

# ADD BASEMAP AND LAYER
wm.basemap = "streets-night-vector"
layer = gis.content.search("type:'Feature Service' tags:earthquakes,DevSummit2023")[0].layers[0]
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
new_wm_item = wm.save(webmap_item_properties, thumbnail=r'D:\Data\WebMap_Icon.png')
print(f"Created item with id: {new_wm_item.id}")

print("Script complete")