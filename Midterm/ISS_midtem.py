# Author: Dontel Harris
# Course: CSC488-01
# Purpose: Build a containerized Flask application for querying and returning interesting information from the ISS(International Space Station) data
# Professor: Dr. Doswell

import json
import xmltodict
import redis
# import xml.dom.minidom
# import os
# from bs4 import BeautifulSoup
# from xml.etree import ElementTree
# import xml.etree.ElementTree 

global uSelect
    # Import files
#     with open('/CSC488/Midterm/ISS.OEM_J2K_EPH.xml','r') as positional_data:
#     #  positional_dict = xml.dom.minidom.parse('/CSC488/Midterm/ISS.OEM_J2K_EPH.xml')
#      positional_dict = xml.dom.minidom.parse(positional_data)
     
# tree_sighting = ElementTree.parse('XMLsightingUSA.xml')
# root_sight = tree_sighting.getroot()
# # print(root_sight.attrib)

# tree_position = ElementTree.parse('ISS.OEM_J2K_EPH.xml')
# root_position = tree_position.getroot()




#Print all Epochs in positional data
def menu1(doc_position):
 '''
        User has selected to Print all Epochs in positional data
 '''
 #Type hints
 doc_position:dict

 for i in doc_position:
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print(doc_position['ndm']['oem']['body']['segment']['data']['stateVector'])
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")

# Print all information about a specific Epoch
def menu2(index,doc_position):
 '''
        User has selected to Print all stored information about a specific Epoch
 '''

 # Type hints
 index:int
 doc_position:dict
 
 # Throw exception for invalid index
 if(index < 1):
     raise IndexError("Index selected is out of range")
 
 print("----------------------------------------------------------------------------------------------------------------------------------------------------")
 print(doc_position['ndm']['oem']['body']['segment']['data']['stateVector'][index-1])
 print("----------------------------------------------------------------------------------------------------------------------------------------------------")
 
 return

def menu3(doc_sight):
 '''
    User has selected to print all countries from Sighting xml
 '''
 
# Type Hints
 doc_sight:dict

 for i in doc_sight:
    # i == visible passes
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    # Range of keys of doc_sight(dict), visible_passes(key) and visible_pass(value/list)
    for j in range(len(doc_sight['visible_passes']['visible_pass'])):
     print(doc_sight['visible_passes']['visible_pass'][j]['country'])
    # print("Length of dictionary" ,len(doc_sight), "Print i: ", i, "Range of dict length: ", range(len(doc_sight['visible_passes']['visible_pass'])))
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")

def menu4(index,doc_sight):
   '''
     User has selected to print all Information about a specific country from Sighting xml
   '''
   # Type Hints
   doc_sight:dict

   if(index < 1):
     raise IndexError("Index selected is out of range")
    # i == visible passes
   print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    # Range of keys of doc_sight(dict), visible_passes(key) and visible_pass(value/list)
   print(doc_sight['visible_passes']['visible_pass'][index-1]['country'])
    # print("Length of dictionary" ,len(doc_sight), "Print i: ", i, "Range of dict length: ", range(len(doc_sight['visible_passes']['visible_pass'])))
   print("----------------------------------------------------------------------------------------------------------------------------------------------------")

def menu5(country,doc_sight):
   '''
    User has selected to print all Regions associated within a given Country
   '''

   #Type Hints
   country:str
   doc_sight:dict

   print("----------------------------------------------------------------------------------------------------------------------------------------------------")
   for j in range(len(doc_sight['visible_passes']['visible_pass'])):
    if(country == doc_sight['visible_passes']['visible_pass'][j]['country']):
     print(doc_sight['visible_passes']['visible_pass'][j]['region'])
   else:
       print(country," is not listed")
   print("----------------------------------------------------------------------------------------------------------------------------------------------------")

def menu6(region,doc_sight):
    '''
      User has selected to print all information about a specific region. The region requested is passed into THIS function
    '''

    #Type Hints
    region:str
    doc_sight:dict

    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    for j in range(len(doc_sight['visible_passes']['visible_pass'])):
     if(region == doc_sight['visible_passes']['visible_pass'][j]['region']):
      print(doc_sight['visible_passes']['visible_pass'][j])
    else:
       print(region," is not listed")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")

