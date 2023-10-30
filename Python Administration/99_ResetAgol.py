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
    print(f"Deleting {len(collaborationContent)} items")
    gis.content.delete_items(collaborationContent)
    print(f"Deleting group {collaborationGroup.title}")
    collaborationGroup.delete()

    # Delete collaboration folder for user
    print(f"Deleting folder collab_{collaborationName}")
    gis.content.delete_folder(f"collab_{collaborationName}")

    # Delete collaboration
    print(f"Deleting collaboration {collaboration.name}")
    res = collaboration.delete()

print("Script complete")
