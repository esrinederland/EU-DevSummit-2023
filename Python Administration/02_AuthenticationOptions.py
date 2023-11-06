##### ARCGIS ENTERPRISE #####

import arcgis
from Settings import PortalUrl,ProfileName
import getpass

# ANONYMOUS
print("Create anonymous GIS")
gis = arcgis.GIS()
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.users.me)) 

# USERNAME & PASSWORD
print("")
print("Use login with username and password")
username = input("Enter username: ")
pwd = getpass.getpass("Enter password: ")
gis2 = arcgis.GIS(
    url=PortalUrl,
    username=username,
    password=pwd
    )
print("Successfully logged into '{}' via the '{}' user".format(gis2.properties.portalHostname,gis2.properties.user.username)) 

# PRO
print("")
print("Using ArcGIS Pro login")
gis3 = arcgis.GIS(
    "Pro"
    )
print("Successfully logged into '{}' via the '{}' user".format(gis3.properties.portalHostname,gis3.properties.user.username)) 

# HOME
print("")
print("Using Home login")
gis4 = arcgis.GIS(
    "Home"
    )
print("Successfully logged into '{}' via the '{}' user".format(gis4.properties.portalHostname,gis4.properties.user.username)) 

# PROFILE
print("")
print("Use profile to sign in")
gis5 = arcgis.GIS(
    url=PortalUrl, 
    profile=ProfileName
    )
print("Successfully logged into '{}' via the '{}' user".format(gis5.properties.portalHostname,gis5.properties.user.username)) 

print("Script complete")