def menu7(region,country,doc_sight):
   '''
    User has selected to print all cities within a given country and region. The region and country names are passed into THIS function
   '''

   #Type Hints
   region:str
   country:str
   doc_sight:dict

   print("----------------------------------------------------------------------------------------------------------------------------------------------------")
   for j in range(len(doc_sight['visible_passes']['visible_pass'])):
     if(country == doc_sight['visible_passes']['visible_pass'][j]['country'] and region == doc_sight['visible_passes']['visible_pass'][j]['region']):
      print(doc_sight['visible_passes']['visible_pass'][j]['city'])
      continue
   else:
       print(region," or ", country, " is not listed")
   print("----------------------------------------------------------------------------------------------------------------------------------------------------")

def menu8(city,doc_sight):
   
   '''
     User has selected to print all information of a city. The city name is passed into THIS function
   '''

   # Type Hints
   city:str
   doc_sight:dict


   print("----------------------------------------------------------------------------------------------------------------------------------------------------")
   for j in range(len(doc_sight['visible_passes']['visible_pass'])):
     if(city == doc_sight['visible_passes']['visible_pass'][j]['city']):
      print(doc_sight['visible_passes']['visible_pass'][j])
      continue
   else:
       print(city, " is not listed")
   print("----------------------------------------------------------------------------------------------------------------------------------------------------")

def main():
    #Global type hints
    doc_sight:dict
    doc_position:dict
    # Parse xml files to Dict
    with open('XMLsightingUSA.xml','r') as sighting_data:
        doc_sight = xmltodict.parse(sighting_data.read())
    with open('ISS.OEM_J2K_EPH.xml','r') as positional_data:
        doc_position = xmltodict.parse(positional_data.read())
    
    # Convert Dict to JSON
    doc_sight_json = json.dumps(doc_sight)
    doc_position_json = json.dumps(doc_position)

    # Create redis object route
    redisS = redis.Redis(host='127.0.0.1',port=6378, db=0)
    


    #Load meteorite data into database
    redisS.set('Sight_Data',doc_sight_json)
    redisS.set('Position_Data', doc_position_json)
    redisS.get('Sight_Data')
    returnJson = json.loads(redisS.get('Sight_Data').decode('utf-8'))
    print(returnJson)
    #Setup Menu
    print("Menu: \n 1. Print Epochs in positional data \n 2. Print all information about a specific Epoch in positional data. \n 3. Print all Countries from sighting data \n 4. Print all information about a specific Country from sighting data")
    print(" 5. Print all Regions associated with a given Country in sighting data \n 6. Print all information about a specific Region in the sighting data \n 7. Print all Cities associated with a given Country and Region in sighting data \n 8. Print all information about a specific City in the sighting data")
    
    #Select 
    uSelect = input(": ")
    # Printing Menu Option
    if(uSelect == '1'):
        # print(uSelect)
        menu1(doc_position)
    elif(uSelect == '2'):
        # print(uSelect)
        index = input("Which index would you like Epochs' information: ")
        menu2(int(index),doc_position)
    elif(uSelect == '3'):
        print(uSelect)
        menu3(doc_sight)
    elif(uSelect == '4'):
        index = input("Which country index would you like information: ")
        menu4(int(index),doc_sight)
    elif(uSelect == '5'):
        country = input("Enter country name: ")
        menu5(country,doc_sight)
    elif(uSelect == '6'):
        region = input("Enter the region you would like information for: ")
        menu6(region,doc_sight)
    elif(uSelect == '7'):
        country = input("Enter requested country: ")
        region = input("Enter the region of the requested country: ")
        menu7(region,country,doc_sight)
    elif(uSelect == '8'):
        city = input("Enter the city for requested information: ")
        menu8(city,doc_sight)
    else:
        print("Invaild index")
        exit()

# Call main function
if __name__ == "__main__":
    main()
