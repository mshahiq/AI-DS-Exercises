from bs4 import BeautifulSoup
import requests
import re
import numpy as np
import pandas as pd

def temperature_conversion(Fahrenheit):
    temperature_in_celsius = (Fahrenheit - 32) * (5/9)

    return temperature_in_celsius

DAYS = []
description = []
min_temp_C = []
max_temp_C = []



url = 'https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148'

page = requests.get(url)
#print(page)

content = BeautifulSoup(page.content, 'html.parser')



for day in range(2,12,2):
    days = content.find_all('div',class_='col-sm-2 forecast-label')
    find_days = days[day].find('b')
    DAYS.append(find_days.get_text())

    # print(find_days.get_text())                               #### PRINT THE DAYS ( INCLUDING NIGHTS)

for night in range(3,13,2):
    nights = content.find_all('div',class_='col-sm-2 forecast-label')
    find_nights = nights[night].find('b')
    
    #print(find_nights.get_text()) 
    

for day_discription in range(2,12,2):
    
    days_discription = content.find_all('div',class_='col-sm-10 forecast-text')
    day_descriptions = days_discription[day_discription]

    # print(day_descriptions.get_text())

    #day_temperature = []

    extracted_day_description = day_descriptions.get_text()         # 'extracted_day_description' prints the forecast description

    description.append(extracted_day_description)

    day_temperature = re.findall('[0-9]+',extracted_day_description)
    string_day_temperature = day_temperature[0]
    int_day_temperature = int(string_day_temperature)
    int_day_C = temperature_conversion(int_day_temperature)
    int_day_C = round(int_day_C,1)
    max_temp_C.append(int_day_C)
    # print(type(int_day_temperature))

    # print(round(temperature_conversion(int_day_temperature),1))     # PRINTING MY DAY TEMPERATURES IN CELSIUS


for night_discription in range(3,13,2):
    
    nights_discription = content.find_all('div',class_='col-sm-10 forecast-text')
    night_descriptions = nights_discription[night_discription]

    # print(night_descriptions.get_text())

    extracted_night_description = night_descriptions.get_text()     # 'extracted_night_description' prints the forecast description

    

    night_temperature = re.findall('[0-9]+',extracted_night_description)
    string_night_temperature = night_temperature[0]
    int_night_temperature = int(string_night_temperature)

    int_night_C = temperature_conversion(int_night_temperature)
    int_night_C = round(int_night_C,1)
    min_temp_C.append(int_night_C)



data = {'Days':DAYS,'Maximum Temperature in C':max_temp_C,'Minimum Temperature in C':min_temp_C,'Description':description}
dates_from_08 = pd.date_range('2022-02-08',periods=5,freq='D')

df = pd.DataFrame(data,index=dates_from_08)
df.index.name = 'Dates'
print(df)