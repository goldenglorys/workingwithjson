"""
    This program help work with some kind of JSON data sample and collate out the needed
    set of key->values into a specified file format to save into.
"""

import json
from random import randint


def collate_json_values_to_file():
    with open('file.json', 'r') as o:
        file_object = json.load(o)
        with open('output.txt', 'w') as output:
            for person in file_object:
                output.write(person['first_name'] + ' ' + person['last_name'] + '\n')
    print('Done')


write_heading = False
csv_heading = []
outputfilename = str(randint(0, 100000)) + 'result.csv'


def convert_json_to_csv():
    global write_heading, outputfilename
    json_file = input('Enter JSON file name to convert: ')
    try:
        print("====================================================================================")
        print("Program Starting...")
        with open(str(json_file), 'r') as o:
            file_object = json.load(o)
            print("Json file given loaded...")
            with open(outputfilename, 'a') as result:
                print("Output csv file created...")
                if not write_heading:
                    for head in file_object[0].keys():
                        result.write(head + ',')
                        csv_heading.append(str(head))
                    print("CSV heading title appended to the output file...")
                    write_heading = True

                print("Started dumping json values to the CSV file...")
                for obj in file_object:
                    result.write('\n')
                    for csv_head in csv_heading:
                        result.write(str(obj[csv_head]) + ',')
                    # result.write('\n' + str(obj['user_id']) + ','+ obj['first_name'] + ',' + obj['last_name'])
                print('Program completed successfully! with file name of' + outputfilename)
        print("====================================================================================")
    except FileNotFoundError:
        print("File not found program exit!")


convert_json_to_csv()
