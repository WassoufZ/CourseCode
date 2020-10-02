CREATE DATABASE  IF NOT EXISTS `course_db` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `course_db`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: course_db
-- ------------------------------------------------------
-- Server version	5.6.17

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'agents'),(4,'parents'),(3,'school administrators'),(2,'teachers');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add content type',3,'add_contenttype'),(8,'Can change content type',3,'change_contenttype'),(9,'Can delete content type',3,'delete_contenttype'),(10,'Can add session',4,'add_session'),(11,'Can change session',4,'change_session'),(12,'Can delete session',4,'delete_session'),(13,'Can add agent',5,'add_agent'),(14,'Can change agent',5,'change_agent'),(15,'Can delete agent',5,'delete_agent'),(16,'Can add client',6,'add_client'),(17,'Can change client',6,'change_client'),(18,'Can delete client',6,'delete_client'),(19,'Can add school',7,'add_school'),(20,'Can change school',7,'change_school'),(21,'Can delete school',7,'delete_school'),(22,'Can add schoolyear',8,'add_schoolyear'),(23,'Can change schoolyear',8,'change_schoolyear'),(24,'Can delete schoolyear',8,'delete_schoolyear'),(25,'Can add admin',9,'add_admin'),(26,'Can change admin',9,'change_admin'),(27,'Can delete admin',9,'delete_admin'),(28,'Can add level',10,'add_level'),(29,'Can change level',10,'change_level'),(30,'Can delete level',10,'delete_level'),(31,'Can add subject',11,'add_subject'),(32,'Can change subject',11,'change_subject'),(33,'Can delete subject',11,'delete_subject'),(34,'Can add user',12,'add_user'),(35,'Can change user',12,'change_user'),(36,'Can delete user',12,'delete_user'),(37,'Can add address',13,'add_address'),(38,'Can change address',13,'change_address'),(39,'Can delete address',13,'delete_address'),(40,'Can add level subject',14,'add_levelsubject'),(41,'Can change level subject',14,'change_levelsubject'),(42,'Can delete level subject',14,'delete_levelsubject');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_agent`
--

DROP TABLE IF EXISTS `client_agent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_agent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `first_name2` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `place_of_birth` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tel_number` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tel_number2` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `gender` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `date` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `image` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `account_id` int(11) DEFAULT NULL,
  `address_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_id` (`account_id`),
  UNIQUE KEY `address_id` (`address_id`),
  CONSTRAINT `client_agent_address_id_8ccd055c_fk_users_address_id` FOREIGN KEY (`address_id`) REFERENCES `users_address` (`id`),
  CONSTRAINT `client_agent_account_id_5b076a5f_fk_users_user_id` FOREIGN KEY (`account_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_agent`
--

LOCK TABLES `client_agent` WRITE;
/*!40000 ALTER TABLE `client_agent` DISABLE KEYS */;
INSERT INTO `client_agent` VALUES (1,'admin','','schools',NULL,NULL,NULL,NULL,'woman','2020-09-30 13:10:57.982787','2020-09-30 13:10:58.582837','',1,NULL);
/*!40000 ALTER TABLE `client_agent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_client`
--

DROP TABLE IF EXISTS `client_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_client` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `name_arabic` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `tel_number1` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tel_number2` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email1` varchar(254) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email2` varchar(254) COLLATE utf8_unicode_ci DEFAULT NULL,
  `adresse` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `image` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `updated_date` datetime(6) NOT NULL,
  `created_by_id` int(11) DEFAULT NULL,
  `updated_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `client_client_created_by_id_a8280477_fk_users_user_id` (`created_by_id`),
  KEY `client_client_updated_by_id_12f0c54f_fk_users_user_id` (`updated_by_id`),
  CONSTRAINT `client_client_updated_by_id_12f0c54f_fk_users_user_id` FOREIGN KEY (`updated_by_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `client_client_created_by_id_a8280477_fk_users_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_client`
--

