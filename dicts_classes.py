class Course(object):
    """Creates courses and gives them attributes listed in the init section"""
    def __init__ (self, course_dict, name):
        self.name = name
        self.eng = course_dict[name][0]
        self.ahse = course_dict[name][1]
        self.math = course_dict[name][2]
        self.sci = course_dict[name][3]
        #self.project = course_dict[name][4]
        self.suggested_sem = course_dict[name][4]
        self.required_sem = course_dict[name][5]
        self.prereq = course_dict[name][6] #TODO: resolve that some of these have a number in slot 7 and those with prereqs have an 8th slot with a number
        self.difficulty = course_dict[name][7]

    def __repr__(self):
        return repr(self.name)


'''Create a Course object for every course in the dictionary'''
course_dict = {'ProbStat': [0, 0, 2, 0, [3,4], 0, 0, 2], 'Design Elective': [4, 0, 0, 0, 0, 0, 0, 2], 'ModBio': [0, 0, 0, 4, [1,2,3], 0, 0, 3], 'SoftSys': [4, 0, 0, 0, [3,4,5,6], 0, 'SoftDes', 2], 'MatSci Elective': [0, 0, 0, 4, [4,5,6,7], 0, 'Chem/MatSci', 3], 'Bio:E': [4, 0, 0, 0, 0, 0, 'ModBio', 4], 'Mech E Math': [0, 0, 4, 0, [4,5,6,7], 0, ['Lin1', 'Lin2'], 3], 'MechE Math': [0,0,4,0,[3,4,5,6,7],0,'Lin2',3], 'FOCS': [4, 0, 0, 0, [3,4,5,6], 0, ['Discrete', 'SofDes'], 4], 'MechE Elective': [4, 0, 0, 0, [4,5,6,7], 0, 'Check', 4], 'MatSci Engineering': [0, 0, 0, 4, [4,5,6,7], 0, 0, 4], 'AHSE Foundation': [0, 4, 0, 0, 0, 0, 0, 2], 'SCOPE/ADE1': [4, 0, 0, 0, 0, 6, 0, 5],'SCOPE/ADE2': [4, 0, 0, 0, 0, 7, 0, 5], 'Computational Robotics': [4,0,0,0,3, 0, ['SoftDes'],4], 'Integrated Robotic Systems': [4,0,0,0,4, 0, ['Computational Robotics', 'Fundamentals of Robotics'],4], 'Fundamentals of Robotics': [4,0,0,0,2, 0, 0,4], 'Intro Microelectronics': [4, 0, 0, 0, 5, 0, 'Lin1', 3], 'SoftDes': [4, 0, 0, 0, [3,4,5,6], 0, 0, 3], 'UOCD': [4, 0, 0, 0, 3, 3, 0, 4], 'ISIM': [4, 0, 0, 0, 0, 0, 0, 3], 'POE': [4, 0, 0, 0, [2,4], 0, 0, 4], 'E:C Elective': [4, 0, 0, 0, [4,5,6,7], 0, 'SoftDes', 4], 'ModSim': [0, 0, 2, 2, 0, 0, 0, 3], 'SigSys': [4, 0, 0, 0, 3, 0, 0, 3], 'ECE Elective': [4, 0, 0, 0, [4,5,6,7], 0, 'Check', 4], 'Advanced Bio': [0, 0, 0, 4, 0, 0, 'ModBio', 3], 'DSP': [4, 0, 0, 0, [4,6], 0, 'SigSys', 2], 'Discrete': [0, 0, 4, 0, 5, 0, ['Lin1', 'Lin2'], 4], 'Chem/MatSci': [0, 0, 0, 4, [1,2,3], 0, 0, 3], 'AnalDig': [4, 0, 0, 0, [4,6], 0, 'SigSys', 3], 'DesNat': [4, 0, 0, 0, 0, 0, 0, 3], 'RoboE Elective': [4, 0, 0, 0, [4,5,6,7], 0, 0, 4], 'MechSolids': [4, 0, 0, 0, [3,5], 3, 'Mechanics', 4], 'E! Foundation': [0, 4, 0, 0, 1, 1, 0, 2], 'Design Depth': [4, 0, 0, 0, [4,5,6,7], 0, 'UOCD', 3], 'CompArch': [4, 0, 0, 0, [4,6], 0, 0, 4], 'Lin2': [0, 0, 4, 0, 2, 2, 0, 3], 'Lin1': [0, 0, 4, 0, 1, 1, 0, 3], 'Physics Foundation': [0, 0, 0, 4, [1,2,3], 0, 0, 3], 'AHSE': [0, 4, 0, 0, [1,2,3,4,5,6,7], 0, 0, 2], 'MechDes': [4, 0, 0, 0, 4, 0, 'MechSolids', 4], 'Advanced Math': [0, 0, 4, 0, [3,4,5,6,7], 0, ['Lin1', 'Lin2'], 3], 'Dynamics': [4,0,0,0,[2,4],0,['Lin1','Mechanics'],5], 'Thermo': [4, 0, 0, 0, [3,5], 0, 'Mechanics', 2], 'Transport': [4, 0, 0, 0, [4,6], 0, ['Lin1', 'Lin2', 'Thermo'], 3]}
course_objects = {}
for course in course_dict:
    course_objects[course] = Course(course_dict, course)
    
    
