#!/usr/bin/env python3

import requests
import pprint

def main ():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    #startdate = "start_date={}".format(input("Enter start date as yyyy-mm-dd: "))
    startdate = 'start_date=2019-05-08'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=DEMO_KEY'

    neourl += startdate + mykey
    neojson = (requests.get(neourl)).json()
    print(neojson)

#def moon_lengths(missdistance):
#    m_length = 238900

#    print(missdistance/m_length)

#moon_lengths(1000000)
main()

