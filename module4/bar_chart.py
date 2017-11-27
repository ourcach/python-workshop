#!/usr/bin/python

import requests
import numpy as np
from matplotlib import pyplot as plt

def get_forecast(url):
    """ Return the forecast data in json 
    """
    r = requests.get(url)
    return r.json()


def process_data(data):
    """ Return data to be used by the plot lib
    """
    info = {
        'cities': [],
        'temperatures': [],
        'humidities': [],
    }
    cities = data['list']
    for city in cities:
        main_data = city['main']
        info['cities'].append(city['name'])
        info['temperatures'].append(main_data['temp'])
        info['humidities'].append(main_data['humidity'])

    return info


def show_plot(data):
    """ 
    """
    cities = tuple(data['cities'])
    temperatures = tuple(data['temperatures'])
    humidities = tuple(data['humidities'])
    N = len(cities)
    
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    
    _, ax = plt.subplots()
    rects1 = ax.bar(ind, temperatures, width, color='r')
    rects2 = ax.bar(ind+width, humidities, width, color='y')
    
    # add some text for labels, title and axes ticks
    ax.set_ylabel('Units')
    ax.set_title('Temperature and humidity by city')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( cities )
    
    ax.legend( (rects1[0], rects2[0]), ('Temperature', 'Humidity') )
    
    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                    ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)
    
    plt.show()
    

# Exec the script
API=''
url = 'http://api.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&cluster=yes&APPID={}'.format(API)
data = get_forecast(url)
processed_data = process_data(data)
show_plot(processed_data)
