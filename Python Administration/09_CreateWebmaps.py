import arcgis
from Settings import PortalUrl,ProfileName, EarthquakeRenderer

gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username))

# SYNC COLLABORATION
print("Syncing collaboration")
collaboration = [collab for collab in gis.admin.collaborations.list() if "EsriNL Events + EsriNL DevTeam" in collab.name][0]
syncresult = collaboration.sync(
    workspace_id=collaboration.workspaces[0]["id"]
)
print(f"Sync result is: {syncresult}")

# GET FEATURE LAYER
layer = gis.content.search("type:'Feature Service' tags:earthquakes,DevSummit2023")[0].layers[0]

# GET UNIQUE VALUES
uniqueValues = layer.get_unique_values("year")

print(f"Found: {len(uniqueValues)} unique values")
uniqueValues.sort(reverse=True)
counter = 0
for unique in uniqueValues:
    counter += 1

    # CREATE A NEW WEBMAP
    print(f"Creating webmap for {unique} ({counter}/{len(uniqueValues)}))")
    wm = arcgis.mapping.WebMap()

    # ADD BASEMAP AND LAYER
    wm.basemap = "dark-gray-vector"
    wm.add_layer(
        layer,
        options= {
        "title": "Earthquakes",
        "renderer": EarthquakeRenderer
    })

    # SET DEFINITION EXPRESSION
    sql_expression = f"year = {unique}"
    wm.layers[0].layerDefinition.definitionExpression = sql_expression

    # SAVE THE WEBMAP
    extent = layer.query(where=sql_expression,return_extent_only = True, out_sr=4326)
    webmap_item_properties = {'title':f'Earthquakes with magnitude above 5.5 in {unique}',
                'snippet':'Map created using Python API',
                'tags':['automation', 'python', "DevSummit2023"],
                'extent': extent['extent']}

    print("Saving the webmap")
    new_wm_item = wm.save(webmap_item_properties, thumbnail=r'D:\Data\WebMap_Icon.png')
    print(f"Created item with id: {new_wm_item.id}")

    # SHARE THE WEBMAP WITH THE COLLABORATION
    print("Sharing webmap with collaboration")
    collaborationGroupID = collaboration.workspaces[0]["participantGroupLinks"][0]["portalGroupId"]
    new_wm_item.share(groups=[collaborationGroupID])

print("Script complete")