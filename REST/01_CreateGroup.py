import Settings
import requests

# generate token
print("Getting token")
token = Settings.GenerateToken()


### SET THE GROUP PARAMETERS
print("Creating group parameters")
newGroupName = "Demo Group for EUDevSummit23"
newGroupDesc = "Group to show how to create groups, the word is: "
newGroupParams = {'title':newGroupName,'access':'account','description':newGroupDesc, "isViewOnly":True,"isInvitationOnly":True,"tags":"EUDevSummit23, REST"}

url='https://www.arcgis.com/sharing/rest/community/createGroup?f=json&token={}'.format(token)

### SEND THE REQUEST TO CREATE THE GROUP
print("Sending request")
r = requests.post(url,newGroupParams)
print(r.json())

print("Script complete")

