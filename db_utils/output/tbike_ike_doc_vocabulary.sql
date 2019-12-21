-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_vocabulary`
--

DROP TABLE IF EXISTS `ike_doc_vocabulary`;
CREATE TABLE `ike_doc_vocabulary` (
  `voc_id_c`    VARCHAR(36) NOT NULL,
  `voc_name_c`  VARCHAR(50) NOT NULL,
  `voc_value_c` TEXT        NOT NULL,
  `voc_order_n` INT(11)     NOT NULL,
  PRIMARY KEY (`voc_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:53
