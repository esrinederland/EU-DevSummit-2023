##### ARCGIS ONLINE #####

import arcgis
from Settings import AgolUrl,AgolProfileName,PortalUrl,ProfileName

gisAgol = arcgis.GIS(AgolUrl, profile=AgolProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gisAgol.properties.portalHostname,gisAgol.properties.user.username))

gisEnterprise = arcgis.GIS(PortalUrl, profile=ProfileName)
print("Successfully logged into '{}' via the '{}' user".format(gisEnterprise.properties.portalHostname,gisEnterprise.properties.user.username))

# COLLABORATION PROPERTIES
collaborationName = "EsriNL Events + EsriNL DevTeam"
collaborationDescription = "Data sharing initiative between EsriNL Events and EsriNL DevTeam"

# CREATE COLLABORATION
collaborationCreated = gisAgol.admin.collaborations.collaborate_with(
    guest_gis=gisEnterprise, 
    collaboration_name=collaborationName, 
    collaboration_description=collaborationDescription
    )

# GET COLLABORATION
collaboration = [collab for collab in gisAgol.admin.collaborations.list() if collaborationName in collab.name][0]
print(f"Successfully created collaboration '{collaboration.name}'")

collaborationWorkspaceID = collaboration.workspaces[0]["id"]
collaborationGroupID = collaboration.workspaces[0]["participantGroupLinks"][0]["portalGroupId"]
collaborationGroupName = collaboration.workspaces[0]["participantGroupLinks"][0]["portalGroupName"]

# UPDATE COLLABORATION SETTINGS
collaboration.update_portal_group_link(
    workspace_id=collaborationWorkspaceID, 
    portal_id=collaborationGroupID, 
    copy_feature_service_data=True
    )
collaboration.update_item_delete_policy(
    participant_id=collaboration["collaborationHostPortalId"], 
    delete_contributed_items=True, 
    delete_received_items=True
    )

# SHARE ITEMS IN COLLABORATION GROUP
items = gisAgol.content.search("tags:earthquakes,DevSummit2023")
sharedItems = gisAgol.content.share_items(
    items=items, 
    groups=[collaborationGroupID]
    )
print(f"Shared {len(sharedItems['results'])} item(s) with the '{collaborationGroupName}' group")

print("Script complete")