import json
import csv

with open('clean_data.json', 'r') as json_file:
    data = json.load(json_file)

with open('clean_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    header_written = False
    for key, resp in data.items():
        if not header_written:
            header = ['key'] + list(resp['values'][0].keys())
            writer.writerow(header)
            header_written = True
        
        for r in resp['values']:
            row = [key] + list(r.values())
            writer.writerow(row)