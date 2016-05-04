# Course Paths

## Project Description:
The goal of our project is to create a tool for Olin students to help them create a course plan for their time at Olin. The program takes into account a variety of factors including: courses already taken, area of academic interest, level of difficulty desired for each semester, and balance of project-based and individual work (this bit isn't implemented yet) desired for each semester. The program uses a reccommendation algorithm that optimizes these chosen factors to suggest specific courses as well as more general course colorings to take in each semester.

## What to Install:
Numpy
```python
sudo apt-get install python-numpy
```
Pygal
```python
sudo apt-get install python-numpy
```
```python
sudo apt-get install python-numpy
```
Copy
TKinter

## How to Use:
First download dictionaries.py, student.py, and display.py. The user only needs to run display.py, but it imports classes and methods from the other two.
When running display.py, the user will be prompted to select a major and input courses they have taken so far.
The program then outputs a link to a plot with classes to be taken in the student's remaining semesters, which the user then copies and pastes into their browser.

## How it Works:
We have created a csv file of all of the required courses offered at Olin with information about how many credits they are worth, what suject areas they are in, when they should be taken, and how difficult they are. We have also created another scv file with each of the common majors offered at Olin and what courses are required for graduation for each. We use the pandas library to import that csv file into python and convert it into a dictionary.

Our program has four classes: Student, Major, Course, and Semester. The latter three are used primarily for storage.
The Semester class is used as a way to store information about a semester: its number, courses, and difficulty. A Semester is created for each of the user's remaining semesters at Olin during the course-recommender algorithm.

The Major class stores the major name and a list of the courses it requires.

The Course class stores properties about the course like name, credits, and difficulty. It has one method that returns the coloring of the course (ENGR, AHSE, MATH, or SCI).

The Student class contains information about that stduent such as their Major, how many semesters they have left at Olin, which Courses they have taken up to this point, and which Courses they still have to take (courses_left). This class has methods that calculate the number of course credits left in each subject area necessary to graduate and a method that uses that information to populate courses_left with major requirements and general course colorings. It has a method called make_course_plan that looks at courses_left, creates Semester objects to put those courses in, and sorts each course randomly among its suggested semesters. It tries this 1000 times and stores the arrangement of Courses with the most even spread of difficulty.

## Change Log:
Version 1 - Given a limited list of courses, the program sorts the courses between two semesters in order to optimize for the lowest overall difficulty for both semesters

Version 2 - Same optimization protocol but using a dictionary of all courses available at Olin

Version 3 - Expanded functionality to account for all semesters, not just 2

Version 4 - Added checkbox inputs and required semesters

Version 5 - Checkbox inputs, dot-plot outputs, and a course plan that takes into account suggested semesters and also recommends other classes to ensure enough credits in each course coloring to graduate

## Contributors:
Ellie Funkhouser, Becca Getto & Emma Price

## FAQs:
- Do I have to select a major?
Yes, in the current version of the program you must select a major.

