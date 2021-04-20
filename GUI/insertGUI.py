import csv
import sys
sys.path.append('../')
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import tkinter
import tkinter.ttk
import tkinter.messagebox
from tkcalendar import Calendar, DateEntry
from db import dates
from db import database



#class to make search & assign window
class newSearchAndAssignWindow:
    def __init__(self, conn):
        self.db = database.Database()
        self.dbconn = conn
        self.window = tkinter.Tk()
        self.window.wm_title("Search and Assign Employees To Projects")   

        #variables
        self.projID = tkinter.StringVar()
        self.taskID = tkinter.StringVar()

        #labels and buttons
        tkinter.Label(self.window, text="Enter Project ID & Task ID to Assign Employees",width = 50).grid( column=1, row=1, columnspan=1)
        
        tkinter.Label(self.window, text="ProjectID:", width=10).grid(column=1, row=2, sticky="W", padx=25)
        self.projIDEntry = tkinter.Entry(self.window, width=10, textvariable=self.projID)
        self.projIDEntry.grid( column=1, row=2 )
        tkinter.Label(self.window, text="TaskID:", width=10).grid(column=1, row=3, sticky="W", padx=25)
        self.taskIDEntry = tkinter.Entry(self.window, width=10, textvariable=self.taskID)
        self.taskIDEntry.grid(column=1, row=3 )

        tkinter.Button(self.window, text="Go", command=self.empWindow).grid(padx=20, pady=20, column=1, row=4, sticky="W")
        tkinter.Button(self.window, text="Back", command=self.window.destroy).grid(padx=20, pady=20, column=1, row=4, sticky="E")

        self.window.mainloop()
    
    #function to create subwindow 
    def empWindow(self):
        self.empWindow = tkinter.Tk()
        self.empWindow.wm_title("Assign Employee to Selected Project")          
        tkinter.Label(self.empWindow, text="Select Employee to Add to Project", width=60).grid(column=1, row=1, columnspan=2)

        #variables
        self.emp = tkinter.StringVar()
        self.startDay = tkinter.StringVar()
        self.startYear = tkinter.StringVar()
        self.startMonth = tkinter.StringVar()
        self.endMonth = tkinter.StringVar()
        self.endDay = tkinter.StringVar()
        self.endYear = tkinter.StringVar()


        self.empCombo = tkinter.ttk.Combobox(self.empWindow, width=20, textvariable=self.emp)
        self.empCombo['values'] = self.get_emps()
        self.empCombo.grid(column=1, row=2, columnspan=2)

        #date entries
        tkinter.Label(self.empWindow, text="Assignment Start Date:", width=20).grid(column=1, row=3, sticky='E')
        self.startMonthEntry = dates.getMonthEntry(self.empWindow, 10, self.startMonth)
        self.startMonthEntry.grid(column=2, row=3, sticky="w")

        self.startDayEntry = dates.getDayEntry( self.empWindow, 2, self.startDay)
        self.startDayEntry.grid(padx=40, column=2, row=3)

        self.startYearEntry = dates.getYearEntry( self.empWindow, 4, self.startYear)
        self.startYearEntry.grid(padx=35, column=2, row=3, sticky='E')

        #end date
        tkinter.Label(self.empWindow, text="Estimated End Date:", width=20).grid(column=1, row=4, sticky='E')
        self.endMonthEntry = dates.getMonthEntry(self.empWindow, 10, self.endMonth)
        self.endMonthEntry.grid(column=2, row=4, sticky="w")

        self.endDayEntry = dates.getDayEntry( self.empWindow, 2, self.endDay)
        self.endDayEntry.grid(padx=40, column=2, row=4)

        self.endYearEntry = dates.getYearEntry( self.empWindow, 4, self.endYear)
        self.endYearEntry.grid(padx=35, column=2, row=4, sticky='E')


        tkinter.Button(self.empWindow, text="Update", command=self.insert).grid(padx=20, pady=10, column=1, row=5, )
        tkinter.Button(self.empWindow, text="Back", command=self.empWindow.destroy).grid(padx=20, pady=10, column=2, row=5)


        self.empWindow.mainloop()

    #fxn to insert selected employee to selected project
    def insert(self):

        startDate = dates.getDate(self.startYearEntry.get(), self.startMonthEntry.get(), self.startDayEntry.get())
        endDate = dates.getDate(self.endYearEntry.get(), self.endMonthEntry.get(), self.endDayEntry.get())

        emp = self.empCombo.get()
        empID = emp[0:3]
        taskSkillID = 0
        for entry in self.emp_list:
            if str(entry[0][0]) == str(empID):
                taskSkillID = entry[1]

        self.db.create_assignment( self.dbconn, startDate, endDate, empID, taskSkillID )
        dates.displayMsg("Insert Success", "Employee Assigned!")

    #function to get a list of employees suitable for a given task
    def get_emps(self):
        #get list of valid employees from db
        self.emp_list = self.db.get_emps_for_search_assign( self.dbconn, self.projIDEntry.get(), self.taskIDEntry.get() )
        emps = []
        for entry in self.emp_list:
            emps.append(entry[0])
        return emps
    

