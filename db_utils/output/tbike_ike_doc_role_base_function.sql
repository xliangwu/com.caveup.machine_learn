-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_role_base_function`
--

DROP TABLE IF EXISTS `ike_doc_role_base_function`;
CREATE TABLE `ike_doc_role_base_function` (
  `rbf_id_c`             VARCHAR(36) NOT NULL,
  `rbf_idrole_c`         VARCHAR(36) DEFAULT NULL,
  `rbf_idbasefunction_c` VARCHAR(20) DEFAULT NULL,
  `rbf_createdate_d`     DATETIME    DEFAULT NULL,
  `rbf_deletedate_d`     DATETIME    DEFAULT NULL,
  PRIMARY KEY (`rbf_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:55
