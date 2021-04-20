/*
CPSC 4620 Relational Schema Project
Joey Binz & Kenny Nguyen
3/9/2021
*/


create table region (
	RegionID int auto_increment NOT NULL unique,
    RegionName char(2) NOT NULLunique,
    primary key (RegionID)
    );
    
create table employee (
	EmpID int auto_increment unique NOT NULL,
    EmpLName varchar(20) NOT NULL,
    EmpMInit char(1),
    EmpFName varchar(20) NOT NULL,
    EmpHireDate date NOT NULL,
    RegID int NOT NULL,
    primary key (EmpID),
    foreign key (RegID) references region(RegionID)
    );
    
create table customer (
	CustID int auto_increment unique NOT NULL,
    CustName varchar(41) NOT NULL,
    CustPhone char(12),
    RegID int NOT NULL,
    primary key (CustID),
    foreign key (RegID) references region(RegionID)
    );
    
create table skill (
	SkillID int auto_increment NOT NULL unique,
    SkillDescrip varchar(255) NOT NULL unique,
    SkillPayRate decimal(10,2) NOT NULL,
    primary key (SkillID)
    );
    
create table employee_skills (
	EmpID int NOT NULL,
    SkillID int NOT NULL,
    primary key (EmpID, SkillID),
    foreign key (EmpID) references employee(EmpID),
    foreign key (SkillID) references skill(SkillID)
    );
    
create table project (
	ProjID int auto_increment unique NOT NULL,
    ProjDescrip varchar(255) NOT NULL,
    ProjEstBudget decimal(10,2) NOT NULL,
    ProjEstEndDate date NOT NULL,
	ProjEstStartDate date NOT NULL,
    ProjActualStartDate date null,
    ProjActualEndDate date null,
    ProjActualCost decimal(10,2) null,
    CustID int NOT NULL,
    EmpID int NOT NULL,
    primary key (ProjID),
    foreign key (CustID) references customer(CustID),
    foreign key (EmpID) references employee(EmpID)
    );
    
create table task (
	TaskID int auto_increment unique NOT NULL,
    TaskDescrip varchar(255) NOT NULL,
    TaskStartDate date,
    TaskEndDate date,
    ProjID int NOT NULL,
    primary key (TaskID),
    foreign key (ProjID) references project(ProjID)
    );
    
create table task_skill (
	TaskSkillID int auto_increment unique NOT NULL,
    SkillID int NOT NULL,
    TaskID int NOT NULL,
    TaskSkillQuant int NOT NULL,
    primary key (TaskSkillID),
    foreign key (SkillID) references skill(SkillID),
    foreign key (TaskID) references task(TaskID)
    );
    
create table assignment (
	AssignID int auto_increment unique NOT NULL,
    AssignBegin date,
    AssignEnd date,
    EmpID int NOT NULL,
    TaskSkillID int NOT NULL,
    primary key (AssignID),
	foreign key (EmpID) references employee(EmpID),
    foreign key (TaskSkillID) references task_skill(TaskSkillID)
    );
    
create table bill (
	BillID int auto_increment unique NOT NULL,
    BillDate date NOT NULL,
    ProjID int NOT NULL,
    primary key (BillID),
    foreign key (ProjID) references project(ProjID)
    );
    
create table worklog (
	WorkLogID int auto_increment unique NOT NULL,
    WorkLogWeekEnding date NOT NULL,
    WorkLogHrsWorked int,
    AssignID int NOT NULL,
    BillID int null,
    primary key (WorkLogID),
    foreign key (AssignID) references assignment(AssignID),
    foreign key (BillID) references bill(BillID)
    );

    

    
    

    
    