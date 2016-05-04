import copy
import numpy
import numpy.random as nprnd
from dictionaries import *

class Student(object):
    """Determines the number of credits left in each course coloring (eng, ahse, math, science)
    also determines which major and general requirements are left to take
    And creates a course plan"""
    def __init__(self, major_name = 'MechE' , courses_taken = ['ModSim', 'ISIM', 'DesNat', 'AHSE Foundation'], semesters_left=7, courses_left=None):
        self.Major = major_objects[major_name]
        self.courses_taken = [course_objects[course_name] for course_name in courses_taken] #list of Course objects
        self.courses_left = courses_left
        self.semesters_left = semesters_left
        self.course_plan = []
        
    def __str__(self):
        return "Major: {}.\nSemesters remaining: {}.\nCourses taken: {}.\nCourses needed: {}.".format(self.Major.name, self.semesters_left, [course.name for course in self.courses_taken], [course.name for course in self.courses_left])
        
    def eng_counter (self, Course_list=None):
        ''' Returns number of ENGR credits the student has left to complete, based on either their courses taken (default)
            or on another course list (as used in coloring_after_courseplan, which gives the list of courses the course plan gives) '''
        Course_list = self.courses_taken if Course_list==None else Course_list
        eng_credit_required = 46
        for course in Course_list:
            eng_credit_required -= course.eng
        
        return eng_credit_required/4
    
    def ahse_counter(self, Course_list=None):
        ''' Returns number of AHSE credits the student has left to complete, based on either their courses taken (default)
            or on another course list (as used in coloring_after_courseplan, which gives the list of courses the course plan gives) '''
        Course_list = self.courses_taken if Course_list==None else Course_list
        ahse_credit_required = 28
        for course in Course_list:
            ahse_credit_required -= course.ahse
        
        return ahse_credit_required/4
    

    def math_sci_counter(self, Course_list=None):
        ''' Returns number of MATH and SCI credits the student has left to complete, based on either their courses taken (default)
            or on another course list (as used in coloring_after_courseplan, which gives the list of courses the course plan gives) '''
        Course_list = self.courses_taken if Course_list==None else Course_list
        math_credits_required = 10
        sci_credits_required = 20
        for course in Course_list:
            # print math_credits_required
            if math_credits_required >= 0:
                math_credits_required -= course.math
                sci_credits_required -= course.sci
            else:
                sci_credits_required -= (course.sci + course.math)
        
        return (math_credits_required/4, sci_credits_required/4) #tuple containing these two variables

    def total_counter(self, Course_list = None):
        """ returns the number of total credits left to complete based on the courses they have taken and the ones that they will be assigned to 
        take either based either on general requirements or major requirements. This is done because there are a few credits where the student can
        decide what coloring they are."""
        Course_list = self.courses_taken if Course_list==None else Course_list
        total_credits_required = 120
        for course in Course_list:
            total_credits_required -= course.eng + course.sci + course.ahse + course.math
        return total_credits_required/4

    
    def major_requirements_left(self):
        ''' Populates courses_left with major requirements, removes them if you've taken them already;
            Fills the rest of your courses_left with placeholder colorings (ie general ENGR or SCI) for the course plan.
            Requires nothing other than having entered the courses you've taken. Returns None, just modifies courses_left. '''
        if self.courses_left==None:
            self.courses_left = []
            self.courses_left = self.Major.major_requirements
        else:
            for course in self.Major.major_requirements:
                if course in self.courses_left:
                    pass
                else:
                    self.courses_left.append(course)
                
        for course in self.courses_left[:]:
            if course in self.courses_taken[:]:
                self.courses_left.remove(course)


        for i in range(self.eng_counter(self.courses_left  + self.courses_taken)):
            self.courses_left.append(course_objects['ENGR'])
        for i in range(self.ahse_counter(self.courses_left + self.courses_taken)):
            self.courses_left.append(course_objects['AHSE'])
        for i in range(self.math_sci_counter(self.courses_left + self.courses_taken)[0]):
            self.courses_left.append(course_objects['MATH'])
        for i in range(self.math_sci_counter(self.courses_left + self.courses_taken)[1]):
            self.courses_left.append(course_objects['SCI'])
        for i in range(self.total_counter(self.courses_left + self.courses_taken)):
            self.courses_left.append(course_objects['GENERAL'])

                
    def choose_random_semesters_for_courses(self):
        ''' Takes in a Student, looks as their list of courses_left
            Looks at its required/suggested semester list and chooses randomly out of the numbers in that list for each course
            Returns that int '''
        list_of_random_semesters = []
        
        for course in self.courses_left:
            possible_semester_list = course.suggested_sem
            if possible_semester_list == [0]:
                possible_semester_list[:] = range((8 - self.semesters_left),8)
            for i in possible_semester_list:
                if i < (8 - self.semesters_left):
                    possible_semester_list.remove(i)
            semester = nprnd.choice(numpy.array(possible_semester_list))
            
            list_of_random_semesters.append(semester)
        
        return list_of_random_semesters
        
    def make_course_plan(self):
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
        
        ### Now we begin trying random orders of classes and comparing them to find out which has the most even spread of difficulty
        min_difficulty = 20.0 * self.semesters_left #Arbitrary high 'minimum difficulty' threshold
        best_distribution_of_classes = None
        random_semester_assigns = []
        
        for i in range(1000):
            '''Try 1000 random arrangements of courses in semesters and store arrangements that spread difficulty evenly'''
            random_semester_assigns[:] = self.choose_random_semesters_for_courses()
            
            for semester in semester_list:
                semester.difficulty = 0
                semester.courses[:] = []
                
                #Assign random semester numbers to what's left in course_list
                sem_indices = numpy.where(numpy.array(random_semester_assigns) == semester.number)[0]
                semester.courses = [course_list[i] for i in sem_indices]
                
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
            semester.courses = [course_list[i] for i in sem_indices] #Required courses + whatever random arrangement worked best
            
            course_plan_dict[semester.number] = [(course.name, course.difficulty, course.coloring()) for course in semester.courses]
                
        self.course_plan = semester_list
        return course_plan_dict