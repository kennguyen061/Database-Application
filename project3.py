import csv
import sys
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta


# connecting to the database 

try:
    print("attempting connection")
    conn = mysql.connector.connect(user="jbinz", password="password",
                                    host="db1.cwkukgaf0ib6.us-east-1.rds.amazonaws.com",
                                    database="project3")
    print("connected")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)


print("running query")
cursor = conn.cursor()

#creates all the tables


table = ("create table region (RegionID int auto_increment NOT NULL unique, RegionName char(2) NOT NULL unique, primary key (RegionID))")
cursor.execute(table)

table = ("create table employee (EmpID int auto_increment unique NOT NULL, EmpLname varchar(20) NOT NULL, EmpMInit char(1) unique, EmpFName varchar(20) NOT NULL, EmpHireDate date NOT NULL, RegID int NOT NULL, primary key (EmpID), foreign key (RegID) references region(RegionID))")
cursor.execute(table)

table = ("create table customer (CustID int auto_increment unique NOT NULL, CustName varchar(41) NOT NULL unique, CustPhone char(12), RegID int NOT NULL, primary key (CustID),foreign key (RegID) references region(RegionID))")
cursor.execute(table)

table = ("create table skill (SkillID int auto_increment NOT NULL unique,SkillDescrip varchar(255) NOT NULL unique,SkillPayRate decimal(10,2) NULL, primary key (SkillID))")
cursor.execute(table)

table = ("create table employee_skills (EmpID int NOT NULL, SkillID int NOT NULL, primary key (EmpID, SkillID), foreign key (EmpID) references employee(EmpID), foreign key (SkillID) references skill(SkillID))")
cursor.execute(table)

table = ("create table project (ProjID int auto_increment unique NOT NULL, ProjDescrip varchar(255) NOT NULL unique, ProjEstBudget decimal(10,2) NOT NULL,ProjEstEndDate date NOT NULL, ProjEstStartDate date NOT NULL, ProjActualStartDate date null, ProjActualEndDate date null, ProjActualCost decimal(10,2) null, CustID int NOT NULL unique, EmpID int NOT NULL, primary key (ProjID), foreign key (CustID) references customer(CustID), foreign key (EmpID) references employee(EmpID))")
cursor.execute(table)

table = ("create table task (TaskID int auto_increment unique NOT NULL,TaskDescrip varchar(255) NOT NULL,TaskStartDate date,TaskEndDate date,ProjID int NOT NULL,primary key (TaskID),foreign key (ProjID) references project(ProjID))")
cursor.execute(table)

table = ("create table task_skill (TaskSkillID int auto_increment unique NOT NULL,SkillID int NOT NULL,TaskID int NOT NULL,TaskSkillQuant int NOT NULL,primary key (TaskSkillID),foreign key (SkillID) references skill(SkillID),foreign key (TaskID) references task(TaskID))")
cursor.execute(table)

table = ("create table assignment (AssignID int auto_increment unique NOT NULL,AssignBegin date,AssignEnd date,EmpID int,TaskSkillID int NOT NULL,primary key (AssignID),foreign key (EmpID) references employee(EmpID),foreign key (TaskSkillID) references task_skill(TaskSkillID))")
cursor.execute(table)

table = ("create table bill (BillID int auto_increment unique NOT NULL,BillDate date NOT NULL,ProjID int NOT NULL,primary key (BillID),foreign key (ProjID) references project(ProjID))")
cursor.execute(table)

table = ("create table worklog (WorkLogID int auto_increment unique NOT NULL,WorkLogWeekEnding date NOT NULL,WorkLogHrsWorked int,AssignID int NOT NULL,BillID int null,primary key (WorkLogID),foreign key (AssignID) references assignment(AssignID),foreign key (BillID) references bill(BillID))")
cursor.execute(table)

#creates all the regions & inserts into region table
#primary key listed above each insert

#1 NW
regions = ("INSERT INTO region (RegionName) VALUES('NW')")
cursor.execute(regions)

#2 SW
regions = ("INSERT INTO region (RegionName) VALUES('SW')")
cursor.execute(regions)

#3 MN
regions = ("INSERT INTO region (RegionName) VALUES('MN')")
cursor.execute(regions)

#4 MS
regions = ("INSERT INTO region (RegionName) VALUES('MS')")
cursor.execute(regions)

#5 NE
regions = ("INSERT INTO region (RegionName) VALUES('NE')")
cursor.execute(regions)

#6 SE
regions = ("INSERT INTO region (RegionName) VALUES('SE')")
cursor.execute(regions)

#creates all the skills & inserts into skill table

#1
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('data entry I')")
cursor.execute(skill)

#2
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('data entry II')")
cursor.execute(skill)

#3
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('systems analyst I')")
cursor.execute(skill)

#4
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('systems analyst II')")
cursor.execute(skill)

#5
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('database designer I')")
cursor.execute(skill)

#6
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('database designer II')")
cursor.execute(skill)

#7
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('Cobol I')")
cursor.execute(skill)

#8
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('Cobol II')")
cursor.execute(skill)

#9
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('C++ I')")
cursor.execute(skill)

