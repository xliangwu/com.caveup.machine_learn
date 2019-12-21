-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_document_tag`
--

DROP TABLE IF EXISTS `ike_doc_document_tag`;
CREATE TABLE `ike_doc_document_tag` (
  `dot_id_c`         VARCHAR(36) NOT NULL,
  `dot_iddocument_c` VARCHAR(36) DEFAULT NULL,
  `dot_idtag_c`      VARCHAR(36) DEFAULT NULL,
  `dot_deletedate_d` DATETIME    DEFAULT NULL,
  PRIMARY KEY (`dot_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:56
