import arcgis
from Settings import PortalUrl, ProfileName

usr = input("Enter the username:")
pwd = input("Enter the password:")
print("Creating gis")
gis = arcgis.GIS(PortalUrl, username=usr, password=pwd, profile=ProfileName)
#gis = arcgis.GIS("https://esribx0814.esrinl.com/portal", username=usr, password=pwd, profile="local_maarten_admin",verify_cert=False)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 