import arcgis
from Settings import PortalUrl,ProfileName

gis = arcgis.GIS(PortalUrl, profile=ProfileName,verify_cert=False)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

#Reset Look and Feel
newTitle = "EsriNL DevTeam ArcGIS Enterprise"

# CHANGE HOMEPAGE TITLE
gis.admin.ux.homepage_settings.set_title(newTitle)
print(f"Home page title updated to {newTitle}")

# CHANGE HOMEPAGE BACKGROUND
filename = r'D:\Data\background_default.png'
gis.admin.ux.homepage_settings.set_background(filename)
print(f"Home page background updated")

# RESET INFORMATINONAL BANNER
gis.admin.ux.security_settings.set_informational_banner(text="", enabled=False)

# Change portal title
gis.admin.ux.name = f"EsriNL DevTeam ArcGIS Enterprise"

#Remove created users
print("finding demo user")
DemoUser = gis.users.get("DevDayUser")

if not DemoUser is None:
    print(f"Deleting user: {DemoUser.username}")
    result = DemoUser.delete()
    print(f"Delete result: {result}")

#Remove Created Group
print("Searching for groups")
foundGroups = gis.groups.search(query='tags:"DevSummit2023"')
print(f"found: {len(foundGroups)}")
for demogroup in foundGroups:
    print(f"Deleting group: {demogroup.title}")
    result = demogroup.delete()
    print(f"Delete result: {result}")


#remove created items:
print("Searching for items")
itemsToRemove = gis.content.search(query='tags:"DevSummit2023"',max_items=1000)
print(f"found: {len(itemsToRemove)}")
for item in itemsToRemove:
    print(f"Start deleting item: {item.title} , {item.type} ({item.id})")
    result = item.delete()
    print(f"deleteresult: {result}")

# Delete collaboration
collaborationName = "EsriNL Events + EsriNL DevTeam"
collaborations = [collab for collab in gis.admin.collaborations.list() if collaborationName in collab.name]
for collaboration in collaborations:
    # Delete collaboration
    print(f"Deleting collaboration {collaboration.name}")
    res = collaboration.remove_participation()

# Delete collaboration group and content
collaborationGroups = gis.groups.search(query=collaborationName)
for collaborationGroup in collaborationGroups:
    print(f"Deleting group: {collaborationGroup.title}")
    collaborationGroup.delete()

# Delete collaboration folder for user
gis.content.delete_folder(f"collab_{collaborationName}")

print("Script complete")
