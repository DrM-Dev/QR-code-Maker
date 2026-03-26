import time
from turtle import Turtle, Screen

#________________________
screen = Screen()
screen.bgcolor("black")
#________________________
available_colors = ["black", "white", "grey", "gray", "blue", "red", "green", "purple", "brown", "cyan", "gold", "pink"]


class MyLoading(Turtle):
    def __init__(self):
        super().__init__()
        ##################
        self.hideturtle()
        # ________________________
        self.STEP = -12  # should be divisor of 360
        self.GAP = 45  # in degrees
        self.PEN_SIZE = 4  # emulated pen width
        self.RADIUS = 24
        ###########
        self.default_color = (1.0, 1.0, 1.0)
        self.color_list = []
        self.degrees = [0, 45, 90, 180, 270, 360]
        self.loading_color = "grey"

        # ________________________
    def await_loading(self, loading_color):  # intentionally dangerous default values
        self.loading_color = loading_color
        #-----------------------------------------
        self.STEP = -12  # should be divisor of 360
        self.GAP = 45  # in degrees
        self.PEN_SIZE = 4  # emulated pen width
        self.RADIUS = 24
        ###########
        if loading_color in available_colors:
            self.default_color = loading_color
        else:
            self.default_color = "grey"
        ###########
        self.color_list = []
        self.degrees = [0, 45, 90, 180, 270, 360]
        #=======================
        color = self.default_color
        ###################
        for colors in self.default_color:
            self.color_list.append(colors)
        ###################
        if self.degrees[0] == 0:
            self.color_list.append(self.color_list.pop(0))
            self.color(color)

        self.tilt(self.STEP)

        self.degrees[0] = (self.degrees[0] + self.STEP) % 360

        # ________________________#________________________
        self.speed('fastest')
        self.backward(self.RADIUS)
        self.right(90)
        #############
        self.begin_poly()
        self.circle(self.RADIUS, 360 - self.GAP, 60)
        self.left(90)
        self.forward(self.PEN_SIZE)
        self.right(90)
        self.circle(self.RADIUS - self.PEN_SIZE, self.GAP - 360, 60)
        self.end_poly()

        # ________________________
        screen.addshape('loading', self.get_poly())


    # ___________________________________________________________________________
    def loading_looper(self):
        self.clear()
        self.hideturtle()
        #
        self.await_loading(self.loading_color)

    #___________________________________________________________________________
    def finished_loading(self):
        self.clear()
        self.hideturtle()
        #

        #
        # print("ALERTED")
