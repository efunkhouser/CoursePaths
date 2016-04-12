# Course Paths

## Project Description:
The goal of our project is to create a tool for Olin students to help them create a course plan for their time at Olin. The program takes into account a variety of factors including: courses already taken, area of academic interest, level of difficulty desired for each semester, and balance of project-based and individual work (this bit isn't implemented yet) desired for each semester. The program uses a reccommendation algorithm that optimizes these chosen factors to suggest specific courses as well as more general course colorings to take in each semester.

## How it Works:
We have created a csv file of all of the required courses offered at Olin with information about how many credits they are worth, what suject areas they are in, when they should be taken, and how difficult they are. We have also created another scv file with each of the common majors offered at Olin and what courses are required for graduation for each. We use the pandas library to import that csv file into python and convert it into a dictionary.

Our program has four classes, the students class, major class, course class, and semester class. 
The course class has many attributes that characterize the course. This class is also used to turn the dictionary of courses into individual course objects with usable attributes.
The major class has the attributes of major name and required courses. The class is used to turn the dictonary of required courses into objects that can be mapped to the course objects.
The semester class has the attributes of smester number. This class is used to store the information about which course should be taken in each semester.
The student class contains information about that stduent such as their major, how many semesters they have left at Olin, and which courses they have taken up to this point. This class has methods for calculating the number of course credits left in each subject area necessary to graduate. Based off of these credit requirements, there is another method that reccommends a course schedule for the semesters remaining at Olin until graduation. 

In its current implementation, the course reccommender places the courses that must be taken in a particular semester into their correct place first then randomply sorts the other courses into the remaining slots and calculates the overall difficulty for each semester. This random sort is performed 1000 times and the scenario with the most even difficulty distributiuon over all semesters in selected as the best course path. 

# What to Install:
This program requires numpy!

## How to Use:
In order to use the Course Paths program, the user must first select a desired major and input each course they have taken thus far. The program then calculates the muber of course credits remianing and determines which specific courses are still needed. The program will then output a potential course plan that is optimized for the user prefrences and also fulfills all of the degree and general graduation requirements. In future implementations we hope too add in the ability of the user to enter their preferences for degree of difficulty as well as balance of group project and individual work desired for each semester.

## Change Log:
Version 1 - Given a limited list of courses, the program sorts the courses between two semesters in order to optimize for the lowest overall difficulty for both semesters.

Version 2 - Same optimization protocol but using a dictionary of all courses available at Olin.

Version 3 - Expanded functionality to account for all semesters, not just 2.

## Contributors:
Ellie Funkhouser, Becca Getto & Emma Price

## FAQs:
-Do I have to select a major?
Yes, in the current version of the program you must select a major.
In future versions we may try to expand the functionality so picking a specific major is not necessary.

## THINGS WE NEED HELP WITH:
- When running the program we are getting the error "TypeError: unhashable type: 'list'"
- Why is this happening? Why is the unhashable type problematic?
