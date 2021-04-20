import csv
import sys
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

class SeedData:
    def __init__(self, conn):
        self.conn = conn

    def create_tables(self):

        cursor = self.conn.cursor()

        #creates all the tables
        table = ("create table if not exists region (RegionID int auto_increment NOT NULL unique, RegionName char(2) NOT NULL unique, primary key (RegionID))")
        cursor.execute(table)

        table = ("create table if not exists employee (EmpID int auto_increment unique NOT NULL, EmpLname varchar(20) NOT NULL, EmpMInit char(1) unique, EmpFName varchar(20) NOT NULL, EmpHireDate date NOT NULL, RegID int NOT NULL, primary key (EmpID), foreign key (RegID) references region(RegionID))")
        cursor.execute(table)

        table = ("create table if not exists customer (CustID int auto_increment unique NOT NULL, CustName varchar(41) NOT NULL unique, CustPhone char(12), RegID int NOT NULL, primary key (CustID),foreign key (RegID) references region(RegionID))")
        cursor.execute(table)

        table = ("create table if not exists skill (SkillID int auto_increment NOT NULL unique,SkillDescrip varchar(255) NOT NULL unique,SkillPayRate decimal(10,2) NULL, primary key (SkillID))")
        cursor.execute(table)

        table = ("create table if not exists employee_skills (EmpID int NOT NULL, SkillID int NOT NULL, primary key (EmpID, SkillID), foreign key (EmpID) references employee(EmpID), foreign key (SkillID) references skill(SkillID))")
        cursor.execute(table)

        table = ("create table if not exists project (ProjID int auto_increment unique NOT NULL, ProjDescrip varchar(255) NOT NULL unique, ProjEstBudget decimal(10,2) NOT NULL,ProjEstEndDate date NOT NULL, ProjEstStartDate date NOT NULL, ProjActualStartDate date null, ProjActualEndDate date null, ProjActualCost decimal(10,2) null, CustID int NOT NULL, EmpID int NOT NULL, primary key (ProjID), foreign key (CustID) references customer(CustID), foreign key (EmpID) references employee(EmpID))")
        cursor.execute(table)

        table = ("create table if not exists task (TaskID int auto_increment unique NOT NULL,TaskDescrip varchar(255) NOT NULL,TaskStartDate date,TaskEndDate date,ProjID int NOT NULL,primary key (TaskID),foreign key (ProjID) references project(ProjID))")
        cursor.execute(table)

        table = ("create table if not exists task_skill (TaskSkillID int auto_increment unique NOT NULL,SkillID int NOT NULL,TaskID int NOT NULL,TaskSkillQuant int NOT NULL,primary key (TaskSkillID),foreign key (SkillID) references skill(SkillID),foreign key (TaskID) references task(TaskID))")
        cursor.execute(table)

        table = ("create table if not exists assignment (AssignID int auto_increment unique NOT NULL,AssignBegin date,AssignEnd date,EmpID int,TaskSkillID int NOT NULL,primary key (AssignID),foreign key (EmpID) references employee(EmpID),foreign key (TaskSkillID) references task_skill(TaskSkillID))")
        cursor.execute(table)

        table = ("create table if not exists bill (BillID int auto_increment unique NOT NULL,BillDate date NOT NULL,ProjID int NOT NULL,primary key (BillID),foreign key (ProjID) references project(ProjID))")
        cursor.execute(table)

        table = ("create table if not exists worklog (WorkLogID int auto_increment unique NOT NULL,WorkLogWeekEnding date NOT NULL,WorkLogHrsWorked int,AssignID int NOT NULL,BillID int null,primary key (WorkLogID),foreign key (AssignID) references assignment(AssignID),foreign key (BillID) references bill(BillID))")
        cursor.execute(table)

        self.conn.commit()
        cursor.close()

    def populate_region(self):
        #creates all the regions & inserts into region table
        #primary key listed above each insert

        cursor = self.conn.cursor()
        
        #1 NW
        regions = ("INSERT IGNORE INTO region (RegionName) VALUES('NW')")
        cursor.execute(regions)

        #2 SW
        regions = ("INSERT IGNORE INTO region (RegionName) VALUES('SW')")
        cursor.execute(regions)

        #3 MN
        regions = ("INSERT IGNORE INTO region (RegionName) VALUES('MN')")
        cursor.execute(regions)

        #4 MS
        regions = ("INSERT IGNORE INTO region (RegionName) VALUES('MS')")
        cursor.execute(regions)

        #5 NE
        regions = ("INSERT IGNORE INTO region (RegionName) VALUES('NE')")
        cursor.execute(regions)

        #6 SE
        regions = ("INSERT IGNORE INTO region (RegionName) VALUES('SE')")
        cursor.execute(regions)

        self.conn.commit()
        cursor.close()

    def populate_skill(self):

        #creates all the skills & inserts into skill table

        cursor = self.conn.cursor()
        #1
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('data entry I')")
        cursor.execute(skill)

        #2
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('data entry II')")
        cursor.execute(skill)

        #3
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('systems analyst I')")
        cursor.execute(skill)

        #4
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('systems analyst II')")
        cursor.execute(skill)

        #5
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('database designer I')")
        cursor.execute(skill)

        #6
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('database designer II')")
        cursor.execute(skill)

        #7
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('Cobol I')")
        cursor.execute(skill)

        #8
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('Cobol II')")
        cursor.execute(skill)

        #9
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('C++ I')")
        cursor.execute(skill)

        #10
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('C++ II')")
        cursor.execute(skill)

        #11
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('VB I')")
        cursor.execute(skill)

        #12
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('VB II')")
        cursor.execute(skill)

        #13
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('ColdFusion I')")
        cursor.execute(skill)

        #14
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('ColdFusion II')")
        cursor.execute(skill)

        #15
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('ASP I')")
        cursor.execute(skill)

        #16
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('ASP II')")
        cursor.execute(skill)

        #17
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('Oracle DBA')")
        cursor.execute(skill)

        #18
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('MS SQL Server DBA')")
        cursor.execute(skill)

        #19
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('network engineer I')")
        cursor.execute(skill)

        #20
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('network engineer II')")
        cursor.execute(skill)

        #21
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('web administrator')")
        cursor.execute(skill)

        #22
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('technical writer')")
        cursor.execute(skill)

        #23
        skill = ("INSERT IGNORE INTO skill (SkillDescrip) VALUES ('project manager')")
        cursor.execute(skill)

        self.conn.commit()
        cursor.close()

    def populate_employee(self):
        #creates all the employees & inserts into employee table

		#queries the NW region's id for the insert
        cursor = self.conn.cursor()
        cursor.execute("SELECT RegionID FROM region WHERE RegionName = 'NW'")
        region = cursor.fetchall()
        #tuple to string
        region = str(region[0][0])
        

        #101
        employee = ("INSERT IGNORE INTO employee (EmpID, EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('101', '2011-03-29','Connor','Sean','" + region + "')")
        cursor.execute(employee)

        #102
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Burklow','Shane','" + region + "')")
        cursor.execute(employee)

        #103
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Smith','Mary','" + region + "')")
        cursor.execute(employee)

        #104
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Bush','Emily','" + region + "')")
        cursor.execute(employee)

        #105
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Zebras','Steve','" + region + "')")
        cursor.execute(employee)

        #106
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Smith','Jose','" + region + "')")
        cursor.execute(employee)

        #107
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2004-03-29','Summers','Anna','" + region + "')")
        cursor.execute(employee)

        #108
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2006-03-29','Ellis','Maria','" + region + "')")
        cursor.execute(employee)

        #109
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Ephanor','Victor','" + region + "')")
        cursor.execute(employee)

        #110
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Kilby','Surgena','" + region + "')")
        cursor.execute(employee)

        #111
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-29','Ellis','Maria','" + region + "')")
        cursor.execute(employee)

        #112
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Seaton','Amy','" + region + "')")
        cursor.execute(employee)

        #113
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Williams','Josh','" + region + "')")
        cursor.execute(employee)

        #114
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Underwood','Trish','" + region + "')")
        cursor.execute(employee)

        #115
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-29','Brett','Craig','" + region + "')")
        cursor.execute(employee)

        #116
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-29','Sewell','Beth','" + region + "')")
        cursor.execute(employee)

        #117
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-29','Robbins','Erin','" + region + "')")
        cursor.execute(employee)

        #118
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-29','Yarbrough','Peter','" + region + "')")
        cursor.execute(employee)

        #119
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2010-03-30','Pascoe','Jonathan','" + region + "')")
        cursor.execute(employee)

        #120
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Kattan','Chris','" + region + "')")
        cursor.execute(employee)

        #121
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Batts','Melissa','" + region + "')")
        cursor.execute(employee)

        #122
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Rogers','Adam','" + region + "')")
        cursor.execute(employee)

        #123
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Leslie','Cope','" + region + "')")
        cursor.execute(employee)

        #124
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Bible','Hanah','" + region + "')")
        cursor.execute(employee)

        #125
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-03-29','Newton','Christopher','" + region + "')")
        cursor.execute(employee)

        #126
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','Duarte','Miriam','" + region + "')")
        cursor.execute(employee)

        #127
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','Bender','Larry','" + region + "')")
        cursor.execute(employee)

        #128
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','2011-03-29''Paine','Brad','" + region + "')")
        cursor.execute(employee)

        #129
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','Mudd','Roger','" + region + "')")
        cursor.execute(employee)

        #130
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','Kenyon','Tiffany','" + region + "')")
        cursor.execute(employee)

        #131
        employee = ("INSERT IGNORE INTO employee (EmpHireDate, EmpLname,EmpFname, RegID) VALUES ('2011-06-29','Chandler','Joseph','" + region + "')")
        cursor.execute(employee)

        self.conn.commit()
        cursor.close()

    def map_empskills(self):

        #maps employees to skills in employee_skill table
        cursor = self.conn.cursor()

        #fetches skillid for data entry i
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'data entry I'")
        skill = cursor.fetchall()
        #tuple to string
        skill = str(skill[0][0])

        #fetches skillid for connor sean
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Connor' AND EmpFName = 'Sean'")
        fetch = cursor.fetchall()
        #tuple to string
        connorsean = str(fetch[0][0])

        #fetches skillid for burklow shane
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Burklow' AND EmpFName = 'Shane'")
        fetch = cursor.fetchall()
        #tuple to string
        burklowshane = str(fetch[0][0])

                #fetches skillid for smith mary
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Smith' AND EmpFName = 'Mary'")
        fetch = cursor.fetchall()
        #tuple to string
        smithmary = str(fetch[0][0])

                #fetches skillid for bush emily
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Bush' AND EmpFName = 'Emily'")
        fetch = cursor.fetchall()
        #tuple to string
        bushemily = str(fetch[0][0])

                #fetches skillid for zebras steve
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Zebras' AND EmpFName = 'Steve'")
        fetch = cursor.fetchall()
        #tuple to string
        zebrassteve = str(fetch[0][0])

                #fetches skillid for smith jose
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Smith' AND EmpFName = 'Jose'")
        fetch = cursor.fetchall()
        #tuple to string
        smithjose = str(fetch[0][0])

                        #fetches skillid for summers anna
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Summers' AND EmpFName = 'Anna'")
        fetch = cursor.fetchall()
        #tuple to string
        summeranna = str(fetch[0][0])

                        #fetches skillid for ellis maria
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Ellis' AND EmpFName = 'Maria'")
        fetch = cursor.fetchall()
        #tuple to string
        ellismaria = str(fetch[0][0])

                                #fetches skillid for ephanor victor
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Ephanor' AND EmpFName = 'Victor'")
        fetch = cursor.fetchall()
        #tuple to string
        ephanorvictor = str(fetch[0][0])

                                #fetches skillid for kilby surgena
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Kilby' AND EmpFName = 'Surgena'")
        fetch = cursor.fetchall()
        #tuple to string
        kilbysurgena = str(fetch[0][0])

                        #fetches skillid for seaton amy
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Seaton' AND EmpFName = 'Amy'")
        fetch = cursor.fetchall()
        #tuple to string
        seatonamy = str(fetch[0][0])

                        #fetches skillid for williams josh
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Williams' AND EmpFName = 'Josh'")
        fetch = cursor.fetchall()
        #tuple to string
        williamsjosh = str(fetch[0][0])

                                #fetches skillid for underwood trish
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Underwood' AND EmpFName = 'Trish'")
        fetch = cursor.fetchall()
        #tuple to string
        underwoodtrish = str(fetch[0][0])

                                #fetches skillid for brett craig
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Brett' AND EmpFName = 'Craig'")
        fetch = cursor.fetchall()
        #tuple to string
        brettcraig = str(fetch[0][0])

                                #fetches skillid for sewell beth
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Sewell' AND EmpFName = 'Beth'")
        fetch = cursor.fetchall()
        #tuple to string
        sewellbeth = str(fetch[0][0])

                                #fetches skillid for robbins erin
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Robbins' AND EmpFName = 'Erin'")
        fetch = cursor.fetchall()
        #tuple to string
        robbinserin = str(fetch[0][0])

                                #fetches skillid for yarbrough peter
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Yarbrough' AND EmpFName = 'Peter'")
        fetch = cursor.fetchall()
        #tuple to string
        yarbroughpeter = str(fetch[0][0])

                                #fetches skillid for pascoe jonathan
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Pascoe' AND EmpFName = 'Jonathan'")
        fetch = cursor.fetchall()
        #tuple to string
        pascoejonathan = str(fetch[0][0])

                                #fetches skillid for kattan chris
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Kattan' AND EmpFName = 'Chris'")
        fetch = cursor.fetchall()
        #tuple to string
        kattanchris = str(fetch[0][0])

                                #fetches skillid for batts melissa
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Batts' AND EmpFName = 'Melissa'")
        fetch = cursor.fetchall()
        #tuple to string
        battsmelissa = str(fetch[0][0])

                                #fetches skillid for rogers adam
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Rogers' AND EmpFName = 'Adam'")
        fetch = cursor.fetchall()
        #tuple to string
        rogersadam = str(fetch[0][0])

                                        #fetches skillid for leslie cope
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Leslie' AND EmpFName = 'Cope'")
        fetch = cursor.fetchall()
        #tuple to string
        lesliecope = str(fetch[0][0])

                                        #fetches bible hanah
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Bible' AND EmpFName = 'Hanah'")
        fetch = cursor.fetchall()
        #tuple to string
        biblehanah = str(fetch[0][0])

                                                #fetches newton christopher
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Newton' AND EmpFName = 'Christopher'")
        fetch = cursor.fetchall()
        #tuple to string
        newtonchristopher = str(fetch[0][0])

                                                #fetches duarte miriam
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Duarte' AND EmpFName = 'Miriam'")
        fetch = cursor.fetchall()
        #tuple to string
        duartemiriam = str(fetch[0][0])

                                                #fetches bender larry
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Bender' AND EmpFName = 'Larry'")
        fetch = cursor.fetchall()
        #tuple to string
        benderlarry = str(fetch[0][0])

                                                #fetches paine brad
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Paine' OR EmpFName = 'Brad'")
        fetch = cursor.fetchall()
        #tuple to string
        painebrad = str(fetch[0][0])

                                                #fetches mudd roger
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Mudd' AND EmpFName = 'Roger'")
        fetch = cursor.fetchall()
        #tuple to string
        muddroger = str(fetch[0][0])

                                                #fetches kenyon tiffany
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Kenyon' AND EmpFName = 'Tiffany'")
        fetch = cursor.fetchall()
        #tuple to string
        kenyontiffany = str(fetch[0][0])

                                                #fetches chandler joseph
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Chandler' AND EmpFName = 'Joseph'")
        fetch = cursor.fetchall()
        #tuple to string
        chandlerjoseph = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + seatonamy + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + williamsjosh + "', '"  + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + underwoodtrish + "', '"  + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'data entry II'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + williamsjosh + "', '"  + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + seatonamy + "', '"  + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'systems analyst I'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + brettcraig + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + sewellbeth + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + robbinserin + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + bushemily + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + zebrassteve + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'systems analyst II'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + chandlerjoseph + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + burklowshane + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + robbinserin + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'database designer I'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + yarbroughpeter + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + smithmary + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'database designer II'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + yarbroughpeter + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + pascoejonathan + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'Cobol I'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + kattanchris + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + ephanorvictor + "', '" + skill + "')")
        cursor.execute(empskills)

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + summeranna + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + ellismaria + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'Cobol II'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + kattanchris + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + ephanorvictor + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + battsmelissa + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'C++ I'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + smithjose + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + rogersadam + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + lesliecope + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'C++ II'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + rogersadam + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + biblehanah + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'VB I'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + zebrassteve + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + ellismaria + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'VB II'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + zebrassteve + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + newtonchristopher + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ColdFusion I'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + duartemiriam + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + bushemily + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ColdFusion II'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + bushemily + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + newtonchristopher + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ASP I'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + duartemiriam + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + bushemily + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ASP II'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + duartemiriam + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + newtonchristopher + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'Oracle DBA'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + smithjose + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + pascoejonathan + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'MS SQL Server DBA'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + yarbroughpeter + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + smithjose + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'network engineer I'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + bushemily + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + smithmary + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'network engineer II'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + bushemily + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + smithmary + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'web administrator'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + bushemily + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + smithmary + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + newtonchristopher + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'technical writer'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + kilbysurgena + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + benderlarry + "', '" + skill + "')")
        cursor.execute(empskills)

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'project manager'")
        fetch = cursor.fetchall()
        #tuple to string
        skill = str(fetch[0][0])

        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + painebrad + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + muddroger + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + kenyontiffany + "', '" + skill + "')")
        cursor.execute(empskills)
        empskills = ("INSERT IGNORE INTO employee_skills(EmpID,SkillID) VALUES ('" + connorsean + "', '" + skill + "')")
        cursor.execute(empskills)

        self.conn.commit()
        cursor.close()

    def populate_customer(self):

        cursor = self.conn.cursor()

        #creates customer to use for Project 1
		
		#queries the NW region's id for the insert
        cursor.execute("SELECT RegionID FROM region WHERE RegionName = 'NW'")
        fetch = cursor.fetchall()
        region = str(fetch[0][0])

        customer = ("INSERT IGNORE INTO customer(CustID,CustName,CustPhone,RegID) VALUES(101,'Bob Dylan','123-567-9111','" + region + "')")
        cursor.execute(customer)

        self.conn.commit()
        cursor.close()

    def populate_project(self):

        cursor = self.conn.cursor()

        #queries the custid for insert
        cursor.execute("SELECT CustID FROM customer WHERE CustName = 'Bob Dylan'")
        fetch = cursor.fetchall()
        #tuple to string
        customer = str(fetch[0][0])

        #queries the empid
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Connor'")
        fetch = cursor.fetchall()
        #tuple to string
        employee = str(fetch[0][0])
        

        #creates project 1
        project = ("INSERT IGNORE INTO project(ProjDescrip,ProjEstBudget,ProjEstEndDate,ProjEstStartDate,ProjActualStartDate,CustID,EmpID) VALUES('Sales Management System','15500.00','2014-07-01','2014-02-12','2014-03-01','" + customer + "', '" + employee + "')")
        cursor.execute(project)

        self.conn.commit()
        cursor.close()

    def populate_tasks(self):

        cursor = self.conn.cursor()

        #queries the projid
        cursor.execute("SELECT ProjID FROM project WHERE ProjDescrip = 'Sales Management System'")
        fetch = cursor.fetchall()
        #tuple to string
        projid = str(fetch[0][0])

        #creates tasks

        #1
        task = ("INSERT IGNORE INTO task (TaskID, TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('1', 'Initial Interview','2014-03-01', '2014-03-06', '" + projid + "')")
        cursor.execute(task)

        #2
        task = ("INSERT IGNORE INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('Database Design','2014-03-11', '2014-03-15', '" + projid + "')")
        cursor.execute(task)

        #3
        task = ("INSERT IGNORE INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('System Design','2014-03-11', '2014-04-12', '" + projid + "')")
        cursor.execute(task)

        #4
        task = ("INSERT IGNORE INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('Database Implementation','2014-03-18', '2014-03-22', '" + projid + "')")
        cursor.execute(task)

        #5
        task = ("INSERT IGNORE INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('System Coding & Testing','2014-03-25', '2014-06-07', '" + projid + "')")
        cursor.execute(task)

        #6
        task = ("INSERT IGNORE INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('System Documentation','2014-03-25', '2014-06-07', '" + projid + "')")
        cursor.execute(task)

        #7
        task = ("INSERT IGNORE INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('Final Evaluation','2014-06-10', '2014-06-14', '" + projid + "')")
        cursor.execute(task)

        #8
        task = ("INSERT IGNORE INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('On-Site System Online and Data Loading','2014-06-17', '2014-06-21', '" + projid + "')")
        cursor.execute(task)

        #9
        task = ("INSERT IGNORE INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('Sign-Off','2014-07-01', '2014-07-01', '" + projid + "')")
        cursor.execute(task)

        self.conn.commit()
        cursor.close()

    def map_taskskills(self):

        cursor = self.conn.cursor()

        #creates task to skills mappings

        #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'Initial Interview'")
        fetch = cursor.fetchall()
        #tuple to string
        task1 = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'Database Design'")
        fetch = cursor.fetchall()
        #tuple to string
        task2 = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'System Design'")
        fetch = cursor.fetchall()
        #tuple to string
        task3 = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'Database Implementation'")
        fetch = cursor.fetchall()
        #tuple to string
        task4 = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'System Coding & Testing'")
        fetch = cursor.fetchall()
        #tuple to string
        task5 = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'System Documentation'")
        fetch = cursor.fetchall()
        #tuple to string
        task6 = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'Final Evaluation'")
        fetch = cursor.fetchall()
        #tuple to string
        task7 = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'On-Site System Online and Data Loading'")
        fetch = cursor.fetchall()
        #tuple to string
        task8 = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'Sign-Off'")
        fetch = cursor.fetchall()
        #tuple to string
        task9 = str(fetch[0][0])

        #fetches skillid for data entry i
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'data entry I'")
        fetch = cursor.fetchall()
        #tuple to string
        dataentry1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'data entry II'")
        fetch = cursor.fetchall()
        #tuple to string
        dataentry2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'systems analyst I'")
        fetch = cursor.fetchall()
        #tuple to string
        systemsanalyst1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'systems analyst II'")
        fetch = cursor.fetchall()
        #tuple to string
        systemsanalyst2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'database designer I'")
        fetch = cursor.fetchall()
        #tuple to string
        dbdesigner1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'database designer II'")
        fetch = cursor.fetchall()
        #tuple to string
        dbdesigner2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'Cobol I'")
        fetch = cursor.fetchall()
        #tuple to string
        cobol1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'Cobol II'")
        fetch = cursor.fetchall()
        #tuple to string
        cobol2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'C++ I'")
        fetch = cursor.fetchall()
        #tuple to string
        cplus1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'C++ II'")
        fetch = cursor.fetchall()
        #tuple to string
        cplus2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'VB I'")
        fetch = cursor.fetchall()
        #tuple to string
        vb1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'VB II'")
        fetch = cursor.fetchall()
        #tuple to string
        vb2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ColdFusion I'")
        fetch = cursor.fetchall()
        #tuple to string
        coldfusion1 = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ColdFusion II'")
        fetch = cursor.fetchall()
        #tuple to string
        coldfusion2 = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ASP I'")
        fetch = cursor.fetchall()
        #tuple to string
        asp1 = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ASP II'")
        fetch = cursor.fetchall()
        #tuple to string
        asp2 = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'Oracle DBA'")
        fetch = cursor.fetchall()
        #tuple to string
        oracledba = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'MS SQL Server DBA'")
        fetch = cursor.fetchall()
        #tuple to string
        sqlserverdba = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'network engineer I'")
        fetch = cursor.fetchall()
        #tuple to string
        networkengineer1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'network engineer II'")
        fetch = cursor.fetchall()
        #tuple to string
        networkengineer2 = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'web administrator'")
        fetch = cursor.fetchall()
        #tuple to string
        webadmin = str(fetch[0][0])
        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'technical writer'")
        fetch = cursor.fetchall()
        #tuple to string
        techwriter = str(fetch[0][0])

        #queries project manager
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'project manager'")
        fetch = cursor.fetchall()
        #tuple to string
        projectmanager = str(fetch[0][0])

        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + projectmanager + "','" + task1 + "','1')")
        cursor.execute(taskskill)
        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + systemsanalyst2 + "','" + task1 + "','1')")
        cursor.execute(taskskill)
        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + dbdesigner1 + "','" + task1 + "','1')")
        cursor.execute(taskskill)

        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + dbdesigner1 + "','" + task2 + "','1')")
        cursor.execute(taskskill)

        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + systemsanalyst2 + "','" + task3 + "','1')")
        cursor.execute(taskskill)
        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + systemsanalyst1 + "','" + task3 + "','2')")
        cursor.execute(taskskill)

        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + oracledba + "','" + task4 + "','1')")
        cursor.execute(taskskill)

        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + cobol1 + "','" + task5 + "','2')")
        cursor.execute(taskskill)
        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + cobol2 + "','" + task5 + "','1')")
        cursor.execute(taskskill)
        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + oracledba + "','" + task5 + "','1')")
        cursor.execute(taskskill)

        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + techwriter + "','" + task6 + "','1')")
        cursor.execute(taskskill)

        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + projectmanager + "','" + task7 + "','1')")
        cursor.execute(taskskill)
        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + systemsanalyst2 + "','" + task7 + "','1')")
        cursor.execute(taskskill)
        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + dbdesigner1 + "','" + task7 + "','1')")
        cursor.execute(taskskill)
        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + cobol2 + "','" + task7 + "','1')")
        cursor.execute(taskskill)

        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + projectmanager + "','" + task8 + "','1')")
        cursor.execute(taskskill)
        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + systemsanalyst2 + "','" + task8 + "','1')")
        cursor.execute(taskskill)
        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + dbdesigner1 + "','" + task8 + "','1')")
        cursor.execute(taskskill)
        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + cobol2 + "','" + task8 + "','1')")
        cursor.execute(taskskill)

        taskskill = ("INSERT IGNORE INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('" + projectmanager + "','" + task9 + "','1')")
        cursor.execute(taskskill)

        self.conn.commit()
        cursor.close()

    def populate_assignment(self):
        
        cursor = self.conn.cursor()

        # creates assignment entries

        #fetches skillid for data entry i
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'data entry I'")
        skill = cursor.fetchall()
        #tuple to string
        skill = str(skill[0][0])

        #fetches skillid for connor sean
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Connor' AND EmpFName = 'Sean'")
        fetch = cursor.fetchall()
        #tuple to string
        connorsean = str(fetch[0][0])

        #fetches skillid for burklow shane
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Burklow' AND EmpFName = 'Shane'")
        fetch = cursor.fetchall()
        #tuple to string
        burklowshane = str(fetch[0][0])

                #fetches skillid for smith mary
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Smith' AND EmpFName = 'Mary'")
        fetch = cursor.fetchall()
        #tuple to string
        smithmary = str(fetch[0][0])

                #fetches skillid for bush emily
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Bush' AND EmpFName = 'Emily'")
        fetch = cursor.fetchall()
        #tuple to string
        bushemily = str(fetch[0][0])

                #fetches skillid for zebras steve
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Zebras' AND EmpFName = 'Steve'")
        fetch = cursor.fetchall()
        #tuple to string
        zebrassteve = str(fetch[0][0])

                #fetches skillid for smith jose
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Smith' AND EmpFName = 'Jose'")
        fetch = cursor.fetchall()
        #tuple to string
        smithjose = str(fetch[0][0])

                        #fetches skillid for summers anna
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Summers' AND EmpFName = 'Anna'")
        fetch = cursor.fetchall()
        #tuple to string
        summeranna = str(fetch[0][0])

                        #fetches skillid for ellis maria
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Ellis' AND EmpFName = 'Maria'")
        fetch = cursor.fetchall()
        #tuple to string
        ellismaria = str(fetch[0][0])

                                #fetches skillid for ephanor victor
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Ephanor' AND EmpFName = 'Victor'")
        fetch = cursor.fetchall()
        #tuple to string
        ephanorvictor = str(fetch[0][0])

                                #fetches skillid for kilby surgena
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Kilby' AND EmpFName = 'Surgena'")
        fetch = cursor.fetchall()
        #tuple to string
        kilbysurgena = str(fetch[0][0])

                        #fetches skillid for seaton amy
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Seaton' AND EmpFName = 'Amy'")
        fetch = cursor.fetchall()
        #tuple to string
        seatonamy = str(fetch[0][0])

                        #fetches skillid for williams josh
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Williams' AND EmpFName = 'Josh'")
        fetch = cursor.fetchall()
        #tuple to string
        williamsjosh = str(fetch[0][0])

                                #fetches skillid for underwood trish
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Underwood' AND EmpFName = 'Trish'")
        fetch = cursor.fetchall()
        #tuple to string
        underwoodtrish = str(fetch[0][0])

                                #fetches skillid for brett craig
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Brett' AND EmpFName = 'Craig'")
        fetch = cursor.fetchall()
        #tuple to string
        brettcraig = str(fetch[0][0])

                                #fetches skillid for sewell beth
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Sewell' AND EmpFName = 'Beth'")
        fetch = cursor.fetchall()
        #tuple to string
        sewellbeth = str(fetch[0][0])

                                #fetches skillid for robbins erin
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Robbins' AND EmpFName = 'Erin'")
        fetch = cursor.fetchall()
        #tuple to string
        robbinserin = str(fetch[0][0])

                                #fetches skillid for yarbrough peter
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Yarbrough' AND EmpFName = 'Peter'")
        fetch = cursor.fetchall()
        #tuple to string
        yarbroughpeter = str(fetch[0][0])

                                #fetches skillid for pascoe jonathan
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Pascoe' AND EmpFName = 'Jonathan'")
        fetch = cursor.fetchall()
        #tuple to string
        pascoejonathan = str(fetch[0][0])

                                #fetches skillid for kattan chris
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Kattan' AND EmpFName = 'Chris'")
        fetch = cursor.fetchall()
        #tuple to string
        kattanchris = str(fetch[0][0])

                                #fetches skillid for batts melissa
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Batts' AND EmpFName = 'Melissa'")
        fetch = cursor.fetchall()
        #tuple to string
        battsmelissa = str(fetch[0][0])

                                #fetches skillid for rogers adam
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Rogers' AND EmpFName = 'Adam'")
        fetch = cursor.fetchall()
        #tuple to string
        rogersadam = str(fetch[0][0])

                                        #fetches skillid for leslie cope
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Leslie' AND EmpFName = 'Cope'")
        fetch = cursor.fetchall()
        #tuple to string
        lesliecope = str(fetch[0][0])

                                        #fetches bible hanah
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Bible' AND EmpFName = 'Hanah'")
        fetch = cursor.fetchall()
        #tuple to string
        biblehanah = str(fetch[0][0])

                                                #fetches newton christopher
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Newton' AND EmpFName = 'Christopher'")
        fetch = cursor.fetchall()
        #tuple to string
        newtonchristopher = str(fetch[0][0])

                                                #fetches duarte miriam
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Duarte' AND EmpFName = 'Miriam'")
        fetch = cursor.fetchall()
        #tuple to string
        duartemiriam = str(fetch[0][0])

                                                #fetches bender larry
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Bender' AND EmpFName = 'Larry'")
        fetch = cursor.fetchall()
        #tuple to string
        benderlarry = str(fetch[0][0])

                                                #fetches paine brad
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Paine' OR EmpFName = 'Brad'")
        fetch = cursor.fetchall()
        #tuple to string
        painebrad = str(fetch[0][0])

                                                #fetches mudd roger
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Mudd' AND EmpFName = 'Roger'")
        fetch = cursor.fetchall()
        #tuple to string
        muddroger = str(fetch[0][0])

                                                #fetches kenyon tiffany
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Kenyon' AND EmpFName = 'Tiffany'")
        fetch = cursor.fetchall()
        #tuple to string
        kenyontiffany = str(fetch[0][0])

                                                #fetches chandler joseph
        cursor.execute("SELECT EmpID FROM employee WHERE EmpLName = 'Chandler' AND EmpFName = 'Joseph'")
        fetch = cursor.fetchall()
        #tuple to string
        chandlerjoseph = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'Initial Interview'")
        fetch = cursor.fetchall()
        #tuple to string
        initialinterview = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'Database Design'")
        fetch = cursor.fetchall()
        #tuple to string
        databasedesign = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'System Design'")
        fetch = cursor.fetchall()
        #tuple to string
        systemdesign = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'Database Implementation'")
        fetch = cursor.fetchall()
        #tuple to string
        databaseimplementation = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'System Coding & Testing'")
        fetch = cursor.fetchall()
        #tuple to string
        systemcodingandtesting = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'System Documentation'")
        fetch = cursor.fetchall()
        #tuple to string
        systemdocumentation = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'Final Evaluation'")
        fetch = cursor.fetchall()
        #tuple to string
        finalevaluation = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'On-Site System Online and Data Loading'")
        fetch = cursor.fetchall()
        #tuple to string
        onsite = str(fetch[0][0])

                #queries task
        cursor.execute("SELECT TaskID FROM task WHERE TaskDescrip = 'Sign-Off'")
        fetch = cursor.fetchall()
        #tuple to string
        signoff = str(fetch[0][0])

        #fetches skillid for data entry i
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'data entry I'")
        fetch = cursor.fetchall()
        #tuple to string
        dataentry1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'data entry II'")
        fetch = cursor.fetchall()
        #tuple to string
        dataentry2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'systems analyst I'")
        fetch = cursor.fetchall()
        #tuple to string
        systemsanalyst1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'systems analyst II'")
        fetch = cursor.fetchall()
        #tuple to string
        systemsanalyst2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'database designer I'")
        fetch = cursor.fetchall()
        #tuple to string
        dbdesigner1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'database designer II'")
        fetch = cursor.fetchall()
        #tuple to string
        dbdesigner2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'Cobol I'")
        fetch = cursor.fetchall()
        #tuple to string
        cobol1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'Cobol II'")
        fetch = cursor.fetchall()
        #tuple to string
        cobol2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'C++ I'")
        fetch = cursor.fetchall()
        #tuple to string
        cplus1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'C++ II'")
        fetch = cursor.fetchall()
        #tuple to string
        cplus2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'VB I'")
        fetch = cursor.fetchall()
        #tuple to string
        vb1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'VB II'")
        fetch = cursor.fetchall()
        #tuple to string
        vb2 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ColdFusion I'")
        fetch = cursor.fetchall()
        #tuple to string
        coldfusion1 = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ColdFusion II'")
        fetch = cursor.fetchall()
        #tuple to string
        coldfusion2 = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ASP I'")
        fetch = cursor.fetchall()
        #tuple to string
        asp1 = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'ASP II'")
        fetch = cursor.fetchall()
        #tuple to string
        asp2 = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'Oracle DBA'")
        fetch = cursor.fetchall()
        #tuple to string
        oracledba = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'MS SQL Server DBA'")
        fetch = cursor.fetchall()
        #tuple to string
        sqlserverdba = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'network engineer I'")
        fetch = cursor.fetchall()
        #tuple to string
        networkengineer1 = str(fetch[0][0])

        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'network engineer II'")
        fetch = cursor.fetchall()
        #tuple to string
        networkengineer2 = str(fetch[0][0])

        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'web administrator'")
        fetch = cursor.fetchall()
        #tuple to string
        webadmin = str(fetch[0][0])
        
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'technical writer'")
        fetch = cursor.fetchall()
        #tuple to string
        techwriter = str(fetch[0][0])

        #queries project manager
        cursor.execute("SELECT SkillID FROM skill WHERE SkillDescrip = 'project manager'")
        fetch = cursor.fetchall()
        #tuple to string
        projectmanager = str(fetch[0][0])

        #fetches taskskill 1
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + projectmanager + "' AND TaskID = '" + initialinterview + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts1 = str(fetch[0][0])

        #fetches taskskill 2
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + systemsanalyst2 + "' AND TaskID = '" + initialinterview + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts2 = str(fetch[0][0])

        #fetches taskskill 3
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + dbdesigner1 + "' AND TaskID = '" + initialinterview + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts3 = str(fetch[0][0])

        #fetches taskskill 4
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + dbdesigner1 + "' AND TaskID = '" + databasedesign + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts4 = str(fetch[0][0])

                #fetches taskskill 5
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + systemsanalyst2 + "' AND TaskID = '" + systemdesign + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts5 = str(fetch[0][0])

                #fetches taskskill 6
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + systemsanalyst1 + "' AND TaskID = '" + systemdesign + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts6 = str(fetch[0][0])

                        #fetches taskskill 7
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + systemsanalyst1 + "' AND TaskID = '" + systemdesign + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts7 = str(fetch[0][0])

                                #fetches taskskill 8
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + oracledba + "' AND TaskID = '" + databaseimplementation + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts8 = str(fetch[0][0])

                                        #fetches taskskill 9
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + cobol1 + "' AND TaskID = '" + systemcodingandtesting + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts9 = str(fetch[0][0])

                                        #fetches taskskill 10
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + cobol1 + "' AND TaskID = '" + systemcodingandtesting + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts10 = str(fetch[0][0])

                                                #fetches taskskill 11
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + cobol2 + "' AND TaskID = '" + systemcodingandtesting + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts11 = str(fetch[0][0])

                                                        #fetches taskskill 12
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + oracledba + "' AND TaskID = '" + systemcodingandtesting + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts12 = str(fetch[0][0])

                                                        #fetches taskskill 13
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + techwriter + "' AND TaskID = '" + systemdocumentation + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts13 = str(fetch[0][0])

                                                                #fetches taskskill 14
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + projectmanager + "' AND TaskID = '" + finalevaluation + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts14 = str(fetch[0][0])

                                                                #fetches taskskill 15
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + systemsanalyst2 + "' AND TaskID = '" + finalevaluation + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts15 = str(fetch[0][0])

                                                                #fetches taskskill 16
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + dbdesigner1 + "' AND TaskID = '" + finalevaluation + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts16 = str(fetch[0][0])

                                                                #fetches taskskill 17
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + cobol2 + "' AND TaskID = '" + finalevaluation + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts17 = str(fetch[0][0])

                                                                #fetches taskskill 18
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + projectmanager + "' AND TaskID = '" + onsite + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts18 = str(fetch[0][0])

                                                                #fetches taskskill 19
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + systemsanalyst2 + "' AND TaskID = '" + onsite + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts19 = str(fetch[0][0])

                                                                #fetches taskskill 20
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + dbdesigner1 + "' AND TaskID = '" + onsite + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts20 = str(fetch[0][0])

                                                                #fetches taskskill 21
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + cobol2 + "' AND TaskID = '" + onsite + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts21 = str(fetch[0][0])

                                                                        #fetches taskskill 22
        cursor.execute("SELECT TaskSkillID FROM task_skill WHERE SkillID = '" + projectmanager + "' AND TaskID = '" + signoff + "'")
        fetch = cursor.fetchall()
        #tuple to string
        ts22 = str(fetch[0][0])

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, AssignEnd, EmpID, TaskSkillID) VALUES ('2014-03-01','2014-03-06','" + connorsean + "','" + ts1 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, AssignEnd, EmpID, TaskSkillID) VALUES ('2014-03-01','2014-03-06','" + connorsean + "','" + ts2 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, AssignEnd, EmpID, TaskSkillID) VALUES ('2014-03-01','2014-03-06','" + smithmary + "','" + ts3 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, AssignEnd, EmpID, TaskSkillID) VALUES ('2014-03-11','2014-03-14','" + smithmary + "','" + ts4 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-11','" + burklowshane + "','" + ts5 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-11','" + bushemily + "','" + ts6 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-11','" + zebrassteve + "','" + ts7 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, AssignEnd, EmpID, TaskSkillID) VALUES ('2014-03-15','2014-03-19','" + smithjose + "','" + ts8 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-21','" + summeranna + "','" + ts9 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-21','" + ellismaria + "','" + ts10 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-21','" + ephanorvictor + "','" + ts11 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-21','" + smithjose + "','" + ts12 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(AssignBegin, EmpID, TaskSkillID) VALUES ('2014-03-25','" + kilbysurgena + "','" + ts13 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(TaskSkillID) VALUES ('" + ts14 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(TaskSkillID) VALUES ('" + ts15 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(TaskSkillID) VALUES ('" + ts16 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(TaskSkillID) VALUES ('" + ts17 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(TaskSkillID) VALUES ('" + ts18 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(TaskSkillID) VALUES ('" + ts19 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(TaskSkillID) VALUES ('" + ts20 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(TaskSkillID) VALUES ('" + ts21 + "')")
        cursor.execute(assignment)

        assignment = ("INSERT IGNORE INTO assignment(TaskSkillID) VALUES ('" + ts22 + "')")
        cursor.execute(assignment)

        self.conn.commit()
        cursor.close()

    def populate_bills(self):

        cursor = self.conn.cursor()

        #queries the projid
        cursor.execute("SELECT ProjID FROM project WHERE ProjDescrip = 'Sales Management System'")
        fetch = cursor.fetchall()
        #tuple to string
        projid = str(fetch[0][0])

        #creates bills to be used in worklog table & bill table

        bill = ( "INSERT IGNORE INTO bill(BillID, BillDate, ProjID) VALUES( 101, '2014-03-15', '" + projid + "')")
        cursor.execute(bill)

        bill = ( "INSERT IGNORE INTO bill(BillDate, ProjID) VALUES('2014-03-22', '" + projid + "')")
        cursor.execute(bill)
        
        self.conn.commit()
        cursor.close()
    
    def populate_worklog(self):

        cursor = self.conn.cursor()

        #creates worklogs
        #creates worklogs
        select = ("select BillID from bill where bill.BillDate = '2014-03-15'")
        cursor.execute(select)
        b1 = cursor.fetchall()

        select = ("select BillID from bill where bill.BillDate = '2014-03-22'")
        cursor.execute(select)
        b2 = cursor.fetchall()

        select = ( "select AssignID from assignment order by AssignID asc" )
        cursor.execute(select)
        a = []
        results = cursor.fetchall()
        a.append(0)
        for entry in results:
            a.append(entry[0])

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-01', '4', '"+str(a[2])+"', '"+str(b1[0][0])+"' )")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-01', '4', '"+str(a[1])+"', '"+str(b1[0][0])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-01', '4', '"+str(a[3])+"', '"+str(b1[0][0])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-08', '24', '"+str(a[2])+"', '"+str(b1[0][0])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-08', '24', '"+str(a[1])+"', '"+str(b1[0][0])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-08', '24', '"+str(a[3])+"', '"+str(b1[0][0])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-15', '40', '"+str(a[5])+"', '"+str(b2[0][0])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-15', '40', '"+str(a[6])+"', '"+str(b2[0][0])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-15', '6', '"+str(a[8])+"', '"+str(b2[0][0])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-15', '32', '"+str(a[4])+"', '"+str(b2[0][0])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID, BillID ) VALUES('2014-03-15', '35', '"+str(a[7])+"', '"+str(b2[0][0])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '40', '"+str(a[5])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '40', '"+str(a[6])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '12', '"+str(a[10])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '12', '"+str(a[11])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '12', '"+str(a[8])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '12', '"+str(a[12])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '12', '"+str(a[9])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-22', '35', '"+str(a[7])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '40', '"+str(a[5])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '40', '"+str(a[6])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '35', '"+str(a[10])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '35', '"+str(a[11])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '40', '"+str(a[13])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '35', '"+str(a[12])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '35', '"+str(a[9])+"')")
        cursor.execute(work_log)

        work_log = ("INSERT IGNORE INTO worklog( WorkLogWeekEnding, WorkLogHrsWorked, AssignID ) VALUES('2014-03-29', '35', '"+str(a[7])+"')")
        cursor.execute(work_log)

        self.conn.commit()
        cursor.close()

    def insert_seed_data(self):

        self.create_tables()
        self.populate_region()
        self.populate_skill()
        self.populate_employee()
        self.map_empskills()
        self.populate_customer()
        self.populate_project()
        self.populate_tasks()
        self.map_taskskills()
        self.populate_assignment()
        self.populate_bills()
        self.populate_worklog()


        



