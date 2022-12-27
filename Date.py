import numpy as np

class Date:
    def __init__(self,Month,Year):
        self.Month = Month
        self.Year = Year
    
    def get_month(self):
        return self.Month
    
    def get_year(self):
        return self.Year
    
    def print(self):
        print(self.Year)
        print(self.Month)