-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_relation`
--

DROP TABLE IF EXISTS `ike_doc_relation`;
CREATE TABLE `ike_doc_relation` (
  `rel_id_c`         VARCHAR(36) NOT NULL,
  `rel_iddocfrom_c`  VARCHAR(36) DEFAULT NULL,
  `rel_iddocto_c`    VARCHAR(36) DEFAULT NULL,
  `rel_deletedate_d` DATETIME    DEFAULT NULL,
  PRIMARY KEY (`rel_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:57
