import csv
import sys
sys.path.append('../')
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from db import dates
from db import database
import tkinter
import tkinter.ttk
import tkinter.messagebox
from tkcalendar import Calendar, DateEntry

#Class for the new bill window
class billWindow:
    def __init__(self, conn):
        self.dbconn = conn
        self.db = database.Database()
        self.window = tkinter.Tk()
        self.window.wm_title("Generate Bill")

        #variables
        self.projID = tkinter.StringVar()
        self.billDate = tkinter.StringVar()

        #labels and butts
        tkinter.Label(self.window, text="Enter Project ID", width = 50).grid(column=1, row=1, columnspan=2)
        self.projIDEntry = tkinter.Entry(self.window, textvariable=self.projID, width=10)
        self.projIDEntry.grid(column=1, row=2, pady=10, columnspan=2)

        #calendar tkinter widget used to collect date
        tkinter.Label(self.window, text="Enter Bill Date:", width=15).grid(column=1, row=3, sticky='E')
        self.cal = Calendar(self.window, selectmode='day', locale='en_US', cursor="hand1",
                                year=2021, month=1,day=1, textvariable=self.billDate, date_pattern="yyyy-mm-dd")
        self.cal.grid(column=1, row=4, columnspan=3, pady=20)

        tkinter.Button(self.window, width=15, text="Go", command=self.update).grid(pady=10, padx=20, sticky="w", column=1, row=5)
        tkinter.Button(self.window, width=15, text="Back", command=self.window.destroy).grid(pady=10, padx=20, sticky="e", column=2, row=5)

        self.window.mainloop()

    #function to update the database & verify inputs
    def update(self):
        pid = self.projIDEntry.get()
        if pid.isdigit():
            result = self.db.get_bill(self.dbconn, self.cal.get_date(), pid)
            if result[0] == 1:
                dates.displayMsg("Success!", "Got Bill with ID: " + str(result[1]) + " and balance of $" + str(result[2]))
            else:
                dates.displayMsg("Created New Bill", "Created a New Bill with ID: "+ str(result[1]) + " and balance of $" + str(result[2]))
        else:
            dates.displayMsg("Error", "Invalid Project ID")
        return 0

#Window for creating a new log time
class logWorkTimeWindow:
    def __init__(self, conn):
        self.dbconn = conn
        self.db = database.Database()
        self.window = tkinter.Tk()
        self.window.wm_title("Log Work Time")  

        #variables
        self.assignmentID = tkinter.StringVar()
        self.weekEnding = tkinter.StringVar()
        self.hrs = tkinter.StringVar()
        self.bill = tkinter.StringVar()

        #labels and buttons
        tkinter.Label(self.window, text="Enter Worklog Info",width = 50).grid( column=1, row=1, columnspan=2)
        
        tkinter.Label(self.window, text="Assignment ID:",width = 25).grid( column=1, row=2, columnspan=2)
        self.assignmentIDEntry = tkinter.Entry(self.window, textvariable=self.assignmentID, width = 15)
        self.assignmentIDEntry.grid(column=2, row=2)

        tkinter.Label(self.window, text="Hrs Worked:",width = 25).grid( column=1, row=3, columnspan=2)
        self.hrsEntry = tkinter.Entry(self.window, textvariable=self.hrs, width = 15)
        self.hrsEntry.grid(column=2, row=3)

        tkinter.Label(self.window, text="Bill ID (optional):",width = 25).grid( column=1, row=4, columnspan=2)
        self.billEntry = tkinter.Entry(self.window, textvariable=self.bill, width = 15)
        self.billEntry.grid(column=2, row=4)

        #calendar tkinter widget used to collect week ending
        tkinter.Label(self.window, text="Week Ending:", width=15).grid(column=1, row=7, sticky='E')
        self.cal = Calendar(self.window, selectmode='day', locale='en_US', cursor="hand1",
                                year=2021, month=1,day=1, textvariable=self.weekEnding, date_pattern="yyyy-mm-dd")
        self.cal.grid(column=1, row=8, columnspan=3, pady=20)

        tkinter.Button(self.window, width=15, text="Go", command=self.update).grid(pady=10, padx=20, sticky="w", column=1, row=10)
        tkinter.Button(self.window, width=15, text="Back", command=self.window.destroy).grid(pady=10, padx=20, sticky="e", column=2, row=10)

        self.window.mainloop()

    #fxn to update the db with the new worklog info
    def update(self):
        if self.billEntry.get() == "":
            self.db.update_worklog(self.dbconn, self.cal.get_date(), self.hrsEntry.get(), self.assignmentIDEntry.get(), -1) 
            dates.displayMsg("Success", "Updated Worklog!")
        elif( (self.hrsEntry.get().isdigit()) and (self.assignmentIDEntry.get().isdigit()) or (self.billEntry.get().isdigit()) ):
            self.db.update_worklog(self.dbconn, self.cal.get_date(), self.hrsEntry.get(), self.assignmentIDEntry.get(), self.billEntry.get())
            dates.displayMsg("Success", "Updated Worklog!")
        else:
            dates.displayMsg("Error", "Invalid Input Please Try Again")

#Class to create the transaction window menu
class TransactionWindow:
    def __init__(self, conn):
        self.dbconn = conn
        self.window = tkinter.Tk()
        self.window.wm_title("Transactions")

        #labels and buttons
        tkinter.Label(self.window, text="Complete Transactions", width=100).grid(pady=20, column=1, row=1)

        tkinter.Button(self.window, text="Create Bill", command=self.create_bill).grid( pady=15, column=1, row=2 )
        tkinter.Button(self.window, text="Update Worklog Hours", command=self.update_worklog).grid( pady=15, column=1, row=3 )

        tkinter.Button(self.window, text="Back", command=self.window.destroy).grid(pady=15, column=1, row=7)
        
        self.window.mainloop()

    #function to call bill window
    def create_bill(self):
        self.billWindow = billWindow(self.dbconn)

    #function to call worklog window
    def update_worklog(self):
        self.workLog = logWorkTimeWindow(self.dbconn)