-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: proj
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Blacklist`
--

DROP TABLE IF EXISTS `Blacklist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Blacklist` (
  `Customer_id` int(11) NOT NULL,
  `Seller_id` int(11) NOT NULL,
  PRIMARY KEY (`Customer_id`,`Seller_id`),
  KEY `blacklist_fk_seller` (`Seller_id`),
  CONSTRAINT `blacklist_fk_customer` FOREIGN KEY (`Customer_id`) REFERENCES `Customer` (`customer_id`) ON DELETE CASCADE,
  CONSTRAINT `blacklist_fk_seller` FOREIGN KEY (`Seller_id`) REFERENCES `Seller` (`Seller_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Blacklist`
--

LOCK TABLES `Blacklist` WRITE;
/*!40000 ALTER TABLE `Blacklist` DISABLE KEYS */;
/*!40000 ALTER TABLE `Blacklist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Category` (
  `Category_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(16) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Parent_category` int(11) DEFAULT NULL,
  PRIMARY KEY (`Category_id`),
  UNIQUE KEY `cgname_UNIQUE` (`Name`),
  KEY `category_fk_parent` (`Parent_category`),
  CONSTRAINT `category_fk_parent` FOREIGN KEY (`Parent_category`) REFERENCES `Category` (`Category_id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
