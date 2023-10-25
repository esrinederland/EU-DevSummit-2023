import arcgis
from Settings import AgolUrl,AgolProfileName

gis = arcgis.GIS(AgolUrl, profile=AgolProfileName,verify_cert=False)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 


print("Script complete")
