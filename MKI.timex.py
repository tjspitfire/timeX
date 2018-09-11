# Copyright 2018 Todd L. Jarolimek II <tljarolimek@gmail.com>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
class TimeX(tk.Frame):
	def __init__(self,master):
		# INIT WINDOW
		tk.Frame.__init__(self,master=master)
		self.pack()
		self.master.title("TimeX") # Add title to main window
		# TOP MENU #
		self.master.menu = tk.Menu(master)
		# TOP MENU # FILE MENU #
		self.master.filemenu = tk.Menu(self.master.menu)
		self.master.exportmenu = tk.Menu(self.master.menu)
		self.master.menu.add_cascade(label="File",menu=self.master.filemenu)
		self.master.filemenu.add_command(label="New File",command=self.new_file)
		self.master.menu.add_cascade(label="Export",menu=self.master.exportmenu)
		self.master.exportmenu.add_command(label="CSV",command=self.export_csv)
		self.master.config(menu=self.master.menu)
		import tempfile
		self.tempfile = tempfile.mkstemp()

		self.idle = "00:00:00"
		self.task = tk.StringVar(self,"Practice Programming")
		self.intvar = {
			"hours":tk.IntVar(self,0),
			"minutes":tk.IntVar(self,0),
			"seconds":tk.IntVar(self,0),
			"status":0,
		}
		self.textvar = {
			"hours":tk.StringVar(self,"0"),
			"minutes":tk.StringVar(self,"0"),
			"seconds":tk.StringVar(self,"0"),
			"time":tk.StringVar(self,self.idle),
			"initialtime":tk.StringVar(self,"0"),
			"task":tk.StringVar(self,"Task"),
			"type":tk.StringVar(self),
			"osc":tk.StringVar(self,"|"),
		}
		self.exportvars = []
		self.labelframes = {
			# FOR PROTOTYPING?
			"input":tk.LabelFrame(self),
			"control":tk.LabelFrame(self),
			"function":tk.LabelFrame(self),
			"output":tk.LabelFrame(self),
		}
		self.frames = {
			"input":tk.Frame(self),
			"control":tk.Frame(self), 
			"function":tk.Frame(self),
			"output":tk.Frame(self),
			}
		frame = self.frames["input"]
		frame.labelframes = {
			"task":tk.LabelFrame(frame,text="Task",labelanchor="w"),
			"hours":tk.LabelFrame(frame,text="Hours",labelanchor="w"),
			"minutes":tk.LabelFrame(frame,text="Minutes",labelanchor="w"),
			"seconds":tk.LabelFrame(frame,text="Seconds",labelanchor="w"),
		}
		# IF LABELFRAMES AS DICTIONARY, USE:
		# for i,(key,labelframe) in enumerate(frame.labelframes.items()):
		# 	labelframe.grid(row=0,column=i,padx=10,pady=10)
		# ENTRIES["TASK"] - 1ST
		frame.entries= {
			"task":tk.Entry(frame.labelframes["task"],textvariable=self.textvar["task"],relief="sunken"),
		}
		# BELOW LINE IS NOT "BULLETPROOF" -> DECIDE ON TASK INPUT FRAMEWORK
		frame.entries["task"].grid(row=0,column=0,padx=10,pady=10)
		# MENUBUTTONS["HOURS"] - 2ND, MENUBUTTONS["MINUTES"] - 3RD, MENUBUTTONS["SECONDS"] - 4TH
		frame.menubuttons = {
			"hours":tk.Menubutton(frame.labelframes["hours"],textvariable=self.textvar["hours"],relief="raised"),
			"minutes":tk.Menubutton(frame.labelframes["minutes"],textvariable=self.textvar["minutes"],relief="raised"),
			"seconds":tk.Menubutton(frame.labelframes["seconds"],textvariable=self.textvar["seconds"],relief="raised"),
		}
		# frame.menubuttons["hours"].bind("<Button-1>",self.menubutton_update_text)
		for i,(key,menubutton) in enumerate(frame.menubuttons.items()):
			menubutton.grid(row=0,column=0,padx=10,pady=10)
		frame.menus = {
			"hours":tk.Menu(frame.menubuttons["hours"]),
			"minutes":tk.Menu(frame.menubuttons["minutes"]),
			"seconds":tk.Menu(frame.menubuttons["seconds"]),
		}
		frame.menubuttons["hours"]["menu"] = frame.menus["hours"]
		frame.menubuttons["minutes"]["menu"] = frame.menus["minutes"]
		frame.menubuttons["seconds"]["menu"] = frame.menus["seconds"]
		xhours = range(0,10)
		xminutes = range(0,60,5)
		xseconds = range(0,60,15)
		for hour in xhours:
			frame.menus["hours"].add_radiobutton(label=str(hour),variable=self.intvar["hours"],value=hour,command=lambda: self.textvar["hours"].set(self.intvar["hours"].get()))
		for minute in xminutes:
			frame.menus["minutes"].add_radiobutton(label=str(minute),variable=self.intvar["minutes"],value=minute,command=lambda: self.textvar["minutes"].set(self.intvar["minutes"].get()))
		for second in xseconds:
			frame.menus["seconds"].add_radiobutton(label=str(second),variable=self.intvar["seconds"],value=second,command=lambda: self.textvar["seconds"].set(self.intvar["seconds"].get()))
		# DECIDED TO EXPLICITLY PUT INTO LIST TO CONTROL GRID ORDER (121-124)
		frame.labelframes = [
			frame.labelframes["task"],
			frame.labelframes["hours"],
			frame.labelframes["minutes"],
			frame.labelframes["seconds"],
		]
		for i,labelframe in enumerate(frame.labelframes):
			labelframe.grid(row=0,column=i,padx=10,pady=10)
		frame = self.frames["control"]
		frame.buttons = {
			"start":tk.Button(frame,text="Start Timer",width=20,command=self.start_timer),
			"reset":tk.Button(frame,text="Reset",width=20,command=self.reset_timer),
			"pause":tk.Button(frame,text="Pause",width=20,command=self.pause_timer),
			"exit":tk.Button(frame,text="Exit",width=20,command=self.master.quit)
		}
		for i,(key,button) in enumerate(frame.buttons.items()):
			button.grid(row=0,column=i,padx=10,pady=10)
		# frame.buttons = list(frame.buttons.values())
		# frame.buttons.reverse()
		# for i,(key,button) in enumerate(frame.buttons.items()):
		# 	button.grid(row=0,column=i,padx=10,pady=10)

		frame = self.frames["function"]

		frame.labelframes = {
			"timer":tk.LabelFrame(frame,text="Timer",labelanchor="w")
		}
		for i,(key,labelframe) in enumerate(frame.labelframes.items()):
			labelframe.grid(row=0,column=i,padx=10,pady=10)
		frame.labels = {
			"osc":tk.Label(frame.labelframes["timer"],textvariable=self.textvar["osc"]),
			"timer":tk.Label(frame.labelframes["timer"],textvariable=self.textvar["time"]),
		}
		# for i,(key,label) in enumerate(frame.labels.items()):
		# 	label.grid(row=0,column=i,padx=10,pady=10)
		frame.labels = [
			frame.labels["osc"],
			frame.labels["timer"]
		]
		for i,label in enumerate(frame.labels):
			label.grid(row=0,column=i,padx=10,pady=10)

		# self.frameslist = [
		# 	self.frames["input"],
		# 	self.frames["control"],
		# 	self.frames["function"],
		# ]
		# MKI CHANGES
		# frame = self.frames["output"]
		# frame.listboxes = {
		# 	"complete":tk.Listbox(frame,)
		# }
		self.leftframes = [
			self.frames["input"],
			self.frames["control"],
		]

		self.centerframes = [
			self.frames["function"],
		]
		# MKI CHANGES
		# self.rightframes = [
		# 	self.frames["output"],
		# ]

		for i,frame in enumerate(self.leftframes):
			for child in frame.winfo_children():
				child.grid_configure(padx=5,pady=5)
			frame.grid(row=i,column=0,padx=10,pady=10)

		for i,frame in enumerate(self.centerframes):
			for child in frame.winfo_children():
				child.grid_configure(padx=5,pady=5)
			frame.grid(row=i,column=1,padx=10,pady=10)
		# for i,frame in enumerate(self.rightframes):
		# 	for child in frame.winfo_children():
		# 		child.grid_configure(padx=5,pady=5)
		# 	frame.grid(row=i,column=2,padx=10,pady=10)


		# MISC BS
		self.after_id = None

	def start_timer(self):
		# Configure button states
		self.frames["control"].buttons["reset"].configure(state=tk.ACTIVE)
		self.frames["control"].buttons["pause"].configure(state=tk.ACTIVE)
		self.frames["control"].buttons["start"].configure(state=tk.DISABLED)
		self.frames["input"].entries["task"].configure(state=tk.DISABLED)
		self.frames["input"].menubuttons["hours"].configure(state=tk.DISABLED)
		self.frames["input"].menubuttons["minutes"].configure(state=tk.DISABLED)
		self.frames["input"].menubuttons["seconds"].configure(state=tk.DISABLED)
		self.tasktime_to_total_seconds()
		self.textvar["initialtime"].set(self.total_seconds_to_standard(self.totalseconds))
		self.intvar["status"] = 1
		self.countdown()

	def reset_timer(self):
		# Configure button states
		self.frames["control"].buttons["reset"].configure(state=tk.DISABLED)
		self.frames["control"].buttons["pause"].configure(text="Pause",state=tk.DISABLED)
		self.frames["control"].buttons["start"].configure(state=tk.ACTIVE)
		self.frames["input"].entries["task"].configure(state=tk.NORMAL)
		self.frames["input"].menubuttons["hours"].configure(state=tk.ACTIVE)
		self.frames["input"].menubuttons["minutes"].configure(state=tk.ACTIVE)
		self.frames["input"].menubuttons["seconds"].configure(state=tk.ACTIVE)
		# Function call
		self.textvar["osc"].set("|")
		self.master.after_cancel(self.after_id)
		self.textvar["time"].set(self.idle)

	def pause_timer(self):
		# Configure button states
		self.frames["control"].buttons["reset"].configure(state=tk.ACTIVE)
		self.frames["control"].buttons["pause"].configure(text="Resume",state=tk.ACTIVE,command=self.resume_timer)
		self.frames["control"].buttons["start"].configure(state=tk.DISABLED)
		# Function call
		self.intvar["status"] = 0
		self.textvar["osc"].set("|")
		self.wait_variable(self.intvar["status"])

	def resume_timer(self):
		self.frames["control"].buttons["reset"].configure(state=tk.ACTIVE)
		self.frames["control"].buttons["pause"].configure(text="Pause",state=tk.ACTIVE,command=self.pause_timer)
		self.frames["control"].buttons["start"].configure(state=tk.DISABLED)
		self.intvar["status"] = 1
		self.countdown()

	def tasktime_to_total_seconds(self):
		hours = int(self.intvar["hours"].get())
		minutes = int(self.intvar["minutes"].get())
		seconds = int(self.intvar["seconds"].get())
		self.totalseconds = hours * 3600 + minutes * 60 + seconds
	
	def total_seconds_to_standard(self,total_seconds):
		seconds = total_seconds
		hoursec = seconds - seconds % 3600
		hours = int(hoursec/3600)
		seconds = seconds - hoursec

		minutesec = seconds - seconds % 60
		minutes = int(minutesec/60)
		seconds = seconds - minutesec
		if hours in range(10):
			hours = "0" + str(hours)
		if minutes in range(10):
			minutes = "0" + str(minutes)
		if seconds in range(10):
			seconds = "0" + str(seconds)
		standard = str(hours) + ":" + str(minutes) + ":" + str(seconds)

		return standard

	def countdown(self):
		if self.intvar["status"] == 0:
			self.master.after_cancel(self.after_id)
		else:
			if self.totalseconds % 2 == 0:
				self.textvar["osc"].set("\\")
			else:
				self.textvar["osc"].set("/")
			self.totalseconds = self.totalseconds - 1
			stdtime = self.total_seconds_to_standard(self.totalseconds)
			self.textvar["time"].set(stdtime)
			self.after_id = self.master.after(1000,self.countdown)
			if self.totalseconds == 0:
				self.textvar["osc"].set("|")
				self.master.bell()
				self.master.after_cancel(self.after_id)
				self.frames["control"].buttons["start"].configure(state=tk.ACTIVE)
				self.task_complete()

	def new_file(self):
		# import new_file
		# new_file.run()
		pass

	def task_complete(self):
		slave = tk.Toplevel(self)
		slave.title("Task Complete")
		frame = tk.Frame(slave)
		frame.pack()
		frame.labelframes = {
			"image":tk.LabelFrame(frame),
			"button":tk.LabelFrame(frame),
		}
		for (key,labelframe) in frame.labelframes.items():
			labelframe.pack()
		from pathlib import Path
		filepath = Path("image.gif")
		slave.image = tk.PhotoImage(file=filepath)
		# tk.Label(slave,text="Good job!").pack()
		frame.labels = {
			"image":tk.Label(frame.labelframes["image"],image=slave.image),
		}
		frame.labels = [frame.labels["image"]]
		frame.buttons = {
			"export":tk.Button(frame.labelframes["button"],text="Export",command=self.export_csv),
			"close":tk.Button(frame.labelframes["button"],text="Close",command=slave.destroy)
		}
		frame.buttons = [frame.buttons["export"],frame.buttons["close"]]
		for i,item in enumerate(frame.labels):
			item.grid(row=i,column=0)		
		for i,item in enumerate(frame.buttons):
			item.grid(row=0,column=i)
	def dump_to_tempfile(self):
		self.exportvars.append(self.textvar)
		import json
		with open(self.tempfile,"w") as file:
			json.dump(self.exportvars,file)

	def reset_task(self):
		self.textvar = {
			"hours":tk.StringVar(self,"0"),
			"minutes":tk.StringVar(self,"0"),
			"seconds":tk.StringVar(self,"0"),
			"time":tk.StringVar(self,self.idle),
			"initialtime":tk.StringVar(self,"0"),
			"task":tk.StringVar(self,"Task"),
			"type":tk.StringVar(self),
			"osc":tk.StringVar(self,"|"),
		}
		self.frames["control"].buttons["reset"].configure(state=tk.DISABLED)
		self.frames["control"].buttons["pause"].configure(state=tk.DISABLED)
		self.frames["control"].buttons["start"].configure(state=tk.ACTIVE)
		self.frames["input"].entries["task"].configure(state=tk.NORMAL)
		self.frames["input"].menubuttons["hours"].configure(state=tk.ACTIVE)
		self.frames["input"].menubuttons["minutes"].configure(state=tk.ACTIVE)
		self.frames["input"].menubuttons["seconds"].configure(state=tk.ACTIVE)

	def export_csv(self):
		export.csv(self.textvar["task"].get(),self.textvar["initialtime"].get())

