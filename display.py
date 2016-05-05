"""
Last updated: 5/4/16 22:00
This code file creates a new window where the user can input which courses they have taken, what their major is, and how many semesters they have left. It then runs the 
user's input through the 'make course plan' function and renders a display of it.
@author: Becca Getto, Emma Price
"""



# Make checkbutton
from Tkinter import *
import tkMessageBox
from pygal import *
from student import Student

"""This program performs both the gui creation and controls the display output. Running this program will create a new window where
the user can input which courses they have taken, how what their major is, and how many semesters they have left. It will then run the 
user's input through the 'make course plan' function. With this output it will create the display using pygal."""


ELECTIVE = ['AHSE','AHSE','AHSE','AHSE','AHSE', 'Advanced Bio', 'Advanced Math', 'Bio:E', 'Design Depth','Design Depth','Design Depth','Design Depth', 'Design Elective','Design Elective','Design Elective','Design Elective', 'E:C Elective', 'E:C Elective', 'E:C Elective', 'ECE Elecective', 'ECE Elecective', 'ECE Elecective', 'ECE Elective', 'MatSci Elective','MatSci Elective','MatSci Elective', 'MatSci Engineering','MatSci Engineering','MatSci Engineering', 'MechE Math', 'MechE Elective','MechE Elective','MechE Elective', 'RoboE Elective','RoboE Elective','RoboE Elective']
SPEC_COURSES = ['AHSE Foundation',  'AnalDig', 'CompArch', 'Chem/MatSci', 'Computational Robotics', 'DSP', 'DesNat', 'Discrete', 'Dynamics', 'E! Foundation', 'FOCS', 'Fundamentals of Robotics', 'ISIM', 'Integrated Robotic Systems', 'Intro Microelectronics', 'Lin1', 'Lin2', 'MechDes', 'MechSolids', 'ModBio', 'ModSim', 'POE', 'Physics Foundation', 'ProbStat', 'SCOPE/ADE1', 'SCOPE/ADE2', 'SigSys', 'SoftDes', 'SoftSys', 'Thermo', 'Transport', 'UOCD']

MAJOR_LIST = ['E:C', 'ECE', 'MechE', 'BioE', 'DesignE', 'MatSciE']
SEM_LEFT = [1,2,3,4,5,6,7]

