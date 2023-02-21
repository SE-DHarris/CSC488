import json
from math import radians, degrees, sin, cos, asin, acos, sqrt
# Read in meteorite landing data in JSON file create
# Calculate time to visit and take samples
#Starting point of robot 16.0 (Lat) 82.0 (Long)
    # Robot visits landing sites in order
    # Top Speed 10km/hr
    # Mars is a sphere radius = 3389.5 km
    # Stony meteorites take 1 hour to sample, iron meteorites take 2 hours to sample, and stony-iron meteorites take 3 hours to sample
    # The trip is “over” after sampling the last meteorite

#Starting point of robot 16.0 (Lat) 82.0 (Long)
robot_lat = 16.0
robot_long = 82.0

# Determine Latitude difference ; Great Circle algorithm to find distance
def great_circle(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    return 3389.5 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )
# Calculate Time to travel
def CalcTravel(tdistance):
    speed = 10
    # Get distance from list and calculate total time
    hour = tdistance[i]/speed
    # return total time rounded to 2 decimal places
    return round(hour,2)
   #Create loop to find hour spent at each site, pass info to print function

#Calculate Time to acquire sample based on composition
def CalcSample(compo):
    match compo:
        case 'stony':
            return 1
        case 'iron':
            return 2
        case 'stony-iron':
            return 3
     # Pass info to print function each iteration

#Open and convert JSON file into Python Object
file = open("MeteoriteLanding_0212.json", 'r')
json_data = json.load(file)
# JSON data read from file stores in variable (json_var)
json_var = json_data


# List to store value from great_circle algorithm
tdistance = []
tTime = []
tSampleTime = []
for i in range(5):
    # Access index in list of dictionaries latitdue and longitude

    mLat = (json_var[i]['latitude'])
    mLong = (json_var[i]['longitude'])
    mCompo = (json_var[i]['composition'])
    # Place total distance into tdistance list
    tdistance.append(great_circle(robot_lat,robot_long,mLat,mLong))
    # Pass meteorite composition to function
    tSampleTime.append(CalcSample(mCompo))
    # value = CalcSample(mCompo)
    # print("\nLeg = " + str(i+1) + ", time to travel = " + str(tdistance[i])+ " time to sample = " + str(value) + "hr")
    # print(tSampleTime[i])

# mCompo = (json_var['sites'][0]['composition'])
CalcTravel(tdistance)

# print(str(mLat) +" "+ str(mLong) + " " + mCompo)
# Print info

for z in range(5):
 print("\nLeg = " + str(z+1) + ", Time to travel = " + str(round(tdistance[z],2)) + "hr, Time to sample = "  + str(tSampleTime[z]) + "hr")

print("=========================================================================================")



#Put JSON file in dictionary
# json_dict = {'JSON File' : json_data