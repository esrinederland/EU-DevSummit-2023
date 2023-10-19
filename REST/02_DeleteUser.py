import Settings
import requests

## Generate token
print("Getting token")
token = Settings.GenerateToken()

## SETTINGS
userToDelete = ""
targetUser = ""
userUrl = f"https://www.arcgis.com/sharing/rest/content/users/{userToDelete}/"

## Get content for user
contentParams = {
    "num": 100,
    "q": f"owner:{userToDelete}"
}
contentUrl = f"https://www.arcgis.com/sharing/rest/search?f=json&token={token}"

print("Retrieving items")
contentResponse = requests.get(contentUrl, contentParams).json()
print(f"{contentResponse['total']} items found")

itemIDs = ",".join([item["id"] for item in r["results"]])

## Check if items can be reassigned
reassignParams = {
    "items": itemIDs,
    "targetUsername": targetUser
}
checkUrl = f"{userUrl}/canReassignItems?f=json&token={token}"

print("Checking reassign items")
checkResponse = requests.post(checkUrl, reassignParams).json()

successIDList = [result["itemId"] for result in checkResponse["results"] if result["success"]]
print(f"Able to reassign {len(successIDList)} items")
successIDs = ",".join(successIDList)

## Reassign items
reassignParams["items"] = successIDs
reassignUrl = f"{userUrl}/reassignItems?f=json&token={token}"

print("Reassigning items")
reassignResponse = requests.post(reassignUrl, reassignParams).json()
successCount = len([result["itemId"] for result in reassignResponse["results"] if result["success"]])
print(f"Reassigned {successCount} items")

## Delete User
deleteUserUrl = f"{userUrl}/delete?f=json&token={token}"

print("Deleting user")
deleteResponse = requests.post(deleteUserUrl).json()
if deleteResponse["success"]:
    print(f"Successfully deleted user {deleteResponse['username']}")
