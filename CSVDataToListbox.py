import csv
from tkinter import *

filepath = '/Users/henrygilbert/Dev/Cars.csv'

File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del(Data[0])

list_of_entries = []
for x in list(range(0,len(Data))):
	list_of_entries.append(Data[x][0])

root = Tk()
root.geometry('280x300')
var = StringVar(value = list_of_entries)
listbox1 = Listbox(root, listvariable = var)
listbox1.grid(row=0 , column=0)

def update():
	index = listbox1.curselection()[0]
	print(index)
	return None

button1 = Button(root, text="Update", command=update)
button1.grid(row=5, column=0)


root.mainloop()