#10
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('C++ II')")
cursor.execute(skill)

#11
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('VB I')")
cursor.execute(skill)

#12
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('VB II')")
cursor.execute(skill)

#13
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('ColdFusion I')")
cursor.execute(skill)

#14
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('ColdFusion II')")
cursor.execute(skill)

#15
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('ASP I')")
cursor.execute(skill)

#16
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('ASP II')")
cursor.execute(skill)

#17
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('Oracle DBA')")
cursor.execute(skill)

#18
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('MS SQL Server DBA')")
cursor.execute(skill)

#19
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('network engineer I')")
cursor.execute(skill)

#20
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('network engineer II')")
cursor.execute(skill)

#21
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('web administrator')")
cursor.execute(skill)

#22
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('technical writer')")
cursor.execute(skill)

#23
skill = ("INSERT INTO skill (SkillDescrip) VALUES ('project manager')")
cursor.execute(skill)

#creates all the employees & inserts into employee table

#101
employee = ("INSERT INTO employee (EmpID, EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('101', '2011-03-29','Connor','Sean','1')")
cursor.execute(employee)

#102
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Burklow','Shane','1')")
cursor.execute(employee)

#103
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Smith','Mary','1')")
cursor.execute(employee)

#104
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Bush','Emily','1')")
cursor.execute(employee)

#105
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Zebras','Steve','1')")
cursor.execute(employee)

#106
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Smith','Jose','1')")
cursor.execute(employee)

#107
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2004-03-29','Summers','Anna','1')")
cursor.execute(employee)

#108
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2006-03-29','Ellis','Maria','1')")
cursor.execute(employee)

#109
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Ephanor','Victor','1')")
cursor.execute(employee)

#110
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Kilby','Surgena','1')")
cursor.execute(employee)

#111
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-29','Ellis','Maria','1')")
cursor.execute(employee)

#112
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Seaton','Amy','1')")
cursor.execute(employee)

#113
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Williams','Josh','1')")
cursor.execute(employee)

#114
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Underwood','Trish','1')")
cursor.execute(employee)

#115
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-29','Brett','Craig','1')")
cursor.execute(employee)

#116
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-29','Sewell','Beth','1')")
cursor.execute(employee)

#117
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-29','Robbins','Erin','1')")
cursor.execute(employee)

#118
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-29','Yarbrough','Peter','1')")
cursor.execute(employee)

#119
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-30','Pascoe','Jonathan','1')")
cursor.execute(employee)

#120
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Kattan','Chris','1')")
cursor.execute(employee)

#121
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Batts','Melissa','1')")
cursor.execute(employee)

#122
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Rogers','Adam','1')")
cursor.execute(employee)

#123
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Leslie','Cope','1')")
cursor.execute(employee)

#124
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Bible','Hanah','1')")
cursor.execute(employee)

#125
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Newton','Christopher','1')")
cursor.execute(employee)

#126
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','Duarte','Miriam','1')")
cursor.execute(employee)

#127
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','Bender','Larry','1')")
cursor.execute(employee)

#128
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','2011-03-29''Paine','Brad','1')")
cursor.execute(employee)

#129
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','Mudd','Roger','1')")
cursor.execute(employee)

#130
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','Kenyon','Tiffany','1')")
cursor.execute(employee)

#131
employee = ("INSERT INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','Chandler','Joseph','1')")
cursor.execute(employee)

#maps employees to skills in employee_skill table

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('112', '1')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('113', '1')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('114', '1')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('113', '2')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('112', '2')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('115', '3')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('116', '3')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('117', '3')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('104', '3')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('105', '3')")
cursor.execute(empskills)


empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('131', '4')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('102', '4')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('117', '4')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('118', '5')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('103', '5')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('118', '6')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('119', '6')")
cursor.execute(empskills)


empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('120', '7')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('109', '7')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('107', '7')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('111', '7')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('120', '8')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('109', '8')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('121', '8')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('106', '9')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('122', '9')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('123', '9')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('122', '10')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('124', '10')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('105', '11')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('108', '11')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('105', '12')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('125', '12')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('126', '13')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('104', '13')")
cursor.execute(empskills)


empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('104', '14')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('125', '14')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('126', '15')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('104', '15')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('126', '16')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('125', '16')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('106', '17')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('119', '17')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('118', '18')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('106', '18')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('104', '19')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('103', '19')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('104', '20')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('103', '20')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('104', '21')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('103', '21')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('125', '21')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('110', '22')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('127', '22')")
cursor.execute(empskills)

empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('128', '23')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('129', '23')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('130', '23')")
cursor.execute(empskills)
empskills = ("INSERT INTO employee_skills(EmpID,SkillID) VALUES ('101', '23')")
cursor.execute(empskills)

#creates customer to use for Project 1

customer = ("INSERT INTO customer(CustID,CustName,CustPhone,RegID) VALUES(101,'Bob Dylan','123-567-9111','1')")
cursor.execute(customer)


#creates project 1
project = ("INSERT INTO project(ProjDescrip,ProjEstBudget,ProjEstEndDate,ProjEstStartDate,ProjActualStartDate,CustID,EmpID) VALUES('Sales Management System','15500.00','2014-07-01','2014-02-12','2014-03-01',101,101)")
cursor.execute(project)

