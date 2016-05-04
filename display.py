# Make checkbutton
from Tkinter import *
import tkMessageBox
from pygal import *

top = Tk()
top.configure(background = 'LightCyan')
CheckVar1 = []
CheckVar2 = []
CheckVar10 = []
ELECTIVE = ['AHSE','AHSE','AHSE','AHSE','AHSE', 'Advanced Bio', 'Advanced Math', 'Bio:E', 'Design Depth','Design Depth','Design Depth','Design Depth', 'Design Elective','Design Elective','Design Elective','Design Elective', 'E:C Elective', 'E:C Elective', 'E:C Elective', 'ECE Elecective', 'ECE Elecective', 'ECE Elecective', 'ECE Elective', 'MatSci Elective','MatSci Elective','MatSci Elective', 'MatSci Engineering','MatSci Engineering','MatSci Engineering', 'MechE Math', 'MechE Elective','MechE Elective','MechE Elective', 'RoboE Elective','RoboE Elective','RoboE Elective']
SPEC_COURSES = ['AHSE Foundation',  'AnalDig', 'CompArch', 'Chem/MatSci', 'Computational Robotics', 'DSP', 'DesNat', 'Discrete', 'Dynamics', 'E! Foundation', 'FOCS', 'Fundamentals of Robotics', 'ISIM', 'Integrated Robotic Systems', 'Intro Microelectronics', 'Lin1', 'Lin2', 'MechDes', 'MechSolids', 'ModBio', 'ModSim', 'POE', 'Physics Foundation', 'ProbStat', 'SCOPE/ADE1', 'SCOPE/ADE2', 'SigSys', 'SoftDes', 'SoftSys', 'Thermo', 'Transport', 'UOCD']

MAJOR_LIST = ['E:C', 'ECE', 'MechE', 'BioE', 'DesignE', 'MatSciE']
SEM_LEFT = [1,2,3,4,5,6,7]
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

courses_taken = []
# def pack_courses(course):
# 	print CheckVar[0].get()


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

# for i, text in enumerate(SEM_LEFT):
#     d = Radiobutton(top, text=text, variable=IntVar1[i]).grid(row = i, column = 2)

Button(top, text="SUBMIT", command = top.destroy, bg = 'LightCyan', fg = 'Teal', highlightbackground='LightCyan', font = ('Helvetica', 16)).grid(row = 36, column = 2)

mainloop()
#C2 = Checkbutton(top, text = OPTIONS[1], variable = CheckVar[1], \
#                 onvalue = 1, offvalue = 0, height=5, \
 #                width = 20)

#C2.pack()
top.mainloop()
for i, value in enumerate(CheckVar1):
	if value.get() == 1:
		courses_taken.append(ELECTIVE[i])

for i, value in enumerate(CheckVar2):
	if value.get() == 1:
		courses_taken.append(SPEC_COURSES[i])

for i, value in enumerate(CheckVar10):
	if value.get() == 1:
		student_major = MAJOR_LIST[i]

for i, value in enumerate(IntVar1):
	if value.get() == 1:
		student_sem = SEM_LEFT[i]

# scrollbar = Scrollbar(top)
# scrollbar.grid(row = 1, column = 3)
# top.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=top.yview)


#courses_left ={2: ['Lin2', 'Design Depth', 'AHSE 4'], 3: ['UOCD', 'POE'], 4: ['AHSE 3', 'Chem/MatSci'], 5: ['ModBio', 'AHSE 2', 'ProbStat'], 6: ['SCOPE/ADE1', 'Design Depth'], 7: ['SCOPE/ADE2', 'Design Depth']

def render_browser(courses_left):
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
			courses.append(something_else)
			#print courses
		chart.add('Semester =' + str(semester), courses)
	return chart.render_in_browser()

from student import Student
# stu = Student(student_sem, student_major, courses_taken)
# render_browser(stu.make_course_plan())

if __name__ == '__main__':
	# stu = Student(7, 'MechE', ['ISIM', 'DesNat', 'ModSim', 'AHSE Foundation'])
	stu = Student(6, 'DesignE', ['AHSE Foundation', 'DesNat', 'Design Elective', 'E! Foundation', 'ISIM', 'Lin1', 'ModSim', 'Physics Foundation', 'SoftDes'])
render_browser(stu.make_course_plan())