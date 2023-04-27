import pytest
import xmltodict
from ISS_midtem import main, menu1, menu2, menu3, menu4, menu5, menu6, menu7, menu8

@pytest.fixture
def setupDictSight():
    with open('XMLsightingUSA.xml','r') as sighting_data:
        doc_sight = xmltodict.parse(sighting_data.read())
        return doc_sight

@pytest.fixture
def setupDictPosition():
    with open('ISS.OEM_J2K_EPH.xml','r') as positional_data:
        doc_position = xmltodict.parse(positional_data.read())
        return doc_position
    
@pytest.fixture
def test_menu_1(setupDictPosition):
    return setupDictPosition

@pytest.fixture
def test_menu_2(setupDictPosition):
    # menu2(int, setupDictPosition)
    return [5, setupDictPosition]
    
@pytest.fixture
def test_menu_3(setupDictSight):
    return setupDictSight
@pytest.fixture
def test_menu_4(setupDictSight):
    return [5,setupDictSight]
@pytest.fixture
def test_menu_5(setupDictSight):
   return ['',setupDictSight]
@pytest.fixture
def test_menu_6(setupDictSight):
    return ['',setupDictSight]
@pytest.fixture
def test_menu_7(setupDictSight):
    return ['','',setupDictSight]
@pytest.fixture
def test_menu_8(setupDictSight):
    return ['', setupDictSight]

#  Python setup test fixture
@pytest.fixture
def test_main():
    uSelect = '1'
    if (uSelect == 1):
        menu1()
    # return uSelect

# Test to check that xml data is converted to dict
def test_xmlFiletoDict():
    with open('XMLsightingUSA.xml','r') as sighting_data:
        doc_sight = xmltodict.parse(sighting_data.read())
    with open('ISS.OEM_J2K_EPH.xml','r') as positional_data:
        doc_position = xmltodict.parse(positional_data.read())
    assert type(doc_sight) is dict
    assert type(doc_position) is dict



# Test to verify that user input is within defined range
def test_userSelect(test_main):
    
    # main()
    assert(test_main) == menu1('')

def test_menu1(test_menu_1):
    assert menu1(test_menu_1) == None
    
def test_menu2(test_menu_2):
    assert menu2(test_menu_2[0],test_menu_2[1]) == None

def test_menu3(test_menu_3):
    assert menu3(test_menu_3) == None

def test_menu4(test_menu_4):
    assert menu4(test_menu_4[0], test_menu_4[1]) == None

def test_menu5(test_menu_5):
    assert menu5(test_menu_5[0],test_menu_5[1]) == None

def test_menu6(test_menu_6):
    assert menu6(test_menu_6[0], test_menu_6[1]) == None

def test_menu7(test_menu_7):
    assert menu7(test_menu_7[0],test_menu_7[1],test_menu_7[2]) == None

def test_menu8(test_menu_8):
    assert menu8(test_menu_8[0],test_menu_8[1]) == None