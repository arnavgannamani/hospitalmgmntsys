SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `HospitalManagement` ;
CREATE SCHEMA IF NOT EXISTS `HospitalManagement` DEFAULT CHARACTER SET latin1 ;
USE `HostpitalManagement` ;

-- -----------------------------------------------------
-- Table `northwind`.`customers`
-- -----------------------------------------------------
CREATE TABLE Person (
    personID INT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    insurance INT,
    tel_number VARCHAR(20)
    FOREIGN KEY insurance REFERENCES insurance(insuranceID)
);

CREATE TABLE Patient (
    patientID INT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    gender ENUM('Male', 'Female', 'Other'),
    tel_number VARCHAR(20),
    email VARCHAR(255),
    inxsurance VARCHAR(255),
    emergencyContact INT
);

CREATE TABLE ChildPatient (
    patientID INT PRIMARY KEY,
    guardian VARCHAR(255),
    pediatrician VARCHAR(255),
    FOREIGN KEY (patientID) REFERENCES Patient(patientID)
);

CREATE TABLE Faculty (
    employeeID INT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    role VARCHAR(255),
    tel_number VARCHAR(20),
    department VARCHAR(255)
);

CREATE Table Doctor (
    employeeID INT Primary Key,
    specialty VARCHAR(255),
    FOREIGN KEY (employeeID) REFERENCES Faculty(employeeID)
);

CREATE TABLE Appointment (
    apptID INT PRIMARY KEY ,
    date DATE,
    pid INT,
    doctorID INT,
    FOREIGN KEY (pid) REFERENCES Person(personID),
    FOREIGN KEY (doctorID) REFERENCES Doctor(employeeID)
);

CREATE TABLE Shift (
    shiftID INT PRIMARY KEY,
    date DATE,
    time TIME,
    employeeID INT,
    FOREIGN KEY (employeeID) REFERENCES Faculty(employeeID)
);

CREATE TABLE Exam (
    examID INT PRIMARY KEY,
    cost VARCHAR(255),
    examType VARCHAR(255)
);

CREATE TABLE ExamResult (
    examResultID INT PRIMARY KEY,
    examID INT,
    date DATE,
    pid INT,
    doctorID INT,
    result VARCHAR(255),
    FOREIGN KEY (examID) REFERENCES Exam(examID),
    FOREIGN KEY (pid) REFERENCES Patient(patientID),
    FOREIGN KEY (doctorID) REFERENCES Faculty(employeeID)
);

CREATE TABLE Department (
    departmentID INT PRIMARY KEY,
    departmentName VARCHAR(255),
    supervisor INT,
    FOREIGN KEY (supervisor) REFERENCES Faculty(employeeID)
);

CREATE TABLE Bill (
    billID INT PRIMARY KEY,
    patientID INT,
    appointmentID INT,
    cost DECIMAL(10, 2),
    FOREIGN KEY (patientID) REFERENCES Patient(patientID),
    FOREIGN KEY (appointmentID) REFERENCES Appointment(apptID)
);

CREATE TABLE Insurance (
    insuranceID INT PRIMARY KEY,
    insuranceName VARCHAR(255),
    percentagePaid VARCHAR(255)
);

CREATE TABLE Item (
    itemID INT PRIMARY KEY,
    itemName VARCHAR(255)
);

CREATE TABLE DepartmentItem (
    itemID INT,
    departmentID INT,
    requiredAmount INT,
    inStock INT,
    FOREIGN KEY (itemID) REFERENCES Item(itemID),
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID)
);

CREATE TABLE DepartmentFinancials (
    departmentFinancialsID INT AUTO_INCREMENT PRIMARY KEY,
    departmentID INT,
    budget DECIMAL(10, 2),
    expenditures DECIMAL(10, 2),
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID)
);
ALTER TABLE ChildPatient DROP FOREIGN KEY FK_ChildPatient_Patient;
ALTER TABLE ChildPatient ADD CONSTRAINT FK_ChildPatient_Patient FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Doctor DROP FOREIGN KEY doctor_ibfk_1;
ALTER TABLE Doctor ADD CONSTRAINT FK_Doctor_Faculty FOREIGN KEY (employeeID) REFERENCES Faculty(employeeID) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE Appointment DROP FOREIGN KEY appointment_ibfk_1;
ALTER TABLE Appointment ADD CONSTRAINT FK_Appointment_Person FOREIGN KEY (pid) REFERENCES Person(personID) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE Appointment DROP FOREIGN KEY appointment_ibfk_2;
ALTER TABLE Appointment ADD CONSTRAINT FK_Appointment_Doctor FOREIGN KEY (doctorID) REFERENCES Doctor(employeeID) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE ExamResult DROP FOREIGN KEY examresult_ibfk_1;
ALTER TABLE ExamResult ADD CONSTRAINT FK_ExamResult_Exam FOREIGN KEY (examID) REFERENCES Exam(examID) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE ExamResult DROP FOREIGN KEY examresult_ibfk_3;
ALTER TABLE ExamResult ADD CONSTRAINT FK_ExamResult_Doctor FOREIGN KEY (doctorID) REFERENCES Faculty(employeeID) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE DepartmentItem DROP FOREIGN KEY departmentitem_ibfk_1;
ALTER TABLE DepartmentItem ADD CONSTRAINT FK_DepartmentItem_Item FOREIGN KEY (itemID) REFERENCES Item(itemID) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE DepartmentItem DROP FOREIGN KEY departmentitem_ibfk_2;
ALTER TABLE DepartmentItem ADD CONSTRAINT FK_DepartmentItem_Department FOREIGN KEY (departmentID) REFERENCES Department(departmentID) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE DepartmentFinancials DROP FOREIGN KEY departmentfinancials_ibfk_1;
ALTER TABLE DepartmentFinancials ADD CONSTRAINT FK_DepartmentFinancials_Department FOREIGN KEY (departmentID) REFERENCES Department(departmentID) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Bill DROP FOREIGN KEY bill_ibfk_1;
ALTER TABLE Bill ADD CONSTRAINT FK_Bill_Patient FOREIGN KEY (patientID) REFERENCES Patient(patientID) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Bill DROP FOREIGN KEY bill_ibfk_2;
ALTER TABLE Bill ADD CONSTRAINT FK_Bill_Appointment FOREIGN KEY (appointmentID) REFERENCES Appointment(apptID) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE Person DROP FOREIGN KEY FK_Person_Insurance;
ALTER TABLE Person ADD CONSTRAINT FK_Person_Insurance FOREIGN KEY (insuranceID) REFERENCES Insurance(insuranceID) ON DELETE SET NULL ON UPDATE CASCADE;

