class GeneralInformation(Frame):
	temperature_frame = Frame
	def __init__(self, parent, width, height):
		Frame.__init__(self, parent)
		self.time_label = Label(time_frame)
		self.time_label.configure(bg=background_color,fg=text_color,font=(font_type, 60))
		self.time_label.grid(row=0,column=0,sticky="nw")
		(*\vdots*)
		self.update_time()
		
	def update_time(self):
		new_time = time.strftime('%H:%M')
		if new_time!=self.current_time_label.__getitem__("text"):
			self.time_label.configure(text=new_time)
        (*\vdots*)
		self.after(200, self.update_time)