#class to hold new project window
class newProjectWindow:
    def __init__(self, conn):

        #initialize window info
        self.db = database.Database()
        self.dbconn = conn
        self.window = tkinter.Tk()
        self.window.wm_title("Add New Project")

        #variables
        self.projDescr = tkinter.StringVar()
        self.projCust = tkinter.StringVar()
        self.projEmp = tkinter.StringVar()
        self.estBudget = tkinter.StringVar()
        self.estStartMo = tkinter.StringVar()
        self.estStartDay = tkinter.StringVar()
        self.estStartYr = tkinter.StringVar()
        self.estEndMo = tkinter.StringVar()
        self.estEndDay = tkinter.StringVar()
        self.estEndYr = tkinter.StringVar()
        self.actualStartMo = tkinter.StringVar()
        self.actualStartDay = tkinter.StringVar()
        self.actualStartYr = tkinter.StringVar()

        
        #labels and butts
        tkinter.Label(self.window, text="Enter New Project Information",width = 50).grid( column=1, row=1, columnspan=2)

        tkinter.Label(self.window, text="Project Description:", width=15).grid(column=1, row=2, sticky='E')
        self.projDescrEntry = tkinter.Entry(self.window, width=25, textvariable=self.projDescr)
        self.projDescrEntry.grid(column=2, row=2, sticky='W')

        tkinter.Label(self.window, text="Select Customer",width = 15).grid( column=1, row=3, sticky='E')
        customers = self.get_customers(self.dbconn)
        self.custCombo = tkinter.ttk.Combobox(self.window, width=22, textvariable=self.projCust)
        self.custCombo['values'] = customers
        self.custCombo.grid(column=2, row=3, sticky="W")
        self.custCombo.current()

        tkinter.Label(self.window, text="Select Employee", width=15).grid(column=1, row=4, sticky='E')
        emps = self.get_emps(self.dbconn)
        self.empCombo = tkinter.ttk.Combobox(self.window, width=22, textvariable=self.projEmp)
        self.empCombo['values'] = emps
        self.empCombo.grid(column=2, row=4, sticky="W")
        self.empCombo.current()

        tkinter.Label(self.window, text="Estimated Budget: $", width=15).grid(column=1, row=5, sticky='E')
        self.estBudgetEntry = tkinter.Entry(self.window, width=25, textvariable=self.estBudget)
        self.estBudgetEntry.grid(column=2, row=5, sticky="W")

        #dates

        #est Start date (esd)
        tkinter.Label(self.window, text="Estimated Start Date:", width=15).grid(column=1, row=7, sticky='E')
        self.esdmonthEntry = dates.getMonthEntry(self.window, 10, self.estStartMo)
        self.esdmonthEntry.grid(column=2, row=7, sticky="w")

        self.esddayEntry = dates.getDayEntry( self.window, 2, self.estStartDay)
        self.esddayEntry.grid(padx=40, column=2, row=7)

        self.esdyearEntry = dates.getYearEntry( self.window, 4, self.estStartYr)
        self.esdyearEntry.grid(padx=35, column=2, row=7, sticky='E')

        #est end date (eed)
        tkinter.Label(self.window, text="Estimated End Date:", width=15).grid(column=1, row=8, sticky='E')
        self.eedmonthEntry = dates.getMonthEntry(self.window, 10, self.estEndMo)
        self.eedmonthEntry.grid(column=2, row=8, sticky="w")

        self.eeddayEntry = dates.getDayEntry( self.window, 2, self.estEndDay)
        self.eeddayEntry.grid(padx=40, column=2, row=8)

        self.eedyearEntry = dates.getYearEntry( self.window, 4, self.estEndYr)
        self.eedyearEntry.grid(padx=35, column=2, row=8, sticky='E')

        #actual start date (asd)
        tkinter.Label(self.window, text="Actual Start Date:", width=15).grid(column=1, row=9, sticky='E')
        self.asdmonthEntry = dates.getMonthEntry(self.window, 10, self.actualStartMo)
        self.asdmonthEntry.grid(column=2, row=9, sticky="w")

        self.asddayEntry = dates.getDayEntry( self.window, 2, self.actualStartDay)
        self.asddayEntry.grid(padx=40, column=2, row=9)

        self.asdyearEntry = dates.getYearEntry( self.window, 4, self.actualStartYr)
        self.asdyearEntry.grid(padx=35, column=2, row=9, sticky='E')

        #buttons
        tkinter.Button(self.window, text="Update Database", command=self.insert).grid(pady=15, column=1, row=11)
        tkinter.Button(self.window, text="Back", command=self.window.destroy).grid(pady=15, column=2, row=11)


        #display window
        self.window.mainloop()

    #function to call query fuxn to get list of customers from db
    def get_customers(self, conn):
        self.customers = self.db.DisplayCustomer()
        names = []
        for entry in self.customers:
            names.append(entry[1])
        return names

    def get_custID(self, name):
        for entry in self.customers:
            if name == entry[1]:
                return entry[0]
        print("[WARNING]: Error Fetching CustID")
        return -1
    
    #function to call query fxn to get list of employee project managers from db
    def get_emps(self, conn):
        emps = self.db.DisplayProjManagers()
        self.emp_ids = []
        self.emp_names = []
        for entry in emps:
            self.emp_ids.append(entry[0])
            self.emp_names.append(entry[2] + " " + entry[1])

        return self.emp_names

    def get_emp_id(self, emp_name):
        i = 0
        for entry in self.emp_names:
            if emp_name == entry:
                return self.emp_ids[i]
            i = i + 1
        print("[WARNING]: Employee ID error.")
        return -1

    #function to insert & validate data to database
    def insert(self):
        valid = self.db.validateproject(self.projDescrEntry.get(), self.estBudgetEntry.get())

        estStartDate = dates.getDate(self.esdyearEntry.get(), self.esdmonthEntry.get(), self.esddayEntry.get())
        estEndDate = dates.getDate(self.eedyearEntry.get(), self.eedmonthEntry.get(), self.eeddayEntry.get())
        actStartDate = dates.getDate(self.asdyearEntry.get(), self.asdmonthEntry.get(), self.asddayEntry.get())
        print(estStartDate)

        if valid == "Success":
            self.db.insertproject(self.dbconn, self.projDescrEntry.get(), self.estBudgetEntry.get(), estEndDate, estStartDate, actStartDate, str(self.get_custID(self.custCombo.get())), str(self.get_emp_id(self.empCombo.get())) )
            projectID = self.db.getProjectID(self.dbconn, self.projDescrEntry.get() )
            pid = projectID[0]

            self.taskWindow = newTaskWindow(self.dbconn, pid[0])
        else:
            print(self.projDescrEntry.get())
            dates.displayMsg("Error", "Invalid " + valid + " Please Retry.")

