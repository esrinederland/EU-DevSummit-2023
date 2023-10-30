import arcgis
from Settings import PortalUrl,ProfileName, EarthquakeRenderer

gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username))

#get featurelayer
layer = gis.content.get("5da9f6e8810741d7859491c32f1b46be").layers[0]

#get unique values
uniqueValues = layer.get_unique_values("year")

print(f"Found: {len(uniqueValues)} unique values")
uniqueValues.sort(reverse=True)
counter = 0
for unique in uniqueValues:
    counter += 1
    print(f"Creating webmap for {unique} ({counter}/{len(uniqueValues)}))")

    sql_expression = f"year = {unique}"

    wm = arcgis.mapping.WebMap()  # new web map

    wm.basemap = "streets-night-vector"

    wm.add_layer(
        layer,
        options= {
        "title": "Earthquakes",
        "renderer": EarthquakeRenderer
    })

    wm.layers[0].layerDefinition.definitionExpression = sql_expression

    # SAVE THE WEBMAP
    webmap_item_properties = {'title':f'Earthquakes with magnitude above 5.5 in {unique}',
                'snippet':'Map created using Python API',
                'tags':['automation', 'python', "DevSummit2023"]}

    print("Saving the webmap")
    new_wm_item = wm.save(webmap_item_properties, thumbnail=r'D:\Data\WebMap_Icon.jpg')
    print(f"Created item with id: {new_wm_item.id}")

print("Script complete")