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
-- Table structure for table `blacklist`
--

DROP TABLE IF EXISTS `blacklist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blacklist` (
  `Customer_id` int(11) NOT NULL,
  `Seller_id` int(11) NOT NULL,
  PRIMARY KEY (`Customer_id`,`Seller_id`),
  KEY `blacklist_fk_seller` (`Seller_id`),
  CONSTRAINT `blacklist_fk_customer` FOREIGN KEY (`Customer_id`) REFERENCES `customer` (`Customer_id`) ON DELETE CASCADE,
  CONSTRAINT `blacklist_fk_seller` FOREIGN KEY (`Seller_id`) REFERENCES `seller` (`Seller_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blacklist`
--

LOCK TABLES `blacklist` WRITE;
/*!40000 ALTER TABLE `blacklist` DISABLE KEYS */;
/*!40000 ALTER TABLE `blacklist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `Category_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(16) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `Parent_category` int(11) DEFAULT NULL,
  PRIMARY KEY (`Category_id`),
  UNIQUE KEY `cgname_UNIQUE` (`Name`),
  KEY `category_fk_parent` (`Parent_category`),
  CONSTRAINT `category_fk_parent` FOREIGN KEY (`Parent_category`) REFERENCES `category` (`Category_id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faq`
--

DROP TABLE IF EXISTS `faq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `faq` (
  `Merchandise_id` int(11) NOT NULL,
  `FAQ_id` int(11) NOT NULL,
  `Customer_id` int(11) DEFAULT NULL,
  `Question_text` text COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `Question_time` datetime DEFAULT NULL,
  `Answer_text` text COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `Answer_time` datetime DEFAULT NULL,
  PRIMARY KEY (`Merchandise_id`,`FAQ_id`),
  KEY `faq_fk_customer` (`Customer_id`),
  CONSTRAINT `faq_fk_customer` FOREIGN KEY (`Customer_id`) REFERENCES `customer` (`Customer_id`),
  CONSTRAINT `faq_fk_merchandise` FOREIGN KEY (`Merchandise_id`) REFERENCES `merchandise` (`Merchandise_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faq`
--

LOCK TABLES `faq` WRITE;
/*!40000 ALTER TABLE `faq` DISABLE KEYS */;
/*!40000 ALTER TABLE `faq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `in_cart`
--

DROP TABLE IF EXISTS `in_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `in_cart` (
  `Customer_id` int(11) NOT NULL,
  `Merchandise_id` int(11) NOT NULL,
  `Number` int(11) NOT NULL,
  PRIMARY KEY (`Customer_id`,`Merchandise_id`),
  KEY `in_cart_fk_merchandise` (`Merchandise_id`),
  CONSTRAINT `in_cart_fk_customer` FOREIGN KEY (`Customer_id`) REFERENCES `customer` (`Customer_id`) ON DELETE CASCADE,
  CONSTRAINT `in_cart_fk_merchandise` FOREIGN KEY (`Merchandise_id`) REFERENCES `merchandise` (`Merchandise_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `in_cart`
--

LOCK TABLES `in_cart` WRITE;
/*!40000 ALTER TABLE `in_cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `in_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `merchandise`
--

DROP TABLE IF EXISTS `merchandise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `merchandise` (
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
  CONSTRAINT `merchandise_fk_category` FOREIGN KEY (`Category_id`) REFERENCES `category` (`Category_id`),
  CONSTRAINT `merchandise_fk_seller` FOREIGN KEY (`Seller_id`) REFERENCES `seller` (`Seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `merchandise`
--

LOCK TABLES `merchandise` WRITE;
/*!40000 ALTER TABLE `merchandise` DISABLE KEYS */;
/*!40000 ALTER TABLE `merchandise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order` (
  `Order_id` int(11) NOT NULL AUTO_INCREMENT,
  `Customer_id` int(11) NOT NULL,
  `Order_time` datetime NOT NULL,
  PRIMARY KEY (`Order_id`),
  KEY `order_fk_customer` (`Customer_id`),
  CONSTRAINT `order_fk_customer` FOREIGN KEY (`Customer_id`) REFERENCES `customer` (`Customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderitem`
--

DROP TABLE IF EXISTS `orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orderitem` (
  `Order_id` int(11) NOT NULL,
  `Merchandise_id` int(11) NOT NULL,
  `Trade_price` int(11) NOT NULL,
  `Number` int(11) NOT NULL,
  `Status` int(1) DEFAULT NULL,
  PRIMARY KEY (`Order_id`,`Merchandise_id`),
  KEY `orderitem_fk_merchandise` (`Merchandise_id`),
  CONSTRAINT `orderitem_fk_merchandise` FOREIGN KEY (`Merchandise_id`) REFERENCES `merchandise` (`Merchandise_id`) ON DELETE CASCADE,
  CONSTRAINT `orderitem_fk_order` FOREIGN KEY (`Order_id`) REFERENCES `order` (`Order_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderitem`
--

LOCK TABLES `orderitem` WRITE;
/*!40000 ALTER TABLE `orderitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `review` (
  `Seller_id` int(11) NOT NULL,
  `Order_id` int(11) NOT NULL,
  `Rating` int(11) NOT NULL,
  `Time` datetime NOT NULL,
  PRIMARY KEY (`Seller_id`,`Order_id`),
  KEY `review_fk_order` (`Order_id`),
  CONSTRAINT `review_fk_order` FOREIGN KEY (`Order_id`) REFERENCES `order` (`Order_id`),
  CONSTRAINT `review_fk_seller` FOREIGN KEY (`Seller_id`) REFERENCES `seller` (`Seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seller`
--

DROP TABLE IF EXISTS `seller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `seller` (
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
-- Dumping data for table `seller`
--

LOCK TABLES `seller` WRITE;
/*!40000 ALTER TABLE `seller` DISABLE KEYS */;
/*!40000 ALTER TABLE `seller` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-15 13:43:45
