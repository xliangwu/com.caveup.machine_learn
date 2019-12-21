-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_authentication_token`
--

DROP TABLE IF EXISTS `ike_doc_authentication_token`;
CREATE TABLE `ike_doc_authentication_token` (
  `aut_id_c`                 VARCHAR(36) NOT NULL,
  `aut_iduser_c`             VARCHAR(36) DEFAULT NULL,
  `aut_longlasted_b`         TINYINT(1)  DEFAULT NULL,
  `aut_creationdate_d`       DATETIME    DEFAULT NULL,
  `aut_lastconnectiondate_d` DATETIME    DEFAULT NULL,
  `aut_ip_c`                 VARCHAR(45) DEFAULT NULL,
  `aut_ua_c`                 TEXT,
  PRIMARY KEY (`aut_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:53
