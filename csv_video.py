import csv

filepath = '/Users/henrygilbert/Dev/Cars.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)

# Grab all column information
list_of_brands = []
for x in list(range(0, len(Data))):
	list_of_brands.append(Data[x][0])

print(list_of_brands)
