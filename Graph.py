from tkinter import *
from math import  sin
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

t = []
for x in list(range(0,101)):
	t.append(x/15.87)

def main():
	root = Tk()
	gui = Window(root)
	gui.root.mainloop()
	return None

class Window:
	def __init__(self, root):
		self.root = root
		self.root.title("Sin Wave")
		self.root.geometry('600x550')
		# A sin(wt + b) + c
		self.amplitude = 1
		self.frequency = 1
		self.vertical_shift = 0
		self.phase_shift = 0
		
		# Amplitude
		Label(self.root, text = "Amplitude").grid(row=0, column=0)
		self.amplitude_entry = Entry(self.root, width = 5)
		self.amplitude_entry.grid(row=0, column = 1)
		
		# Frequency
		Label(self.root, text = "Frequency").grid(row=1, column=0)
		self.frequency_entry = Entry(self.root, width = 5)
		self.frequency_entry.grid(row=1, column=1)
		
		# Vertical Shift
		Label(self.root, text = "Vertical Shift").grid(row=2, column=0)
		self.vertical_shift_entry = Entry(self.root, width = 5)
		self.vertical_shift_entry.grid(row=2, column=1)
		
		# Horizontal Shift
		Label(self.root, text = "Phase Shift").grid(row=3, column=0)
		self.phase_shift_entry = Entry(self.root, width = 5)
		self.phase_shift_entry.grid(row=3, column=1)
		
		# Update Button
		button1 = Button(self.root, text="Calculate", command = self.update_values)
		button1.grid(row=4, column=0)
		self.root.bind("<Return>", self.update_values)
		self.plot_values()
		pass
	
	def update_values(self, event=None):
		self.amplitude = float(self.amplitude_entry.get())
		self.phase_shift = float(self.phase_shift_entry.get())
		self.vertical_shift = float(self.vertical_shift_entry.get())
		self.frequency = float(self.frequency_entry.get())
		self.plot_values()
		return None
	
	def plot_values(self):
		y = []
		for x in t:
			y.append(self.amplitude * sin(self.frequency * x + self.phase_shift) + self.vertical_shift)
		
		figure = plt.figure(figsize = (5,4), dpi = 100)
		figure.add_subplot(111).plot(t,y)
		chart = FigureCanvasTkAgg(figure, self.root)
		chart.get_tk_widget().grid(row = 5, column = 0)
		
		plt.grid()
		axes = plt.axes()
		axes.set_xlim([0, 6.3])
		axes.set_ylim([-3, 3])
		
		return None
	
	pass

main()