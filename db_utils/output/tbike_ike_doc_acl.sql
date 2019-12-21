-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_acl`
--

DROP TABLE IF EXISTS `ike_doc_acl`;
CREATE TABLE `ike_doc_acl` (
  `acl_id_c`         VARCHAR(36) NOT NULL,
  `acl_perm_c`       VARCHAR(30) DEFAULT NULL,
  `acl_sourceid_c`   VARCHAR(36) DEFAULT NULL,
  `acl_targetid_c`   VARCHAR(36) DEFAULT NULL,
  `acl_deletedate_d` DATETIME    DEFAULT NULL,
  `acl_type_c`       VARCHAR(30) DEFAULT NULL,
  PRIMARY KEY (`acl_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:52
