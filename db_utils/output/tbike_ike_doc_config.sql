-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_config`
--

DROP TABLE IF EXISTS `ike_doc_config`;
CREATE TABLE `ike_doc_config` (
  `cfg_id_c`    VARCHAR(50) NOT NULL,
  `cfg_value_c` VARCHAR(250) DEFAULT NULL,
  PRIMARY KEY (`cfg_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:56
