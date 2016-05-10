import csv
import pandas as pd
import collections

    
def get_courses():
    f = 'CourseTypes_Courses.csv'
    df = pd.read_csv(f)
    course_dict = df.set_index('name').T.to_dict('list')
    return course_dict

def get_majors():
    f = 'CourseTypes_Majors.csv'
    df = pd.read_csv(f)
    course_dict = df.set_index('Major').T.to_dict('list')
    return course_dict

print get_majors()
print get_courses()