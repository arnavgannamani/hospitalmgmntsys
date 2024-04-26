
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

USE `HospitalManagement`;

insert into Exam (examID, examType, cost) values (1, 'Colonoscopy', 800);
insert into Exam (examID, examType, cost) values (2, 'X-Ray', 150);
insert into Exam (examID, examType, cost) values (3, 'Blood Test', 50);
insert into Exam (examID, examType, cost) values (4, 'ECG', 200);
insert into Exam (examID, examType, cost) values (5, 'MRI', 500);
insert into Exam (examID, examType, cost) values (6, 'Ultrasound', 1000);