def make_gui():
	"""sets all variables and creates the lists of labels to be included in the gui window"""
	top = Tk()
	top.configure(background = 'LightCyan')
	CheckVar1 = []
	CheckVar2 = []
	CheckVar10 = []
	IntVar1 = []

	a = Label(top, text="Have you taken any of these electives?",bg = 'LightCyan', fg = 'Teal', highlightbackground='LightCyan', font = ('Helvetica', 16)).grid(row = 0, column = 1)
	d = Label(top, text="Don't double select!",bg = 'LightCyan', fg = 'Teal', highlightbackground='LightCyan', font = ('Helvetica', 16)).grid(row = 2, column = 1)
	b = Label(top, text="Have you taken any of these classes?",bg = 'LightCyan', fg = 'Teal', highlightbackground='LightCyan', font = ('Helvetica', 16)).grid(row = 0, column = 0)
	c = Label(top, text="What's your major?",bg = 'LightCyan', fg = 'Teal', highlightbackground='LightCyan', font = ('Helvetica', 16)).grid(row = 0, column = 2)
	c = Label(top, text="How many semesters do you have left?",bg = 'LightCyan', fg = 'Teal', highlightbackground='LightCyan', font = ('Helvetica', 16)).grid(row = 0, column = 3)

	for i, course in enumerate(MAJOR_LIST):
		CheckVar10.append(IntVar())

	for i, course in enumerate(ELECTIVE):
		CheckVar1.append(IntVar())

	for i, course in enumerate(SPEC_COURSES):
		CheckVar2.append(IntVar())

	for i, course in enumerate(SEM_LEFT):
		IntVar1.append(IntVar())

	"""actually creates the checkbuttons that the user will interact with in the gui"""
	for i, val in enumerate(ELECTIVE):
		C = Checkbutton(top, text = val, variable = CheckVar1[i], \
		                 onvalue = 1, offvalue = 0, height=1, \
		                 width = 20,bg = 'LightCyan', fg = 'Teal', highlightbackground='LightCyan', font = ('Helvetica', 12)).grid(row = i+1, column = 1)

	for i, val in enumerate(SPEC_COURSES):
		C = Checkbutton(top, text = val, variable = CheckVar2[i], \
		                 onvalue = 1, offvalue = 0, height=1, \
		                 width = 20, bg = 'LightCyan', fg = 'Teal', highlightbackground='LightCyan', font = ('Helvetica', 12)).grid(row = i+2, column = 0)

	for i, val in enumerate(MAJOR_LIST):
		C = Checkbutton(top, text = val, variable = CheckVar10[i], \
		                 onvalue = 1, offvalue = 0, height=1, \
		                 width = 20, bg = 'LightCyan', fg = 'Teal', highlightbackground='LightCyan', font = ('Helvetica', 12)).grid(row = i+1, column = 2)


	for i, val in enumerate(SEM_LEFT):
		C = Checkbutton(top, text = val, variable = IntVar1[i], \
		                 onvalue = 1, offvalue = 0, height=1, \
		                 width = 20, bg = 'LightCyan', fg = 'Teal', highlightbackground='LightCyan', font = ('Helvetica', 12)).grid(row = i+1, column = 3)

	Button(top, text="SUBMIT", command = top.destroy, bg = 'LightCyan', fg = 'Teal', highlightbackground='LightCyan', font = ('Helvetica', 16)).grid(row = 36, column = 2)

	"""these loops use the information from the gui and makes it into a usable input for the 'make course plan' function"""
	top.mainloop()
	return [CheckVar1, CheckVar2, CheckVar10, IntVar1]
	
def make_input(a_tuple):
	courses_taken = []
	for i, value in enumerate(a_tuple[0]):
		if value.get() == 1:
			courses_taken.append(ELECTIVE[i])

	for i, value in enumerate(a_tuple[1]):
		if value.get() == 1:
			courses_taken.append(SPEC_COURSES[i])

	for i, value in enumerate(a_tuple[2]):
		if value.get() == 1:
			student_major = MAJOR_LIST[i]

	for i, value in enumerate(a_tuple[3]):
		if value.get() == 1:
			student_sem = SEM_LEFT[i]
	return [student_major, courses_taken, student_sem]

def render_browser(courses_left):
	"""this funciton takes in the output of 'make_course_plan' and makes it visually pleasing"""
	chart = Dot(x_label_rotation=30, show_legend=False)
	chart.title = 'Your Course Plan'
	chart.x_labels = ['Course 1', 'Course 2', 'Course 3', 'Course 4 (Semi-Optional)', 'Course 5 (Optional)']
	for semester in courses_left:
		#print semester
		courses = []
		for i, course in enumerate(courses_left[semester]):
			if course[2] == 'AHSE':
				something_else = {'value': course[1], 'label': course[0], 'color': 'rgba(204, 153, 255, 1)'}
			if course[2] == 'ENGR':
				something_else = {'value': course[1], 'label': course[0], 'color': 'rgba(51, 153, 255, 1)'}
			if course[2] == 'SCI':
				something_else = {'value': course[1], 'label': course[0], 'color': 'rgba(153, 255, 51, 1)'}
			if course[2] == 'MATH':
				something_else = {'value': course[1], 'label': course[0], 'color': 'rgba(255, 153, 51, 1)'}
			if course[2] == 'GENERAL':
				something_else = {'value': course[1], 'label': course[0], 'color': 'rgba(192, 192, 192, 1)'}
			courses.append(something_else)
			#print courses
		chart.add('Semester =' + str(semester), courses)
	return chart.render_in_browser()

creation = make_input(make_gui())
stu = Student(creation[0], creation[1], creation[2])
render_browser(stu.make_course_plan())
