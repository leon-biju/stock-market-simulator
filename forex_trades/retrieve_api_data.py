import requests
import json
import os.path
from django.conf import settings


def getAPIKey() -> str:
  file_path = os.path.join(settings.BASE_DIR, "forex_trades", "API_KEY.txt")
  if not os.path.isfile(file_path):
    print("API_KEY.txt not found in this directory please provide an api key file")
    exit(1)
  with open(file_path) as f:
    apikey = f.readline().strip()
  return apikey

def getJSONExchangeRates(api_key: str):
  #for NOW send an api request every time this is called.HOWEVER
  #Will need to use a cache based system for the api calls

  currencies = []
  url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/GBP"
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    return data["conversion_rates"]
  else:
    return None