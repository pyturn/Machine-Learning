-- MySQL dump 10.13  Distrib 5.7.20, for Win64 (x86_64)
--
-- Host: localhost    Database: zauba_database
-- ------------------------------------------------------
-- Server version	5.7.20-log

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
-- Table structure for table `parseddata`
--

DROP TABLE IF EXISTS `parseddata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parseddata` (
  `SRN` text,
  `Service_Request_Date` text,
  `Payment_Mode_Into` text,
  `Address` text,
  `Name` text,
  `Service_Type` text,
  `Service_Description` text,
  `Type_of_Fee` text,
  `Amount` double DEFAULT NULL,
  `Total` double DEFAULT NULL,
  `Received_Payment_Rs` text,
  `Mode_of_Payment` text,
  `Received_From` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parseddata`
--

LOCK TABLES `parseddata` WRITE;
/*!40000 ALTER TABLE `parseddata` DISABLE KEYS */;
INSERT INTO `parseddata` VALUES ('U16571275','03/08/2017','ICICI BANK','No 1/10, II Floor, Near Gate No 9APMC Yard, YeshwanthpurBangalore , KarnatakaIndia - 00560022','Zauba Technologies and Data Services Privat','Fee for inspection of Public documents','Inspection of Public documents of KEYSTONE  REALTORS PRIVATE LIMITED  ( U45200MH1995PTC094208  )','Normal',100,100,'One Hundred Only','Credit Card/Prepaid Card - ICICI Bank','Nan'),('U16572745','03/08/2017','ICICI BANK','No 1/10, II Floor, Near Gate No 9APMC Yard, YeshwanthpurBangalore , KarnatakaIndia - 00560022','Zauba Technologies and Data Services Privat','Fee for inspection of Public documents','Inspection of Public documents of LANDMARK  CRAFTS PRIVATE LIMITED   ( U74999DL2007PTC163299  )','Normal',100,100,'One Hundred Only','Credit Card/Prepaid Card - ICICI Bank','Nan'),('U16573131','03/08/2017','ICICI BANK','No 1/10, II Floor, Near Gate No 9APMC Yard, YeshwanthpurBangalore , KarnatakaIndia - 00560022','Zauba Technologies and Data Services Privat','Fee for inspection of Public documents','Inspection of Public documents of WESNIA INFO  SOLUTIONS PRIVATE LIMITED  ( U72200KA2006PTC039676  ) ','Normal',100,100,'One Hundred Only','Credit Card/Prepaid Card - ICICI Bank','Nan');
/*!40000 ALTER TABLE `parseddata` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-15 11:00:17