/*!40000 ALTER TABLE `Category` DISABLE KEYS */;
/*!40000 ALTER TABLE `Category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customer` (
  `Customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `Account` varchar(32) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Password` varchar(32) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Name` varchar(20) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Register_time` datetime DEFAULT NULL,
  `Bill_info` text COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `Email` varchar(64) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`Customer_id`),
  UNIQUE KEY `Account_UNIQUE` (`Account`),
  UNIQUE KEY `mail_UNIQUE` (`Email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Faq`
--

DROP TABLE IF EXISTS `Faq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Faq` (
  `Merchandise_id` int(11) NOT NULL,
  `FAQ_id` int(11) NOT NULL,
  `Customer_id` int(11) DEFAULT NULL,
  `Question_text` text COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `Question_time` datetime DEFAULT NULL,
  `Answer_text` text COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `Answer_time` datetime DEFAULT NULL,
  PRIMARY KEY (`Merchandise_id`,`FAQ_id`),
  KEY `faq_fk_customer` (`Customer_id`),
  CONSTRAINT `faq_fk_customer` FOREIGN KEY (`Customer_id`) REFERENCES `Customer` (`Customer_id`),
  CONSTRAINT `faq_fk_merchandise` FOREIGN KEY (`Merchandise_id`) REFERENCES `Merchandise` (`merchandise_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Faq`
--

LOCK TABLES `Faq` WRITE;
/*!40000 ALTER TABLE `Faq` DISABLE KEYS */;
/*!40000 ALTER TABLE `Faq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `In_Cart`
--

DROP TABLE IF EXISTS `In_Cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `In_Cart` (
  `Customer_id` int(11) NOT NULL,
  `Merchandise_id` int(11) NOT NULL,
  `Number` int(11) NOT NULL,
  PRIMARY KEY (`Customer_id`,`Merchandise_id`),
  KEY `in_cart_fk_merchandise` (`Merchandise_id`),
  CONSTRAINT `in_cart_fk_customer` FOREIGN KEY (`Customer_id`) REFERENCES `Customer` (`Customer_id`) ON DELETE CASCADE,
  CONSTRAINT `in_cart_fk_merchandise` FOREIGN KEY (`Merchandise_id`) REFERENCES `Merchandise` (`merchandise_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `In_Cart`
--

LOCK TABLES `In_Cart` WRITE;
/*!40000 ALTER TABLE `In_Cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `In_Cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Merchandise`
--

DROP TABLE IF EXISTS `Merchandise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Merchandise` (
  `Merchandise_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Price` int(11) NOT NULL,
  `Number_in_stock` int(11) NOT NULL,
  `Number_sold` int(11) NOT NULL,
  `Category_id` int(11) DEFAULT NULL,
  `Seller_id` int(11) NOT NULL,
  `Description` text COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`Merchandise_id`),
  UNIQUE KEY `Merchandise_id_UNIQUE` (`Merchandise_id`),
  KEY `merchandise_fk_category` (`Category_id`),
  KEY `merchandise_fk_seller` (`Seller_id`),
  CONSTRAINT `merchandise_fk_category` FOREIGN KEY (`Category_id`) REFERENCES `Category` (`Category_id`),
  CONSTRAINT `merchandise_fk_seller` FOREIGN KEY (`Seller_id`) REFERENCES `Seller` (`Seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Merchandise`
--

LOCK TABLES `Merchandise` WRITE;
/*!40000 ALTER TABLE `Merchandise` DISABLE KEYS */;
/*!40000 ALTER TABLE `Merchandise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Order`
--

DROP TABLE IF EXISTS `Order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Order` (
  `Order_id` int(11) NOT NULL AUTO_INCREMENT,
  `Customer_id` int(11) NOT NULL,
  `Order_time` datetime NOT NULL,
  PRIMARY KEY (`Order_id`),
  KEY `order_fk_customer` (`Customer_id`),
  CONSTRAINT `order_fk_customer` FOREIGN KEY (`Customer_id`) REFERENCES `Customer` (`Customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Order`
--

LOCK TABLES `Order` WRITE;
/*!40000 ALTER TABLE `Order` DISABLE KEYS */;
/*!40000 ALTER TABLE `Order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `OrderItem`
--

DROP TABLE IF EXISTS `OrderItem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `OrderItem` (
  `Order_id` int(11) NOT NULL,
  `Merchandise_id` int(11) NOT NULL,
  `Trade_price` int(11) NOT NULL,
  `Number` int(11) NOT NULL,
  `Status` int(1) DEFAULT NULL,
  PRIMARY KEY (`Order_id`,`Merchandise_id`),
  KEY `orderitem_fk_merchandise` (`Merchandise_id`),
  CONSTRAINT `orderitem_fk_merchandise` FOREIGN KEY (`Merchandise_id`) REFERENCES `Merchandise` (`Merchandise_id`) ON DELETE CASCADE,
  CONSTRAINT `orderitem_fk_order` FOREIGN KEY (`Order_id`) REFERENCES `Order` (`Order_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `OrderItem`
--

LOCK TABLES `OrderItem` WRITE;
/*!40000 ALTER TABLE `OrderItem` DISABLE KEYS */;
/*!40000 ALTER TABLE `OrderItem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Review`
--

DROP TABLE IF EXISTS `Review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Review` (
  `Seller_id` int(11) NOT NULL,
  `Order_id` int(11) NOT NULL,
  `Rating` int(11) NOT NULL,
  `Time` datetime NOT NULL,
  PRIMARY KEY (`Seller_id`,`Order_id`),
  KEY `review_fk_order` (`Order_id`),
  CONSTRAINT `review_fk_order` FOREIGN KEY (`Order_id`) REFERENCES `Order` (`Order_id`),
  CONSTRAINT `review_fk_seller` FOREIGN KEY (`Seller_id`) REFERENCES `Seller` (`Seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Review`
--

LOCK TABLES `Review` WRITE;
/*!40000 ALTER TABLE `Review` DISABLE KEYS */;
/*!40000 ALTER TABLE `Review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Seller`
--

DROP TABLE IF EXISTS `Seller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Seller` (
  `Seller_id` int(11) NOT NULL AUTO_INCREMENT,
  `Account` varchar(32) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Password` varchar(32) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Name` varchar(45) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Register_Time` datetime NOT NULL,
  `Email` varchar(64) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`Seller_id`),
  UNIQUE KEY `saccount_UNIQUE` (`Account`),
  UNIQUE KEY `sname_UNIQUE` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Seller`
--

LOCK TABLES `Seller` WRITE;
/*!40000 ALTER TABLE `Seller` DISABLE KEYS */;
/*!40000 ALTER TABLE `Seller` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-17 15:12:02