LOCK TABLES `client_client` WRITE;
/*!40000 ALTER TABLE `client_client` DISABLE KEYS */;
INSERT INTO `client_client` VALUES (1,'Savoir','المعرفة','02134568','0212121','savoir@gmail.com','','Alger','photos/thumbnail_l_1_ntX28pl.jpeg','2020-09-30 13:11:53.827959','2020-09-30 13:11:53.827959',1,1);
/*!40000 ALTER TABLE `client_client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_school`
--

DROP TABLE IF EXISTS `client_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `name_arabic` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `tel_number1` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tel_number2` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email1` varchar(254) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email2` varchar(254) COLLATE utf8_unicode_ci DEFAULT NULL,
  `creation_date` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `adresse` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `approval_number` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `pupils_number` int(11) DEFAULT NULL,
  `client_id` int(11) NOT NULL,
  `current_schoolyear_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `client_school_client_id_c496baa0_fk_client_client_id` (`client_id`),
  KEY `client_school_current_schoolyear_i_635466b2_fk_client_sc` (`current_schoolyear_id`),
  CONSTRAINT `client_school_current_schoolyear_i_635466b2_fk_client_sc` FOREIGN KEY (`current_schoolyear_id`) REFERENCES `client_schoolyear` (`id`),
  CONSTRAINT `client_school_client_id_c496baa0_fk_client_client_id` FOREIGN KEY (`client_id`) REFERENCES `client_client` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_school`
--

LOCK TABLES `client_school` WRITE;
/*!40000 ALTER TABLE `client_school` DISABLE KEYS */;
INSERT INTO `client_school` VALUES (1,'Savoir','المعرفة','022515','0212121','savoir@gmail.com','','2020-09-30 13:12:15.147902','2020-09-30 13:12:15.147902','Alger','2020','primary',10,1,1),(2,'Savoir','المعرفة','02134568','0212121','savoir@gmail.com','','2020-09-30 13:14:54.795086','2020-09-30 13:14:54.795086','Alger','2020','primary',10,1,2);
/*!40000 ALTER TABLE `client_school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client_schoolyear`
--

DROP TABLE IF EXISTS `client_schoolyear`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client_schoolyear` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `label` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `starts_at` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ends_at` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `arabic_name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `date` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client_schoolyear`
--

LOCK TABLES `client_schoolyear` WRITE;
/*!40000 ALTER TABLE `client_schoolyear` DISABLE KEYS */;
INSERT INTO `client_schoolyear` VALUES (1,'2020-09-01','2021-07-20','2020-2021','','',NULL,NULL,'2020-09-30 13:12:15.083435','2020-09-30 13:12:15.083435'),(2,'2020-09-01','2021-07-20','2020-2021','','',NULL,NULL,'2020-09-30 13:14:54.711082','2020-09-30 13:14:54.711082');
/*!40000 ALTER TABLE `client_schoolyear` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'auth','group'),(1,'auth','permission'),(5,'client','agent'),(6,'client','client'),(7,'client','school'),(8,'client','schoolyear'),(3,'contenttypes','contenttype'),(9,'scolarité','admin'),(10,'scolarité','level'),(14,'scolarité','levelsubject'),(11,'scolarité','subject'),(4,'sessions','session'),(13,'users','address'),(12,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-09-30 13:10:00.702774'),(2,'contenttypes','0002_remove_content_type_name','2020-09-30 13:10:01.554833'),(3,'auth','0001_initial','2020-09-30 13:10:04.919077'),(4,'auth','0002_alter_permission_name_max_length','2020-09-30 13:10:05.603588'),(5,'auth','0003_alter_user_email_max_length','2020-09-30 13:10:05.643622'),(6,'auth','0004_alter_user_username_opts','2020-09-30 13:10:05.695626'),(7,'auth','0005_alter_user_last_login_null','2020-09-30 13:10:05.743608'),(8,'auth','0006_require_contenttypes_0002','2020-09-30 13:10:05.779600'),(9,'auth','0007_alter_validators_add_error_messages','2020-09-30 13:10:05.831604'),(10,'auth','0008_alter_user_username_max_length','2020-09-30 13:10:05.887608'),(11,'users','0001_initial','2020-09-30 13:10:10.615969'),(12,'client','0001_initial','2020-09-30 13:10:16.984382'),(13,'scolarité','0001_initial','2020-09-30 13:10:23.790878'),(14,'sessions','0001_initial','2020-09-30 13:10:24.391111'),(15,'users','0002_user_school','2020-09-30 13:10:25.648504'),(16,'scolarité','0002_levelsubject','2020-09-30 13:14:18.961889');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('6f9swy7nrmdz7n4o8ubn15qehqahurh5','NzU1ZjFlMTlkZTljMzg4ZTc3YWE2ZjQ1MDEzYTc4NjNhODU3OGVlMDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMuYmFja2VuZHMuRW1haWxPclVzZXJuYW1lTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOWNiZmRjZDBiZjZlNjkwN2MwNDYyM2ZlYzc1NzBhZjcxYTFhMDU1NCIsImFkbWluX2lkIjoxLCJzY2hvb2xfaWQiOjJ9','2020-10-14 13:51:00.413837'),('oqznos2z8t0o2jmu5c1dp93l56ddm4m7','NzU1ZjFlMTlkZTljMzg4ZTc3YWE2ZjQ1MDEzYTc4NjNhODU3OGVlMDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMuYmFja2VuZHMuRW1haWxPclVzZXJuYW1lTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOWNiZmRjZDBiZjZlNjkwN2MwNDYyM2ZlYzc1NzBhZjcxYTFhMDU1NCIsImFkbWluX2lkIjoxLCJzY2hvb2xfaWQiOjJ9','2020-10-14 13:26:58.406887');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scolarité_admin`
--

DROP TABLE IF EXISTS `scolarité_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scolarité_admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `first_name2` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `last_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `place_of_birth` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tel_number` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tel_number2` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `gender` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `date` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `is_activated` tinyint(1) NOT NULL,
  `is_super_admin` tinyint(1) NOT NULL,
  `account_id` int(11) DEFAULT NULL,
  `address_id` int(11) DEFAULT NULL,
  `school_id` int(11) NOT NULL,
  `schoolyear_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_id` (`account_id`),
  UNIQUE KEY `address_id` (`address_id`),
  KEY `scolarité_admin_school_id_e5656bda_fk_client_school_id` (`school_id`),
  KEY `scolarité_admin_schoolyear_id_3f0c4a1d_fk_client_schoolyear_id` (`schoolyear_id`),
  CONSTRAINT `scolarité_admin_schoolyear_id_3f0c4a1d_fk_client_schoolyear_id` FOREIGN KEY (`schoolyear_id`) REFERENCES `client_schoolyear` (`id`),
  CONSTRAINT `scolarité_admin_account_id_ee2477c4_fk_users_user_id` FOREIGN KEY (`account_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `scolarité_admin_address_id_e68074b6_fk_users_address_id` FOREIGN KEY (`address_id`) REFERENCES `users_address` (`id`),
  CONSTRAINT `scolarité_admin_school_id_e5656bda_fk_client_school_id` FOREIGN KEY (`school_id`) REFERENCES `client_school` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scolarité_admin`
--

LOCK TABLES `scolarité_admin` WRITE;
/*!40000 ALTER TABLE `scolarité_admin` DISABLE KEYS */;
INSERT INTO `scolarité_admin` VALUES (1,'Admin','','Savoir','0010-02-02','Alger','250535','0212121','man','2020-09-30 13:15:35.493327','2020-09-30 13:15:35.493327',1,1,2,NULL,2,2);
/*!40000 ALTER TABLE `scolarité_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scolarité_level`
--

DROP TABLE IF EXISTS `scolarité_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scolarité_level` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `name_arabic` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `code` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `code_arabic` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `branch` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `rank` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `school_id` int(11) DEFAULT NULL,
  `schoolyear_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `scolarité_level_school_id_96c98859_fk_client_school_id` (`school_id`),
  KEY `scolarité_level_schoolyear_id_4db88358_fk_client_schoolyear_id` (`schoolyear_id`),
  CONSTRAINT `scolarité_level_schoolyear_id_4db88358_fk_client_schoolyear_id` FOREIGN KEY (`schoolyear_id`) REFERENCES `client_schoolyear` (`id`),
  CONSTRAINT `scolarité_level_school_id_96c98859_fk_client_school_id` FOREIGN KEY (`school_id`) REFERENCES `client_school` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scolarité_level`
--

LOCK TABLES `scolarité_level` WRITE;
/*!40000 ALTER TABLE `scolarité_level` DISABLE KEYS */;
INSERT INTO `scolarité_level` VALUES (1,'Préscolaire','التحضيري','Préscolaire','Préscolaire','primary',NULL,0,'2020-09-30 13:12:15.203909','2020-09-30 13:12:15.203909',1,1),(2,'1ère Année Primaire','الأولى إبتدائي','1AP','1 إبتدائي','primary',NULL,1,'2020-09-30 13:12:15.283909','2020-09-30 13:12:15.283909',1,1),(3,'2ème Année Primaire','الثانية إبتدائي','2AP','2 إبتدائي','primary',NULL,2,'2020-09-30 13:12:15.339913','2020-09-30 13:12:15.339913',1,1),(4,'3ème Année Primaire','الثالثة إبتدائي','3AP','3 إبتدائي','primary',NULL,3,'2020-09-30 13:12:15.407919','2020-09-30 13:12:15.407919',1,1),(5,'4ème Année Primaire','الرابعة إبتدائي','4AP','4 إبتدائي','primary',NULL,4,'2020-09-30 13:12:15.435922','2020-09-30 13:12:15.435922',1,1),(6,'5ème Année Primaire','الخامسة إبتدائي','5AP','5 إبتدائي','primary',NULL,5,'2020-09-30 13:12:15.459921','2020-09-30 13:12:15.459921',1,1),(7,'Préscolaire','التحضيري','Préscolaire','Préscolaire','primary',NULL,0,'2020-09-30 13:14:54.919099','2020-09-30 13:14:54.919099',2,2),(8,'1ère Année Primaire','الأولى إبتدائي','1AP','1 إبتدائي','primary',NULL,1,'2020-09-30 13:14:55.011111','2020-09-30 13:14:55.011111',2,2),(9,'2ème Année Primaire','الثانية إبتدائي','2AP','2 إبتدائي','primary',NULL,2,'2020-09-30 13:14:55.099337','2020-09-30 13:14:55.099337',2,2),(10,'3ème Année Primaire','الثالثة إبتدائي','3AP','3 إبتدائي','primary',NULL,3,'2020-09-30 13:14:55.244355','2020-09-30 13:14:55.244355',2,2),(11,'4ème Année Primaire','الرابعة إبتدائي','4AP','4 إبتدائي','primary',NULL,4,'2020-09-30 13:14:55.300355','2020-09-30 13:14:55.300355',2,2),(12,'5ème Année Primaire','الخامسة إبتدائي','5AP','5 إبتدائي','primary',NULL,5,'2020-09-30 13:14:55.384543','2020-09-30 13:14:55.384543',2,2);
/*!40000 ALTER TABLE `scolarité_level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scolarité_levelsubject`
--

DROP TABLE IF EXISTS `scolarité_levelsubject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scolarité_levelsubject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `coefficient` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `level_id` int(11) NOT NULL,
  `schoolyear_id` int(11) DEFAULT NULL,
  `subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `scolarité_levelsubject_level_id_d2c98558_fk_scolarité_level_id` (`level_id`),
  KEY `scolarité_levelsubje_schoolyear_id_a96158c2_fk_client_sc` (`schoolyear_id`),
  KEY `scolarité_levelsubje_subject_id_8998977b_fk_scolarité` (`subject_id`),
  CONSTRAINT `scolarité_levelsubje_subject_id_8998977b_fk_scolarité` FOREIGN KEY (`subject_id`) REFERENCES `scolarité_subject` (`id`),
  CONSTRAINT `scolarité_levelsubject_level_id_d2c98558_fk_scolarité_level_id` FOREIGN KEY (`level_id`) REFERENCES `scolarité_level` (`id`),
  CONSTRAINT `scolarité_levelsubje_schoolyear_id_a96158c2_fk_client_sc` FOREIGN KEY (`schoolyear_id`) REFERENCES `client_schoolyear` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scolarité_levelsubject`
--

LOCK TABLES `scolarité_levelsubject` WRITE;
/*!40000 ALTER TABLE `scolarité_levelsubject` DISABLE KEYS */;
INSERT INTO `scolarité_levelsubject` VALUES (1,1,'2020-09-30 13:14:56.161111','2020-09-30 13:14:56.161111',8,2,15),(2,1,'2020-09-30 13:14:56.197082','2020-09-30 13:14:56.197082',8,2,16),(3,1,'2020-09-30 13:14:56.253086','2020-09-30 13:14:56.253086',8,2,17),(4,1,'2020-09-30 13:14:56.329123','2020-09-30 13:14:56.329123',8,2,18),(5,1,'2020-09-30 13:14:56.365095','2020-09-30 13:14:56.365095',8,2,19),(6,1,'2020-09-30 13:14:56.385096','2020-09-30 13:14:56.385096',8,2,20),(7,1,'2020-09-30 13:14:56.417098','2020-09-30 13:14:56.417098',8,2,21),(8,1,'2020-09-30 13:14:56.445100','2020-09-30 13:14:56.445100',8,2,23),(9,1,'2020-09-30 13:14:56.473102','2020-09-30 13:14:56.473102',8,2,24),(10,1,'2020-09-30 13:14:56.497104','2020-09-30 13:14:56.497104',8,2,25),(11,1,'2020-09-30 13:14:56.529107','2020-09-30 13:14:56.529107',8,2,26),(12,1,'2020-09-30 13:14:56.553108','2020-09-30 13:14:56.553108',8,2,27),(13,1,'2020-09-30 13:14:56.585110','2020-09-30 13:14:56.585110',8,2,28),(14,1,'2020-09-30 13:14:56.609113','2020-09-30 13:14:56.609113',9,2,15),(15,1,'2020-09-30 13:14:56.641113','2020-09-30 13:14:56.641113',9,2,16),(16,1,'2020-09-30 13:14:56.665117','2020-09-30 13:14:56.665117',9,2,17),(17,1,'2020-09-30 13:14:56.697119','2020-09-30 13:14:56.697119',9,2,18),(18,1,'2020-09-30 13:14:56.729129','2020-09-30 13:14:56.729129',9,2,19),(19,1,'2020-09-30 13:14:56.761130','2020-09-30 13:14:56.761130',9,2,20),(20,1,'2020-09-30 13:14:56.785123','2020-09-30 13:14:56.785123',9,2,21),(21,1,'2020-09-30 13:14:56.817133','2020-09-30 13:14:56.817133',9,2,23),(22,1,'2020-09-30 13:14:56.841139','2020-09-30 13:14:56.841139',9,2,24),(23,1,'2020-09-30 13:14:56.873132','2020-09-30 13:14:56.873132',9,2,25),(24,1,'2020-09-30 13:14:56.897139','2020-09-30 13:14:56.897139',9,2,26),(25,1,'2020-09-30 13:14:56.929134','2020-09-30 13:14:56.929134',9,2,27),(26,1,'2020-09-30 13:14:56.953372','2020-09-30 13:14:56.953372',9,2,28),(27,1,'2020-09-30 13:14:56.981402','2020-09-30 13:14:56.981402',10,2,15),(28,1,'2020-09-30 13:14:57.009355','2020-09-30 13:14:57.009355',10,2,16),(29,1,'2020-09-30 13:14:57.037353','2020-09-30 13:14:57.041348',10,2,17),(30,1,'2020-09-30 13:14:57.065349','2020-09-30 13:14:57.065349',10,2,18),(31,1,'2020-09-30 13:14:57.093351','2020-09-30 13:14:57.093351',10,2,19),(32,1,'2020-09-30 13:14:57.121354','2020-09-30 13:14:57.121354',10,2,20),(33,1,'2020-09-30 13:14:57.161355','2020-09-30 13:14:57.161355',10,2,21),(34,1,'2020-09-30 13:14:57.185357','2020-09-30 13:14:57.185357',10,2,22),(35,1,'2020-09-30 13:14:57.229362','2020-09-30 13:14:57.229362',10,2,23),(36,1,'2020-09-30 13:14:57.265364','2020-09-30 13:14:57.265364',10,2,24),(37,1,'2020-09-30 13:14:57.297367','2020-09-30 13:14:57.297367',10,2,25),(38,1,'2020-09-30 13:14:57.317363','2020-09-30 13:14:57.317363',10,2,26),(39,1,'2020-09-30 13:14:57.349400','2020-09-30 13:14:57.349400',10,2,27),(40,1,'2020-09-30 13:14:57.373369','2020-09-30 13:14:57.373369',10,2,28),(41,1,'2020-09-30 13:14:57.401502','2020-09-30 13:14:57.401502',11,2,15),(42,1,'2020-09-30 13:14:57.429510','2020-09-30 13:14:57.429510',11,2,16),(43,1,'2020-09-30 13:14:57.457488','2020-09-30 13:14:57.457488',11,2,17),(44,1,'2020-09-30 13:14:57.481489','2020-09-30 13:14:57.481489',11,2,18),(45,1,'2020-09-30 13:14:57.513500','2020-09-30 13:14:57.513500',11,2,19),(46,1,'2020-09-30 13:14:57.541503','2020-09-30 13:14:57.541503',11,2,20),(47,1,'2020-09-30 13:14:57.569494','2020-09-30 13:14:57.569494',11,2,21),(48,1,'2020-09-30 13:14:57.597529','2020-09-30 13:14:57.597529',11,2,22),(49,1,'2020-09-30 13:14:57.625507','2020-09-30 13:14:57.625507',11,2,23),(50,1,'2020-09-30 13:14:57.649532','2020-09-30 13:14:57.649532',11,2,24),(51,1,'2020-09-30 13:14:57.681534','2020-09-30 13:14:57.681534',11,2,25),(52,1,'2020-09-30 13:14:57.705536','2020-09-30 13:14:57.705536',11,2,26),(53,1,'2020-09-30 13:14:57.737517','2020-09-30 13:14:57.737517',11,2,27),(54,1,'2020-09-30 13:14:57.761569','2020-09-30 13:14:57.761569',11,2,28),(55,1,'2020-09-30 13:14:57.805658','2020-09-30 13:14:57.805658',12,2,15),(56,1,'2020-09-30 13:14:57.829660','2020-09-30 13:14:57.829660',12,2,16),(57,1,'2020-09-30 13:14:57.857691','2020-09-30 13:14:57.857691',12,2,17),(58,1,'2020-09-30 13:14:57.885632','2020-09-30 13:14:57.885632',12,2,18),(59,1,'2020-09-30 13:14:57.913695','2020-09-30 13:14:57.913695',12,2,19),(60,1,'2020-09-30 13:14:57.937810','2020-09-30 13:14:57.941752',12,2,20),(61,1,'2020-09-30 13:14:57.969910','2020-09-30 13:14:57.969910',12,2,21),(62,1,'2020-09-30 13:14:57.994005','2020-09-30 13:14:57.994005',12,2,22),(63,1,'2020-09-30 13:14:58.025980','2020-09-30 13:14:58.025980',12,2,23),(64,1,'2020-09-30 13:14:58.050106','2020-09-30 13:14:58.050106',12,2,24),(65,1,'2020-09-30 13:14:58.082193','2020-09-30 13:14:58.082193',12,2,25),(66,1,'2020-09-30 13:14:58.106307','2020-09-30 13:14:58.106307',12,2,26),(67,1,'2020-09-30 13:14:58.138421','2020-09-30 13:14:58.138421',12,2,27),(68,1,'2020-09-30 13:14:58.162390','2020-09-30 13:14:58.162390',12,2,28),(69,1,'2020-09-30 13:14:58.190392','2020-09-30 13:14:58.190392',7,2,15),(70,1,'2020-09-30 13:14:58.218425','2020-09-30 13:14:58.218425',7,2,16),(71,1,'2020-09-30 13:14:58.246432','2020-09-30 13:14:58.246432',7,2,17),(72,1,'2020-09-30 13:14:58.282458','2020-09-30 13:14:58.282458',7,2,18);
/*!40000 ALTER TABLE `scolarité_levelsubject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scolarité_subject`
--

DROP TABLE IF EXISTS `scolarité_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scolarité_subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `name_arabic` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `code` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `date` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `school_id` int(11) NOT NULL,
  `schoolyear_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `scolarité_subject_school_id_c0f7e920_fk_client_school_id` (`school_id`),
  KEY `scolarité_subject_schoolyear_id_21723a08_fk_client_schoolyear_id` (`schoolyear_id`),
  CONSTRAINT `scolarité_subject_schoolyear_id_21723a08_fk_client_schoolyear_id` FOREIGN KEY (`schoolyear_id`) REFERENCES `client_schoolyear` (`id`),
  CONSTRAINT `scolarité_subject_school_id_c0f7e920_fk_client_school_id` FOREIGN KEY (`school_id`) REFERENCES `client_school` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scolarité_subject`
--

LOCK TABLES `scolarité_subject` WRITE;
/*!40000 ALTER TABLE `scolarité_subject` DISABLE KEYS */;
INSERT INTO `scolarité_subject` VALUES (1,'Arabe','اللغة العربية','Arabe','2020-09-30 13:12:15.491925','2020-09-30 13:12:15.491925',1,1),(2,'Anglais','اللغة الإنجليزية','Anglais','2020-09-30 13:12:15.527956','2020-09-30 13:12:15.527956',1,1),(3,'Français','اللغة الفرنسية','Français','2020-09-30 13:12:15.555959','2020-09-30 13:12:15.559960',1,1),(4,'Mathématique','الرياضيات','Math','2020-09-30 13:12:15.583937','2020-09-30 13:12:15.583937',1,1),(5,'Education Islamique','تربية إسلامية','Education islamique','2020-09-30 13:12:15.611940','2020-09-30 13:12:15.611940',1,NULL),(6,'Education Scientifique','تربية العلمية','Education Scientifique','2020-09-30 13:12:15.639944','2020-09-30 13:12:15.639944',1,NULL),(7,'Education Civique','تربية مدنية ','Education Civique','2020-09-30 13:12:15.667997','2020-09-30 13:12:15.667997',1,1),(8,'Histoire - Géographie','الجغرافيا- التاريخ','Histoire-Géo','2020-09-30 13:12:15.691998','2020-09-30 13:12:15.695970',1,1),(9,'Récitation','محفوظات','Récitation','2020-09-30 13:12:15.723939','2020-09-30 13:12:15.723939',1,1),(10,'Sport','تربية بدنية','Sport','2020-09-30 13:12:15.747943','2020-09-30 13:12:15.747943',1,1),(11,'Dessin','التربية الفنية','Dessin','2020-09-30 13:12:15.779953','2020-09-30 13:12:15.779953',1,1),(12,'Math (Fr)','Math (Fr)','Math (Fr)','2020-09-30 13:12:15.804006','2020-09-30 13:12:15.804006',1,1),(13,'Français (Fr)','Français (Fr) ','Français (Fr)','2020-09-30 13:12:15.847980','2020-09-30 13:12:15.847980',1,1),(14,'Sciences et Technologies','Sciences et Technologies','Sciences et Technologies','2020-09-30 13:12:15.871966','2020-09-30 13:12:15.871966',1,1),(15,'Arabe','اللغة العربية','Arabe','2020-09-30 13:14:55.440610','2020-09-30 13:14:55.440610',2,2),(16,'Anglais','اللغة الإنجليزية','Anglais','2020-09-30 13:14:55.528885','2020-09-30 13:14:55.528885',2,2),(17,'Français','اللغة الفرنسية','Français','2020-09-30 13:14:55.608927','2020-09-30 13:14:55.608927',2,2),(18,'Mathématique','الرياضيات','Math','2020-09-30 13:14:55.741050','2020-09-30 13:14:55.741050',2,2),(19,'Education Islamique','تربية إسلامية','Education islamique','2020-09-30 13:14:55.789056','2020-09-30 13:14:55.789056',2,NULL),(20,'Education Scientifique','تربية العلمية','Education Scientifique','2020-09-30 13:14:55.841058','2020-09-30 13:14:55.841058',2,NULL),(21,'Education Civique','تربية مدنية ','Education Civique','2020-09-30 13:14:55.877060','2020-09-30 13:14:55.877060',2,2),(22,'Histoire - Géographie','الجغرافيا- التاريخ','Histoire-Géo','2020-09-30 13:14:55.905062','2020-09-30 13:14:55.909065',2,2),(23,'Récitation','محفوظات','Récitation','2020-09-30 13:14:55.933067','2020-09-30 13:14:55.933067',2,2),(24,'Sport','تربية بدنية','Sport','2020-09-30 13:14:55.961067','2020-09-30 13:14:55.961067',2,2),(25,'Dessin','التربية الفنية','Dessin','2020-09-30 13:14:55.985068','2020-09-30 13:14:55.985068',2,2),(26,'Math (Fr)','Math (Fr)','Math (Fr)','2020-09-30 13:14:56.021071','2020-09-30 13:14:56.021071',2,2),(27,'Français (Fr)','Français (Fr) ','Français (Fr)','2020-09-30 13:14:56.041073','2020-09-30 13:14:56.045073',2,2),(28,'Sciences et Technologies','Sciences et Technologies','Sciences et Technologies','2020-09-30 13:14:56.073074','2020-09-30 13:14:56.073074',2,2);
/*!40000 ALTER TABLE `scolarité_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_address`
--

DROP TABLE IF EXISTS `users_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country_name` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `country_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `state_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `state_code` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `street_address` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `postal_code` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_address`
--

LOCK TABLES `users_address` WRITE;
/*!40000 ALTER TABLE `users_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `username` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `user_type` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_confirmed` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `school_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `users_user_school_id_e82aaa0a_fk_client_school_id` (`school_id`),
  CONSTRAINT `users_user_school_id_e82aaa0a_fk_client_school_id` FOREIGN KEY (`school_id`) REFERENCES `client_school` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (1,'pbkdf2_sha256$36000$HrdlBynYGO3F$vvcism3Xksz4swYqfTQTp6g/95oa+Kmz+QRPFHvyU9w=','2020-09-30 13:13:25.125050',0,'adminschools@gmail.com',NULL,'admin','schools','agent',1,1,'2020-09-30 13:10:58.442849','2020-09-30 13:10:58.490831',NULL),(2,'pbkdf2_sha256$36000$omdBHVel132D$DnP3HLPTVokHTdD8KPvp+1YcRra8AztXW00Mfm7FS1M=','2020-09-30 13:51:00.373832',0,'savoir@gmail.com','asavoir3015','Admin','Savoir','school_admin',1,1,'2020-09-30 13:15:35.353261','2020-09-30 13:17:36.849850',2);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
INSERT INTO `users_user_groups` VALUES (1,1,1),(2,2,3);
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'course_db'
--

--
-- Dumping routines for database 'course_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-30 21:52:52