#class for the inserting a new task window
class newTaskWindow:
    def __init__(self, conn, projID):
        self.dbconn = conn
        self.projID = projID #storing projectID passed in by corresponding project
        self.db = database.Database()

        self.window = tkinter.Tk()
        self.window.wm_title("Add Tasks to Project")

        #variables to be used
        self.taskDescr = tkinter.StringVar()
        self.startDay = tkinter.StringVar()
        self.startMonth = tkinter.StringVar()
        self.startYear = tkinter.StringVar()
        self.endDay = tkinter.StringVar()
        self.endMonth = tkinter.StringVar()
        self.endYear = tkinter.StringVar()

        #labels & buttons
        tkinter.Label(self.window, text="Enter New Task Information",width = 50).grid( column=1, row=1, columnspan=2)

        #task description
        tkinter.Label(self.window, text="Task Description:", width=15).grid(column=1, row=2, sticky='E')
        self.taskDescrEntry = tkinter.Entry(self.window, width=25, textvariable=self.taskDescr)
        self.taskDescrEntry.grid(column=2, row=2, sticky='W')

        #start & end date entries
        #start date
        tkinter.Label(self.window, text="Task Start Date:", width=15).grid(column=1, row=3, sticky='E')
        self.startMonthEntry = dates.getMonthEntry(self.window, 10, self.startMonth)
        self.startMonthEntry.grid(column=2, row=3, sticky="w")

        self.startDayEntry = dates.getDayEntry( self.window, 2, self.startDay)
        self.startDayEntry.grid(padx=40, column=2, row=3)

        self.startYearEntry = dates.getYearEntry( self.window, 4, self.startYear)
        self.startYearEntry.grid(padx=35, column=2, row=3, sticky='E')

        #end date
        tkinter.Label(self.window, text="Estimated End Date:", width=15).grid(column=1, row=4, sticky='E')
        self.endMonthEntry = dates.getMonthEntry(self.window, 10, self.endMonth)
        self.endMonthEntry.grid(column=2, row=4, sticky="w")

        self.endDayEntry = dates.getDayEntry( self.window, 2, self.endDay)
        self.endDayEntry.grid(padx=40, column=2, row=4)

        self.endYearEntry = dates.getYearEntry( self.window, 4, self.endYear)
        self.endYearEntry.grid(padx=35, column=2, row=4, sticky='E')

        #buttons

        tkinter.Button(self.window, text="Add Task Skills", command=self.insert).grid(pady=15, column=1, row=6)
        tkinter.Button(self.window, text="Back", command=self.window.destroy).grid(pady=15, column=2, row=6)

        self.window.mainloop()

    #function to insert new task into database
    def insert(self):
        startDate = dates.getDate(self.startYearEntry.get(), self.startMonthEntry.get(), self.startDayEntry.get())
        endDate = dates.getDate(self.endYearEntry.get(), self.endMonthEntry.get(), self.endDayEntry.get())
        self.db.insertTask(self.dbconn, str(self.projID), self.taskDescrEntry.get(), startDate, endDate )

        self.skillWindow()
        return 0

    #function used to get skill names to be displayed in combobox
    def get_skill_names(self):
        self.skills = self.db.get_skills(self.dbconn)
        self.skillDescs = []
        for entry in self.skills:
            self.skillDescs.append(entry[1])

        return self.skillDescs
    
    #function used to get skill requirements for a task
    def skillWindow(self):

        self.skwindow = tkinter.Tk()
        self.skwindow.wm_title("Add Skill Requirements to Task")

        self.skldscrp = tkinter.StringVar()
        self.skillQuant = tkinter.StringVar()

        tkinter.Label(self.skwindow, text="Enter Skill Requirements",width = 50).grid( column=1, row=1, columnspan=2)

        tkinter.Label(self.skwindow, text="Select Skill:", width = 25).grid(column=1, row=2)

        self.skillCombo = tkinter.ttk.Combobox(self.skwindow, width=25, textvariable=self.skldscrp)
        self.skillCombo['values'] = self.get_skill_names()
        self.skillCombo.grid(column=2, row=2)

        tkinter.Label(self.skwindow, text="Enter Skill Req Quantity", width = 25).grid(column=1, row=3)

        self.skillQuantEntry = tkinter.Entry(self.skwindow, width = 10, textvariable=self.skillQuant)
        self.skillQuantEntry.grid(column=2, row=3)

        tkinter.Button(self.skwindow, text="Add Skill Req.", width=15, command=self.insertSkill).grid(column=1, row=4)
        tkinter.Button(self.skwindow, text="Back", width=15, command=self.skwindow.destroy).grid(column=2, row=4)

        self.skwindow.mainloop()

    #function used to insert/map skill requirements into a task
    def insertSkill(self):

        for entry in self.skills:
            if entry[1] == self.skillCombo.get():
                skillID = entry[0]
        
        if (self.skillQuantEntry.get()).isdigit:
            self.db.map_task_skill(self.dbconn, skillID, self.db.get_taskID(self.dbconn, self.taskDescrEntry.get()), self.skillQuantEntry.get() )
            self.nextSkillWindow()
        else:
            dates.displayMsg("Input Error", "Invalid Skill Quantity Entry (Please enter a number).")

    #function used to make a window asking if the user wants to keep adding skill requirements
    def nextSkillWindow(self):
        self.nswindow = tkinter.Tk()
        self.nswindow.wm_title("Insert Another Skill Requirement?")

        tkinter.Label(self.nswindow, width=50, text="Insert Another Skill Requirement For This Task?").pack()

        tkinter.Button(self.nswindow, text="Yes", command=self.refreshSkillWindow).pack(side = BOTTOM)
        tkinter.Button(self.nswindow, text="No", command=self.destroySkillWindow).pack(side = BOTTOM)

    #destroys skill windows
    def destroySkillWindow(self):
        self.nswindow.destroy()
        self.skwindow.destroy()
        dates.displayMsg("Add More Tasks", "To add more tasks use existing Task Window!")

    #refreshes skill windows for re-use
    def refreshSkillWindow(self):
        self.nswindow.destroy()
        self.skwindow.destroy()
        self.skillWindow()


