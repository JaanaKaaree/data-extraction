import requests
import json
from pandas.io.json import json_normalize

import configparser
config = configparser.RawConfigParser()
config.read('config.ini')

APIKEY = config.get('Google', 'google_api_key')
print (APIKEY)


def findPlaces(loc=("46.814309","-71.207917"),radius=10000, pagetoken = None):
   lat, lng = loc
   type = "police"
   url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={APIKEY}{pagetoken}".format(lat = lat, lng = lng, radius = radius, type = type,APIKEY = APIKEY, pagetoken = "&pagetoken="+pagetoken if pagetoken else "")
   print(url)
   try:
   	response = requests.get(url)
   except requests.exceptions.RequestException as e:
   	print (e)

   
   res = json.loads(response.text)
   df = json_normalize(res['results'])
   df = df[df.columns[df.columns.isin(['id', 'name','rating','user_ratings_total','types'])]]
   print('no of columns')
   print(len(df.columns))
   print (df.columns.values.tolist())
   print (df)

   pagetoken = res.get("next_page_token",None)

   #print("here -->> ", pagetoken)

   return pagetoken

pagetoken = None

while True:
     pagetoken = findPlaces(pagetoken=pagetoken)
     import time
     time.sleep(5)

     if not pagetoken:
         break