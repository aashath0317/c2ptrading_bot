import re
import time
import telegram
from telegram.ext import Updater
import telegram.ext
from telegram.ext import CommandHandler
from time import sleep
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
#from telegram.message import Message
#from telegram.update import Update
from telegram.error import RetryAfter
from pyrogram.errors import FloodWait
from pyrogram import Client
from pyrogram import filters
import sys, traceback
import os
import subprocess
import sys
from datetime import datetime
import glob
import requests
import asyncio
import telethon
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.events import NewMessage
from telethon import events
from metaapi_cloud_sdk import MetaApi
import asyncio
import logging
import math

#session_string = "94755039496,BQAuPHAAJTJsYNzJo67WCOcle9jarh7uYxI1nUZBmbQFLJrep6XqYqbfc8_0L9W3KQKpTO6slV2pf5aF2w5WHN_Lh5n8_qYJTHLmwMsbOR7zqQ6FCZtUFNdpXFlAEpF10uFIHZGPLbY2761VP88lDN9a0YmF31fQiGO-7oeS9pP1wjogd_Aw1bLBdPAT87YJepwAMVuBCycDid6hKHmxmEl0McphpYWijWTnWz7y-6XqUQ0ohkB9nYqugtATWldRcjAZ27JYMplYxHGREVR-wh-DaMVAUT_rykgONMOfXktKQbEFtyRRouP5khywrZM6tmvvWoJrb7i4qZOdzy6MJYEun2WlSQAAAABL5wISAA"
#app = Client(session_name="new",api_id = 3030128,api_hash = 'cfc3885f5d2cbdbc5f10e6a643de2711')
#s = await app.export_session_string()
#app.run()
string='1BVtsOHIBu6uyrely3orb5aEP2hThv6Ah4OJAGRziVuVzL03aZAxP9hIX19jlPLRsA3VHsI9eZQdr8jk-0OLi9Pna-ctebI5oLFTA_HOE2p9JdxlfelTANLr6HP9cXZoAENFDHwGSU8bwxMl3Lp2N-an9vl10HK1TVR09yljJl_CYKUYXQTtx7UMSmg2ztjh7yseQC4fYGg6MVdZvJyfXHS37p4SQzFjt3PqBGfidmVUbf7HhWl6JX3M-xkd8q62nVcZMS5Ks3re6Wb-j5mv_JNXh3dF3hr0Bu2cbPGJpZ5EY7Ggt_lIFcEVp2mNxxSqBvvHLA-C8k4PG2EYoA5YCrjnafcrZ-TQ='
client = telethon.TelegramClient(StringSession(string),api_id=3030128, api_hash='cfc3885f5d2cbdbc5f10e6a643de2711')
client.connect()
API_KEY = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJmOWI4ZGVlMzljMzVhNDY4ZmNmOGE1ZDlkYTAzNzFiZCIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1ycGMtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoicmlzay1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsicmlzay1tYW5hZ2VtZW50LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtdC1tYW5hZ2VyLWFwaSIsIm1ldGhvZHMiOlsibXQtbWFuYWdlci1hcGk6cmVzdDpkZWFsaW5nOio6KiIsIm10LW1hbmFnZXItYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX1dLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiZjliOGRlZTM5YzM1YTQ2OGZjZjhhNWQ5ZGEwMzcxYmQiLCJpYXQiOjE2ODkzMzk5MjV9.NsgW8ziS-GvcqoSK1UEOiheJpun1PViBtrWAqqzWbrsEHfgsAdtnRkt0SwPnQCzdr4kyQSiN7JIBy8Ug1x4mX_aW4xAT9oX8PGRunwh2DLYjSsc8yuw1cOiCKUeg1suZVmEGUB9F1omkF0057_Mx2tgkzN-9a-rANohy5jplhmlcEyj4FjVs6924Tyf9CTGl-O-YJ8YT66163JlTngXhzYOqlxFKSPiPPnNT18aMWE6hq46_n4LAC-1Owm4Xm_yp_TH3q09ve_SAP01phIYgSy7YI_n3hJOfIR3MWXyghqMTjm7hWovYaq9w47mhkuqlZ5kmhYDSVtIw0ClW0gp02HDH5-HG0tQQuZZ9eVdcmD-IYRiyldV7SDVNQPGP4YLKjwkVB9bThATtOKzVjfwzgSbkLvp0NcmZ0U7rLacSTCXezJdy4gXOK41fA6b67re-nVxwnNuN7cLfjMHUNtWJtroc6nYDJJpIWxOYgiATDgumonbhCtJvOlkww88lHvEUYZwxhjUHGNmbcw116Jg9Litpiqt-MhwylqcrX0UHjfZhMhK-il-yZF-MdRcoU-pUFI_GiMbDUnn6KwkEOgHz0DJEHJpsV7eS89I6ZzN_XyAHG6PpfSBHK1QkXzhAWqWPyiamlgoB7QQF-yCkiRmQehZY8xvHhg8Dq5xuLVpNeS0"
ACCOUNT_ID = "8d735df5-6f9f-451f-a5f6-952183f72aae"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

channel_id = -1001963686318
#group_id = "@C2P_forex_bot"   #5007713837
igroup = -990951103

