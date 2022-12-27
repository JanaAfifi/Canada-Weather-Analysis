import numpy as np
from FileIO import*
from Date import*
from TemperatureData import*
from Chart import *
from WeatherAnalyser import *
import matplotlib.pyplot as plt

def main(): 
    
    print("\n-------------------------------------------------------------\n")
    print(" 1- Get Minimum Temperature of 1990-2019")
    print(" 2- Get Maximum Temperature of 1990-2019")
    print(" 3- Get Minimum Temperature of 1990-2019 Annually")
    print(" 4- Get Maximum Temperature of 1990-2019 Annually")
    print(" 5- Get Average Snowfall between 1990-2019 Annually")
    print(" 6- Get Average Temperature between 1990-2019 Annually")
    print(" 7- LineChart Minimum Temperature of 1990-2019 Annually")
    print(" 8- LineChart Maximum Temperature of 1990-2019 Annually")
    print(" 9- BarChart Average Snowfall between 1990-2019 Annually")
    print(" 10- BarChart Average Temperature between 1990-2019 Annually")
    print("\n-------------------------------------------------------------\n")
    
    
    file_name = "CalgaryWeather.csv"
    file_obj = FileIO(file_name)
    data = file_obj.read_weather()
    np.set_printoptions(suppress=True)
    
    temperature = []
    for row in data:
        date = Date(row[1],row[0])
        T = TemperatureData(date,row[3],row[2],row[4])
        temperature.append(T)
        a = WeatherAnalyser(temperature)
    
    def get_min_temp_1990_2019(Weather_Analyser):
        
        print("\n---------------------------------------------------\n")
        print("The min Temperature between 1990 to 2019 is:",\
        a.getMinTemp())
        print("\n----------------------------------------------------\n")
    
    def get_max_temp_1990_2019(Weather_Analyser):
        
        print("\n----------------------------------------------------\n")
        print("The max Temperature between 1990 to 2019 is:",\
        a.getMaxTemp())
        print("\n----------------------------------------------------\n")
    
    def get_min_temp_1990_2019_Annually(Weather_Analyser):
        
        print("\n----------------------------------------------------\n")
        print("The min Temperature between 1990 to 2019 Annually is:",\
        a.getMinTempAnnully())
        print("\n----------------------------------------------------\n")
    
    def get_max_temp_1990_2019_Annually(Weather_Analyser):
    
        print("\n----------------------------------------------------\n")
        print("The max Temperature between 1990 to 2019 Annually is:",\
        a.getMaxTempAnnully())
        print("\n----------------------------------------------------\n")
    
    def get_Avg_snowfall_1990_2019_Annually(Weather_Analyser):
    
        print("\n----------------------------------------------------\n")
        print("The average snowfall between 1990 to 2019 Annually is:",\
        a.getAvgSnowFallAnnually())
        print("\n----------------------------------------------------\n")
    
    def get_Avg_temp_1990_2019_Annually(Weather_Analyser):
    
        print("\n----------------------------------------------------\n")
        print("The average temperature between 1990 to 2019 Annually is:",\
        a.getAvgTempAnnually())
        print("\n----------------------------------------------------\n")
    
    def linechart_min_1990_2019(Weather_Analyser):
    
        print("\n----------------------------------------------------\n")
        print("LineChart of minimum Temperature between 1990 to 2019 Annually is:")
        chart = Chart() 
        min_annual_ = a.getMinTempAnnully()
        x = [min_annual_[i][0] for i in range(len(min_annual_))]
        y = [min_annual_[i][1] for i in range(len(min_annual_))]
        title = "Minimum Temperature between 1990 to 2019 Annually"
        xlabel = "Years"
        ylabel = "Minimum temperature"
        chart.draw_Line_Chart(x,y,title,xlabel,ylabel)
        print("\n----------------------------------------------------\n")
    
    def linechart_max_1990_2019(Weather_Analyser):
    
        print("\n----------------------------------------------------\n")
        print("LineChart of maximum Temperature between 1990 to 2019 Annually is:")
        chart = Chart() 
        max_annual_ = a.getMaxTempAnnully()
        x = [max_annual_[i][0] for i in range(len(max_annual_))]
        y = [max_annual_[i][1] for i in range(len(max_annual_))]
        title = "Maximum Temperature between 1990 to 2019 Annually"
        xlabel = "Years"
        ylabel = "Maximum temperature"
        chart.draw_Line_Chart(x,y,title,xlabel,ylabel)
        print("\n----------------------------------------------------\n")
    
    def barchart_avg_snowfall_1990_2019(Weather_Analyser):
    
        print("\n----------------------------------------------------\n")
        print("BarChart of Average Snowfall between 1990 to 2019 Annually is:")
        chart = Chart() 
        Avg_snowfall_annual_ = a.getAvgSnowFallAnnually()
        x = [Avg_snowfall_annual_[i][0] for i in range(len(Avg_snowfall_annual_))]
        y = [Avg_snowfall_annual_[i][1] for i in range(len(Avg_snowfall_annual_))]
        title = "Average Snowfall between 1990 to 2019 Annually"
        xlabel = "Years"
        ylabel = "Average Snowfall"
        chart.draw_Bar_Chart(x,y,title,xlabel,ylabel)
        print("\n----------------------------------------------------\n")
    
    def barchart_avg_1990_2019(Weather_Analyser):
    
        print("\n----------------------------------------------------\n")
        print("BarChart of Average Temperature between 1990 to 2019 Annually is:")
        chart = Chart() 
        avg_annual_ = a.getAvgTempAnnually()
        x = [avg_annual_[i][0] for i in range(len(avg_annual_))]
        y = [avg_annual_[i][1] for i in range(len(avg_annual_))]
        title = "Average Temperature between 1990 to 2019 Annually"
        xlabel = "Years"
        ylabel = "Average temperature"
        chart.draw_Bar_Chart(x,y,title,xlabel,ylabel)
        print("\n----------------------------------------------------\n")
    
    while True:
        
        n = int(input("Pick a number from the menu: "))
        
        while n < 1 or n > 10 :
            n = int(input("Please pick a number from the menu: "))    
        if n == 1 :
            get_min_temp_1990_2019(a)
        elif n == 2 :
            get_max_temp_1990_2019(a)
        elif n == 3 :
            get_min_temp_1990_2019_Annually(a)
        elif n == 4 :
            get_max_temp_1990_2019_Annually(a)
        elif n == 5 :
            get_Avg_snowfall_1990_2019_Annually(a)
        elif n == 6 :
            get_Avg_temp_1990_2019_Annually(a)
        elif n == 7:
            linechart_min_1990_2019(a)
        elif n == 8:
            linechart_max_1990_2019(a)
        elif n == 9:
            barchart_avg_snowfall_1990_2019(a)
        elif n == 10:
            barchart_avg_1990_2019(a)


if __name__=="__main__":
    main()