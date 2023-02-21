import random
import json

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

json_file = json.dumps(meteor_sites)
with open("MeteoriteLanding_0212.json", 'w+') as outfile:
   outfile.write(json_file)

# Print the list of meteor sites
print(rocks)