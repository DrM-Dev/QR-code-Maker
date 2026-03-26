import time
from loadingV1 import MyLoading
#----------------------------
from turtle import Turtle
#____________________________
available_bar_colors = ["black", "white", "grey", "gray", "blue", "red", "green", "purple", "brown", "cyan", "gold", "pink"]
#____________________________

class LoadingScreen:
    def __init__(self):
        #defaults:
        self.loader = MyLoading()
        self.loading_speed = 0.1
        self.buffer_time = 5
        #---------------------
        self.number_of_times = 0 #debug

    # ======================================================================
    def start_loading_screen(self, loading_speed, buffer_time, loading_color):
        if loading_speed > 0:
            self.loading_speed = loading_speed
        else:
            self.loading_speed = 0.1
        #-------------------
        if buffer_time > 0:
            self.buffer_time = buffer_time
        else:
            self.buffer_time = 5
        #===================================
        self.number_of_times = 0 #debug
        #=============================================|Loading TEXT|
        #some text:
        loading_text = Turtle()
        loading_text.hideturtle()
        loading_text.penup()
        loading_text.color(loading_color)
        loading_text.goto(0,-80)
        loading_text.write("Creating QR-Code...", align="Center", font=("Arial", 15, "normal"))
        loading_text.goto(-8,-100)
        loading_text.write("Please wait", align="Center", font=("Arial", 10, "normal"))
        #===================================
        for numbers in range(1,self.buffer_time):
            self.loader.await_loading(loading_color)
            self.number_of_times +=1 #debug
            self.loader.await_loading(loading_color)
            self.loader.await_loading(loading_color)
            self.loader.await_loading(loading_color)
            time.sleep(self.loading_speed)
            print(self.number_of_times) #debug
            self.loader.loading_looper()
        ###################################FINISHED LOADING STEPS:
        self.loader.finished_loading()
        for numbers in range(1,5):#-------->stabling loading icon
            self.loader.await_loading(loading_color)
        loading_text.clear()
        loading_text.write("DONE! :)\n", align="Center", font=("Arial", 15, "normal"))
        loading_text.goto(-8, -100)
        loading_text.write("opening file...", align="Center", font=("Arial", 10, "normal"))

        #==================================================================================|
    def start_loading_bar(self, buffer_time, loading_color):
        ######################
        if loading_color in available_bar_colors:
            loading_color = loading_color
        else:
            loading_color = "grey"
        #-------------------
        if buffer_time != 0:
            self.buffer_time = buffer_time
        else:
            self.buffer_time = 10
        # ===========================
        # ===========================
        loading_bar = Turtle()
        loading_bar.penup()
        loading_bar.hideturtle()
        # -----------------------
        loading_bar.color(loading_color)
        space = " "
        # -----------------------
        loading_bar.goto(0, -100)
        # -----------------------
        space = space * buffer_time * 2
        loading_bar.write("(" + space + ")", align="Center", font=("Arial", 20, "normal"))
        # -----------------------
        loading_bar.goto(-buffer_time * 8, -85)
        loading_bar.pensize(15)
        loading_bar.setheading(0)
        #########################
        for _ in range(1, buffer_time):
            loading_bar.pendown()
            loading_bar.forward(8.5)
            time.sleep(1)
            loading_bar.forward(9)



#Example for use:
# load_it = LoadingScreen()
# load_it.start_loading_screen(0,0, "cyan")
# # load_it.start_loading_bar(10, "cyan")
