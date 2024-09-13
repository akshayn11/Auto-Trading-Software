from SmartApi  import SmartConnect
import pyotp,time
import threading
import requests
import pandas as pd

requests_data=requests.get("https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json").json()
df=pd.DataFrame.from_dict(requests_data)
df['expiry2']=pd.to_datetime(df['expiry'], format= "mixed").apply(lambda x:x.date())

# print(df

# -------------------------------Login Code for Angle------------------------------------  






API_KEY= "xxxxxxxxxxx"

totp_key="xxxxxxxxxxxxx"
CLIENT_CODE= "xxxxxxxx"
pin= "xxxxxxxx"

smartApi = SmartConnect(api_key=API_KEY)

def validate_client(refresh_token):
    global smartApi
    data=smartApi.getProfile(refresh_token)
    cid=data["data"]['clientcode']
    valid_client_id=['xxxxxx','xxxxxx']
    if cid in valid_client_id:
        print(f"[+]  Welcome {data['data']['name']}")
        return True
    else:
        print("[+]  Client id is not available. Please contact to developer..!")
        return False


while True:
    data = smartApi.generateSession(CLIENT_CODE, pin,pyotp.TOTP(totp_key).now())
    # print(data)
    AUTH_TOKEN = data['data']['jwtToken']
    refreshToken = data['data']['refreshToken']
    if validate_client(refreshToken):
        break

    else: 
        print("[+]  Retrying validation...")
# fetch the feedtoken
FEED_TOKEN = smartApi.getfeedToken()
# fetch User Profile
res = smartApi.getProfile(refreshToken)
smartApi.generateToken(refreshToken)
res=res['data']['exchanges']