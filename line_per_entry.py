# File: Load CSV Example
# ----------------------

# A useful library for reading files
# with "comma seperated values".
import csv
import argparse


def split_fields(filename, columnnumber, delimiter):
	x = 0
	file_tag = filename[5:]
	field_name = get_field_name(filename,columnnumber)
	# open a file
	with open(field_name + file_tag + '.csv','w') as csvfile:
		with open(filename) as f:
			reader = csv.reader(f)
			# loop over each row in the file
			for row in reader:
				if x != 0:
					entries = row[columnnumber]
					if entries.strip() != "":
						entry_list = entries.split(delimiter)
						for entry in entry_list:
							writeRow = row[:]
							writeRow[columnnumber] = entry.strip() 
							for i in range(len(writeRow)):
								writeRow[i] = writeRow[i].replace('"','')
								writeRow[i] = writeRow[i].replace("'","")
								writeRow[i] = "\"" + writeRow[i] + "\""
							writeRow = ','.join(writeRow) + '\n'
							csvfile.write(writeRow)
							x += 1
				else:
					print("Splitting up " + row[columnnumber])
					for j in range(len(row)):
						row[j] = "\"" + row[j] + "\""
					row = ','.join(row) + '\n'
					csvfile.write(row)
				x += 1
			print("Split complete. Total Rows: " + str(x));



def get_field_name(filename, columnnumber):
	with open(filename) as f:
		x = 0
		reader = csv.reader(f)
		for row in reader:
			field_name = row[columnnumber]
			return field_name

				


# Prints out a 2d array
def printData(matrix):
	for row in matrix:
		print(row)

# This if statement passes if this
# was the file that was executed
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Take in list of cases and split them up on a given field that potentially has multiple entries.")
	parser.add_argument('-filename',metavar="filename",help="Filename for lines of cases")
	parser.add_argument('-columnnumber',type=int, metavar="columnnumber", help="Column number of field to be split.")
	parser.add_argument('-delimiter', metavar="delimiter",help="Character that separates each entry of the relevant field")
	args = parser.parse_args()
	filename = args.filename
	# Subtract one for 0 indexing.
	columnnumber = args.columnnumber - 1
	delimiter = args.delimiter
	split_fields(filename, columnnumber, delimiter)