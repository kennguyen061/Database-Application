INSERT INTO region (RegionName) VALUES('NW');
INSERT INTO employee (EmpLName,EmpMInit,EmpFName,EmpHireDate,RegID) VALUES ('Nguyen','T','Kenny','2021-03-07','1');
INSERT INTO customer (CustName,CustPhone,RegID) VALUES ('John Doe', '864-999-999', '1');
INSERT INTO skill (SkillDescrip,SkillPayRate) VALUES ('Information Systems', '15.00');
INSERT INTO empoyee_skills(EmpID,SkillID) VALUES ('1', '1');
INSERT INTO project(ProjDescrip,ProjBudget,ProjEstEndDate,ProjEstStartDate,ProjActualStartDate,ProjActualEndDate,ProjActualCost,CustID,EmpID)
VALUES('Project 1','15000.00','2021-07-02','2021-03-07','2021-03-10','2021-08-10','18600.00','1','1');
INSERT INTO task (TaskDescrip,TaskStartDate,TaskEndDate,ProjID) VALUES ('Code stuff','2021-03-10', '2021-04-01', '1');
INSERT INTO task_skill (SkillID,TaskID,TaskSkillQuant) VALUES ('1','1','10');
INSERT INTO assignment (AssignBegin,AssignEnd,EmpID,TaskSkillID) VALUES ('2021-03-07', '2021-05-08', '1', '1');
INSERT INTO bill (BillDate,ProjID) VALUES ('2021-08-10', '1');
INSERT INTO worklog (WorkLogWeekEnding,WorkLogHrsWorked,AssignID,BillID) VALUES ('2021-03-13', '40', '1', '1');
