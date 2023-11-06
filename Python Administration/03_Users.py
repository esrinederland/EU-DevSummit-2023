##### ARCGIS ENTERPRISE #####

import arcgis
from Settings import PortalUrl,ProfileName

print("Getting GIS")
gis = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

# SETTING USER PARAMETERS
NewUsername = "DevDayUser"
PassWord = "5BC76C4C9865774F0B08ABE3AC8A4DD455234A8872AD2B5D0611467F8B536C59"
FirstName = "DevSummit"
LastName = "User"
EmailAddress = "developers@esri.nl"
UserDesc = "This is a newly created user for the 2023 DevSummit. The word is: DevSummit2023"
UserType= "Viewer"
UserImage = r"D:\Data\User_Image.png"
roleId = "iAAAAAAAAAAAAAAA" #defaults to viewer role

# CREATE THE USER
print("Creating user")
newUser = gis.users.create(
    username=NewUsername, 
    password=PassWord, 
    firstname=FirstName, 
    lastname=LastName, 
    email=EmailAddress, 
    description=UserDesc, 
    role=roleId, 
    user_type = UserType,
    thumbnail=UserImage
    )
print(newUser)

print("Script complete")