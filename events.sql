CREATE DATABASE Conference;

USE Conference;

CREATE TABLE Incharge (
    InchargeId INT PRIMARY KEY,
    InchargeName VARCHAR(30) NOT NULL,
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
    Name VARCHAR(60) NOT NULL,
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
    Title VARCHAR(60) NOT NULL,
    CONSTRAINT fk3 FOREIGN KEY(EventId) REFERENCES Event(EventId),
    CONSTRAINT fk4 FOREIGN KEY(SpeakerId) REFERENCES Speaker(SpeakerId)
);

CREATE TABLE Warning ( 
    EventId INT,
    StartTime DATETIME,
    PlaceId INT
);

DELIMITER ;;

CREATE PROCEDURE Warn (IN StartTime DATETIME, IN PlaceId INT, IN EventId INT )
BEGIN
INSERT INTO Warning values(EventId, StartTime, PlaceId);
END;;

DELIMITER ;

DELIMITER ;;

CREATE TRIGGER warn_same_place 
AFTER INSERT 
ON Event FOR EACH ROW
BEGIN
    IF NEW.StartTime IN ( SELECT StartTime from Event where PlaceId = NEW.PlaceId)
    THEN CALL WARN(NEW.StartTime, NEW.PlaceId, NEW.EventId);
    END IF; 
END ;;

DELIMITER ;

INSERT INTO Incharge values(1,'Gayatri',9732712213),(2,'Saakshi',9452003415),(3,'Ramesh',9872003415),(4,'Alice',8419876423),(5,'Aditya',7609327663);


INSERT INTO Location values(1,'Seminar Hall 1'),(2,'Seminar Hall 2'),(3,'Room 001'),(4,'Room 002'),(5,'Room 003');

INSERT INTO Speaker values(1,'Dr. Manikandan J '),(2,'Mrs. Divya Aggarwal '),(3,'Dr. Chintan Shah'),(4,'Mr.  Sunil Bhutada '),(5,'Dr. Shetty'),(6,'Mr. Chetan'),(7,'Mrs. Amanda'),(8,'Mr. Ramesh');

INSERT INTO Sponsor values(1,'Cisco','Platinum Sponsor'),(2,'LAM Research','Gold Sponsor'),(3,'Cambridge University Press','Silver Sponsor'),(4,'Springer','Research Sponsor');

INSERT INTO Event VALUES (1,'TedX',3,'2019-01-22 10:00:00',2),(2,'Ingenius',1,'2018-10-30 08:30:00',4),(3,'Kalpana',1,'2019-02-15 09:00:00',1),(4,'Maaya',2,'2018-11-11 10:00:00',5);
INSERT INTO Event values(INSERT INTO `Event` VALUES (1,'Computer Vision and the Internet (VisionNet'18)',3,'2019-01-22 10:00:00',2),(2,'Natural Language Processing (NLP'18)',1,'2018-10-30 08:30:00',4),(3,'Artificial Intelligence',1,'2019-02-15 09:00:00',1),(4,'Machine Learning/Data Engineering',2,'2018-11-11 10:00:00',5);

INSERT INTO Event values(INSERT INTO `Event` VALUES (1,'Computer Vision and the Internet (VisionNet'18)',3,'2019-01-22 10:00:00',2),(2,'Natural Language Processing (NLP'18)',1,'2018-10-30 08:30:00',4),(3,'Artificial Intelligence',1,'2019-02-15 09:00:00',1),(4,'Machine Learning/Data Engineering',2,'2018-11-11 10:00:00',5);
INSERT INTO Talk values(1,1,3,'2019-01-22 10:00:00','Activation Function Optimisations for Capsule Networks'),(2,1,1,'2019-01-22 10:20:00','Crowd counting and Density Estimation using Multicolumn Discriminator in GAN'),(3,1,4,'2019-01-22 11:00:00',' Semantic Deep Image Inpainting'),(4,1,2,'2019-01-22 12:00:00','Enhanced Deep Image Super-Resolution'),
(5,2,1,'2018-10-30 08:30:00','Sentiment Analysis on Interview Transcripts'),(6,2,3,'2018-10-30 08:50:00',' Automatic Parallel Corpus Creation for Hindi-English News Translation Task'),(7,2,2,'2018-10-30 09:30:00',' Laughter Synthesis using Mass-spring Model and Excitation Source Characteristics'),(8,2,5,'2018-10-30 10:30:00','PESUBot: An Empathetic Goal Oriented Chatbot'),
 (9,3,7,'2019-02-15 09:00:00',' Solving Multi-Objective Optimization Problems using Differential Evolution Algorithm with Different Population Initialization Techniques'),(10,3,6,'2019-02-15 10:00:00','Cardiac Arrhythmia Detection from Single-lead ECG using CNN and LSTM assisted by Oversampling'),(11,3,5,'2019-02-15 11:00:00',' Folding Paper Currency Recognition and Research Based on Convolution Neural Network'),(12,4,1,'2018-11-11 10:00:00','Diabetes Prediction Model Using Cloud Analytics'),(13,4,5,'2018-11-11 11:00:00','Post-Surgical Survival forecasting of breast cancer patient: a novel approach'),(14,4,1,'2018-11-11 12:00:00','An Automatic Chord Progression Generator Based On Reinforcement Learning');

INSERT INTO Talk values(1,1,3,'2019-01-22 10:00:00','Activation Function Optimisations for Capsule Networks'),(2,1,1,'2019-01-22 10:20:00','Crowd counting and Density Estimation'),(3,1,4,'2019-01-22 11:00:00',' Semantic Deep Image Inpainting'),(4,1,2,'2019-01-22 12:00:00','Enhanced Deep Image Super-Resolution'),
(5,2,1,'2018-10-30 08:30:00','Sentiment Analysis on Interview Transcripts'),(6,2,3,'2018-10-30 08:50:00',' Automatic Parallel Corpusfor Hindi-English Translation'),(7,2,2,'2018-10-30 09:30:00',' Laughter Synthesis using Mass-spring Model'),(8,2,5,'2018-10-30 10:30:00','PESUBot: An Empathetic Chatbot'),
 (9,3,7,'2019-02-15 09:00:00',' Solving Multi-Objective Optimization'),(10,3,6,'2019-02-15 10:00:00','Cardiac Arrhythmia Detection'),(11,3,5,'2019-02-15 11:00:00',' Folding Paper Currency Recognition'),(12,4,1,'2018-11-11 10:00:00','Diabetes Prediction Model '),(13,4,5,'2018-11-11 11:00:00','Post-Surgical Survival forecasting'),(14,4,1,'2018-11-11 12:00:00','An Automatic Chord Progression Generator');

INSERT INTO Event VALUES(1,'Computer Vision and the Internet (VisionNet-18)',3,'2019-01-22 10:00:00',2),(2,'Natural Language Processing (NLP-18)',1,'2018-10-30 08:30:00',4),(3,'Artificial Intelligence',1,'2019-02-15 09:00:00',1),(4,'Machine Learning/Data Engineering',2,'2018-11-11 10:00:00',5);

INSERT INTO Location values(1,'Seminar Hall 1'),(2,'Seminar Hall 2'),(3,'Room 001'),(4,'Room 002'),(5,'Room 003');

INSERT INTO Speaker values(1,'Dr. Manikandan J '),(2,'Mrs. Divya Aggarwal '),(3,'Dr. Chintan Shah'),(4,'Mr.  Sunil Bhutada '),(5,'Dr. Shetty'),(6,'Mr. Chetan'),(7,'Mrs. Amanda'),(8,'Mr. Ramesh');