@client.on(events.NewMessage(chats=channel_id))
async def my_event_handler(event):
    message = str(event.text)
    #send_channel = message.chat.title
    pair = ""
    string = message
    tstring = string.split("\n")
    def remove_empty_datatypes(list_of_strings):
        new_list = []
        for string in list_of_strings:
            if string:
                new_list.append(string)
        return new_list
    try:
        list_of_strings = tstring
        tstring = remove_empty_datatypes(list_of_strings)
        pao = tstring[0].split(" ")
        pair = pao[0]
        order = pao[1]
        order_check = pao[2].upper()
    except IndexError:
         await client.send_message(igroup, 'Trading Not Placed \n Check this string  \n '+str(tstring))
         return
    if order_check == "NOW":
        sl = str(tstring[1].split(":")[1].strip(" "))
        tp1 = str(tstring[2].split(":")[1].strip(" "))
        tp2 = str(tstring[3].split(":")[1].strip(" "))
        if pair == "GOLD":
            pair = "XAUUSD"
        else:
            pass 
        s_message = order+" "+pair+"\n"+"Entry NOW"+"\n"+"SL "+sl+"\n"+"TP "+tp1
       # s_message = order+" "+pair+"\n"+"Entry NOW"+"\n"+"SL "+sl+"\n"+"TP1 "+tp1+"\n"+"TP2 "+tp2
        await client.send_message(group_id, "/trade")
        await client.send_message(group_id, s_message)
        api = MetaApi(API_KEY)
        account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
        initial_state = account.state
        deployed_states = ['DEPLOYING', 'DEPLOYED']
        if initial_state not in deployed_states:
                #  wait until account is deployed and connected to broker
            logger.info('Deploying account')
            await account.deploy()

        logger.info('Waiting for API server to connect to broker ...')
        await account.wait_connected()

            # connect to MetaApi API
        connection = account.get_rpc_connection()
        await connection.connect()
        logger.info('Waiting for SDK to synchronize to terminal state ...')
        await connection.wait_synchronized()
        await client.send_message(igroup, 'connecting to metatrader')
        account_information = await connection.get_account_information()
        await client.send_message(igroup, 'Successfuly connected')
        #current_price=terminalState.price(symbol='EURUSD')
        current_price = await connection.get_symbol_price(symbol='XAUUSD')
        bid = float(current_price['bid'])
        ask = float(current_price['ask'])
        spread = ask - bid
        print(spread)
        
    else:
        await client.send_message(igroup, 'Trading Not Placed \n Check this string  \n '+str(tstring))




@client.on(events.NewMessage(chats=channel_2))
async def my_event_handler(event):
    message = str(event.text)
    await client.send_message(igroup, message)


#from telegram import ParseMode, Update
#token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJmOWI4ZGVlMzljMzVhNDY4ZmNmOGE1ZDlkYTAzNzFiZCIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1ycGMtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoicmlzay1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsicmlzay1tYW5hZ2VtZW50LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtdC1tYW5hZ2VyLWFwaSIsIm1ldGhvZHMiOlsibXQtbWFuYWdlci1hcGk6cmVzdDpkZWFsaW5nOio6KiIsIm10LW1hbmFnZXItYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX1dLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiZjliOGRlZTM5YzM1YTQ2OGZjZjhhNWQ5ZGEwMzcxYmQiLCJpYXQiOjE2ODk0NDQ1NDF9.m9mEFct9EnPUU1QLox9qF34PjRTTaCQ08gou3mXJz3i7d-0w7MKzkxojBGh47sZ3f-y5jypBLMYLTNnZ-ezb3hOL9zkeYH2r44KQ9kuYZw0CG-NPi-OdhEbwjWMfaQo13jhunFm2UyoUsjx7U6yHLVo1Fzs7jzMUo9OUgzJO-cscbZJ1Qg129jGk87y1pO7G38SM9a8DwK6pCTfnfb6wkbxIYPwrnxL9XTa6KXVbDnmXBUNIbXDMG2xxjCOM0h3wqRowzwjiWqz8hMEdy0CNXfwmx_C-iAMigdXZOPieea3KHpK8HTPzWS2b8AJ80LbpXWSSRziKdModrGdauARbzRIjzTBzS0E6mh538iPm8JddcCrCCVC16fSgJIPaD28Q-0Oh8mRl5dWEY1yq9elyjGFRhN3ePAsV7qvd7cn35OVi8fHqyWR3CdNg2PvvUs7JerhmC1xfHVRmcIxgKe6fOaB3u1EHg2XFQivb_P_GD3ZAM8JQ8QYfsFM5dHbClxHCOXzx8psNYIYB9wYlXborbIlSaHvo-jKYJtrtkp9GAAEbPSIxMUZLr5Qw7bKxH0bXBBJgFw5UFugvZ0LLE0u9pROUtm1q2iMZPL0_I4_lnupP1TLuBYF6pfdJrnwGSvdXzSh86S0bXe7R7HsyKa0-36-C6qm9wTckbi2ZHSZRqso"


#async def ConnectMetaTrader(trade: dict, enterTrade: bool):
'''
async def ConnectMetaTrader(pair):
    api = MetaApi(API_KEY)
    account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
    initial_state = account.state
    deployed_states = ['DEPLOYING', 'DEPLOYED']
    if initial_state not in deployed_states:
            #  wait until account is deployed and connected to broker
        logger.info('Deploying account')
        await account.deploy()

    logger.info('Waiting for API server to connect to broker ...')
    await account.wait_connected()

        # connect to MetaApi API
    connection = account.get_rpc_connection()
    await connection.connect()
    logger.info('Waiting for SDK to synchronize to terminal state ...')
    await connection.wait_synchronized()
    print("connecting to metatrader")
    account_information = await connection.get_account_information()
    print("Successfuly connected")
    #current_price=terminalState.price(symbol='EURUSD')
    current_price = await connection.get_symbol_price(symbol='XAUUSD')
    bid = float(current_price['bid'])
    ask = float(current_price['ask'])
    spread = ask - bid
    print(spread)
    

client.start()
client.run_until_disconnected()
