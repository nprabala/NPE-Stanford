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
	writeCsvData('2016-17 import.csv')

# Reads a files into a 2d array. There are
# other ways of doing this (do check out)
# numpy. But this shows 
def loadCsvData(fileName):
	matrix = []
	# open a file
	with open(fileName) as f:
		reader = csv.reader(f)
		# loop over each row in the file
		for row in reader:
			# cast each value to a float
			doubleRow = []
			for value in row:
				doubleRow.append(value)
			# store the row into our matrix
			matrix.append(doubleRow)
	return matrix

def writeCsvData(filename):
	matrix = []
	# open a file
	with open('split.csv','w',newline='') as csvfile:
		with open(filename) as f:
			reader = csv.reader(f)
			# loop over each row in the file
			i = 0
			for row in reader:
				newRow = row
				if i is not 0:
					newRow[8] = str(', '.join(str(row[8]).splitlines()))
					print(newRow[8])
				for i in range(len(row)):
					newRow[i] = "\"" + row[i] + "\""
				newRow = ','.join(newRow) + '\n'
				i += 1
				csvfile.write(newRow)


# Prints out a 2d array
def printData(matrix):
	for row in matrix:
		print(row)

# This if statement passes if this
# was the file that was executed
if __name__ == '__main__':
	main()