#class to create the add employee menu
class addEmployeeWindow:
    def __init__(self, conn):

        #initialize database object
        self.db = database.Database()

        #initializing window info
        self.dbconn = conn
        self.window = tkinter.Tk()
        self.window.wm_title("Add New Employee")

        #declaring variables to be used for entries/comboboxes
        self.lname = tkinter.StringVar()
        self.fname = tkinter.StringVar()
        self.midInitial = tkinter.StringVar()
        self.hireDate = tkinter.StringVar()
        self.regID = tkinter.StringVar()

        #labels for entries

        tkinter.Label(self.window, text="Enter New Employee's Information",width = 50).grid( column=1, row=1, columnspan=2)

        tkinter.Label(self.window, text="First Name:", width=15).grid(column=1, row=2, sticky='E')
        self.fnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.fname)
        self.fnameEntry.grid(column=2, row=2, sticky='W')

        tkinter.Label(self.window, text="Last Name:", width=15).grid(column=1, row=3, sticky='E')
        self.lnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lname)
        self.lnameEntry.grid(column=2, row=3, sticky="W")

        tkinter.Label(self.window, text="Middle Initial:", width=15).grid(column=1, row=4, sticky='E')
        self.MnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.midInitial)
        self.MnameEntry.grid(column=2, row=4, sticky="W")

        #getting list of regions to be displayed on drop down menu
        self.regions = self.db.DisplayRegion()

        #regions dropdown menu
        tkinter.Label(self.window, text="Region:", width=15).grid(column=1, row=4, sticky='E')
        self.regCombo = tkinter.ttk.Combobox(self.window, width=25, textvariable=self.regID)
        self.regCombo['values'] = self.get_regions(self.regions)
        self.regCombo.grid(column=2, row=4, sticky="W")
        self.regCombo.current()

        #calendar tkinter widget used to collect hire date
        tkinter.Label(self.window, text="Hire Date:", width=15).grid(column=1, row=7, sticky='E')
        self.cal = Calendar(self.window, selectmode='day', locale='en_US', cursor="hand1",
                                year=2021, month=1,day=1, textvariable=self.hireDate, date_pattern="yyyy-mm-dd")
        self.cal.grid(column=1, row=8, columnspan=3)
        


        #update database & back buttons
        tkinter.Button(self.window, text="Update Database", command=self.insert).grid(pady=15, column=1, row=9)
        tkinter.Button(self.window, text="Back", command=self.window.destroy).grid(pady=15, column=2, row=9)

        self.window.mainloop()

    #function to validate and insert data into the databse
    def insert(self):

        #gets the regionID based off the region name/abbreviation
        realregID = self.get_regID(self.regCombo.get())

        #validates employee
        valid = self.db.validateemployee(self.cal.get_date(), self.lnameEntry.get(), self.fnameEntry.get(), realregID)
        if valid == "Success":
            self.db.insertemployee(self.dbconn, self.cal.get_date(), self.lnameEntry.get(), self.fnameEntry.get(), str(realregID) )
            tkinter.Label(self.window, text="Insert Successful!",width = 40).grid( column=1, row=8, columnspan=2)
        else:
            tkinter.Label(self.window, text="Invalid "+valid+" Please Re-Enter",width = 40).grid( column=1, row=8, columnspan=2)
    
    #function to get the id from a given region name
    def get_regID(self, regName):
        for entry in self.regions:
            if regName == entry[1]:
                return entry[0]
        print("[WARNING]: Region ID error")
        return -1

    #gets entries from the region table, in the form of entry: (RegID, RegName)
    def get_regions(self, regions):

        regnames = []
        for entry in regions:
            regnames.append(entry[1])

        return regnames    



