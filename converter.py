import csv
import json
import xml.etree.ElementTree as ET
import sys

def convert_to_csv(data, filename):
    with open(filename + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

def convert_to_json(data, filename):
    with open(filename + '.json', 'w') as jsonfile:
        json.dump(data, jsonfile)

def convert_to_xml(data, filename):
    root = ET.Element('data')
    for row in data:
        item = ET.SubElement(root, 'item')
        for i, cell in enumerate(row):
            ET.SubElement(item, 'field'+str(i)).text = cell
    tree = ET.ElementTree(root)
    tree.write(filename + '.xml')

if len(sys.argv) != 3:
    print("Usage: python program.py <filename> <-c/-j/-x>")
    sys.exit(1)

filename = sys.argv[1]
format = sys.argv[2]

with open(filename, 'r') as file:
    data = [line.strip().split('\t') for line in file]

if format == '-c':
    convert_to_csv(data, filename)
elif format == '-j':
    convert_to_json(data, filename)
elif format == '-x':
    convert_to_xml(data, filename)
else:
    print("Invalid format argument. Use -c for CSV, -j for JSON, or -x for XML.")