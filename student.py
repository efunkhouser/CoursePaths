import csv
#import pandas as pd
# import collections
import copy
import numpy
import numpy.random as nprnd
from dicts_classes import *

class Student(object):
    """determines the number of credits left in each course coloring (eng, ahse, math, science)
    also determines which major and general requirements are left to take"""
    def __init__(self, semesters_left=None, major_name = 'MechE' , courses_taken = ['ModSim', 'ISIM', 'Design Nature', 'AHSE Foundation'], courses_left=None):
        self.Major = major_objects[major_name]
        self.courses_taken = [course_objects[course_name] for course_name in courses_taken] #list of Course objects
        self.courses_left = courses_left #possible bug: if courses_left is not None it'll get overwritten when major_requirements_left is run
        #Addtl note on self.courses_left: must be a list of Course objects
        self.semesters_left = 0 if semesters_left==None else semesters_left
        
    def __str__(self):
    	return "Major: {}.\nSemesters remaining: {}.\nCourses taken: {}.\nCourses needed: {}.".format(self.Major.name, self.semesters_left, [course.name for course in self.courses_taken], [course.name for course in self.courses_left])
        
    def eng_counter(self):
        eng_credit_required = 46
        for course in self.courses_taken:
            eng_credit_required -= course.eng
        
        return eng_credit_required
    
    def ahse_counter(self):
        ahse_credit_required = 28
        for course in self.courses_taken:
            ahse_credit_required -= course.ahse
        
        return ahse_credit_required
    

    def math_sci_counter(self):
        math_credits_required = 10
        sci_credits_required = 20
        for course in self.courses_taken:
            if math_credits_required >= 0:
                math_credits_required -= course.math
                sci_credits_required -= course.sci
            else:
                sci_credits_required -= (course.sci + course.math)
        
        return (math_credits_required, sci_credits_required) #tuple containing these two variables
        
    def major_requirements_left(self):
        if self.courses_left==None:
        	self.courses_left = []
        	self.courses_left = self.Major.major_requirements
        else:
            for course in self.Major.major_requirements:
            	if course in self.courses_left:
            		pass
            	else:
            		self.courses_left.append(course)
            		
        for course in self.courses_left:
            if course in self.courses_taken:
            	self.courses_left.remove(course)
                
    def given_coursedict_make_schedule(self):
		'''This is a method of the Student class.
			It needs two attributes belonging to the Student object:
				courses_left, which is a list of Course objects that this method must arrange into a schedule, and
				semesters_left, which is the number of semesters in which to fit these Courses.
			It returns a dictionary whose keys are the semesters remaining and values are classes in those semesters.'''
			
		self.major_requirements_left() #Populates self.courses_left
		course_list = copy.deepcopy(self.courses_left) #list of Course objects
		
		semester_list = []
		for number in range((8 - self.semesters_left), 8):
			semester_list.append(Semester(number)) #This creates however many Semesters the Student needs
	
		### Place classes that must be taken in a specific semester
		for course in course_list:
			for semester in semester_list:
				if course.required_sem == semester.number: #If we already know when the class must be taken,
					semester.base_courses.append(course) #	    #Move it to the appropriate semester
					course_list.remove(course)#					#And remove it from the course_list for later
		
		### Now we begin trying random orders of classes and comparing them to find out which has the most even spread of difficulty
		random_semester_assigns = []
		min_difficulty = 20.0 * self.semesters_left #Arbitrary high 'minimum difficulty' threshold
		best_distribution_of_classes = None
		
		for i in range(10000):
			'''Try 1000 random arrangements of courses in semesters and store arrangements that spread difficulty evenly'''
			random_semester_assigns[:] = nprnd.randint((8 - self.semesters_left), 8, size=len(course_list))
			
			for semester in semester_list:
				semester.difficulty = 0
				semester.courses[:] = []
				
				#Assign random semester numbers to what's left in course_list
				sem_indices = numpy.where(numpy.array(random_semester_assigns) == semester.number)[0]
				semester.courses = semester.base_courses + [course_list[i] for i in sem_indices]
				
				#Now calculate the difficulty of each semester
				for course in semester.courses:
					semester.difficulty += course.difficulty
					
			if all(semester.difficulty < min_difficulty for semester in semester_list):
				min_difficulty = max(semester.difficulty for semester in semester_list)
				best_distribution_of_classes = copy.copy(random_semester_assigns)

		course_plan_dict = {}
		
		for semester in semester_list:
			semester.difficulty = 0 #Reset these values before reassigning them to the best distribution values
			semester.courses[:] = []
			
			sem_indices = numpy.where(numpy.array(best_distribution_of_classes) == semester.number)[0]
			semester.courses = semester.base_courses + [course_list[i] for i in sem_indices] #Required courses + whatever random arrangement worked best
			
			course_plan_dict[semester.number] = semester.courses #Format: {semester number: [Course1, Course2, Course3], ...}
			#Possible modification: Semester object as key rather than sem # int
		return course_plan_dict


'''Create a Student object for the user and prompt them for their major, courses taken, and semesters remaining'''
# stu_major = raw_input("What's your major? (E:C, BioE, DesignE, ECE, MechE, RoboE, MatSciE) \n>>")
# stu_courses_taken = raw_input("What courses have you taken? \n>>")
# stu_courses_taken_list = [course.strip() for course in stu_courses_taken.split(',')]
# stu_semesters_left = int(raw_input("How many semesters do you have left? \n>>"))
# stu = Student(stu_semesters_left, stu_major, stu_courses_taken_list)

if __name__ == '__main__':
	stu = Student(6, 'MechE', ['ISIM', 'DesNat', 'ModSim', 'AHSE Foundation'])
	print stu.given_coursedict_make_schedule()

### Code graveyard
		
			# print 'Semester {}:'.format(semester.number)
			# for course in semester.courses:
			# 	print course
			# 	semester.difficulty += course.difficulty
			# print 'Total semester difficulty: {}'.format(semester.difficulty)
			
# from course_dict import Course

# f = 'CourseTypes_Majors.csv'
# df = pd.read_csv(f)

# '''Create GENERAL, the global list of general-requirement Course objects'''
# GENERAL_strings = ['ModSim', 'ModBio', 'Lin1', 'Lin2', 'ISIM', 'POE', 'E! Foundation', 'DesNat', 'UOCD', 'AHSE Foundation', 'AHSE 2', 'AHSE 3', 'AHSE 4', 'Chem/MatSci', 'ProbStat', 'E&M', 'Mechanics', 'Design Depth', 'SCOPE/ADE1', 'SCOPE/ADE2']
# GENERAL = [course_objects[course_name] for course_name in GENERAL_strings]