from tkinter import *


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
		# A sin (wt + b)
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
		return None
	
	def plot_values(self):
		
		return None
	
	pass

main()