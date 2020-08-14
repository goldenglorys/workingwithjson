"""
    This program help work with some kind of JSON data sample and collate out the needed
    set of key->values into a specified file format to save into.
"""

import json

with open('file.json', 'r') as o:
    file_object = json.load(o)
    with open('output.txt', 'w') as output:
        for person in file_object:
            output.write(person['first_name'] + ' ' + person['last_name'] + '\n')
print('Done')
