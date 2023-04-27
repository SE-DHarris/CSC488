import random
import json
import sys

# Composition list
compo = ["stony", "iron", "stony-iron"]
rocks={}
# Randomly generate 5 meteor sites
meteor_sites = []
for i in range(5):
    # Generate latitude and longitude
    latitude = round(random.uniform(16, 19), 7)
    longitude = round(random.uniform(82, 85), 7)
    # Choose a random composition
    composition = random.choice(compo)
    # Create a dictionary for the site
    site_dict = {
        "siteID": i+1,
        "latitude": latitude,
        "longitude": longitude,
        "composition": composition
    }
    # Add the site to the list of meteor sites
    meteor_sites.append(site_dict)
    
rocks={"sites":meteor_sites}

#Meteor hemisphere summart (0 degree latitude = equator, above or below 90, 0 degree latitude = prime meridian, above or below 90)
longHemisphere = []
latHemisphere = []
for z in rocks["sites"]:
    if(z["latitude"] < 0.0):
        latHemisphere.append("Eastern")
    elif(z["latitude"] == 0):
        latHemisphere.append("Prime Meridian") 
    else:
        latHemisphere.append("Western")

for j in rocks["sites"]:
    if(j["longitude"] < 0):
        longHemisphere.append("Southern")
    elif(j["longitude"] == 0):
        longHemisphere.append("Equator")
    else:
        longHemisphere.append("Northern")

#Loop through both list and combining indexes at both locationns
hemisphere=[longHemisphere[y] + latHemisphere[y] for y in range(len(latHemisphere))] 

# Create dictionary to store number of instances
hemiCount = {
    "North & Eastern" : 0,
    "North & Western" : 0,
    "North & Prime Merdian"  : 0,
    "South & Eastern" : 0,
    "South & Western" : 0,
    "South & Prime Merdian" : 0,
    "Equator & Eastern" : 0,
    "Equator & Western" : 0,
    "Equator & Prime Merdian" : 0

}
# Loop to count instances of hemisphere
for y in range(len(hemisphere)):
  
  if(hemisphere[y] == "NorthernEastern"): hemiCount["North & Eastern"] += 1
  if(hemisphere[y] == "NorthernWestern"): hemiCount["North & Western"] += 1
  if(hemisphere[y] == "NorthernPrime Merdian"): hemiCount["North & Prime Merdian"] += 1
  if(hemisphere[y] == "SouthernEastern"): hemiCount["South & Eastern"] += 1
  if(hemisphere[y] == "SouthernWestern"): hemiCount["South & Western"] = + 1
  if(hemisphere[y] == "SouthernPrime Merdian"): hemiCount["South & Prime Merdian"]  += 1
  if(hemisphere[y] == "EquatorEastern"): hemiCount["Equator & Eastern"]  += 1
  if(hemisphere[y] == "EquatorWestern"): hemiCount["Equator & Western"]  += 1
  if(hemisphere[y] == "EquatorPrime Merdian"): hemiCount["Equator & Prime Merdian"]  += 1
json_file = json.dumps(meteor_sites)
json_file2 = json.dumps(hemiCount)
with open("Meteorite_Landings0303", 'w+') as outfile:
   outfile.write("'___Meteor sites___'\n" + json_file)
   outfile.write("\n")
   outfile.write("'___Hemisphere summary___'\n" + json_file2)
