-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_webhook`
--

DROP TABLE IF EXISTS `ike_doc_webhook`;
CREATE TABLE `ike_doc_webhook` (
  `whk_id_c`         VARCHAR(36) NOT NULL,
  `whk_event_c`      VARCHAR(50) NOT NULL,
  `whk_url_c`        TEXT        NOT NULL,
  `whk_createdate_d` DATETIME    NOT NULL,
  `whk_deletedate_d` DATETIME DEFAULT NULL,
  PRIMARY KEY (`whk_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:54
