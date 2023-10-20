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
foundGroups = gis.groups.search(query='tags:"DevDay2023"')
print(f"found: {len(foundGroups)}")
for demogroup in foundGroups:
    print(f"Deleting group: {demogroup.title}")
    result = demogroup.delete()
    print(f"Delete result: {result}")


#remove created items:
print("Searching for items")
itemsToRemove = gis.content.search(query='tags:"DevDay2023"',max_items=1000)
print(f"found: {len(itemsToRemove)}")
for item in itemsToRemove:
    print(f"Start deleting item: {item.title} , {item.type} ({item.id})")
    result = item.delete()
    print(f"deleteresult: {result}")

print("Starting sampleworldcities")
print("Getting admin")
admin = gis.admin

print("Getting serverManager")
serverManager = admin.servers

print("getting hosting server")
gis_server = serverManager.get("HOSTING_SERVER")[0]

print("Getting services manager")
servicesManager = gis_server.services
swcService = [serv for serv in servicesManager.list() if serv.properties.serviceName =="SampleWorldCities"][0]

print(f"Service status: {swcService.status}")

print("Start Service")
swcService.start()

print(f"Service status: {swcService.status}")

print("Script complete")
