# File: Load CSV Example
# ----------------------
# This is some sample code. Use it in any way 
# that you would like. It is meant to both give
# you a head start on the assignments and show you
# what some python code looks like :-). - Piech.

# A useful library for reading files
# with "comma seperated values".
import csv

# The main method
def main():
	split_patents('cases-2019-01-24PST17-50-37.csv')


def split_patents(filename):
	x = 0
	# open a file
	with open('patents.csv','w') as csvfile:
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
	main()
