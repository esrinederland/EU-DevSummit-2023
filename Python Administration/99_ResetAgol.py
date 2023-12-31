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

#remove created items:
print("Searching for items")
itemsToRemove = gis.content.search(query='tags:"DevSummit2023"',max_items=1000)
print(f"found: {len(itemsToRemove)}")
for item in itemsToRemove:
    print(f"Start deleting item: {item.title} , {item.type} ({item.id})")
    result = item.delete()
    print(f"deleteresult: {result}")

#Remove Created Group
print("Searching for groups")
foundGroups = gis.groups.search(query='tags:"DevSummit2023"')
print(f"found: {len(foundGroups)}")
for demogroup in foundGroups:
    print(f"Deleting group: {demogroup.title}")
    result = demogroup.delete()
    print(f"Delete result: {result}")

print("Script complete")
