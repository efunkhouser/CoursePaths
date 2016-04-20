# Make checkbutton
from Tkinter import *
import tkMessageBox

top = Tk()
CheckVar1 = []
CheckVar10 = []
COURSE_LIST = ['AHSE','AHSE','AHSE','AHSE','AHSE', 'AHSE Foundation', 'Advanced Bio', 'Advanced Math', 'AnalDig', 'Bio:E', 'Chem/MatSci', 'CompArch', 'Computational Robotics', 'DSP', 'DesNat', 'Design Depth','Design Depth','Design Depth','Design Depth', 'Design Elective','Design Elective','Design Elective','Design Elective', 'Discrete', 'Dynamics', 'E! Foundation', 'E:C Elective', 'E:C Elective', 'E:C Elective', 'E:C Elective', 'ECE Elecective', 'ECE Elecective', 'ECE Elecective', 'ECE Elective', 'FOCS', 'Fundamentals of Robotics', 'ISIM', 'Integrated Robotic Systems', 'Intro Microelectronics', 'Lin1', 'Lin2', 'MatSci Elective','MatSci Elective','MatSci Elective', 'MatSci Engineering','MatSci Engineering','MatSci Engineering', 'Mech E Math', 'MechDes', 'MechE Elective','MechE Elective','MechE Elective', 'MechE Math', 'MechSolids', 'ModBio', 'ModSim', 'POE', 'Physics Foundation','Physics Foundation', 'ProbStat', 'RoboE Elective','RoboE Elective','RoboE Elective', 'SCOPE/ADE1', 'SCOPE/ADE2', 'SigSys', 'SoftDes', 'SoftSys', 'Thermo', 'Transport', 'UOCD']
MAJOR_LIST = ['E:C', 'ECE', 'MechE', 'BioE', 'DesignE', 'MatSciE']
SEM_LEFT = [1,2,3,4,5,6,7]
IntVar1 = []


for i, course in enumerate(MAJOR_LIST):
	CheckVar10.append(IntVar())

for i, course in enumerate(COURSE_LIST):
	CheckVar1.append(IntVar())

for i, course in enumerate(SEM_LEFT):
	IntVar1.append(IntVar())

courses_taken = []
# def pack_courses(course):
# 	print CheckVar[0].get()


for i, val in enumerate(COURSE_LIST):
	C = Checkbutton(top, text = val, variable = CheckVar1[i], \
	                 onvalue = 1, offvalue = 0, height=1, \
	                 width = 20).grid(row = i, column = 0)

for i, val in enumerate(MAJOR_LIST):
	C = Checkbutton(top, text = val, variable = CheckVar10[i], \
	                 onvalue = 1, offvalue = 0, height=1, \
	                 width = 20).grid(row = i, column = 1)


for i, val in enumerate(SEM_LEFT):
	C = Checkbutton(top, text = val, variable = IntVar1[i], \
	                 onvalue = 1, offvalue = 0, height=1, \
	                 width = 20).grid(row = i, column = 2)

# for i, text in enumerate(SEM_LEFT):
#     d = Radiobutton(top, text=text, variable=IntVar1[i]).grid(row = i, column = 2)

b = Button(top, text="OK", command = top.destroy).grid()

mainloop()
#C2 = Checkbutton(top, text = OPTIONS[1], variable = CheckVar[1], \
#                 onvalue = 1, offvalue = 0, height=5, \
 #                width = 20)

#C2.pack()
top.mainloop()
for i, value in enumerate(CheckVar1):
	if value.get() == 1:
		courses_taken.append(COURSE_LIST[i])

for i, value in enumerate(CheckVar10):
	if value.get() == 1:
		student_major = MAJOR_LIST[i]

for i, value in enumerate(IntVar1):
	if value.get() == 1:
		student_sem = SEM_LEFT[i]

from student import Student
stu = Student(student_sem, student_major, courses_taken)
print stu.given_coursedict_make_schedule()