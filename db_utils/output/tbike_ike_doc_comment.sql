-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_comment`
--

DROP TABLE IF EXISTS `ike_doc_comment`;
CREATE TABLE `ike_doc_comment` (
  `com_id_c`         VARCHAR(36) NOT NULL,
  `com_iddoc_c`      VARCHAR(36) DEFAULT NULL,
  `com_iduser_c`     VARCHAR(36) DEFAULT NULL,
  `com_content_c`    TEXT,
  `com_createdate_d` DATETIME    DEFAULT NULL,
  `com_deletedate_d` DATETIME    DEFAULT NULL,
  PRIMARY KEY (`com_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:57
