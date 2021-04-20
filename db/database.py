import csv
import sys
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from db import seed as Seed

class Database:
    def __init__(self):

        try: self.dbConnection = mysql.connector.connect(host="db1.cwkukgaf0ib6.us-east-1.rds.amazonaws.com",
                                               user="jbinz",
                                               passwd="password", database="p4ex")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        self.dbCursor = self.dbConnection.cursor()

    def TableCreate(self):

        #need to check if there already exists entries in tables or not

        seed = Seed.SeedData(self.dbConnection)
        seed.insert_seed_data()

	#displays all employees and their assigned skills
    def DisplayEmpSkill(self):
        #self.dbCursor.execute("SELECT * FROM employee_skills")
        self.dbCursor.execute("SELECT `SkillDescrip`, EmpLName, EmpFName FROM skill,employee, employee_skills WHERE employee.EmpID = employee_skills.EmpID AND skill.SkillID = employee_skills.SkillID")
        records = self.dbCursor.fetchall()
        return records


	#displays all employee skills by an employee
    def DisplayEmpSkillbyEmp(self, empid):
        self.dbCursor.execute("SELECT SkillDescrip, EmpLName, EmpFName FROM skill, employee_skills, employee WHERE skill.SkillID = employee_skills.SkillID AND employee_skills.EmpID = employee.EmpID AND employee_skills.EmpID = '" + empid + "'")
        records = self.dbCursor.fetchall()
        return records

	#displays all project schedules in all projects
    def DisplayProjSchedule(self):
        self.dbCursor.execute("SELECT project.ProjID, project.ProjDescrip, customer.CustName AS 'Company',project.ProjEstStartDate AS 'Contract Date', region.RegionName, project.ProjActualStartDate, project.ProjActualEndDate, project.projEstBudget, task.TaskStartDate,task.TaskEndDate,task.TaskDescrip,skill.SkillDescrip,task_skill.TaskSkillQuant FROM project, task, skill, task_skill, customer, region WHERE task.TaskID = task_skill.TaskID AND skill.SkillID = task_skill.SkillID AND project.CustID = customer.CustID AND customer.RegID = region.RegionID")
        records = self.dbCursor.fetchall()
        return records
    	
	#displays all project schedules within a project
    def DisplayProjSchedulebyProj(self, projid):
        self.dbCursor.execute("SELECT project.ProjID, project.ProjDescrip, customer.CustName AS 'Company',project.ProjEstStartDate AS 'Contract Date', region.RegionName, project.ProjActualStartDate, project.ProjActualEndDate, project.projEstBudget, task.TaskStartDate,task.TaskEndDate,task.TaskDescrip,skill.SkillDescrip,task_skill.TaskSkillQuant FROM project, task, skill, task_skill, customer, region WHERE task.TaskID = task_skill.TaskID AND skill.SkillID = task_skill.SkillID AND project.CustID = customer.CustID AND project.ProjID = '" + projid + "' AND customer.RegID = region.RegionID")
        records = self.dbCursor.fetchall()
        return records

    #displays the assignment form
    def DisplayAssignment(self):
        self.dbCursor.execute("SELECT project.ProjID, project.ProjDescrip, customer.CustName AS 'Company', project.ProjEstStartDate AS 'Contract Date', CURRENT_DATE AS 'As of', task.TaskDescrip, task.TaskStartDate, task.TaskEndDate, skill.SkillDescrip, employee.EmpID, employee.EmpLname, employee.EmpFName, assignment.AssignBegin, assignment.AssignEnd FROM project, customer, task, skill, employee, employee_skills, assignment, task_skill WHERE project.ProjID = task.ProjID AND project.CustID = customer.CustID AND task_skill.SkillID = skill.SkillID AND task_skill.TaskID = task.TaskID AND employee_skills.EmpID = employee.EmpID AND employee_skills.SkillID = skill.SkillID AND assignment.EmpID = employee.EmpID AND assignment.TaskSkillID = task_skill.TaskSkillID")
        records = self.dbCursor.fetchall()
        return records

    #displays the assignment form by project
    def DisplayAssignmentbyProj(self, projid):
        self.dbCursor.execute("SELECT project.ProjID, project.ProjDescrip, customer.CustName AS 'Company', project.ProjEstStartDate AS 'Contract Date', CURRENT_DATE AS 'As of', task.TaskDescrip, task.TaskStartDate, task.TaskEndDate, skill.SkillDescrip, employee.EmpID, employee.EmpLname, employee.EmpFName, assignment.AssignBegin, assignment.AssignEnd FROM project, customer, task, skill, employee, employee_skills, assignment, task_skill WHERE project.ProjID = task.ProjID AND project.CustID = customer.CustID AND task_skill.SkillID = skill.SkillID AND task_skill.TaskID = task.TaskID AND employee_skills.EmpID = employee.EmpID AND employee_skills.SkillID = skill.SkillID AND assignment.EmpID = employee.EmpID AND assignment.TaskSkillID = task_skill.TaskSkillID" + " AND project.ProjID = '" + projid + "'")
        records = self.dbCursor.fetchall()
        return records

    #displays the assignment form by employee
    def DisplayAssignmentbyEmployee(self, empid):
        self.dbCursor.execute("SELECT project.ProjID, project.ProjDescrip, customer.CustName AS 'Company', project.ProjEstStartDate AS 'Contract Date', CURRENT_DATE AS 'As of', task.TaskDescrip, task.TaskStartDate, task.TaskEndDate, skill.SkillDescrip, employee.EmpID, employee.EmpLname, employee.EmpFName, assignment.AssignBegin, assignment.AssignEnd FROM project, customer, task, skill, employee, employee_skills, assignment, task_skill WHERE project.ProjID = task.ProjID AND project.CustID = customer.CustID AND task_skill.SkillID = skill.SkillID AND task_skill.TaskID = task.TaskID AND employee_skills.EmpID = employee.EmpID AND employee_skills.SkillID = skill.SkillID AND assignment.EmpID = employee.EmpID AND assignment.TaskSkillID = task_skill.TaskSkillID" + " AND employee.EmpID = '" + empid + "'")
        records = self.dbCursor.fetchall()
        return records

	#displays all worklogs
    def DisplayWorklog(self):
        self.dbCursor.execute("SELECT project.ProjID, employee.EmpLName, employee.EmpFName, worklog.WorkLogWeekEnding, assignment.AssignID, employee.EmpID, worklog.WorkLogHrsWorked, bill.BillID FROM project, employee, assignment, worklog LEFT JOIN bill ON worklog.BillID = bill.BillID WHERE worklog.AssignID = assignment.AssignID AND employee.EmpID = assignment.EmpID")
        records = self.dbCursor.fetchall()
        return records

	#displays all the worklogs by a project
    def DisplayWorklogbyProj(self, projid):
        self.dbCursor.execute("SELECT project.ProjID, employee.EmpLName, employee.EmpFName, worklog.WorkLogWeekEnding, assignment.AssignID, employee.EmpID, worklog.WorkLogHrsWorked, bill.BillID FROM employee, worklog, assignment, bill, project WHERE worklog.BillID = bill.BillID AND worklog.AssignID = assignment.AssignID AND employee.EmpID = assignment.EmpID and project.ProjID = '" + projid + "'")
        records = self.dbCursor.fetchall()
        return records

	#displays all the worklogs assigned to an employee by empid
    def DisplayWorklogbyEmp(self, empid):
        self.dbCursor.execute("SELECT project.ProjID, employee.EmpLName, employee.EmpFName, worklog.WorkLogWeekEnding, assignment.AssignID, employee.EmpID, worklog.WorkLogHrsWorked, bill.BillID FROM project, employee, assignment, worklog LEFT JOIN bill ON worklog.BillID = bill.BillID WHERE worklog.AssignID = assignment.AssignID AND employee.EmpID = assignment.EmpID and employee.EmpID = '" + empid + "'")
        records = self.dbCursor.fetchall()
        return records

	#displays all regionids and their region names
    def DisplayRegion(self):
        self.dbCursor.execute("SELECT region.RegionID,region.RegionName FROM region")
        records = self.dbCursor.fetchall()
        return records

	#displays all customers' custID and custname
    def DisplayCustomer(self):
        self.dbCursor.execute("SELECT CustID, CustName FROM customer")
        records = self.dbCursor.fetchall()
        return records
	
	#displays all projectids and project names
    def DisplayProjects(self):
        self.dbCursor.execute("SELECT ProjID, ProjDescrip FROM project")
        records = self.dbCursor.fetchall()
        return records

	#displays employees that have a 'project manager' skill
    def DisplayProjManagers(self):
        self.dbCursor.execute("SELECT employee.EmpID, employee.EmpLName, employee.EmpFName FROM employee, employee_skills, skill WHERE employee.EmpID = employee_skills.EmpID AND employee_skills.SkillID = skill.SkillID AND skill.SkillDescrip = 'project manager'")
        records = self.dbCursor.fetchall()
        return records

    #validates employees    
    def validateemployee(self, hiredate, lastname, firstname, region):
        if not(lastname.isalpha()):
            print(lastname)
            return "Last name"
        elif not(firstname.isalpha()):
            return "First name"
        else:
            return "Success"

    #inserts employees
    def insertemployee(self, conn, hiredate, lastname, firstname, region):
        cursor = conn.cursor()
        new_employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ( '" + hiredate + "','" + lastname + "','" + firstname + "','" + region + "')")
        print(new_employee)
        cursor.execute(new_employee)
        conn.commit()
        cursor.close()

    #validates project inputs
    def validateproject(self, projdesc, budget):
	    # if not(projdesc.isalpha()):
		#     return "Project Description"  --- This does not work, counts spaces as not alpha & you could also have a number in a project description
	    if (not(budget.isdigit()) ):
		    return "Budget"
	    else:
		    return "Success"

    #inserts a project
    def insertproject(self, conn, projdesc, budget, estenddate, eststartdate, projactualstart, custid, empid):
        cursor = conn.cursor()
        new_project = ("INSERT INTO project(ProjDescrip,ProjEstBudget,ProjEstEndDate,ProjEstStartDate,ProjActualStartDate,CustID,EmpID) VALUES('" + projdesc + "','" + budget + "','" + estenddate + "','" + eststartdate + "','" + projactualstart + "','" + custid + "','" + empid + "')")
        print(new_project)
        cursor.execute(new_project)
        conn.commit()
        cursor.close()

    #assign manager to project
    def assignmanager(self, conn, empid, projid):
        cursor = conn.cursor()
        assign = ("UPDATE project SET EmpID = '" + empid + "', WHERE ProjID = '" + projid + "')")
        conn.commit()
        cursor.close()
    
    #check if the hours employees put in are valid
    def validhours(self, hours):
        if not(hours.isdigit()):
            return "Hours"
        else:
            return "Success"

    #updates the worklog
    def updateworklog(self, conn, hours, assignid):
        cursor = conn.cursor()
        worklog = ("UPDATE worklog SET worklog.WorkLogHrsWorked = '" + hours + "' WHERE worklog.assignID = '" + assignid + "')")
        cursor.execute(worklog)
        conn.commit()
        cursor.close()

	#checks if the skill inputted is alphabetic
    def validateskill(self, new_skill):
        if not (new_skill.isalpha()):
            return "Skill Name"
        else:
            return "Success"

	#inserts the skill string call after validating
    def insertskill(self, skilldesc, conn):
        cursor = conn.cursor()
        skilldata = (skilldesc)
        new_skill = ("INSERT INTO skill (SkillDescrip) VALUES('" + skilldesc + "')")
        #print(new_skill)
        cursor.execute(new_skill)
        conn.commit()
        cursor.close()
    
    #function to take a project description & return the corresponding ID
    def getProjectID(self, conn, pd):
        cursor = conn.cursor()
        select = ("SELECT ProjID FROM project WHERE project.ProjDescrip = '" + pd + "'")
        cursor.execute(select)
        record = cursor.fetchall()
        
        return record

    #function to add a task entity to the database
    def insertTask(self, conn, projID, descrip, startDate, endDate):
        cursor = conn.cursor()
        new_task = ("INSERT INTO task(TaskDescrip, TaskStartDate, TaskEndDate, ProjID) VALUES('"+ descrip + "', '"+ startDate + "', '"+ endDate + "', '"+ projID +"')")
        print("Printing sql command:")
        print(new_task)
        cursor.execute(new_task)
        conn.commit()
        cursor.close()

    #function to return a list of skillID's and skill descriptions
    def get_skills(self, conn):
        cursor = conn.cursor()
        cursor.execute("SELECT SkillID, SkillDescrip from skill")
        records = cursor.fetchall()
        return records

	#returns the taskid based on the desc given
    def get_taskID(self, conn, desc):
        cursor = conn.cursor()
        select = ("SELECT TaskID FROM task WHERE task.TaskDescrip = '" + desc + "'")
        cursor.execute(select)
        record = cursor.fetchall()
        tid = record[0]
        
        return tid[0]

	#inserts the task_skill object based on the given skillid, taskid, and taskskill quant
    def map_task_skill(self, conn, skillID, TaskID, TaskSkillQuant):
        cursor = conn.cursor()
        insert = ("INSERT INTO task_skill(SkillID, TaskID, TaskSkillQuant) VALUES('"+str(skillID)+"', '"+str(TaskID)+"', '"+str(TaskSkillQuant)+"')")
        cursor.execute(insert)
        conn.commit()
        cursor.close()

    #function to get a list of employees that have skills to work on a given task
    def get_emps_for_search_assign( self, conn, projID, taskID ):
        cursor = conn.cursor()
        skills_sel = ("SELECT SkillID, TaskSkillID FROM task_skill WHERE task_skill.TaskID = '"+str(taskID)+"' group by SkillID")
        cursor.execute(skills_sel)
        skill_list = cursor.fetchall()
        full_emp_list = []
        for skill in skill_list:
            emps = ("SELECT employee.EmpID, EmpFName, EmpLName FROM (employee JOIN employee_skills ON employee.EmpID = employee_skills.EmpID) WHERE skillID = '"+str(skill[0])+"'")
            cursor.execute(emps)
            emp_list = cursor.fetchall()
            for emp in emp_list:
                full_emp_list.append((emp, skill[1]))
        return full_emp_list
        
	#creates a new assignment object based on assign_begin, assign_end, empid, and taskskillid
    def create_assignment(self, conn, assign_begin, assign_end, EmpID, TaskSkillID):
        cursor = conn.cursor()
        insert = ("INSERT INTO assignment(AssignBegin, AssignEnd, EmpID, TaskSkillID) VALUES('"+assign_begin+"', '"+assign_end+"', '"+str(EmpID)+"', '"+str(TaskSkillID)+"')")
        cursor.execute(insert)
        conn.commit()
        cursor.close()

	#updates worklog based on the weekEnding, hrs, assignID, and billID
    def update_worklog(self, conn, weekEnding, hrs, assignID, billID):
        cursor = conn.cursor()
	#if there is no bill attached
        if billID == -1:
            insert = ("INSERT INTO worklog(WorkLogWeekEnding, WorkLogHrsWorked, AssignID) VALUES('"+weekEnding+"', '"+str(hrs)+"', '"+str(assignID)+"')")
        #if there is a bill attached
        else:
            insert = ("INSERT INTO worklog(WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID) VALUES('"+weekEnding+"', '"+str(hrs)+"', '"+str(assignID)+"', '"+str(billID)+"')")
        cursor.execute(insert)
        conn.commit()
        cursor.close()

    def get_bill(self, conn, date, projID):
        cursor = conn.cursor()
        select = ("select count(BillID), BillID from bill where bill.ProjID = '"+str(projID)+"' and bill.BillDate = '"+str(date)+"'")
        cursor.execute(select)
        result = cursor.fetchall()
        if result[0][0] == 1:   #if the bill already exists, calculate the amount & return it
            amt = self.calc_bill_amt(conn, result[0][1])
            cursor.close()
            return (1, result[0][1], amt)    #(if exists, billID, amount)
        else:   #make a new bill
            insert = ("insert into bill(BillDate, ProjID) values('"+str(date)+"', '"+str(projID)+"')")
            cursor.execute(insert)
            conn.commit()
            select = ("select BillID from bill where bill.ProjID = '"+str(projID)+"' and bill.BillDate = '"+str(date)+"'")
            cursor.execute(select)
            result = cursor.fetchall()
            cursor.close()
            return (0, result[0][0], 0)

        
    
    def calc_bill_amt(self, conn, billID):
        cursor = conn.cursor()
        select = ("select WorkLogHrsWorked, SkillPayRate from (select WorkLogHrsWorked, SkillID from (select WorkLogHrsWorked, TaskSkillID from (select WorkLogHrsWorked, AssignID from worklog where BillID = '"+str(billID)+"') as t1 join assignment where t1.AssignID = assignment.AssignID) as t2 join task_skill where t2.TaskSkillID = task_skill.TaskSkillID) as t3 join skill where t3.SkillID = skill.SkillID")
        cursor.execute(select)
        result = cursor.fetchall()
        amt = 0
        for entry in result:
            if entry[1] == None:
                #If no skill pay rate is listed use default of $20 an hour
                amt = amt + (entry[0]*20)
            else:
                amt = amt + (entry[0]*entry[1])
        cursor.close()
        return amt
