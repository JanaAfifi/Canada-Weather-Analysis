import numpy as np

class FileIO:
    def __init__(self,filename):
        self.filename = filename
    
    def read_weather(self):
        
        data = np.loadtxt( self.filename , delimiter=',', 
                            skiprows=1, usecols=(0,1,2,3,4), dtype=np.float)
        return data

