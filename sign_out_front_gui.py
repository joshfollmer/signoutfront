import tkinter as tk
import sign_out_front

class Sign_GUI:
    def __init__(self, window):
        settings_label = tk.Label(window, width=20, text="Simulation Settings")
        settings_label.grid()

        weeks_label = tk.Label(window, text="Weeks")
        weeks_label.grid(row=1)

        #number of weeks sim runs for 
        weeks_var = tk.DoubleVar(value=1)
        self.weeks = tk.Spinbox(window, from_= 1, to= 16, wrap=True, width=5,increment=1, textvariable=weeks_var)
        self.weeks.grid(row=2)
        
        
        speed_range_lower_label = tk.Label(window, width = 20, text="Lower Speed Range")
        speed_range_lower_label.grid(row=3)
        #the minimum and max their speed can be when theyre early
        min_speed_lower = tk.DoubleVar(value=20)
        max_speed_lower = tk.DoubleVar(value=30)
        
        self.min_speed_lower = tk.Spinbox(window, from_=10, to=40, width=5, textvariable=min_speed_lower)
        self.max_speed_lower = tk.Spinbox(window, from_=20, to= 60, width = 5, textvariable=max_speed_lower)

        self.min_speed_lower.grid(row=4, sticky=tk.W)
        self.max_speed_lower.grid(row=4, sticky=tk.E)

        #the minimum their speed can be when theyre late
        speed_range_higher_label = tk.Label(window, width = 20, text="Higher Speed Range")
        speed_range_higher_label.grid(row=5)

        min_speed_higher= tk.DoubleVar(value = 30)
        max_speed_higher = tk.DoubleVar(value=40)

        self.min_speed_higher =tk.Spinbox(window, from_=20, to=80, textvariable=min_speed_higher, width=5)
        self.max_speed_higher = tk.Spinbox(window, from_=30, to=100, textvariable=max_speed_higher, width=5)

        self.min_speed_higher.grid(row=6, sticky=tk.W)
        self.max_speed_higher.grid(row=6, sticky=tk.E)

        #how likely they are to be early
        constist_label = tk.Label(window, width= 20, text="Student Puncuality")
        constist_label.grid(row=7)

        #min and max  range of their puncuality
        min_consist = tk.DoubleVar(value=1)
        max_consist = tk.DoubleVar(value=10)

        self.min_consist = tk.Spinbox(window,from_=1, to=10, width= 5, textvariable=min_consist)
        self.max_consist = tk.Spinbox(window, from_=1, to=10, width= 5, textvariable=max_consist)

        self.min_consist.grid(row=8, sticky=tk.W)
        self.max_consist.grid(row=8, sticky=tk.E)

        time_label = tk.Label(window, text="24 hour sign cycle")
        time_label.grid(row=9)

        #determines if the sign starts on a  random slide at 750 or always on the same slide at midnight
        self.hours = False
        on_button = tk.Button(window, text="On", command=self.set_true)
        off_button = tk.Button(window, text = "Off", command=self.set_false)

        on_button.grid(row=10, sticky=tk.W)
        off_button.grid(row=10,sticky=tk.E)

        start_button = tk.Button(window, text="Start", command=self.start_program)
        start_button.grid(row=11)

    def set_true(self):
        self.hours = True
    
    def set_false(self):
        self.hours = False

    def start_program(self):
        #this is my really stupid but effective way of clearing the last runs results
        for i in range(17):
            gfd = tk.Label(window, text = '                                                                    ')
            gfd.grid(column=1, row=i)
        #creates a studnet with the attributes determined  by the user
        s = sign_out_front.Student(int(self.min_speed_lower.get()), int(self.max_speed_lower.get()), int(self.min_speed_higher.get()), int(self.max_speed_higher.get()), int(self.min_consist.get()), int(self.max_consist.get()))
        #makes a nested loop, the outer one is number of weeks, inner one is days in the week
        for g in range(int(self.weeks.get())):
            for i in range(1, 5):
                s.simulate(i, bool(self.hours))
            #gets rid of duplicate slides in the weeks list
            s.seen_slides = set(s.seen_slides)
            #outputs result on the right
            result = f'On week {g} {s.name} saw {len(s.seen_slides)} unique slides.'
            result_label = tk.Label(window, text=result)
            result_label.grid(column = 1, row=g)
            #resets their weekly list
            s.seen_slides = []
        #gets their unique slides from the total slides
        total_unique_slides = set(s.total_slides)
        #outputs the final result
        total_results_label = tk.Label(window, text=f"{s.name} saw {len(s.total_slides)} total slides and {len(total_unique_slides)} unique slides")
        total_results_label.grid(column=1, row=g+1)
    

window = tk.Tk()
window.title('Sign Simulation')
window.geomtery = ('1400x600')
sign_simulation = Sign_GUI(window)
window.mainloop()