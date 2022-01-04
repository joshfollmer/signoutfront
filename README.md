This was a midterm projected created for the class python concepts and methodology, taken in spring 2021. The prompt was as follows:

Assume the sign cycles every 20 seconds, you can see and read the sign at the top of the hill for approximately 60 seconds (normal distribution, sd of 5), 
and there are 20 slides. What percentage of the slides will a student see if they come to school 4 days a week?

Goals
Write a script using a circular linked list to answer this question with some simulations.
Take user input for these numbers.

Explanation:
The simulation uses a datetime object to keep track of time, and advances in 20 second increments. Each tick, a new sign is picked from the list and a check is performed to see if
it is time for a student to get to school.

At the start of each run, a student will be generated at random. First they get a name, which is picked randomly. Then they get a Monday - Wednsesday schedule, and a 
Tuesday - Thursday schedule. Then, stats are chosen. Each student gets a punctuality, or how likely they are to be late for class. Then they randomly get a range of speeds 
they will drive, they will drive faster if they are late and slower if they are early. 

The first thing that happens is a list of signs is generated, and then a student is generate. The user can change the generate settings in the gui. Once the program is run,
the simulate method will run four times for each day of the week. The simulation will decide if they are late or early, and will generate the time that they are actually getting 
to school. Once it is time for them to arrive, the see_slides method will run. 

see_slides will determine and store how many slides they see on their strip to class. First, the amount of time they can see each slide for must be determined. 
First, their feet per second (FPS) must be found by multipliyng their miles per hour by 1.47. Then, this must be converted into seconds that they can see the slide for. 
This is done by dividing 2205 by their FPS, 2205 the amount of feet that the sign can be seen for. I found this number by taking the mean number of time seeing the sign of 60 
seconds from the prompt, assumed a speed limit of 25 (that is the speed limit near where the sign is in real life), took the Fps of 25 MPH and multiplyed that by 60, the amount of
time the sign can be seen for. 
The number of slides seen is found by dividing the time they could see the sign for by 20, and rounding it up because seeing a sign for less than 20 seconds still counts. 
The amount of slides they saw during the day is appended to two lists, one will be the weekly total and one will be the total for all weeks.

GUI
The GUI works through TKinter. First, it will set up a grid and populate it with options. The user has control over how many weeks will simulate, the speed range of an early student 
and of a late student, the chance of them being late, and a 24 hour cycle or not. The 24 cycle will change whether the slide is chosen at random, or if it will simulate a 24 sign.
Running from the GUI will generate a student according to the users selections, and then run the backend. It will get the results back, and display how many signs they saw and
how many of those slides were unique. 
