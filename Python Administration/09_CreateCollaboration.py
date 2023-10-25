import arcgis
from Settings import AgolUrl,AgolProfileName, PortalUrl, ProfileName

gisAgol = arcgis.GIS(AgolUrl, profile=AgolProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gisAgol.properties.portalHostname,gisAgol.properties.user.username))

gisEnterprise = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gisEnterprise.properties.portalHostname,gisEnterprise.properties.user.username))


### Create a collaboration ###
# Collaboration properties
collaborationName = "EsriNL Events + EsriNL DevTeam"
collaborationDescription = "Data sharing initiative between EsriNL Events and EsriNL DevTeam"

# Create collaboration
collaborationCreated = gisAgol.admin.collaborations.collaborate_with(gisEnterprise, collaborationName, collaborationDescription)
print(collaborationCreated)

if collaborationCreated:
    
    # Get collaboration
    collaboration = [collab for collab in gisEnterprise.admin.collaborations.list() if collaborationName in collab.name][0]
    print(f"Successfully created collaboration '{collaboration.name}'")

    # Get collaboration group on Enterprise portal to share Items
    collaborationGroupID = collaboration.workspaces[0]["participantGroupLinks"][0]["portalGroupId"]

    # Share a list of Items with the collaboration group
    items = ["aacd190707e94fc285215b77f35427a5"]
    sharedItems = gisEnterprise.content.share_items(items, groups=[collaborationGroupID])

print("Script complete")