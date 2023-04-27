import json
import random


#Composition list
compo = ["stony", "iron", "stony-iron"]
#Dictionary for all 5 rocks
rocks = {}
geoLat = []
geoLong = []


def geoLatitude():
     geoLat = []
     for i in range(5):
     #Generate Lat 16.0 - 18.0
       latitude = round(random.uniform(16,19), 7)
       geoLat.insert(i, latitude)  
      #  print("\n Latitude: " + str(geoLat[i]))
     return geoLat

# Random number generator Longitude
def geoLongitude():
     geoLong = []
     for i in range(5):
     # Generate Long 82.0 - 84.0
       longitude = round(random.uniform(82,85), 7)
       geoLong.insert(i, longitude)
      #  print("\n Longitude " + str(geoLat[i]))
     return geoLong

#Random found rocks function
def randomRocks(compo,rocks,geoLAT,geoLONG):
  #Create dictionary
  rocks_2 = {}
  #List(Array)
  rocksList = []
  i = 0
 #Random Latitude, Longitude, and Composistion
  # latitude = random.choice(geoLAT)
  # longitude = random.choice(geoLONG)
  # composition = random.choice(compo)
  #Identify 5 rocks 
  while i < 5:
    latitude = geoLAT[i]
    longitude = geoLONG[i]
    # latitude = random.choice(geoLAT)
    # longitude = random.choice(geoLONG)
    composition = random.choice(compo)
    print(" latitude in func: " + str(latitude) + "\n")
    #Create multiple dictionary (Key:Value) pairs
    rock_2 = {"site_id":i, "latitude":latitude, "longitude":longitude, "composition":composition}
    #Identify 5 rocks
    #Place random generated rocks into List 
    rocksList.append(rocks_2)
    i=i+1
  #add rockList (list) to rocks dictionary
  rocks = {"rocksList": rocksList}
  print(rocks)
  return rocks
  

geoLat = geoLatitude()
geoLong = geoLongitude()
rocks2 = randomRocks(compo,rocks,geoLat,geoLong)
json_file = json.dumps(rocks)
with open("MeteoriteLanding_0212.json", 'w+') as outfile:
   outfile.write(json_file)
    # json.dump(rocks,outfile)
# print(json_file)
print(rocks)