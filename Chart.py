import numpy as np
import matplotlib.pyplot as pyplot

class Chart:
    def __init__(self):
        pass
        
    def draw_Line_Chart(self,x,y,title,xlabel,ylabel):
       
        fig = pyplot.figure()
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)
        pyplot.plot(x,y, marker='o')
        pyplot.show()

    def draw_Bar_Chart(self,x,y,title,xlabel,ylabel):
        
        fig = pyplot.figure()
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)
        pyplot.bar(x,y)
        pyplot.show()