class Major(object):
    """Creates the majors and maps all required courses held within the major
    to the actual course objects so that they have all connected attributes"""
    def __init__(self, name, major_requirements):
        self.name = name
        self.major_requirements = major_requirements
    
#major_requirements is a list of Course objects
'''Create a Major object for every major in the dictionary'''        
major_dict = {'E:C': ['Discrete', 'SoftDes', 'FOCS', 'SoftSys', 'E:C Elective', 'E:C Elective', 'ModSim', 'ModBio', 'Lin1', 'Lin2', 'ISIM', 'POE', 'E! Foundation', 'DesNat', 'UOCD', 'AHSE Foundation', 'AHSE', 'Chem/MatSci', 'ProbStat', 'Physics Foundation', 'Design Depth', 'SCOPE/ADE1', 'SCOPE/ADE2'], 'BioE': ['Advanced Math', 'Advanced Bio', 'Chem/MatSci', 'Bio:E', 'Bio:E', 'Bio:E', 'ModSim', 'ModBio', 'Lin1', 'Lin2', 'ISIM', 'POE', 'E! Foundation', 'DesNat', 'UOCD', 'AHSE Foundation', 'AHSE', 'AHSE', 'AHSE', 'Chem/MatSci', 'ProbStat', 'Physics Foundation', 'Design Depth', 'SCOPE/ADE1', 'SCOPE/ADE2'], 'ECE': ['Discrete', 'SigSys', 'Intro Microelectronics', 'SoftDes', 'CompArch', 'DSP', 'AnalDig', 'ECE Elective', 'ModSim', 'ModBio', 'Lin1', 'Lin2', 'ISIM', 'POE', 'E! Foundation', 'DesNat', 'UOCD', 'AHSE Foundation', 'AHSE', 'AHSE', 'AHSE', 'Chem/MatSci', 'ProbStat', 'Physics Foundation', 'Design Depth', 'SCOPE/ADE1', 'SCOPE/ADE2'], 'DesignE': ['Design Depth', 'Design Depth', 'Design Elective', 'Design Elective', 'Design Elective', 'Design Elective', 'ModSim', 'ModBio', 'Lin1', 'Lin2', 'ISIM', 'POE', 'E! Foundation', 'DesNat', 'UOCD', 'AHSE Foundation', 'AHSE', 'AHSE', 'AHSE', 'Chem/MatSci', 'ProbStat', 'Physics Foundation', 'Design Depth', 'SCOPE/ADE1', 'SCOPE/ADE2'], 'MechE': ['MechSolids', 'Dynamics', 'Thermo', 'Transport', 'MechDes', 'MechE Math', 'MechE Elective', 'ModSim', 'ModBio', 'Lin1', 'Lin2', 'ISIM', 'POE', 'E! Foundation', 'DesNat', 'UOCD', 'AHSE Foundation', 'AHSE', 'AHSE', 'AHSE', 'Chem/MatSci', 'ProbStat', 'Physics Foundation', 'Design Depth', 'SCOPE/ADE1', 'SCOPE/ADE2'], 'MatSciE': ['MatSci Elective', 'MatSci Elective', 'MatSci Elective', 'MatSci Engineering', 'MatSci Engineering', 'ModSim', 'ModBio', 'Lin1', 'Lin2', 'ISIM', 'POE', 'E! Foundation', 'DesNat', 'UOCD', 'AHSE Foundation', 'AHSE', 'AHSE', 'AHSE', 'Chem/MatSci', 'ProbStat', 'Physics Foundation', 'Design Depth', 'SCOPE/ADE1', 'SCOPE/ADE2'], 'RoboE': ['Advanced Math', 'E:C Elective', 'MechE Elective', 'Integrated Robotic Systems', 'Fundamentals of Robotics', 'Computational Robotics', 'RoboE Elective', 'ModSim', 'ModBio', 'Lin1', 'Lin2', 'ISIM', 'POE', 'E! Foundation', 'DesNat', 'UOCD', 'AHSE Foundation', 'AHSE', 'AHSE', 'AHSE', 'Chem/MatSci', 'ProbStat', 'Physics Foundation', 'Design Depth', 'SCOPE/ADE1', 'SCOPE/ADE2']}
major_objects = {}
major_requirements = []
for major in major_dict:
    major_requirements = [course_objects[course_name] for course_name in major_dict[major]]
    major_objects[major] = Major(major, major_requirements)
#print major_objects



class Semester(object):
    '''Allows for easy creation of multiple semesters with their own properties'''
    def __init__(self, number):
		self.number = number # 0-7
		self.difficulty = 0
		self.base_courses = [] #These are courses that MUST always live in this semester, ie: UOCD in sem 3
		self.courses = []

    def __str__(self):
	    return "Semester {}".format(self.number)