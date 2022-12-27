import numpy as np
from TemperatureData import *
from FileIO import *
from Chart import *

class WeatherAnalyser:
    
    def __init__(self,TemperatureData):
        self.TemperatureData = TemperatureData
    
    def getMinTemp(self):
        min_temp_list = [self.TemperatureData[i].get_minTemperature() for i in range(len(self.TemperatureData))]
        return np.min(min_temp_list)

    def getMinTempAnnully(self):
        
        years = [self.TemperatureData[i].get_date().get_year() for i in range(len(self.TemperatureData))]
        unique_years = np.unique(years, axis = 0)
        yearList = []
        for yearIndex in range(len(unique_years)) :
            year_row = []
            for td in self.TemperatureData:       #temperature data
                if td.get_date().get_year() == unique_years[yearIndex]:
                    year_row.append(td.get_minTemperature())
            yearList.append(year_row)
        result_annual_Min_temp = np.zeros((len(unique_years),2)) # 2, creates an array to fill it out with years and annual min temperature
        for i in range(len(unique_years)):
            result_annual_Min_temp[i][0] = unique_years[i]
            result_annual_Min_temp[i][1] = np.min(yearList[i])
        return result_annual_Min_temp

    def getMaxTemp(self):
        
        max_temp_list = [self.TemperatureData[i].get_maxTemperature() for i in range(len(self.TemperatureData))]
        return np.max(max_temp_list)
 

    def getMaxTempAnnully(self):
        
        years = [self.TemperatureData[i].get_date().get_year() for i in range(len(self.TemperatureData))]
        unique_years = np.unique(years, axis = 0)
        yearList = []
        for yearIndex in range(len(unique_years)) :
            year_row = []
            for td in self.TemperatureData:       #temperature data
                if td.get_date().get_year() == unique_years[yearIndex]:
                    year_row.append(td.get_maxTemperature())
            yearList.append(year_row)
        result_annual_Max_temp = np.zeros((len(unique_years),2)) # 2, creates an array to fill it out with years and annual min temperature
        for i in range(len(unique_years)):
            result_annual_Max_temp[i][0] = unique_years[i]
            result_annual_Max_temp[i][1] = np.max(yearList[i])
        return result_annual_Max_temp
        
    
    def getAvgSnowFallAnnually(self):

        years = [self.TemperatureData[i].get_date().get_year() for i in range(len(self.TemperatureData))]
        unique_years = np.unique(years, axis = 0)
        yearList = []
        for yearIndex in range(len(unique_years)) :
            year_row = []
            for td in self.TemperatureData:       #td ---> temperature data
                if td.get_date().get_year() == unique_years[yearIndex]:
                    year_row.append(td.get_snowfall())
            yearList.append(year_row)
        result_annual_avg_SnowFall = np.zeros((len(unique_years),2)) # 2, creates an array to fill it out with years and annual min temperature
        for i in range(len(unique_years)):
            result_annual_avg_SnowFall[i][0] = unique_years[i]
            result_annual_avg_SnowFall[i][1] = np.average(yearList[i])
        return result_annual_avg_SnowFall

    def getAvgTempAnnually(self):
        
        years = [self.TemperatureData[i].get_date().get_year() for i in range(len(self.TemperatureData))]
        unique_years = np.unique(years, axis = 0)
        yearList = []
        for yearIndex in range(len(unique_years)) :
            year_row = []
            for td in self.TemperatureData:       #temperature data
                if td.get_date().get_year() == unique_years[yearIndex]:
                    year_row.append(td.get_minTemperature())
                    year_row.append(td.get_maxTemperature())
            yearList.append(year_row)
        result_annual_avg_temp = np.zeros((len(unique_years),2)) # 2, creates an array to fill it out with years and annual min temperature
        for i in range(len(unique_years)):
            result_annual_avg_temp[i][0] = unique_years[i]
            result_annual_avg_temp[i][1] = np.average(yearList[i])
        
        return result_annual_avg_temp