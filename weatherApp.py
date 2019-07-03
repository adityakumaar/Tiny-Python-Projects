import requests
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#CreateWidgets() function to create tkinter widgets
def CreateWidgets():
    cityLabel = Label(root, text = "Enter City Name: ", bg = "skyblue")
    cityLabel.grid(row = 0, column = 0, padx = 10, pady = 5)
    cityEntry = Entry(root, width = 36, textvariable = cityName)
    cityEntry.grid(row = 0, column = 1, padx = 10, pady = 5)

    findButton = Button(root, text = "Find Weather: ", command = findWeather)
    findButton.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 2)

    cityCoord = Label(root, text = "City Co-ordinates: ", bg = "skyblue")
    cityCoord.grid(row = 2, column = 0, padx = 10, pady = 5)
    root.cityCoord = Entry(root, width = 36)
    root.cityCoord.grid(row = 2, column = 1, padx = 10, pady = 5)

    tempLabel = Label(root, text="Temperature: ", bg = "skyblue")
    tempLabel.grid(row = 3, column = 0, padx = 10, pady = 5)
    root.tempEntry = Entry(root, width = 36)
    root.tempEntry.grid(row = 3, column = 1, padx = 10, pady = 5)

    humidityLabel = Label(root, text="Humidity: ", bg = "skyblue")
    humidityLabel.grid(row = 4, column = 0, padx = 10, pady = 5)
    root.humidityEntry = Entry(root, width = 36)
    root.humidityEntry.grid(row = 4, column = 1, padx = 10, pady = 5)

    windLabel = Label(root, text="Wind: ", bg = "skyblue")
    windLabel.grid(row = 5, column = 0, padx = 10, pady = 5)
    root.windEntry = Entry(root, width = 36)
    root.windEntry.grid(row = 5, column = 1, padx = 10, pady = 5)

    pressureLabel = Label(root, text="Atmospheric Pressure: ", bg = "skyblue")
    pressureLabel.grid(row = 6, column = 0, padx = 10, pady = 5)
    root.pressureEntry = Entry(root, width = 36)
    root.pressureEntry.grid(row = 6, column = 1, padx = 10, pady = 5)

    descLabel = Label(root, text="Weather Description: ", bg = "skyblue")
    descLabel.grid(row = 7, column = 0, padx = 10, pady = 5)
    root.descEntry = Entry(root, width = 36)
    root.descEntry.grid(row = 7, column = 1, padx = 10, pady = 5)

#findWeather() function to find the weather of user specified city
def findWeather():

    #API KEY
    APIKey = "36a4945eea2aa596089bd167f09bd806"

    #Weather URL
    weatherURL = "http://api.openweathermap.org/data/2.5/weather?"

    #Storing user-input city name
    cityname = cityName.get()

    #Storing the complete URL with units = metric which means temparture will
    #be shown in CELCIUS
    requestURL = weatherURL + "appid=" + APIKey + "&q=" + cityname + "&units=metric"

    #Fetching the results and storing the response
    response = requests.get(requestURL)

    #Converting json format data into Python Format
    weatherResponse = response.json()

    #Checking if the value of is not equal to 404
    if weatherResponse["cod"] != "404":

        #value of "main" key
        weatherPARA = weatherResponse["main"]

        #value of  "coord" key
        coordinates = weatherResponse["coord"]
        latitude = coordinates["lat"]
        longitude = coordinates["lon"]

        #value of "wind" key
        wind = weatherResponse["wind"]
        windSpeed = wind['speed']
        windDirect = wind['deg']

        #temparature value in Celcius which is in Kelvin
        temperature = weatherPARA["temp"]

        #pressure value
        pressure = weatherPARA["pressure"]

        #humidity value
        humidiy = weatherPARA["humidity"]

        #weather value from weatherResponse
        weatherDesc = weatherResponse["weather"]

        #value corresponding to the "description"
        weatherDescription = weatherDesc[0]["description"]

        #Printing the results
        root.cityCoord.insert('0',"Lattitude: " + str(latitude) + " Longitude: "+str(longitude))
        root.tempEntry.insert('0',str(temperature) +" °C")
        root.humidityEntry.insert('0',str(humidiy) +" %")
        root.windEntry.insert('0',"Speed: " + str(windSpeed)+" meter/sec " + " Direction: "+str(windDirect)+"°")
        root.pressureEntry.insert('0',str(pressure) +" hPa")
        root.descEntry.insert('0',weatherDescription)

    # If cod key value is 404 then city is not found
    else:
        messagebox.showerror("ERROR", "City Not Found")

# Creating object of tk class
root = tk.Tk()

# Setting the title and background color
# disabling the resizing property
root.title("Weather Informtion")
root.resizable(False, False)
root.config(background = "skyblue")

# Creating tkinter variable
cityName = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
