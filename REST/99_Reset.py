import Settings
import requests

def main():
    print("Script start")
    token = Settings.GenerateToken()

    #delete group
    RemoveGroups(token)

    #create user and reassign items
    createUserAndReassignItems(token)
    EmptySurveyResultsService(token)
    #add content

    #delete webmap

    #delete features from surveyservice

    #
    RemoveOprahResults06(token)

    print("Script complete")


def EmptySurveyResultsService(token):
    #delete features from surveyservice
    print("EmptySurveyResultsService")
    surveyServiceUrl = "https://services9.arcgis.com/7e6lF03RcLhwFtm5/arcgis/rest/services/survey123_d4b3ab2513384ea48ae3cb62a9e0e5df_form/FeatureServer/0/deleteFeatures"
    params = {'token':token,'f':'json','where':'1=1'}
    r = requests.post(surveyServiceUrl,params)
    print(r.text)

def RemoveGroups(token):
    #remove 4 groups
    groupSearchUrl = "https://www.arcgis.com/sharing/rest/community/groups"
    query = f"tags:EUDevSummit23"
    params = {'token':token,'f':'json','q':query}
    
    print(f"Sending group search request: {query}")
    groupSearchResult = requests.post(groupSearchUrl,params)
    groupSearchResultJson = groupSearchResult.json()
    for group in groupSearchResultJson["results"]:
        print(f"Deleting group: {group['title']} ({group['id']})")

        deleteGroupUrl = f"https://www.arcgis.com/sharing/rest/community/groups/{group['id']}/delete"
        params = {'token':token,'f':'json'}
        r = requests.post(deleteGroupUrl,params)
        print(r.text)

def RemoveOprahResults06(token):
    # remove webmaps from oprah
    webmapSearchUrl = "https://www.arcgis.com/sharing/rest/search"
    tags = "EUDevSummit23"

    ##Demo 14 Oprah
    print("Remove Webmaps")
    #items = searchPortalItems(f"type:Web Map AND tags:{tags} AND owner:{Security.GetUsername()}",token)
    items = searchPortalItems(f"tags:{tags} AND owner:{Settings.Username}",token)
    print("nrof items found: {}".format(len(items)))
    counter = 0
    for item in items:
        counter += 1
        print(
            "deleting {} with title {} id {}, {}/{}".format(
                item["type"], item["title"], item["id"], counter, len(items)
            )
        )

        url = "https://www.arcgis.com/sharing/rest/content/users/{}/items/{}/delete?f=json&token={}".format(
            Settings.Username, item["id"], token
        )

        # dummy params to force post
        r = requests.post(url)
        print(r.text)

    print("Script complete")

def searchPortalItems(wherestring, token, start=1):
    print("SearchPortalItems::start:{},{}".format(wherestring, start))
    questionParams = {"q": wherestring, "sortField": "name", "start": start, "num": 100}
    url = r"https://www.arcgis.com/sharing/rest/search?f=json&token={}".format(token)
    print("Start searching portal: {}, start: {}".format(wherestring, start))

    r = requests.post(url, questionParams)
    retObject = r.json()
    # retObject = _sendRequest(url,questionParams)
    returnResults = []
    if retObject["total"] > 0:
        returnResults = retObject["results"]
        if "nextStart" in retObject:
            if retObject["nextStart"] > start:
                extraResults = searchPortalItems(
                    wherestring, token, retObject["nextStart"]
                )
                returnResults = returnResults + extraResults

    else:
        print("No results for wherestring: {}".format(wherestring))
    return returnResults

def createUserAndReassignItems(token):
    ## User settings
    inviteParams = {"invitationList":'{"invitations":[{"email":"mholtslag@esri.nl","firstname":"Student","lastname":"Intern","username":"intern_esrinl_events","password":"intern_esrinl_events0","role":"xFfw0BwQVw0N6Yj4","userLicenseType":"creatorUT","fullname":"Student Intern","userType":"arcgisonly","groups":"","userCreditAssignment":500,"applyActUserDefaults":False}]}'}
    inviteUrl = f"https://www.arcgis.com/sharing/rest/portals/self/invite?f=json&token={token}"

    r = requests.post(inviteUrl, inviteParams)
    print(r.text)

    ## Reassign items
    itemIDs = "2f05a537faea4b24b62b09724381235b"
    reassignParams = {
        "items": itemIDs,
        "targetUsername": "intern_esrinl_events",
        "targetFoldername": "intern_esrinl_events"
    }
    reassignUrl = f"https://www.arcgis.com/sharing/rest/content/users/archief_esrinl_events/reassignItems?f=json&token={token}"

    r = requests.post(reassignUrl, reassignParams)
    print(r.text)

if __name__ == '__main__':
    main()