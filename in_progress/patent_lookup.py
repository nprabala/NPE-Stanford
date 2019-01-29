#!/usr/bin/env python

import requests
import argparse
import json
import csv

def look_up(fields):
	payload = {}
	payload["f"] = fields
	x = 0
	with open('results.csv','w') as csvfile:
		with open("patents.csv") as f:
			reader = csv.reader(f)
			# loop over each row in the file
			for row in reader:
				if x != 0:
					code = str(row[13])
					patent = row[9]
					if patent != "" and code != "":
						payload["q"] = {"patent_number":patent}
						print(payload)
						url = 'http://www.patentsview.org/api/patents/query'
						try: 
							r = requests.post(url, timeout=1, json=payload)
							data = r.json()
							write_row = [str(patent),code]
							for key, value in dict_to_csv(data):
								write_row.append(value)
							write_row = normalize_row(write_row)
							csvfile.write(write_row)
							x += 1
						except requests.ConnectionError, e:
							print(e)
				else:
					x += 1
				if x % 100 == 0:
					print(x)
	print(x)
				 



def normalize_row(row):
	for i in range(len(row)):
		row[i] = str(row[i])
		row[i] = row[i].replace('"','')
		row[i] = row[i].replace("'","")
		row[i] = "\"" + row[i] + "\""
	row = ','.join(row) + '\n'
	return row

def dict_to_csv(data):
    for key, value in data.items():
        if type(value) is dict:
        	for val in dict_to_csv(value):
        		yield str(val)
        else:
            yield (key, value)


# This if statement passes if this
# was the file that was executed
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Return fields from patent lookup")
	parser.add_argument('-fields',metavar="fields", nargs="+",help="List of fields to store in csv.")
	args = parser.parse_args()
	print args
	fields = args.fields
	if fields is None:
		fields = ["ipc_section","ipc_class"]
	look_up(fields)
