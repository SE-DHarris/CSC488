import json

with open('Meteorite_Landings.json', 'r') as f: 
    ml_data = json.load(f)

# Prints out the variable that holds file data (dict: ml_data)
print(type(ml_data))

# Print out value data type of the dictionary (dict: ml_data(whole) list: 'meteorite_landings'(key) )
print(type(ml_data['meteorite_landings']))

# Print first index of list whose value is a dictionary (dict: ml_data(whole) list: 'meteorite_landing (key) 0: index value which is a dict)
print(type(ml_data['meteorite_landings'][0]))

# Print string(name) index of list whose value is a dictionary (dict: ml_data(whole) list: 'meteorite_landing (key) 0: index value which is a dict)
print(type(ml_data['meteorite_landings'][0]['name']))

# Dictionary for storing count of class
count_reclass = {
                    'L5' : 0,
                     'H6' : 0,
                     'EH4' : 0,
                     'Acapulcoite' : 0,
                     'L6' : 0,
                     'LL3-6' : 0,
                     'H5' : 0,
                     'L' : 0,
                     'Diogenite-pm' : 0,
                     'Stone-uncl' : 0,
                     'H4' : 0,
                     'H': 0,
                     'Iron-IVA' : 0,
                     'CR2-an' : 0,
                     'LL5' : 0,
                     'CI1' : 0,
                     'CV3' : 0,
                     'L/LL4' : 0,
                     'Eucrite-mmict' : 0
                     }

for i in ml_data['meteorite_landings']:
    # print(i['recclass'])
    # If statements to count instances of reclass values
    if i['recclass'] == "L5":
        count_reclass['L5'] += 1

    if i['recclass'] == "H6":
        count_reclass['H6'] += 1

    if i['recclass'] == "H4":
        count_reclass['H4'] += 1
    
    if i['recclass'] == "EH4":
        count_reclass['EH4'] += 1
   
    if i['recclass'] == "Acapulcoite":
        count_reclass['Acapulcoite'] += 1

    if i['recclass'] == "L6":
        count_reclass['L6'] += 1

    if i['recclass'] == "LL3-6":
        count_reclass['LL3-6'] += 1

    if i['recclass'] == "H5":
        count_reclass['H5'] += 1

    if i['recclass'] == "L":
        count_reclass['L'] += 1    

    if i['recclass'] == "Diogenite-pm":
        count_reclass['Diogenite-pm'] += 1

    if i['recclass'] == "Stone-uncl":
        count_reclass['Stone-uncl'] += 1

    if i['recclass'] == "Iron-IVA":
        count_reclass['Iron-IVA'] += 1

    if i['recclass'] == "H":
        count_reclass['H'] += 1

    if i['recclass'] == "CR2-an":
        count_reclass['CR2-an'] += 1

    if i['recclass'] == "CI1":
        count_reclass['CI1'] += 1

    if i['recclass'] == "L/LL4":
        count_reclass['L/LL4'] += 1

    if i['recclass'] == "Eucrite-mmict":
        count_reclass['Eucrite-mmict'] += 1

    if i['recclass'] == "CV3":
        count_reclass['CV3'] += 1

    if i['recclass'] == "LL5":
        count_reclass['LL5'] += 1

print("After update: " ,count_reclass)
