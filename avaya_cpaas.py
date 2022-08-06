#!/usr/bin/env python3

#
# Imports
#
import sys

try:
    import requests
except ImportError as ie:
    print(ie)
    # python3 -m pip install requests
    sys.exit("Please install python-requests!")
# try:
#     import urllib3
# except ImportError as ie:
#     print(ie)
#     # This comes as dependency of requests, so should always be there.
#     # python3 -m pip install urllib3
#     sys.exit("Please install urllib3!")
#import datetime
from mysecrets import secrets

print("List Calls:")
res = requests.get(f"{secrets['baseURL']}/Accounts/{secrets['accountSID']}/Calls.json", auth=(secrets["accountSID"], secrets["authToken"]))
if res.status_code == 200:
    print(res.json())

print("List Usages:")
res = requests.get(f"{secrets['baseURL']}/Accounts/{secrets['accountSID']}/Usages.json", auth=(secrets["accountSID"], secrets["authToken"]))
if res.status_code == 200:
    print(res.json())    

sms_data = f"To={secrets['toNbr']}&From={secrets['fromNbr']}&Body=This is a test message from Avaya CPaaS"

print("Send SMS")
res = requests.post(f"{secrets['baseURL']}/Accounts/{secrets['accountSID']}/SMS/Messages.json", auth=(secrets["accountSID"], secrets["authToken"]), data=sms_data)
if res.status_code == 200:
    print("SUCCESS")
    print(res.json())
else:
    print(res.json())

print("List Notifications:")
res = requests.get(f"{secrets['baseURL']}/Accounts/{secrets['accountSID']}/Notifications.json", auth=(secrets["accountSID"], secrets["authToken"]))
if res.status_code == 200:
    print(res.json())    

print("List local available numbers in UK:")
res = requests.get(f"{secrets['baseURL']}/Accounts/{secrets['accountSID']}/AvailablePhoneNumbers/GB/Local.json", auth=(secrets["accountSID"], secrets["authToken"]))
if res.status_code == 200:
    print(res.json())
