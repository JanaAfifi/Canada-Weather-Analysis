import numpy as np

class TemperatureData:
    def __init__(self, date_object, minTemperature, maxTemperature, snowfall):
        self.date_object = date_object
        self.minTemperature = minTemperature
        self.maxTemperature = maxTemperature
        self.snowfall = snowfall
    def get_date(self):
        
        return self.date_object
    def get_minTemperature(self):
        
        return self.minTemperature
    def get_maxTemperature(self):
        
        return self.maxTemperature
    def get_snowfall(self):
        
        return self.snowfall
    def print(self):
        self.date_object.print()
        print(self.minTemperature)
        print(self.maxTemperature)
        print(self.snowfall)