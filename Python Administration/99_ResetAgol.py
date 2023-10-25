import arcgis
from Settings import AgolUrl,AgolProfileName

gis = arcgis.GIS(AgolUrl, profile=AgolProfileName,verify_cert=False)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

# Get collaboration
collaborationName = "EsriNL Events + EsriNL DevTeam"
collaborations = [collab for collab in gis.admin.collaborations.list() if collaborationName in collab.name]
if len(collaborations) > 0:
    collaboration = collaborations[0]

    # Delete collaboration group and content
    collaborationGroupID = collaboration.workspaces[0]["participantGroupLinks"][0]["portalGroupId"]
    collaborationGroup = gis.groups.get(collaborationGroupID)
    collaborationContent = collaborationGroup.content()
    gis.content.delete_items(collaborationContent)
    collaborationGroup.delete()

    # Delete collaboration folder for user
    gis.content.delete_folder(f"collab_{collaborationName}")

    # Delete collaboration
    res = collaboration.delete()
    print(res)

print("Script complete")
