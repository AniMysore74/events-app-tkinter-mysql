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

INSERT INTO Incharge values(1,'ABC',123),(2,'ABCDE',141423),(3,'ASda',17823),(4,'ATW',111423),(5,'PWE',5163);

INSERT INTO Location values(1,'Seminar Hall 1'),(2,'Seminar Hall 2'),(3,'Room 001'),(4,'Room 002'),(5,'Room 003');

INSERT INTO Speaker values(1,'QWERTY'),(2,'QWQWRTY'),(3,'QASDY'),(4,'QWRQWRY'),(5,'QWqrqrY'),(6,'asdasdTY'),(7,'QhyjTY'),(8,'cmancmY');

INSERT INTO Event values(1,'TedX',1,'2018-10-11 10:06:59',1),(2,'Ingenius',2,'2018-10-11 10:06:59',2),(3,'Kalpana',3,'2018-10-11 10:06:59',1),(4,'Maaya',3,'2018-10-11 10:06:59',2);
