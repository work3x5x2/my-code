#!/usr/bin/env python3
import urllib.request
import json
## Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

## Call the webservice
groundctrl = urllib.request.urlopen(majortom)

## put fileobject into helmet
helmet = groundctrl.read()

## decode json to python data structure
helmetson = json.loads(helmet.decode('utf-8'))

for key, value in helmetson.items():
    new_dict = value

print(new_dict)
#for key, value in new_dict.items(): 
    #dict =  [ key : value ]
    #print(dict.key, dict.value)
    #print(value.get('name'))
    #for key, value in helmetson.items()

#print(helmetson.value, "\n")

## display our pythonic data
print("\n\nConverted python data")
print(helmetson)

# print(helmetson.value, "\n")

print('\n\nPeople in Space: ', helmetson['number'])
people = helmetson['people']
print(people)
