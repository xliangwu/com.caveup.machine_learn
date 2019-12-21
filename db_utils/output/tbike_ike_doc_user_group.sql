-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_user_group`
--

DROP TABLE IF EXISTS `ike_doc_user_group`;
CREATE TABLE `ike_doc_user_group` (
  `ugp_id_c`         VARCHAR(36) NOT NULL,
  `ugp_iduser_c`     VARCHAR(36) NOT NULL,
  `ugp_idgroup_c`    VARCHAR(36) NOT NULL,
  `ugp_deletedate_d` DATETIME DEFAULT NULL,
  PRIMARY KEY (`ugp_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:56
