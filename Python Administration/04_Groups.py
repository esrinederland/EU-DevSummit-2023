##### ARCGIS ONLINE #####

import arcgis
from Settings import AgolUrl,AgolProfileName

print("Getting GIS")
gis = arcgis.GIS(AgolUrl, profile=AgolProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gis.properties.portalHostname,gis.properties.user.username)) 

# CREATE A NEW GROUP
print("Creating new group")
GroupTitle = "Doomed To Stay"
GroupDescription = "This is a group created for the 2023 DevSummit. The word is: DevSummit"
GroupTags = "DevSummit2023, Demo, NoLeaving"
GroupIconPath = r"D:\Data\Group_Image.png"

newGroup = gis.groups.create(
    title=GroupTitle, 
    description=GroupDescription, 
    tags=GroupTags, 
    access='private',
    max_file_size=500000 , 
    leaving_disallowed=True,
    thumbnail=GroupIconPath
    )
print(f"Group '{newGroup.title}' created!")

# ADD USERS
groupUsers = ['mholtslag_esrinl_events', 'mvanhulzen_esrinl_events']
print("Adding users to group")
usersAdded = newGroup.add_users(groupUsers)
if len(usersAdded['notAdded']) > 0:
    for i, notAddedUser in enumerate(usersAdded['notAdded']):
        print(f"{notAddedUser} was not added: ")

for user in groupUsers:
    if user not in usersAdded['notAdded']:
        print(f"User '{user}' was successfully added to the group.")

# CHANGE DESCRIPTION
descriptionUpdated = newGroup.update(description='You are really not allowed to leave this group...')
print(f"Update result: {descriptionUpdated}")

print("Script complete")