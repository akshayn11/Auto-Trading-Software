import asyncio
import json
import pandas as pd
import webbrowser
from datetime import datetime,date
import time
import configparser
import warnings
import requests
import os
import angel_login
import threading
import sys
import os
import pandas as pd
import requests
from datetime import datetime,timedelta
import logging

smartApi = angel_login.smartApi
contract_hub_exchng={}
df=None

def setup_logging():
    base_log_dir = 'software_logs'
    if not os.path.exists(base_log_dir):
        os.makedirs(base_log_dir)
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    log_dir = os.path.join(base_log_dir, date_str)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, f"application_{datetime.now().strftime('%H-%M-%S')}.log")
    
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )
    return logging.getLogger()

logger = setup_logging()
# print(logger)
# sys.exit()

def is_within_allowed_date_range():
    """
    Checks if today's date is within the allowed date range (19-08-2024 to 20-08-2024).

    Returns:
        bool: True if the date is within the range, False otherwise.
    """
    start_date = datetime(2024, 8, 19)
    end_date = datetime(2024, 8, 20)
    today_date_obj = datetime.today()
    return start_date <= today_date_obj <= end_date


def preprocess_contract_hub_exchange():
    global df
    global contract_hub_exchng
    global logger
    """
    Preprocesses data by checking if today's CSV file is present. 
    If not, downloads data from the API, filters it, saves it to a CSV file, 
    and creates a dictionary with exchange token as the key and other details as values.

        dict: The dictionary containing the filtered contract hub exchange data.
    """

    # if not is_within_allowed_date_range():
    #     print("[!] The program is not allowed to run outside the date range 19-08-2024 to 20-08-2024.")
    #     return

    today_date = datetime.today().strftime('%Y%m%d')
    instruments_file = f"{today_date}_instrument_file.csv"

    previous_date = (datetime.today() - timedelta(days=1)).strftime('%Y%m%d')
    previous_file = f"{previous_date}_instrument_file.csv"
    if os.path.isfile(previous_file):
        os.remove(previous_file)

    if os.path.isfile(instruments_file):
        print(f"[+]  Instrument file is already present for today.")
        logger.info("[+]  CSV file not found for today. Downloading...")
        filtered_df = pd.read_csv(instruments_file, index_col='token')
        df = pd.read_csv(instruments_file)
        # print("df is present",df)
    else:
        print("[+]  CSV file not found for today. Downloading...")
        logger.info("[+]  CSV file not found for today. Downloading...")
        url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
        requests_data = requests.get(url).json()
        df = pd.DataFrame.from_dict(requests_data)
        df['token'] = df['token'].astype(str)
        filtered_df = df[(df['exch_seg'].isin(['NFO', 'BFO']) ) & (df['instrumenttype'].isin(['OPTIDX', 'FUTIDX']))  ]
        filtered_df.set_index(['token'], inplace=True)
        filtered_df.to_csv(instruments_file)
        df = pd.read_csv(instruments_file)
        print("[+]  Instrument file Downlaoded succefully")
        logger.info("[+]  Instrument file Downlaoded succefully")
        # print(f"Filtered data has been saved to {instruments_file}")

    contract_hub_exchng = filtered_df.to_dict(orient='index')
    
    # print(contract_hub_exchng)

    # return contract_hub_exchng
preprocess_contract_hub_exchange()


# sys.exit()

map_dict={"NIFTY 50":{'NAME':'NIFTY','SEGMENT':'NFO'},
          'NIFTY BANK':{'NAME':'BANKNIFTY','SEGMENT':'NFO'},
          'NIFTY FIN SERVICE':{'NAME':'FINNIFTY','SEGMENT':'NFO'},
          'NIFTY MID SELECT':{'NAME':'MIDCPNIFTY','SEGMENT':'NFO'},
          'SENSEX':{'NAME':'SENSEX','SEGMENT':'BFO'},
          'BANKEX':{'NAME':'BANKEX','SEGMENT':'BFO'},

          }

exchange_token_hub={}

def fetch_exchange_tokens(index_value, list_of_expiries):
    '''This will fetch the all the exchange tokens for angel'''
    global df
    global exchange_token_hub 

    index_name = map_dict[index_value]['NAME']
    segment = map_dict[index_value]['SEGMENT']
    
    df['expiry'] = pd.to_datetime(df['expiry'], dayfirst=True)
    df['expiry_str'] = df['expiry'].astype(str)
    
    filtered_df = df[(df['name'] == index_name) & (df['exch_seg'] == segment)]

    
    for expiry in list_of_expiries:
        tokens_for_ce_expiry = filtered_df[(filtered_df['expiry_str'] == expiry) & (filtered_df['symbol'].str.endswith("CE")) ]
        tokens_for_pe_expiry = filtered_df[(filtered_df['expiry_str'] == expiry) & (filtered_df['symbol'].str.endswith("PE")) ]
        # tokens_for_ce_expiry = filtered_df[(filtered_df['expiry_str'] == expiry) ]
        key=f"{index_value}_{expiry}"
        ce_tokens = [str(token) for token in tokens_for_ce_expiry['token'].tolist()]
        pe_tokens = [str(token) for token in tokens_for_pe_expiry['token'].tolist()]
        exchange_token_hub[key]={"CE":ce_tokens,"PE":pe_tokens}
        # print(exchange_token_hub)
    return exchange_token_hub


