-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: EVENTS
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `EVENTS`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `EVENTS` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `EVENTS`;

--
-- Table structure for table `Event`
--

DROP TABLE IF EXISTS `Event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Event` (
  `EventId` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `PlaceId` int(11) NOT NULL,
  `StartTime` datetime NOT NULL,
  `InchargeId` int(11) NOT NULL,
  PRIMARY KEY (`EventId`),
  KEY `fk1` (`PlaceId`),
  KEY `fk2` (`InchargeId`),
  CONSTRAINT `fk1` FOREIGN KEY (`PlaceId`) REFERENCES `Location` (`PlaceId`),
  CONSTRAINT `fk2` FOREIGN KEY (`InchargeId`) REFERENCES `Incharge` (`InchargeId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Event`
--

LOCK TABLES `Event` WRITE;
/*!40000 ALTER TABLE `Event` DISABLE KEYS */;
INSERT INTO `Event` VALUES (1,'TedX',3,'2019-01-22 10:00:00',2),(2,'Ingenius',1,'2018-10-30 08:30:00',4),(3,'Kalpana',1,'2019-02-15 09:00:00',1),(4,'Maaya',2,'2018-11-11 10:00:00',5);
/*!40000 ALTER TABLE `Event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Incharge`
--

DROP TABLE IF EXISTS `Incharge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Incharge` (
  `InchargeId` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `ContactNo` int(11) NOT NULL,
  PRIMARY KEY (`InchargeId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Incharge`
--

LOCK TABLES `Incharge` WRITE;
/*!40000 ALTER TABLE `Incharge` DISABLE KEYS */;
INSERT INTO `Incharge` VALUES (1,'Sam',9732712213),(2,'Sarah',1414231123),(3,'John',1782323456),(4,'Alice',1119876423),(5,'Alex',5109327663);
/*!40000 ALTER TABLE `Incharge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Location`
--

DROP TABLE IF EXISTS `Location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Location` (
  `PlaceId` int(11) NOT NULL,
  `PlaceName` varchar(30) NOT NULL,
  PRIMARY KEY (`PlaceId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Location`
--

LOCK TABLES `Location` WRITE;
/*!40000 ALTER TABLE `Location` DISABLE KEYS */;
INSERT INTO `Location` VALUES (1,'Seminar Hall 1'),(2,'Seminar Hall 2'),(3,'Room 001'),(4,'Room 002'),(5,'Room 003');
/*!40000 ALTER TABLE `Location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Speaker`
--

DROP TABLE IF EXISTS `Speaker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Speaker` (
  `SpeakerId` int(11) NOT NULL,
  `SpeakerName` varchar(30) NOT NULL,
  PRIMARY KEY (`SpeakerId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Speaker`
--

LOCK TABLES `Speaker` WRITE;
/*!40000 ALTER TABLE `Speaker` DISABLE KEYS */;
INSERT INTO `Speaker` VALUES (1,'Dr. Shyam'),(2,'Mr. Rohan'),(3,'Dr. Paul'),(4,'Mrs. Walker'),(5,'Dr. Shetty'),(6,'Mr. Chetan'),(7,'Mrs. Amanda'),(8,'Mr. Ramesh');
/*!40000 ALTER TABLE `Speaker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sponsor`
--

DROP TABLE IF EXISTS `Sponsor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Sponsor` (
  `SponsorId` int(11) NOT NULL,
  `SponsorName` varchar(30) NOT NULL,
  `Role` varchar(30) NOT NULL,
  PRIMARY KEY (`SponsorId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sponsor`
--

LOCK TABLES `Sponsor` WRITE;
/*!40000 ALTER TABLE `Sponsor` DISABLE KEYS */;
/*!40000 ALTER TABLE `Sponsor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Talk`
--

DROP TABLE IF EXISTS `Talk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Talk` (
  `TalkId` int(11) NOT NULL,
  `EventId` int(11) NOT NULL,
  `SpeakerId` int(11) NOT NULL,
  `StartTime` datetime NOT NULL,
  `Title` varchar(30) NOT NULL,
  PRIMARY KEY (`TalkId`),
  KEY `fk3` (`EventId`),
  KEY `fk4` (`SpeakerId`),
  CONSTRAINT `fk3` FOREIGN KEY (`EventId`) REFERENCES `Event` (`EventId`),
  CONSTRAINT `fk4` FOREIGN KEY (`SpeakerId`) REFERENCES `Speaker` (`SpeakerId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Talk`
--

LOCK TABLES `Talk` WRITE;
/*!40000 ALTER TABLE `Talk` DISABLE KEYS */;
INSERT INTO `Talk` VALUES (1,1,1,'2019-01-22 10:00:00','Networking'),(2,1,2,'2019-01-22 10:00:00','AI'),(3,1,3,'2019-01-22 10:00:00','Data Structures'),(4,2,4,'2018-10-30 08:30:00','Software Testing'),(5,2,5,'2018-10-30 08:30:00','Data analytics'),(6,2,6,'2018-10-30 08:30:00','Embedded systems'),(7,3,7,'2019-02-15 09:00:00','Data Security'),(8,3,2,'2019-02-15 09:00:00','Android'),(9,3,5,'2019-02-15 09:00:00','ML'),(10,4,2,'2018-10-11 10:06:59','Web dev'),(11,4,1,'2018-11-11 10:00:00','Java');
/*!40000 ALTER TABLE `Talk` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-13 19:15:52
