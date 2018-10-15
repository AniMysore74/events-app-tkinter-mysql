CREATE DATABASE EVENTS;

USE EVENTS;

CREATE TABLE Incharge (
    InchargeId INT PRIMARY KEY,
    Name VARCHAR(30) NOT NULL,
    ContactNo INT NOT NULL
);

CREATE TABLE Location ( 
    PlaceId INT PRIMARY KEY,
    PlaceName VARCHAR(30) NOT NULL
);

CREATE TABLE Sponsor (
    SponsorId INT PRIMARY KEY,
    SponsorName VARCHAR(30) NOT NULL,
    Role VARCHAR(30) NOT NULL
);

CREATE TABLE Speaker ( 
    SpeakerId INT PRIMARY KEY,
    SpeakerName VARCHAR(30) NOT NULL
);

CREATE TABLE Event ( 
    EventId INT PRIMARY KEY,
    Name VARCHAR(30) NOT NULL,
    PlaceId INT NOT NULL,
    StartTime DateTime NOT NULL,
    InchargeId INT NOT NULL,
    CONSTRAINT fk1 FOREIGN KEY(PlaceId) REFERENCES Location(PlaceId),
    CONSTRAINT fk2 FOREIGN KEY(InchargeId) REFERENCES Incharge(InchargeId)
);

CREATE TABLE Talk (
    TalkId INT PRIMARY KEY,
    EventId INT NOT NULL,
    SpeakerId INT NOT NULL,
    StartTime DATETIME NOT NULL,
    Title VARCHAR(30) NOT NULL,
    CONSTRAINT fk3 FOREIGN KEY(EventId) REFERENCES Event(EventId),
    CONSTRAINT fk4 FOREIGN KEY(SpeakerId) REFERENCES Speaker(SpeakerId)
);

INSERT INTO Incharge values(1,'Sam',9732712213),(2,'Sarah',1414231123),(3,'John',1782323456),(4,'Alice',1119876423),(5,'Alex',5109327663);


INSERT INTO Location values(1,'Seminar Hall 1'),(2,'Seminar Hall 2'),(3,'Room 001'),(4,'Room 002'),(5,'Room 003');

INSERT INTO Speaker values(1,'Dr. Shyam'),(2,'Mr. Rohan'),(3,'Dr. Paul'),(4,'Mrs. Walker'),(5,'Dr. Shetty'),(6,'Mr. Chetan'),(7,'Mrs. Amanda'),(8,'Mr. Ramesh');

INSERT INTO Sponsor values(1,'TechSpecs','Platinum'),(2,'JetWorks','Silver'),(3.'Horizon','Gold');

INSERT INTO Event values(INSERT INTO `Event` VALUES (1,'TedX',3,'2019-01-22 10:00:00',2),(2,'Ingenius',1,'2018-10-30 08:30:00',4),(3,'Kalpana',1,'2019-02-15 09:00:00',1),(4,'Maaya',2,'2018-11-11 10:00:00',5);

