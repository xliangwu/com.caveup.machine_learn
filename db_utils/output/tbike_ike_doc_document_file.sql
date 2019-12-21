-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_document_file`
--

DROP TABLE IF EXISTS `ike_doc_document_file`;
CREATE TABLE `ike_doc_document_file` (
  `file_id`       VARCHAR(36) NOT NULL,
  `document_file` VARCHAR(100) DEFAULT NULL,
  `pdf_file`      VARCHAR(100) DEFAULT NULL,
  `doc_content`   mediumblob,
  PRIMARY KEY (`file_id`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:58
