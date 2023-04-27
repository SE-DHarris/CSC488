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
hemisphere = []
for z in rocks["sites"]:
    print(z["latitude"])
    if(z["latitude"] < 0.0):
        hemisphere[z["latitude"]] == "Eastern"
    elif(z["latitude"] == 0):
        hemisphere[z] == "Prime Meridian" 
    else:
        hemisphere[z] == "Western"
    # if(z[longitude] < 0):
    #     hemisphere[z] == "Southern"
    # elif(z[longitude] == 0):
    #     hemisphere[z] == "Equator"
    # else:
    #     hemisphere[z] == "Northern"
json_file = json.dumps(meteor_sites)
with open("homework04.json", 'w+') as outfile:
   outfile.write(json_file)

# Print the list of meteor sites
print(rocks)