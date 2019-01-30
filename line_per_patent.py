# File: Load CSV Example
# ----------------------

# A useful library for reading files
# with "comma seperated values".
import csv
import argparse

# The main method


def split_patents(filename):
	x = 0
	file_tag = filename[5:]
	# open a file
	with open('patents' + file_tag + '.csv','w') as csvfile:
		with open(filename) as f:
			reader = csv.reader(f)
			# loop over each row in the file
			for row in reader:
				if x != 0:
					patents = row[9]
					patent_list = patents.split(";")
					for patent_number in patent_list:
						writeRow = row[:]
						writeRow[9] = patent_number 
						for i in range(len(writeRow)):
							writeRow[i] = writeRow[i].replace('"','')
							writeRow[i] = writeRow[i].replace("'","")
							writeRow[i] = "\"" + writeRow[i] + "\""
						writeRow = ','.join(writeRow) + '\n'
						csvfile.write(writeRow)
				else:
					for j in range(len(row)):
						row[j] = "\"" + row[j] + "\""
					row = ','.join(row) + '\n'
					csvfile.write(row)
				x += 1
				


# Prints out a 2d array
def printData(matrix):
	for row in matrix:
		print(row)

# This if statement passes if this
# was the file that was executed
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Take in list of cases and split them up where a patent is on every row.")
	parser.add_argument('-filename',metavar="filename",help="Filename for lines of cases")
	args = parser.parse_args()
	filename = args.filename
	split_patents(filename)