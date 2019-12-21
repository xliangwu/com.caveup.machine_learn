-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_role`
--

DROP TABLE IF EXISTS `ike_doc_role`;
CREATE TABLE `ike_doc_role` (
  `rol_id_c`         VARCHAR(36) NOT NULL,
  `rol_name_c`       VARCHAR(36) DEFAULT NULL,
  `rol_createdate_d` DATETIME    DEFAULT NULL,
  `rol_deletedate_d` DATETIME    DEFAULT NULL,
  PRIMARY KEY (`rol_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:51
