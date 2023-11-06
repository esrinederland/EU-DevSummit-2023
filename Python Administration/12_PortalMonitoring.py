import arcgis
from Settings import AgolUrl,AgolProfileName, PortalUrl, ProfileName

gisAgol = arcgis.GIS(AgolUrl, profile=AgolProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gisAgol.properties.portalHostname,gisAgol.properties.user.username))

gisEnterprise = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gisEnterprise.properties.portalHostname,gisEnterprise.properties.user.username))

# AGOL List scheduled tasks
activeTasks = gisAgol.admin.scheduled_tasks(active=True)
print(activeTasks)