class export:
	def csv(*argv):
		filename = filedialog.asksaveasfilename(initialdir="~",filetypes=[("Comma-separated values","*.csv")])
		with open(filename,"w") as file:
			for i,arg in enumerate(argv):
				if i == (len(argv) - 1):
					file.write(arg)
				else:	
					file.write(arg + ",")

# class filedialog:
# 	# def save(initialdir,filetypes):
# 	def save(initialdir,filetypes):
# 		return filedialog.asksaveasfilename(initialdir="~",filetypes=[("Comma-separated values","*.csv")])
# 	# def open(initialdir,filetypes):
# 	def open(initialdir,filetypes):
# 		return filedialog.askopenfilename(initialdir="~",filetypes=[("Comma-separated values","*.csv")])
			

class Timer(tk.Frame):
	def __init__(self,master):
		# INIT WINDOW
		tk.Frame.__init__(self,master=master)
		self.pack()
		# self.title("Timer")
		self.textvar["time"] = tk.StringVar(self,"00:00:00")
		self.frame = tk.Frame(self)
		# self.frames = [
		# 	tk.Frame(self) # 
		# ]
		# frame = self.frames[0]
		# frame.labels = [
		# 	tk.Label(frame,text=self.textvar["time"]r.get())
		# ]
		# for label in frame.labels:
		# 	label.pack()
		self.label = tk.Label(self.frame,text=self.textvar["time"].get())

		self.totalseconds = self.tasktime_to_total_seconds(TimeX.taskhours.get(),TimeX.taskminutes.get())


	def tasktime_to_total_seconds(taskhours,taskminutes):
		taskhours = int(taskhours)
		taskminutes = int(taskminutes)
		totalseconds = taskhours * 3600 + taskminutes * 60
		return totalseconds

	def countdown(totalseconds):
		totalseconds = totalseconds - 1
		stdtime = total_seconds_to_standard(totalseconds)
		self.textvar["time"].set(stdtime)
		self.label.configure(text=self.textvar["time"])

		self.master.after(1000,self.countdown)

	def total_seconds_to_standard(total_seconds):
		seconds = total_seconds
		hoursec = seconds - seconds % 3600
		hours = int(hoursec/3600)
		seconds = seconds - hoursec

		minutesec = seconds - seconds % 60
		minutes = int(minutesec/60)
		seconds = seconds - minutesec

		standard = str(hours) + ":" + str(minutes) + ":" + str(seconds)

		return standard

def run():
	root = tk.Tk()
	app = TimeX(root)
	app.mainloop()

run()
