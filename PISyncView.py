
import tkinter as tk
root = tk.Tk(className="Step/Flow Viewer")

flows = []

# class Flow(list):
# 	def __init__(self):
# 		self.fullString = ""

class Line():
	def __init__(self, string, step, time):
		self.str = string
		self.time = time
		self.step = step

def flow_filter(logFile, flowNum):
	with open(logFile, 'r') as f:
		output = ""
		step = ""
		active = False
		for line in f:
			step += line
			if line.startswith("========"):
				if active:
					output += step
				step = ""
			elif line.startswith("FLOW {} is active".format(flowNum)):
				active = True
			elif line.startswith("FLOW {} is blocked".format(flowNum)):
				active = False
		if active:
			output += step + "\n========================\n"
	return "========================\n" + output


def parseLogFile(logFile):
	with open(logFile, 'r') as f:
		# Create the detected number of flow objects
		#numFlows = f.readline().count(',') + 1
		numFlows = 3
		for i in range(numFlows):
			# flows.append( Flow() )
			flows.append( list() )

		# Start the parsing
		buffer = []
		activeflows = [] # [1, 2, 3, etc]
		time = -1.0
		step = 0
		for line in f:
			# add line to buffer
			buffer.append(line)
			# At the end of each step, put those lines into the active flows
			if line.startswith("+-+-"):
				for flow in activeflows:
					for bLine in buffer:
						#put buffer into each active flow along with step # and time.
						flows[flow-1].append(Line(bLine, step, time))
				#clear step specific vars
				activeflows = []
				buffer = []
				time = -1.0
				step = 0
			elif line.startswith("Time"):
				# line has time store time
				time = float(line[line.index("= ")+2:line.index(" min")])
			elif line.startswith("FLOW ") and "active" in line:
				# line has active, add flow # to active flows
				activeflows.append(int(line[ line.index("FLOW ")+5: line.index(" is") ]))
			elif line.startswith("STEP "):
				# line has step, store step number
				step = int(line[line.index("STEP ")+5:line.index(" (")])




# Custom Scroll functions
def all_yview(*args):
	""" Called by the scrollbar to set the 
	position of	the text views.
	"""
	print("yview args", args)
	T1.yview(*args)
	T2.yview(*args)

def all_scroll_set(*args):
	""" Called by the text views to set the 
	position of the scrollbar.
	"""
	print("scroll_set args", args)
	S.set(*args)

# general configuration of the tkinter text widgets
def configure_text(widget):
	widget.tag_configure("header", background="black", foreground="white", spacing1=10, spacing3=10)

if __name__ == '__main__':

	parseLogFile("Test_Part_2_6099.txt")
	
	# Create widgets
	#T1 = tk.Text(root)
	#T2 = tk.Text(root)
	#S = tk.Scrollbar(root)
	windows = []
	#windows.append(T1)
	#windows.append(T2)
	for i in range(len(flows)):
		tkText = tk.Text(root)
		configure_text(tkText)
		tkText.pack(side='left', fill='y')
		windows.append(tkText)

	# Configure window
	root.config(height=30)
	root.resizable(False, True)
	
	for i, flow in enumerate(flows):
		w = windows[i]
		#w.config(yscrollcommand=S.set)
		w.config(width=70)
		for line in flow:
			w.insert("end", line.str, line.step)

	#S.config(command=all_yview)

	# Layout Widgets
	#T1.pack(side='left', fill='y')
	#S.pack(side='left', fill='y')
	#T2.pack(side='left', fill='y')

	# Display the App and keep listening for events
	root.mainloop()
    