#creates tasks

#1
task = ("INSERT INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('Initial Interview','2014-03-01', '2014-03-06', '1')")
cursor.execute(task)

#2
task = ("INSERT INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('Database Design','2014-03-11', '2014-03-15', '1')")
cursor.execute(task)

#3
task = ("INSERT INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('System Design','2014-03-11', '2014-04-12', '1')")
cursor.execute(task)

#4
task = ("INSERT INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('Database Implementation','2014-03-18', '2014-03-22', '1')")
cursor.execute(task)

#5
task = ("INSERT INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('System Coding & Testing','2014-03-25', '2014-06-07', '1')")
cursor.execute(task)

#6
task = ("INSERT INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('System Documentation','2014-03-25', '2014-06-07', '1')")
cursor.execute(task)

#7
task = ("INSERT INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('Final Evaluation','2014-06-10', '2014-06-14', '1')")
cursor.execute(task)

#8
task = ("INSERT INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('On-Site System Online and Data Loading','2014-06-17', '2014-06-21', '1')")
cursor.execute(task)

#9
task = ("INSERT INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('Sign-Off','2014-07-01', '2014-07-01', '1')")
cursor.execute(task)

#creates task to skills mappings

taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('23','1','1')")
cursor.execute(taskskill)
taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('4','1','1')")
cursor.execute(taskskill)
taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('5','1','1')")
cursor.execute(taskskill)

taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('5','2','1')")
cursor.execute(taskskill)

taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('4','3','1')")
cursor.execute(taskskill)
taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('3','3','2')")
cursor.execute(taskskill)

taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('17','4','1')")
cursor.execute(taskskill)

taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('7','5','2')")
cursor.execute(taskskill)
taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('8','5','1')")
cursor.execute(taskskill)
taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('17','5','1')")
cursor.execute(taskskill)

taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('22','6','1')")
cursor.execute(taskskill)

taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('23','7','1')")
cursor.execute(taskskill)
taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('4','7','1')")
cursor.execute(taskskill)
taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('5','7','1')")
cursor.execute(taskskill)
taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('8','7','1')")
cursor.execute(taskskill)

taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('23','8','1')")
cursor.execute(taskskill)
taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('4','8','1')")
cursor.execute(taskskill)
taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('5','8','1')")
cursor.execute(taskskill)
taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('8','8','1')")
cursor.execute(taskskill)

taskskill = ("INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('23','9','1')")
cursor.execute(taskskill)

# creates assignment entries

assignment = ("INSERT INTO assignment(AssignBegin, AssignEnd, EmpID, TaskSkillID) VALUES ('2014-03-01','2014-03-06',101,'1')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, AssignEnd, EmpID, TaskSkillID) VALUES ('2014-03-01','2014-03-06',102,'2')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, AssignEnd, EmpID, TaskSkillID) VALUES ('2014-03-01','2014-03-06',103,'3')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, AssignEnd, EmpID, TaskSkillID) VALUES ('2014-03-11','2014-03-14',104,'4')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-11','105','5')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-11','106','6')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-11','107','6')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, AssignEnd, EmpID, TaskSkillID) VALUES ('2014-03-15','2014-03-19',108,'7')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-21','109','8')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-21','110','8')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-21','111','9')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-21','112','10')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-25','113','11')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(TaskSkillID) VALUES ('12')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(TaskSkillID) VALUES ('13')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(TaskSkillID) VALUES ('14')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(TaskSkillID) VALUES ('15')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(TaskSkillID) VALUES ('16')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(TaskSkillID) VALUES ('17')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(TaskSkillID) VALUES ('18')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(TaskSkillID) VALUES ('19')")
cursor.execute(assignment)

assignment = ("INSERT INTO assignment(TaskSkillID) VALUES ('20')")
cursor.execute(assignment)

#creates bills to be used in worklog table & bill table

bill = ( "INSERT INTO bill(BillID, BillDate, ProjID) VALUES( 101, '2014-03-15', '1')" )
cursor.execute(bill)

bill = ( "INSERT INTO bill(BillDate, ProjID) VALUES('2014-03-22', '1')" )
cursor.execute(bill)

#creates worklogs

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-01', '4', '2', '101' )")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-01', '4', '1', '101')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-01', '4', '3', '101')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-08', '24', '2', '101')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-08', '24', '1', '101')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-08', '24', '3', '101')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-15', '40', '5', '102')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-15', '40', '6', '102')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-15', '6', '8', '102')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-15', '32', '4', '102')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-15', '35', '7', '102')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '40', '5')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '40', '6')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '12', '10')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '12', '11')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '12', '8')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '12', '12')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '12', '9')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '35', '7')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '40', '5')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '40', '6')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '35', '10')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '35', '11')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '40', '13')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '35', '12')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '35', '9')")
cursor.execute(work_log)

work_log = ("INSERT INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '35', '7')")
cursor.execute(work_log)

conn.commit()
cursor.close()

conn.close()



