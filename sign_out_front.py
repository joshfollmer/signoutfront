import circular_linked_list
from random import randint
from random import choice
from datetime import datetime
from datetime import timedelta
from math import ceil

class Sign:
    def __init__(self):
        self.slides = circular_linked_list.CircularLinkedList()
        #populates the list with slides
        for i in range(1, 21):
            self.slides.append_right(f"Slide {i}")

class Student:
    def __init__(self, min_speed_lower, max_speed_lower, min_speed_higher, max_speed_higher, min_punc, max_punc, ):
        #makes a list of arrival times. it is in the format of year, month, day, hour, minute. the date must be included so the time can be added to or subtracted from (which is think is dumb)
        arrive_times = [datetime(2021, 1, 1,8), datetime(2021, 1, 1,9,40), datetime(2021, 1, 1,11,10), datetime(2021, 1, 1,12,50), datetime(2021, 1, 1,14,30), datetime(2021, 1, 1,16,50), datetime(2021, 1, 1,17, 50), datetime(2021, 1, 1,19)]
        names = ["Lucas", "Will", "Noah", "Alex", "Josh", "Doug", "Mike", "John", "David", "Aaron", "Joye", "Abby", "Sofia", "Fiona", "Zoey", "Lily", "Hannah", "Bella", "Anna", "Elena"]
        #in my experience i had the same schedule in pairs for monday and wednesday and tuesday and thursday, so i did that here
        self.mw = choice(arrive_times)
        self.tt = choice(arrive_times)
        #this is their punctuality, or the % chance of them being late on any given day
        self.punc = randint(min_punc, max_punc)
        self.seen_slides = []
        self.total_slides = []
        self.name = choice(names)
        self.temp = sign.slides.head
        self.min_speed_lower = min_speed_lower
        self.max_speed_lower = max_speed_lower
        self.min_speed_higher = min_speed_higher
        self.max_speed_higher = max_speed_higher
 
    def simulate(self, day, cycle_24):

        #day 1 is monday, day 2 is tuesday, etc
        if day == 1 or day == 3:
            arrive = self.mw 
        if day == 2 or day == 4:
            arrive = self.tt
        
        #picks a nnmber between one and ten. if that number is less than their puncuality, they are early. this is my way of making a variable a percentage
        odds = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
        tardy = choice(odds)
        if tardy <= self.punc:
            # if they are early, subtract some time amount of minutes between one and ten from their arrival time
            arrive -= timedelta(minutes=randint(1, 10))
            #if theyre early, theyll be more likely to drive slowly, and see more slides
            self.speed = randint(self.min_speed_lower, self.max_speed_lower)
        else:
            #opposite is true for if they are late
            arrive += timedelta(minutes=randint(1,10))
            self.speed = randint(self.min_speed_higher, self.max_speed_higher) 

        if cycle_24 == True:
             t = datetime(2021, 1, 1, 0)
             loops = 4320
        else:
            t = datetime(2021, 1, 1, 7,50)
            loops = 2046
            #picks a random slide to start the day at
            for i in range(randint(1, 21)):
                self.temp = self.temp.next 
        
        #this loop will simulate the school day, in 20 second increments. if the time of the day is equal to their arrival time, it will run the function to see the slides
        #keep in mind that if the arrival time is altered by seconds, this whole thing falls apart because it has to be a multiple of 20 seconds
        for i in range(loops):
            self.temp = self.temp.next
            if t == arrive:
                self.see_slides()
            t += timedelta(seconds=20)

    def see_slides(self):
        #we need to find out how long they can see the sign for
        #first we find the feet per second, found by multiplying their current speed by 1.47
        fps = self.speed * 1.47
        #we divide the number of feet where they can see the sign and divide it by the feet per second, giving us the number of seconds they can see the sign for
        #i found 2205 by taking the mean amount of time of 60 seconds, assuming thats at the speed limit of 25 mph, finding the ft/s of 25 nad multiplying that by 60
        time_seeing = 2205 / fps
        #number of slides seen is the number of seconds divided by 20, rounded up. note that a decimal number refers to the amount of time seeing the slide, not the slide itself
        num_of_slides = ceil(time_seeing / 20)
        
        for i in range(num_of_slides):
            #the reason there is two is because seen slides will get cleared each week but total slides will not cleared
            self.seen_slides.append(self.temp)
            self.total_slides.append(self.temp)
            self.temp = self.temp.next
        

sign = Sign()