#class to make the new skill menu
class skillWindow:
    def __init__(self, conn):
        self.dbconn = conn
        self.window = tkinter.Tk()
        self.window.wm_title("Add New Skill")
        self.db = database.Database()

        self.skillDesc = tkinter.StringVar()

        tkinter.Label(self.window, text="Add a New Skill", width=100).grid(pady=20,column=1,row=1)

        self.skillDescEntry = tkinter.Entry(self.window, width = 20, textvariable=self.skillDesc)
        self.skillDescEntry.grid(pady=5, column=1, row=2)

        tkinter.Button(self.window, text="Update Database", command=self.insert).grid(pady=15, column=1, row=3)
        tkinter.Button(self.window, text="Back", command=self.window.destroy).grid(pady=15, column=1, row=4)
        self.window.mainloop()

    #validates & inserts new skill
    def insert(self):
        #validate values
        valid = self.db.validateskill(self.skillDescEntry.get())
        if( valid != "Success"):
            tkinter.Label(self.window, text="Invalid "+valid+" Please Retry", width=100).grid(pady=20, column=1, row=1)
        else:
            self.db.insertskill(self.skillDescEntry.get(), self.dbconn)
            print("Got skill descrip of " + self.skillDescEntry.get() )
            tkinter.Label(self.window, text="Insert Successfull", width=100).grid(pady=20, column=1, row=1)


