SELECT `assignment`.`AssignID`,
    `assignment`.`AssignBegin`,
    `assignment`.`AssignEnd`,
    `assignment`.`EmpID`,
    `assignment`.`TaskSkillID`
FROM `project2`.`assignment`;
SELECT `bill`.`BillID`,
    `bill`.`BillDate`,
    `bill`.`ProjID`
FROM `project2`.`bill`;
SELECT `customer`.`CustID`,
    `customer`.`CustName`,
    `customer`.`CustPhone`,
    `customer`.`RegID`
FROM `project2`.`customer`;
SELECT `employee`.`EmpID`,
    `employee`.`EmpLName`,
    `employee`.`EmpMInit`,
    `employee`.`EmpFName`,
    `employee`.`EmpHireDate`,
    `employee`.`RegID`
FROM `project2`.`employee`;
SELECT `empoyee_skills`.`EmpID`,
    `empoyee_skills`.`SkillID`
FROM `project2`.`empoyee_skills`;
SELECT `project`.`ProjID`,
    `project`.`ProjDescrip`,
    `project`.`ProjBudget`,
    `project`.`ProjEstEndDate`,
    `project`.`ProjEstStartDate`,
    `project`.`ProjActualStartDate`,
    `project`.`ProjActualEndDate`,
    `project`.`ProjActualCost`,
    `project`.`CustID`,
    `project`.`EmpID`
FROM `project2`.`project`;
SELECT `region`.`RegionID`,
    `region`.`RegionName`
FROM `project2`.`region`;
SELECT `skill`.`SkillID`,
    `skill`.`SkillDescrip`,
    `skill`.`SkillPayRate`
FROM `project2`.`skill`;
SELECT `task`.`TaskID`,
    `task`.`TaskDescrip`,
    `task`.`TaskStartDate`,
    `task`.`TaskEndDate`,
    `task`.`ProjID`
FROM `project2`.`task`;
SELECT `task_skill`.`TaskSkillID`,
    `task_skill`.`SkillID`,
    `task_skill`.`TaskID`,
    `task_skill`.`TaskSkillQuant`
FROM `project2`.`task_skill`;
SELECT `worklog`.`WorkLogID`,
    `worklog`.`WorkLogWeekEnding`,
    `worklog`.`WorkLogHrsWorked`,
    `worklog`.`AssignID`,
    `worklog`.`BillID`
FROM `project2`.`worklog`;
