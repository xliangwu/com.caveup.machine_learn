-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11

SET NAMES utf8;

--
-- Table structure for table `ike_doc_audit_log`
--

DROP TABLE IF EXISTS `ike_doc_audit_log`;
CREATE TABLE `ike_doc_audit_log` (
  `log_id_c`          VARCHAR(36) NOT NULL,
  `log_identity_c`    VARCHAR(36) DEFAULT NULL,
  `log_classentity_c` VARCHAR(50) DEFAULT NULL,
  `log_type_c`        VARCHAR(50) DEFAULT NULL,
  `log_message_c`     TEXT,
  `log_createdate_d`  DATETIME    DEFAULT NULL,
  `log_iduser_c`      VARCHAR(36) DEFAULT NULL,
  PRIMARY KEY (`log_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:57
