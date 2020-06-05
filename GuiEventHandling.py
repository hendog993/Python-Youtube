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

def update(event = None):
	index = listbox1.curselection()[0]
	brandlabel2.config(text = Data[index][0])
	stockpricelabel2.config(text = Data[index][1])
	countrylabel2.config(text = Data[index][2])
	datelabel2.config(text = Data[index][3])
	return None

button1 = Button(root, text="Update", command=update)
button1.grid(row=5, column=0)
root.bind('<Return>', update)


brandlabel = Label(root, text="Brand").grid(row=1, column=0,sticky="w")
stockpricelabel = Label(root, text="Stock Price").grid(row=2, column=0,sticky="w")
countrylabel = Label(root, text="Country").grid(row=3, column=0,sticky="w")
datelabel = Label(root, text="Date").grid(row=4, column=0,sticky="w")

brandlabel2 = Label(root, text="")
brandlabel2.grid(row=1, column=1,sticky="w")
stockpricelabel2 = Label(root, text="")
stockpricelabel2.grid(row=2, column=1,sticky="w")
countrylabel2 = Label(root, text="")
countrylabel2.grid(row=3, column=1,sticky="w")
datelabel2 = Label(root, text="")
datelabel2.grid(row=4, column=1,sticky="w")
brandlabel2.bind('<Button-1>', update)

root.mainloop()