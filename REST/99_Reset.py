import Settings
import requests

def main():
    print("Script start")
    token = Settings.GenerateToken()

    #delete group
    RemoveGroups(token)
    #create user

    #add content

    #delte webmap

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

if __name__ == '__main__':
    main()