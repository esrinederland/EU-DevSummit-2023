##### ARCGIS ENTERPRISE #####

import arcgis
from Settings import PortalUrl,ProfileName
import datetime
import os

from pathlib import Path

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

ux = gis.admin.ux

# CHANGE HOMEPAGE TITLE
newTitle = "DevTeam Server [European DevSummit 2023]"
ux.homepage_settings.set_title(newTitle)
print(f"Home page title updated to {newTitle}")

# CHANGE HOMEPAGE BACKGROUND
filename = Path(r'D:\Data\background.jpg')
if filename.exists():
    ux.homepage_settings.set_background(
        background_file=filename
        )
else:
    print("file does not exist!")

# CHANGE PORTAL NAME
editDatTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
ux.name = f"Our Fabulous portal {editDatTime}"

# SET INFORMATINONAL BANNER
ux.security_settings.set_informational_banner(
    text=f"Information: This Portal's look and feel was updated on {editDatTime}", 
    bg_color="white", 
    enabled=True)

print("Script complete")