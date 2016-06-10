import os
import csv
import sys

allowed_ext = ['.avi', '.mp4', '.mkv']

def grab_all(folder):
	data = []
	for row in os.walk(folder):
		data.append(row)
	return data

def create_list(data):
	filenames = []
	for glob in data:
		for item in glob[2]:
			filenames.append(glob[0] + '/' + item)
	return filenames

def split(fullpath):
	pieces = {}
	pieces['dir'] = os.path.split(fullpath)[0]
	pieces['name'] = os.path.split(fullpath)[1]
	pieces['ext'] = os.path.splitext(fullpath)[1]
	return pieces

def writer(filenames, outfile):
	with open(outfile, 'wb') as book:
		writer = csv.writer(book)
		writer.writerow(['Name', 'Filename'])
		for row in filenames:
			if split(row)['ext'] in allowed_ext:
				writer.writerow([
					split(row)['name'],
					row
					])	

def main():
	data = grab_all(sys.argv[1]) # folder to index
	filenames = create_list(data)
	writer(filenames, sys.argv[2]) # filename to write
	

if __name__ == '__main__':
	main()