#Class to create the insert main menu
class InsertWindow:
    def __init__(self, conn):
        self.dbconn = conn
        self.window = tkinter.Tk()
        self.window.wm_title("Insert Data")




        tkinter.Label(self.window, text="Insert Data", width=100).grid(pady=20, column=1, row=1)

        tkinter.Button(self.window, text="New Skill", command=self.insert_skill).grid(pady=15, column=1, row=2)
        tkinter.Button(self.window, text="New Employee", command=self.insert_employee).grid(pady=15, column=1, row=3)
        tkinter.Button(self.window, text="New Project", command=self.insert_project).grid(pady=15, column=1, row=4)
        tkinter.Button(self.window, text="Search & Assign Employee", command=self.search_assign).grid(pady=15, column=1, row=5)

        tkinter.Button(self.window, text="Back", command=self.window.destroy).grid(pady=15, column=1, row=7)

        self.window.mainloop()

    #functions to open different sub menus by calling classes

    def insert_skill(self):
        self.insertSkillWindow = skillWindow(self.dbconn)
    
    def insert_employee(self):
        self.insertEmployeeWindow = addEmployeeWindow(self.dbconn)
    
    def insert_project(self):
        self.insertProjectWindow = newProjectWindow(self.dbconn)

    def search_assign(self):
        self.searchAndAssignWindow = newSearchAndAssignWindow(self.dbconn)
    
    def log_work(self):
        self.logWorkWindow = logWorkTimeWindow(self.dbconn)