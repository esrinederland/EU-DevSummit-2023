import arcgis
from Settings import PortalUrl,ProfileName

gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username))

#get featurelayer
layer = gis.content.get("96cbbfd990844b78a3150313ea9971d6").layers[0]

#get unique values
uniqueValues = layer.get_unique_values("Gemeente")

print(f"Found: {len(uniqueValues)} unique values")
uniqueValues.sort(reverse=True)
counter = 0
for unique in uniqueValues:
    counter += 1
    print(f"Creating webmap for {unique} ({counter}/{len(uniqueValues)}))")

    sql_expression = f"Gemeente = '{unique}'"

    wm = arcgis.mapping.WebMap()  # new web map

    wm.basemap = "dark-gray-vector"

    wm.add_layer(layer)  # add some layers

    wm.layers[0].layerDefinition.definitionExpression = sql_expression

    extent = layer.query(where=sql_expression,return_extent_only = True, out_sr=4326)

    # SAVE THE WEBMAP
    webmap_item_properties = {'title':f'DevSummit Created Webmap for {unique}',
                'snippet':'Map created using Python API',
                'tags':['automation', 'python', "DevSummit2023"],
                'extent': extent['extent']}

    print("Saving the webmap")
    new_wm_item = wm.save(webmap_item_properties, thumbnail=r'D:\Data\WebMap_Icon.jpg')
    print(f"Created item with id: {new_wm_item.id}")

print("Script complete")