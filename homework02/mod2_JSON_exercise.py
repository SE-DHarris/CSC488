import json

# [{"siteID": 1, "latitude": 18.1476001, "longitude": 83.7513166, "composition": "stony-iron"}, {"siteID": 2, "latitude": 18.027645, "longitude": 82.4698489, "composition": "stony"}, {"siteID": 3, "latitude": 16.1001307, "longitude": 82.1341222, "composition": "iron"}, {"siteID": 4, "latitude": 18.8339628, "longitude": 82.3604557, "composition": "stony-iron"}, {"siteID": 5, "latitude": 16.7191315, "longitude": 82.7815397, "composition": "iron"}]
# Open fie and read contents
with open("MeteoriteLanding_0212.json", 'r') as infile:
#    print(infile.readline())
   json_in = infile.readlines()
# Create file to write new information
with open("MeteoriteLanding_updated.json", 'w+') as outfile:
#    print(outfile.readline())
    print()

# print(type(json_in))
# print(json_in)
# for i in range(len(json_in)):
#     print(type(i))

print(len(range(json_in[0])))