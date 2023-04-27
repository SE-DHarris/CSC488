""" 

 DO I HAVE TO EQUALIZE DETECTOR CURRENT TO .99 BEFORE DETERMINING TURBIDITY??

 HOW TO CREATE DOCSTRING
    1. Multi line comment MUST be the first lines of a class, method, fuction... 
        - To print docstring to terminal use syntax: print(<functionName>.__doc__)
        

 """

import json
import sys



#Decay function for water Turbidity 
def decay(turblvl):
    ''''
        Equation use for minimum time to return below a safe threshold
        Arguments: Int
        Return type: Int
    '''
    #Type Hints
    hours:int
    decayPercent:float
    turblvl:float


    # Print docstring
    print(decay.__doc__)
    decayPercent = 0.02
    hours = 0
    #Decrease turbidity lvls to safe and increment hours
    while turblvl > 1.0:
            hours += 1
            turblvl = turblvl * (1 - decayPercent) ** hours
    return hours

def calcTurbidity(json_var):
    '''
       Equation use for minimum time to return below a safe threshold
       Arguments: JSON file
       Return type: float
    '''
    #Type hints:
    json_var:dict
    average:float
    I90:float
    I90total:float
    turbidity:float
    turbidityList:list
    print(calcTurbidity.__doc__)

    calibrationValue = []
    turbidityList = []
    listIndex = 0 
    i=0
    start = 0
    for key,values in json_var.items():
        while i < len(values):
            average = 0
            start = i
            i = i + 5
            for z in range(start,i):
             average = average + values[z]['calibration_constant']
            if(int(values[listIndex]['detector_current'])> .99):
                I90 = values[listIndex]['detector_current'] - .99
                I90total = values[listIndex]['detector_current'] - I90
                turbidity = (average / 5) * I90total
            else:
                turbidity = (average / 5) * int(values[listIndex]['detector_current'])
            turbidityList.append(turbidity)
    return turbidityList


def main():
    # Read in JSON file
    #Open and convert JSON file into Python Object
    with open(sys.argv[1], 'r') as file:
        json_data = json.load(file)
    json_var = json_data
    #List to store first five values and find average
    #Type Hints
    dataSet:list
    totalTime:int
    turbidity:list
    json_data:dict

    # dataSet = []
    turbidity = calcTurbidity(json_data)
    # Determine if water is safe
    for i in turbidity:
        if(i > 1.0):
            # print("Water is not safe " + str(i))
            print("Average turbidity based on most recent five measurements = " + str(i) +  " NTU")
            print("Warning: Turbidity is above threshold for safe use")
            totalTime = decay(i)
            print("Minimum time required to return below a safe threshold = " + str(totalTime) + " hours")
            print()

        else:
            print("Average turbidity based on most recent five measurements = " + str(i) + " NTU")
            print("Info: Turbidity is below threshold for safe use")
            print("Minimum time required for turbidity to reach safe levels: 0 hrs")
            print()

if __name__ == "__main__":
    main()
