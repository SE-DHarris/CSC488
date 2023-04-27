#!/usr/bin/env python3
import json
def compute_average_mass(a_list_of_dicts, a_key_string):
    """
    Iterates through a list of dictionaries, pulling out values associated with a given key. Returns the average of those values.
    Args:
    a_list_of_dicts (list): A list of dictionaries, each dict should have the
    same set of keys.
    a_key_string (string): A key that appears in each dictionary associated
                           with the desired value (will enforce float type).
    Returns:
    esult (float): Average value.
    """

    total_mass = 0.
    for item in a_list_of_dicts:
        total_mass += float(item[a_key_string]) 
    return(total_mass / len(a_list_of_dicts) )
def check_hemisphere(latitude, longitude):
    """
    Given latitude and longitude in decimal notation, returns which hemispheres those coordinates land in.
    Args:
    latitude (float): Latitude in decimal notation. longitude (float): Longitude in decimal notation.
    Returns:
    location (string): Short string listing two hemispheres.
    """

    location = 'Northern' if (latitude > 0) else 'Southern'
    location = f'{location} & Eastern' if (longitude > 0) else f'{location} & Western' 
    return(location)
def count_classes(a_list_of_dicts, a_key_string):
    """ 
    Given a_list_of_dicts and a_key_string in dictionary and string notattion, returns classes_observed (dict)
    which prints the count of the number of times string is found.
    Args:
    a_list_of_dicts (dict). a_key_string
    Returns:
     classes_observed (dict)
     """
    classes_observed = {}
    for item in a_list_of_dicts:
        if item[a_key_string] in classes_observed: 
            classes_observed[item[a_key_string]] += 1
        else:
            classes_observed[item[a_key_string]] = 1
    return(classes_observed)

def main():
    with open('../homework02/MeteoriteLanding_0212.json', 'r') as f:
        ml_data = json.load(f)
    print(compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'))
    for row in ml_data['meteorite_landings']: print(check_hemisphere(float(row['reclat']), float(row['reclong'])))

    print(count_classes(ml_data['meteorite_landings'], 'recclass'))
    print(__doc__)
if __name__ =='main': main()
