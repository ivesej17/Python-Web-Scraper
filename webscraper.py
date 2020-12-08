#This is a web scraping application that collects weather data.
from list import Node
from list import List
from bs4 import BeautifulSoup
import requests, urllib, csv, os, datetime, urllib.request, re, sys

#URL Bank for different cities
Baltimore = "https://weather.com/weather/tenday/l/USMD0018:1:US"
Boston = "https://weather.com/weather/tenday/l/USMA0046:1:US"
Chicago = "https://weather.com/weather/tenday/l/USIL0225:1:US"
LA = "https://weather.com/weather/tenday/l/USCA0638:1:US"
NYC = "https://weather.com/weather/tenday/l/USNY0996:1:US"
Seattle = "https://weather.com/weather/tenday/l/USWA0395:1:US"
Wichita = "https://weather.com/weather/tenday/l/USKS0620:1:US"

cities = [Baltimore, Boston, Chicago, LA, NYC, Seattle, Wichita]
cityNames = ["Baltimore, MD", "Boston, MA", "Chicago, IL", "Los Angeles, CA", "New York City, NY", "Seattle, WA", "Wichita, KS"]
print("Welcome to Python Weather Scraper!")
print("Please select the city for which you wish to view weather details by inputting its corresponding number.")
selection = input("1. Baltimore, MD" + "\n" + "2. Boston, MA" + "\n" + "3. Chicago, IL" + "\n" + "4. Los Angeles, CA" + "\n" + "5. New York City, NY" + "\n" + "6. Seattle, WA" + "\n" + "7. Wichita, KS" + "\n")
print("\n" + "Currently viewing the weather for: " + cityNames[int(selection) - 1] + "\n")

#Create our BeautifulSoup object, and the list for our forecast objects.
url =  cities[int(selection) - 1]
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "lxml")
list = List()

class Forecast:
    def __init__(self, date, weather_description, precip, long_desc, temps):
        self.date = date
        self.weather_description = weather_description
        self.precip = precip
        self.long_desc = long_desc
        self.temps = temps

    def print(self):
        print(self.date)
        print("---------------")
        print("Short description: " + self.weather_description + "\n")
        print("Chance of precipitation: " + self.precip + "\n")
        print("Detailed description: " + self.long_desc + "\n")

    def temperaturePrint(self):
        if len(self.temps) == 5:
            print("Temperature (only one temp reported): " + self.temps[2] + self.temps[3] + " F")

        elif len(self.temps) == 6:
            print("High temp: " + self.temps[0] + self.temps[1] + " F" + "\n")
            print("Low temp: " + self.temps[3] + self.temps[4] + " F")

        print("\n \n")


for i in range(15): #This for loop is doing the main legwork of the program. It is using the lxml parser to grab the data we need from each row and column of the HTML.
    name_of_day = soup.find_all("tr")[i+1].find_all("td")[1].find(attrs={"class":"date-time"}).text

    numerical_date = soup.find_all("tr")[i+1].find_all("td")[1].find(attrs={"class":"day-detail clearfix"}).text

    day = name_of_day + " - " + numerical_date

    short_description = soup.find_all("tr")[i+1].find_all("td")[2].text

    precip = soup.find_all("tr")[i+1].find_all("td")[4].text

    long_desc = soup.find_all("tr")[i+1].find_all("td")[1]['title']

    temps = soup.find_all("tr")[i+1].find_all("td")[3].text

    list.push(Forecast(day, short_description, precip, long_desc, temps))


weatherTable = soup.find("div",{"class":"twc-table-scroller"})
description = weatherTable.find(attrs={"class":"clickable closed"})
soup.find_all("td")[1].find_all("td", attrs={"class":"description"})
soup.find_all("tr")[1].find_all("td")[1]['title']

for j in range(15):
    list[j].print()
    list[j].temperaturePrint()

terminate = input("Press enter to exit")