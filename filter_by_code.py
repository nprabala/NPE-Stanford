# File: Load CSV Example
# ----------------------
# This is some sample code. Use it in any way 
# that you would like. It is meant to both give
# you a head start on the assignments and show you
# what some python code looks like :-). - Piech.

# A useful library for reading files
# with "comma seperated values".
import csv
import argparse

# The main method



def filter(codes, filename):
	x = 0
	# open a file
	filter_tag = "_".join(codes)
	date_tag = filename.split(".")
	date_tag = date_tag[0][7:]
	with open('filtered_patents' + filter_tag + "-"+ date_tag + '.csv','w') as csvfile:
		with open(filename) as f:
			reader = csv.reader(f)
			# loop over each row in the file
			for row in reader:
				if x != 0:
					code = row[13]
					code_list = code.split(";")
					for c in code_list:
						c = c.strip()
						if c in codes:
							writeRow = row
							for i in range(len(writeRow)):
								writeRow[i] = writeRow[i].replace('"','')
								writeRow[i] = writeRow[i].replace("'","")
								writeRow[i] = "\"" + writeRow[i] + "\""
							writeRow = ','.join(writeRow) + '\n'
							csvfile.write(writeRow)
							break
				else:
					for j in range(len(row)):
						row[j] = "\"" + row[j] + "\""
					row = ','.join(row) + '\n'
					csvfile.write(row)
				x += 1
				


# This if statement passes if this
# was the file that was executed
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Filter out case entries by asserter codes.")
	parser.add_argument('-codes',metavar="codes", nargs="+",help="List of fields to store in csv.")
	parser.add_argument('-filename',metavar="filename",help="Filename for lines of cases")
	args = parser.parse_args()
	filename = args.filename
	codes = args.codes
	if codes is None:
		codes = [1,5]
	filter(codes, filename)
