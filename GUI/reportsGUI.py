import csv
import sys
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import tkinter
import tkinter.ttk
import tkinter.messagebox
from db import dates


#creates the employee skill window
class EmpSkillsWindow:
    def __init__(self, data):
        self.window = tkinter.Tk()
        self.window.wm_title("Employee Skills Inventory")

        # Label widgets
        tkinter.Label(self.window, text="Employee Skills Inventory", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tkinter.ttk.Treeview(self.window)
        self.databaseView.grid(pady=5, padx=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = (
        "Skill", "lname", "fname" )

        # Treeview column headings
        self.databaseView.heading("Skill", text="Skill")
        self.databaseView.heading("lname", text="Last Name")
        self.databaseView.heading("fname", text="First Name")

        # Treeview columns
        self.databaseView.column("Skill", width=200)
        self.databaseView.column("lname", width=100)
        self.databaseView.column("fname", width=100)

        #fills table with data
        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.window.mainloop()

        #project schedule window
class projscheduleWindow:
    def __init__(self, data):
        self.window = tkinter.Tk()
        self.window.wm_title("Project Schedule")

        # Label widgets
        tkinter.Label(self.window, text="Project Schedule", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tkinter.ttk.Treeview(self.window)
        self.databaseView.grid(pady=20, padx=5, column=1, row=50)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = (
        "ProjID", "ProjDescrip", "Company", "Contract Date", "RegionName", "ProjActualStartDate", "ProjActualEndDate", "projBudget", "TaskStartDate", "TaskEndDate", "TaskDescrip", "SkillDescrip", "TaskSkillQuant" )


        # Treeview column headings
        self.databaseView.heading("ProjID", text="ProjID")
        self.databaseView.heading("ProjDescrip", text="ProjDescrip")
        self.databaseView.heading("Company", text="Company")
        self.databaseView.heading("Contract Date", text="Contract Date")
        self.databaseView.heading("RegionName", text="RegionName")
        self.databaseView.heading("ProjActualStartDate" , text="ProjActualStartDate")
        self.databaseView.heading("ProjActualEndDate", text="ProjActualEndDate")
        self.databaseView.heading("projBudget", text="projBudget")
        self.databaseView.heading("TaskStartDate", text="TaskStartDate")
        self.databaseView.heading("TaskEndDate", text="TaskEndDate")
        self.databaseView.heading("TaskDescrip", text="TaskDescrip")
        self.databaseView.heading("SkillDescrip", text="SkillRequirement")
        self.databaseView.heading("TaskSkillQuant", text="TaskSkillQuant")

        # Treeview columns
        self.databaseView.column("ProjID", width=100)
        self.databaseView.column("ProjDescrip", width=100)
        self.databaseView.column("Company", width=100)
        self.databaseView.column("Contract Date", width=100)
        self.databaseView.column("RegionName", width=100)
        self.databaseView.column("ProjActualStartDate", width=100)
        self.databaseView.column("ProjActualEndDate", width=100)
        self.databaseView.column("projBudget", width=100)
        self.databaseView.column("TaskStartDate", width=100)
        self.databaseView.column("TaskEndDate", width=100)
        self.databaseView.column("TaskDescrip", width=100)
        self.databaseView.column("SkillDescrip", width=100)
        self.databaseView.column("TaskSkillQuant", width=100)

                #fills table with data
        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.window.mainloop()

        #assignment form window
class assignmentformWindow:
    def __init__(self, data):
        self.window = tkinter.Tk()
        self.window.wm_title("Assignment Form")

        # Label widgets
        tkinter.Label(self.window, text="Assignment Form", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tkinter.ttk.Treeview(self.window)
        self.databaseView.grid(pady=5, padx=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = (
        "ProjID", "ProjDescrip", "Company", "Contract Date", "As of", "TaskDescrip", "TaskStartDate", "TaskEndDate", "SkillDescrip", "EmpID", "EmpLName", "EmpFName", "AssignBegin", "AssignEnd" )

        # Treeview column headings
        self.databaseView.heading("ProjID", text="ProjID")
        self.databaseView.heading("ProjDescrip", text="ProjDescrip")
        self.databaseView.heading("Company", text="Company")
        self.databaseView.heading("Contract Date", text="Contract Date")
        self.databaseView.heading("As of", text="As of")
        self.databaseView.heading("TaskDescrip" , text="TaskDescrip")
        self.databaseView.heading("TaskStartDate", text="TaskStartDate")
        self.databaseView.heading("TaskEndDate", text="TaskEndDate")
        self.databaseView.heading("SkillDescrip", text="SkillDescrip")
        self.databaseView.heading("EmpID", text="EmpID")
        self.databaseView.heading("EmpLName", text="EmpLName")
        self.databaseView.heading("EmpFName", text="EmpFName")
        self.databaseView.heading("AssignBegin", text= "AssignBegin")
        self.databaseView.heading("AssignEnd", text="AssignEnd")


        # Treeview columns
        self.databaseView.column("ProjID", width=100)
        self.databaseView.column("ProjDescrip", width=100)
        self.databaseView.column("Company", width=100)
        self.databaseView.column("Contract Date", width=100)
        self.databaseView.column("As of", width=100)
        self.databaseView.column("TaskDescrip", width=100)
        self.databaseView.column("TaskStartDate", width=100)
        self.databaseView.column("TaskEndDate", width=100)
        self.databaseView.column("SkillDescrip", width=100)
        self.databaseView.column("EmpID", width=100)
        self.databaseView.column("EmpLName", width=100)
        self.databaseView.column("EmpFName", width=100)
        self.databaseView.column("AssignBegin", width=100)
        self.databaseView.column("AssignEnd", width=100)

        
        #fills table with data
        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.window.mainloop()

class worklogreportWindow:
    def __init__(self, data):
        self.window = tkinter.Tk()
        self.window.wm_title("Work-log")

        # Label widgets
        tkinter.Label(self.window, text="Work-log", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tkinter.ttk.Treeview(self.window)
        self.databaseView.grid(pady=5, padx=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = (
        "projID", "EmpLname", "EmpFname", "WorkLogWeekEnding", "AssignID", "EmpID", "WorkLogHrsWorked", "BillID")

        # Treeview column headings
        self.databaseView.heading("projID", text="projID")
        self.databaseView.heading("EmpLname", text="EmpLname")
        self.databaseView.heading("EmpFname", text="EmpFname")
        self.databaseView.heading("WorkLogWeekEnding", text="WorkLogWeekEnding")
        self.databaseView.heading("AssignID", text="AssignID")
        self.databaseView.heading("EmpID", text="EmpID")
        self.databaseView.heading("WorkLogHrsWorked", text="WorkLogHrsWorked")
        self.databaseView.heading("BillID", text="BillID")

        # Treeview columns
        self.databaseView.column("projID", width=200)
        self.databaseView.column("EmpLname", width=100)
        self.databaseView.column("EmpFname", width=100)
        self.databaseView.column("WorkLogWeekEnding", width=100)
        self.databaseView.column("AssignID", width=100)
        self.databaseView.column("EmpID", width=100)
        self.databaseView.column("WorkLogHrsWorked", width=100)
        self.databaseView.column("BillID", width=100)

                #fills table with data
        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.window.mainloop()

#Reports main menu window
class ReportsWindow:
    def __init__(self, conn):
        self.dbconn = conn
        self.window = tkinter.Tk()
        self.window.wm_title("Reports")
        self.database = conn


        #Creates menu items and heading
        tkinter.Label(self.window, text="Generate Reports", width=100).grid(pady=20, column=1, row=1)

        tkinter.Button(self.window, text="Employee Skills Inventory", command=self.emp_skills_option).grid( pady=15, column=1, row=2 )
        tkinter.Button(self.window, text="Project Schedule Report", command=self.proj_schedule_option).grid( pady=15, column=1, row=3 )
        tkinter.Button(self.window, text="Assignments Form", command=self.assignments_form_option).grid( pady=15, column=1, row=4 )
        tkinter.Button(self.window, text="Work-Log Report", command=self.worklog_report_option).grid( pady=15, column=1, row=5 )

        tkinter.Button(self.window, text="Back", command=self.window.destroy).grid(pady=15, column=1, row=7)

        self.window.mainloop()
    
    #the window to choose what you search by
    def emp_skills_option(self):
        window = tkinter.Tk()
        window.wm_title("Employee Skills Report")

        employee = tkinter.StringVar()

        #Asks user what report they want
        tkinter.Label(window, text="Enter Employee ID or Display All", width=50).grid(pady=5, column=1, row=1)
        optEntry = tkinter.Entry(window, textvariable=employee, width=15)
        optEntry.grid(column=1, row=2)

        #executes the respective query
        tkinter.Button(window, text="Search By EmpID", command=lambda:self.emp_skillsbyemp(optEntry.get()), width=20).grid(pady=15, column=1, row=3)
        tkinter.Button(window, text="Display All", command=self.emp_skills, width=20).grid(pady=15, column=1, row=4)
        tkinter.Button(window, text="Back", command=window.destroy, width=20).grid(pady=20, column=1, row=5)

        window.mainloop()

        #display employee skills
    def emp_skills(self):
        data = self.database.DisplayEmpSkill()
        esWindow = EmpSkillsWindow(data)

        #display employee skills by the given empid
    def emp_skillsbyemp(self, empid):
        if(empid.isdigit()):
            data = self.database.DisplayEmpSkillbyEmp(empid) # does not work
            esWindow = EmpSkillsWindow(data)
        else:
            dates.displayMsg("Error", "Invalid EmpID Entry")

        #diplays menus for project schedule
    def proj_schedule_option(self):
        window = tkinter.Tk()
        window.wm_title("Project Schedule Report")

        proj = tkinter.StringVar()

        tkinter.Label(window, text="Enter Project ID or Display All", width=50).grid(pady=5, column=1, row=1)
        optEntry = tkinter.Entry(window, textvariable=proj, width=15)
        optEntry.grid(column=1, row=2)
        
        #executes the respective query
        tkinter.Button(window, text="Search By Project ID", command=lambda:self.proj_schedulebyproj(optEntry.get()), width=20).grid(pady=15, column=1, row=3)
        tkinter.Button(window, text="Display All", command=self.proj_schedule, width=20).grid(pady=15, column=1, row=4)
        tkinter.Button(window, text="Back", command=window.destroy, width=20).grid(pady=20, column=1, row=5)

        window.mainloop()

        #displays all project schedules
    def proj_schedule(self):
        data = self.database.DisplayProjSchedule()
        projWindow = projscheduleWindow(data)

        #displays project schedule by the given project id
    def proj_schedulebyproj(self, projid):
        if projid.isdigit():
            data = self.database.DisplayProjSchedulebyProj(projid)
            projWindow = projscheduleWindow(data)
        else:
            dates.displayMsg("Error", "Invalid Project ID")

        #displays the assignment form menu
    def assignments_form_option(self):
        window = tkinter.Tk()
        window.wm_title("Assignments Form")

        proj = tkinter.StringVar()
        emp = tkinter.StringVar()

        tkinter.Label(window, text="Enter Project ID or Employee ID or Press Display All", width=75).grid(pady=5, column=1, row=1)

        tkinter.Label(window, text="Project ID:", width=15).grid(pady=5, padx=40, column=1, row=2, sticky="W")
        projEntry = tkinter.Entry(window, textvariable=proj, width=15)
        projEntry.grid(column=1, row=2)

        tkinter.Label(window, text="Employee ID:", width=15).grid(pady=5, padx=40, column=1, row=3, sticky="W")
        empEntry = tkinter.Entry(window, textvariable=emp, width=15)
        empEntry.grid(column=1, row=3)

                #executes the respective query
        tkinter.Button(window, text="Search By Project ID", command=lambda:self.assignments_formbyproj(projEntry.get()), width=20).grid(pady=15, column=1, row=4)
        tkinter.Button(window, text="Search By Employee ID", command=lambda:self.assignments_formbyemp(empEntry.get()), width=20).grid(pady=15, column=1, row=5)
        tkinter.Button(window, text="Display All", command=self.assignments_form, width=20).grid(pady=15, column=1, row=6)
        tkinter.Button(window, text="Back", command=window.destroy, width=20).grid(pady=20, column=1, row=7)

        window.mainloop()
    
    #queries all assignments and window
    def assignments_form(self):
        data = self.database.DisplayAssignment()
        assignWindow = assignmentformWindow(data)

        #queries assignment based on projid
    def assignments_formbyproj(self, projid):
        if projid.isdigit():
            data = self.database.DisplayAssignmentbyProj(projid)
            assignWindow = assignmentformWindow(data)
        else:
            dates.displayMsg("Error", "Invalid Proj ID")

        #queries assignmentform by empid
    def assignments_formbyemp(self, empid):
        if empid.isdigit():
            data = self.database.DisplayAssignmentbyEmployee(empid)
            assignWindow = assignmentformWindow(data)
        else:
            dates.displayMsg("Error", "Invalid Emp ID")

        #displays worklog option menu
    def worklog_report_option(self):
        window = tkinter.Tk()
        window.wm_title("Worklog Report")

        proj = tkinter.StringVar()
        emp = tkinter.StringVar()

        tkinter.Label(window, text="Enter Project ID or Employee ID or Press Display All", width=75).grid(pady=5, column=1, row=1)

        tkinter.Label(window, text="Project ID:", width=15).grid(pady=5, padx=40, column=1, row=2, sticky="W")
        projEntry = tkinter.Entry(window, textvariable=proj, width=15)
        projEntry.grid(column=1, row=2)

        tkinter.Label(window, text="Employee ID:", width=15).grid(pady=5, padx=40, column=1, row=3, sticky="W")
        empEntry = tkinter.Entry(window, textvariable=emp, width=15)
        empEntry.grid(column=1, row=3)

                #executes the respective query
        tkinter.Button(window, text="Search By Project ID", command=lambda:self.worklog_reportbyproj(projEntry.get()), width=20).grid(pady=15, column=1, row=4)
        tkinter.Button(window, text="Search By Employee ID", command=lambda:self.worklog_reportbyemp(empEntry.get()), width=20).grid(pady=15, column=1, row=5)
        tkinter.Button(window, text="Display All", command=self.worklog_report, width=20).grid(pady=15, column=1, row=6)
        tkinter.Button(window, text="Back", command=window.destroy, width=20).grid(pady=20, column=1, row=7)

        window.mainloop()
    
    #shows all worklogs
    def worklog_report(self):
        data = self.database.DisplayWorklog()
        worklogWindow = worklogreportWindow(data)

        #shows worklog based on the projid
    def worklog_reportbyproj(self, projid):
        if projid.isdigit():
            data = self.database.DisplayWorklogbyProj(projid)
            worklogWindow = worklogreportWindow(data)
        else:
            dates.displayMsg("Error", "Invalid Proj ID")

        #shows worklog based on empid
    def worklog_reportbyemp(self, empid):
        if empid.isdigit():
            data = self.database.DisplayWorklogbyEmp(empid)
            worklogWindow = worklogreportWindow(data)
        else:
            dates.displayMsg("Error", "Invalid Emp ID")
