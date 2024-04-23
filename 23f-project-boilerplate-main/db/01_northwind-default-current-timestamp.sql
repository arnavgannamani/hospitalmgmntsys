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
    insurance VARCHAR(255),
    tel_number VARCHAR(20)
);

CREATE TABLE Patient (
    patientID INT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    gender ENUM('Male', 'Female', 'Other'),
    tel_number VARCHAR(20),
    email VARCHAR(255),
    insurance VARCHAR(255),
    emergencyContact VARCHAR(255)
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
