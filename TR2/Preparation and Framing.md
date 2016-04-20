## Course Paths Framing Document
### Emma Price, Ellie Funkhouser & Becca Getto

#### Agenda: 
- Outline problem - 1 minute
- What we have done - 1-2 minutes
- What’s working - 2 minutes
- Demo! - 2 minutes
- What we still need to do - 2 minutes
- Questions and feedback - 15 minutes

#### Background:
Currently, it is very challenging to plan what classes you have to take at Olin and at what point in time you should take them so that you can optimize your time and energy. In order to plan when to take course you have to consult your advisor, talk to many upperclassman, and refer to the course listings website which is very challenging to navigate. To improve upon this current system, we are attempting to create an interactive program that allows you to input your interests, intended major, and the classes you have taken and then generates a proposed plan for what future classes you can take and when you should take them.

#### Portions completed:
Thus far, we have implemented a program that takes in a user’s major, what courses they have taken, and how many semesters they have left to complete and compiles a course plan. This plan first fulfills the required courses for a major and then looks at when those courses are typically taken. The course plan is then optimized around course difficulty to make sure all of the semesters have somewhat even challenge levels. We have been able to implement a graphical user interface for inputting a student’s major, courses taken, and how many semesters are left at Olin. This information is sent to the recommender algorithm in order to generate a course path. Currently the course path is simply a list of the names of courses that should be taken in each semester without a graphical component. We will be adding in this graphical aspect as we proceed with program development. We framed our data and manipulated it using the pandas library and are using the Tkinter library to formulate our graphical user interface (GUI). 

#### End goal:
At the end of this project we hope to have a program that allows users to input the information described above and generate a graphic of what classes the user should take and when they should take them. We would like this graphic to be based on the prefered semester to take the course and the difficulty level of the course. We think we would also like it to take into account the user’s preference for work distribution (alternating vs. balanced ENG/AHSE semesters, easier fall or easier spring, etc…). Our stretch goal would be to also suggest classes the user may like based on their interests without having to select a major.

#### Possible challenges:
- Optimizing the data (algorithm/weighting system)
- Intuitive user input system
- Data display for maximum effective communication

#### Questions:
- What should the output look like?
- What other than difficulty and required or suggested semester should the recommender take into account?