def get_keys_from_value(d, target_value):
    '''This function will return the instrument token from the exchange token'''

    keys = [key for key, value in d.items() if value.get('exchange_token') == target_value]
    return keys

freeze_lotsize_dict=requests.get('https://9mbqrxwx53.execute-api.ap-south-1.amazonaws.com/default/lotsize_freeze_limits').json()

def convert_dates_to_strings(dates):
    return [date.strftime('%Y-%m-%d') for date in dates[:5]]


def get_recent_expiry(index_value):
    global df
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        try:
            df['expiry'] = pd.to_datetime(df['expiry'], dayfirst=True)
        except Exception as e:
            print(f"An error occurred while parsing dates: {e}")
            logger.info(f"[+]  Instrument file Downlaoded succefully {e}")
            return None, None  # Or handle the error as needed

    index_name=map_dict[index_value]['NAME']
    segment=map_dict[index_value]['SEGMENT']
    filtered_df_for_nifty = df[(df['name'] == index_name)  & (df['exch_seg'] == segment)]
    # print(filtered_df_for_nifty)
    unique_expiry_dates = {timestamp.date() for timestamp in filtered_df_for_nifty['expiry']}

    today = datetime.now().date()
    # closest_date = min(unique_expiry_dates, key=lambda x: abs(x - today))
    sorted_dates = sorted(unique_expiry_dates, key=lambda x: abs(x - today))
    list_of_expiries=convert_dates_to_strings(sorted_dates)
    exchange_tokens= fetch_exchange_tokens(index_value,list_of_expiries)
    return ({index_name : list_of_expiries},exchange_tokens)
# get_recent_expiry("NIFTY 50")


# --------------------------------------------------Websocket Conenctivity---------------------------------------------------------------------

from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from logzero import logger
correlation_id = "abc123"
action = 1
mode = 3

ltp_dict={}
data_dict = {}
data_dict_exchng={}  

token_list = [
    {
        "action": 1,
        "exchangeType": 2,
        "tokens": ["35830","35822"]
    }
]

sws = SmartWebSocketV2(angel_login.AUTH_TOKEN, angel_login.API_KEY, angel_login.CLIENT_CODE, angel_login.FEED_TOKEN)

def on_ticks(wsapp, message):
    # logger.info("Ticks: {}".format(message))
    # print("Ticks: {}".format(message))
    # print(f"{message['token']} : {message['last_traded_price']}")
    # ltp_dict[message['token']] = message['last_traded_price']
    # print("ltp dict is",ltp_dict)
    # close_connection()
    data_dict_exchng[message['token']]=(message['last_traded_price']) / 100

    # print(data_dict_exchng)
    
    # print(ltp_dict)

def on_open(wsapp):
    logger.info("on open")
    sws.subscribe(correlation_id, mode, token_list)
    # sws.unsubscribe(correlation_id, mode, token_list1)

def on_error(wsapp, error):
    logger.error(error)

def on_close(wsapp):
    logger.info("Close")

def close_connection():
    sws.close_connection()


# Assign the callbacks.
sws.on_open = on_open
sws.on_data = on_ticks
sws.on_error = on_error
sws.on_close = on_close

# sws.connect()
threading.Thread(target=sws.connect).start()


# ----------------------------------------------------------------------------------------------------------------------------------------

all_expiries = {}

for i in map_dict: 
    item, exchange_token_hub = get_recent_expiry(i)
    # item1,exchange_token_hub=get_recent_expiry(i)
    all_expiries.update(item)
# print(exchange_token_hub)

# sys.exit()
###----------------------------- UI PART ---------------------------------------------------##

# import vinod_shukla_ui
import auto_trading_ui

import wx
# import wx.xrcpy 
import wx.grid
# print("Excahneg hub is",contract_hub_exchng)
# sys.exit()

class CalcFrame(vinod_shukla_ui.MyFrame1): 
   def __init__(self,parent): 
        global smartApi
        vinod_shukla_ui.MyFrame1.__init__(self, parent)

app = wx.App(False) 
frame = CalcFrame(None)
# print("Excahneg hub is",contract_hub_exchng)
frame.set_broker_obj(all_expiries,map_dict,data_dict,smartApi,sws,exchange_token_hub,data_dict_exchng,contract_hub_exchng.copy(),mode,correlation_id,freeze_lotsize_dict)
# frame.set_angel_obj(smartApi,sws,exchange_token_hub,all_expiries.copy(),map_dict,data_dict_exchng,contract_hub_exchng.copy())
frame.Show(True) 
app.MainLoop() 