import socket
import keyring
import requests
import datetime

#PortalUrl = "https://devteam.esri.nl/portal"
KeyringKeyword = "EUDevSummit2023_REST"
Username = "devteamesrinl"
if socket.getfqdn() == "ESRIBX0814.esrinl.com":
    Username = "mvanhulzen_esrinl_events"

def GetPassword():
    pwd = keyring.get_password(KeyringKeyword, Username)
    if pwd is None:
        print("No password set for {}: {}".format(KeyringKeyword, Username))  
    return pwd

def GenerateToken():
    print("GenerateToken::Start")
    
    # Get token
    token_URL = 'https://www.arcgis.com/sharing/generateToken'
    token_params = {'username':Username,'password':GetPassword(),'referer': "https://www.arcgis.com",'f':'json','expiration':60}
    
    r = requests.post(token_URL,token_params)
    token_obj= r.json()
    
    token = token_obj['token']
    expires = token_obj['expires']

    tokenExpires = datetime.datetime.fromtimestamp(int(expires)/1000)

    print("new token: {}".format(token))
    print(f"token for {Username} expires: {tokenExpires}")
    return token


