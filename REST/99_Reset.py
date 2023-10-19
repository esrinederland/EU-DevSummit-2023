import Settings
import requests

def main():
    print("Script start")
    token = Settings.GenerateToken()

    #delete group
    RemoveGroups(token)

    #create user

    #add content

    #delete webmap

    #delete features from surveyservice

    #

    print("Script complete")

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
    items = searchPortalItems(f"tags:{tags} AND owner:{Security.GetUsername()}",token)
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
            Security.GetUsername(), item["id"], token
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


if __name__ == '__main__':
    main()