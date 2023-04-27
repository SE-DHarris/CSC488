
import pytest
import json
import sys
from ml_homework04 import meteor_sites, hemisphere, rocks, longitude,latitude,json_file,compo,sys,site_dict,outfile

#Test for appropriate sizes of lists and dictionaries
def test_cmdLine():
 assert len(hemisphere) == 5

def test_meteor_sitesSize():
 assert len(meteor_sites) == 5

# List of dictionaries with 1 key
def test_rocksSize():
 assert len(rocks) == 1


def test_site_dictSize():
 #Range from 0 - 4 = 5
 assert len(site_dict) == 4


#Check dictionary value is a list
def test_dictList():
 assert rocks == {"sites": meteor_sites}

def test_latWrong():
 assert outfile.close 