
'''
    Script Requirements:
    - 5 tests for each function
    - Must work with pytest
    - Tests are created for hard coded values not theoretical values
'''
# import SpaceTurbidity
import pytest
import json
# Import functions to test: (from <fileName> import <function>)
from SpaceTurbidity import decay, calcTurbidity, main

#Test Methods must start with "test" keyword
    #Test pass parameters and variable types

#test to make sure turbidity is below 1 
# Test to see if list is empty
# If you can't assume an input test for definite output
# Test to see if rate of decay is called if turbidity is below 1
# Test for 


    

#main method tests
def test_file_exist():
    #Test for json file import
    exFile = open("/Users/d.l.harris77953/Desktop/NSU/SPRING2023/CSC-488/GIT Repo/CSC488/homework03/turbidity_data.json", 'r')
    assert json.load(exFile) != ImportError
def test_turbidity():
    # Test that list length  is 74 (***Average 5 points*** 370/5=74)
    tValue = calcTurbidity(json.load(open("/Users/d.l.harris77953/Desktop/NSU/SPRING2023/CSC-488/GIT Repo/CSC488/homework03/turbidity_data.json",'r')))
    assert len(tValue) == 74
def test_turbidityOver():
    #Test that is water is NOT safe Decay isnt necessary
    tValue = calcTurbidity(json.load(open("/Users/d.l.harris77953/Desktop/NSU/SPRING2023/CSC-488/GIT Repo/CSC488/homework03/turbidity_data.json",'r')))
    for i in tValue:
        if(i > 1.0):
            assert decay(i)
def test_turbidityUnder():
        #Test that if water is safe Decay isnt necessary 
    tValue = calcTurbidity(json.load(open("/Users/d.l.harris77953/Desktop/NSU/SPRING2023/CSC-488/GIT Repo/CSC488/homework03/turbidity_data.json",'r')))
    for i in tValue:
        assert (i<1.0) != decay(i)
def test_DecayReturn():
    #Test that is water is NOT safe Decay isnt necessary
    tValue = calcTurbidity(json.load(open("/Users/d.l.harris77953/Desktop/NSU/SPRING2023/CSC-488/GIT Repo/CSC488/homework03/turbidity_data.json",'r')))
    for i in tValue:
        if(i > 1.0):
            assert decay(i) == 1.0
def test_calcTurbidity():
    #Test json data passes successfully to function
   assert calcTurbidity(json.load(open("/Users/d.l.harris77953/Desktop/NSU/SPRING2023/CSC-488/GIT Repo/CSC488/homework03/turbidity_data.json",'r')))

def test_decay():
    assert decay(1.02) == 1

def test_decay2():
    assert decay(0.02) == 0

def test_decay3():
    assert decay(-1.02) == 0

def test_decay4():
    assert decay(1.03) == 2
# @pytest.skip
# def test_calcTurbidityEmptyfileName():
#     assert calcTurbidity(json.load(open(""))) == FileNotFoundError
    
# @pytest.fixture
# def calcT(filesf):
#     filesf = ["f"]
# @pytest.fixture
# def calcTDict(dict):
#     dict = {"turbidity": []}

# @pytest.skip
# def test_calcTDict(calcTDict):
#     assert calcTurbidity(dict)



    
