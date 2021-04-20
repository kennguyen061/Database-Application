import csv
import sys
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import tkinter
import tkinter.ttk
import tkinter.messagebox

#this file contains functions used to create date entry boxes throughout the application & error messages

    #displays the message window for date entry boxes
def displayMsg( title, message ):
    window = tkinter.Tk()
    window.wm_title(title)

    tkinter.Label(window, text=message, pady=20, padx=20, width=len(message)).pack()


    window.mainloop()

    #returns a string that is fit for sql usage
def getDate( year, month, day ):
    months = (("01", "January"), ("02", "February"), ("03", "March"), ("04", "April"), ("05", "May"), ("06", "June"), ("07", "July"), ("08", "August"), ("09","September"), ("10","October"), ("11", "November"), ("12", "December") )
    for m in months:
        if m[1] == month:
            return year + "-" + m[0] + "-" + day

    #gets the month entry
def getMonthEntry(window, width, var):
    monthEntry = tkinter.ttk.Combobox(window, width=width, textvariable=var)

    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    monthEntry['values'] = months

    return monthEntry

    #gets the day entry
def getDayEntry(window, width, var):
    dayEntry = tkinter.ttk.Combobox(window, width=width, textvariable=var)

    days = tuple(range(1, 32))
    dayEntry['values'] = days

    return dayEntry

    #gets the year entry
def getYearEntry(window, width, var):
    yearEntry = tkinter.ttk.Combobox(window, width=width, textvariable=var)
    today = datetime.today()

    years = tuple(range(1900, today.year+1))
    years = tuple(reversed(years))
    yearEntry['values'] = years

    return yearEntry
