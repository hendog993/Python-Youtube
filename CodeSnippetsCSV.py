import csv

filepath = '/Users/henrygilbert/Dev/Cars.csv'

File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)

# Print Row Data
row1 = Data[0]
row2 = Data[1]
print("Row 1 is : ", row1)
print("Row 2 is : ", row2)

# Access a single element.
toyota_row = Data[1]
toyota_country = toyota_row[2]
print(toyota_country)
print(Data[1][2])


# Print multiple column indexes
print(Data[0][0])
print(Data[1][0])
print(Data[2][0])
print(Data[3][0])
print(Data[4][0])

# Print all columns
list_of_columns = []
for x in list(range(1,len(Data))):
	list_of_columns.append(Data[x][0])

print(list_of_columns)
