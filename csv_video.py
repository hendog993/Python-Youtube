import csv

filepath = '/Users/henrygilbert/Dev/Cars.csv'

File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)

list_of_entries = []
for x in list(range(0,len(Data))):
	list_of_entries.append(Data[x][0])

