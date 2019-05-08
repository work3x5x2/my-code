#!/usr/bin/env python3

import requests

def main ():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startdate = 'start_date=2019-05-08'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=DEMO_KEY'

    neourl += startdate + mykey
    neojson = (requests.get(neourl)).json()

    print(neojson)

main()
