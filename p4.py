import csv
import sys
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import tkinter
import tkinter.ttk
import tkinter.messagebox
from GUI import insertGUI
from GUI import reportsGUI
from db import database
from GUI import transactionsGUI


#Homewindow definition
class HomePage:
    def __init__(self):

        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("Clemson Computer Solutions DB App")
        self.database = database.Database()

        self.database.TableCreate() #temporarily commented out to save time when testing GUI

        #creates homepage menu
        tkinter.Label(self.homePageWindow, text="Home Page", width=100).grid(pady=20, column=1, row=1)
        
        #executes one of the four options
        tkinter.Button(self.homePageWindow, width=20, text="Reports", command=self.Reports).grid(pady=15, column=1, row=2)
        tkinter.Button(self.homePageWindow, width=20, text="Transaction", command=self.Transaction).grid(pady=15, column=1, row=3)
        tkinter.Button(self.homePageWindow, width=20, text="Insert", command=self.Insert).grid(pady=15, column=1, row=4)

        tkinter.Button(self.homePageWindow, width=20, text="Exit", command=self.homePageWindow.destroy).grid(pady=15,
                                                                                                             column=1,
                                                                                                             row=7)

        self.homePageWindow.mainloop()
    
    #creates report window object
    def Reports(self):
        #do something
        self.reportWindow = reportsGUI.ReportsWindow(self.database)
    
    #creates transaction window object
    def Transaction(self):
        #do something
        self.transactionWindow = transactionsGUI.TransactionWindow(self.database.dbConnection)

    #creates insert window object
    def Insert(self):
        self.insertWindow = insertGUI.InsertWindow(self.database.dbConnection)


#GO!

homePage = HomePage()
