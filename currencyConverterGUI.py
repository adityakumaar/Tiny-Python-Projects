import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk

#Making a list of currencies
currencyList = ['AED', 'AUD', 'BHD', 'BRL', 'CAD',
                'CNY', 'EUR', 'HKD', 'INR', 'USD']

#CreateWidgets() function to create widgets for the GUI
def CreateWidgets():
    inputAMTL = Label(root, text="ENTER THE AMOUNT:", bg="skyblue")
    inputAMTL.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

    inputAMTTxt = Entry(root, width=20, textvariable=getAMT)
    inputAMTTxt.grid(row=1, column=3, columnspan=2, pady=10)

    fromLabel = Label(root, text="FROM:", bg="skyblue")
    fromLabel.grid(row=2, column=1)

    root.fromCombo = ttk.Combobox(root, values=currencyList)
    root.fromCombo.grid(row=2, column=2)

    toLabel = Label(root, text="TO:", bg="skyblue")
    toLabel.grid(row=2, column=3)

    root.toCombo = ttk.Combobox(root, values=currencyList)
    root.toCombo.grid(row=2, column=4)

    convertButton = Button(root, text="CONVERT", width=20, command=Convert)
    convertButton.grid(row=3, column=1, columnspan=4, padx=10, pady=10)

    outputAMTL = Label(root, text="CONVERTED AMOUNT:", font=('Helvetica',10),bg="skyblue")
    outputAMTL.grid(row=4, column=2, columnspan=2, pady=50)

    root.outputAMTAns = Label(root, font=('Helvetica',20),bg="skyblue")
    root.outputAMTAns.grid(row=4, column=3, columnspan=2, pady=50)

#Convert() function for converting the curreny
def Convert():
    #Fetching and storing the user-inputs in resepective variables
    inputAmt = float(getAMT.get())
    fromCur = root.fromCombo.get()
    toCur = root.toCombo.get()

    #API Key from https://www.alphavantage.co/
    apiKey = "TPXCXTXMEQRUG566"

    #base URL
    baseURL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    #complete URL
    inputURL = baseURL + "&from_currency=" + fromCur\
               + "&to_currency=" + toCur + "&apikey=" + apiKey

    #Returning the response object using get() of request
    requestObj = requests.get(inputURL)
    #Converting the json format data to Python Dictionary
    result = requestObj.json()

    #Getting the exchange rate (Required Information)
    exchangeRate = float(result["Realtime Currency Exchange Rate"]
                                              ['5. Exchange Rate'])

    #Calculating the converted amount and rounding the decimal to 2 places
    calculateAmt = round(inputAmt * exchangeRate, 2)
    #Displaying the converted amount in the respective label
    root.outputAMTAns.config(text=str(calculateAmt))

#Creating object of tk class
root = tk.Tk()

#Setting the title, background color
#and size of the tkinter window and
#disabling the resizing property
root.geometry("400x250")
root.resizable(False, False)
root.title("Real Time Curreny Converter")
root.config(bg = "skyblue")

#Creating tkinter variables
getAMT = StringVar()

#Calling the CreateWidgets() function
CreateWidgets()

#Defining infinite loop to run application
root.mainloop()
