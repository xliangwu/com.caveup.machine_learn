-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_route_model`
--

DROP TABLE IF EXISTS `ike_doc_route_model`;
CREATE TABLE `ike_doc_route_model` (
  `rtm_id_c`         VARCHAR(36) NOT NULL,
  `rtm_name_c`       VARCHAR(50) NOT NULL,
  `rtm_steps_c`      TEXT        NOT NULL,
  `rtm_createdate_d` DATETIME    NOT NULL,
  `rtm_deletedate_d` DATETIME DEFAULT NULL,
  PRIMARY KEY (`rtm_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:59
