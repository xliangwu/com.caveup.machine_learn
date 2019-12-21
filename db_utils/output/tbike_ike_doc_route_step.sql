-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_route_step`
--

DROP TABLE IF EXISTS `ike_doc_route_step`;
CREATE TABLE `ike_doc_route_step` (
  `rtp_id_c`              VARCHAR(36)  NOT NULL,
  `rtp_idroute_c`         VARCHAR(36)  NOT NULL,
  `rtp_name_c`            VARCHAR(200) NOT NULL,
  `rtp_type_c`            VARCHAR(50)  NOT NULL,
  `rtp_transition_c`      VARCHAR(50) DEFAULT NULL,
  `rtp_comment_c`         TEXT,
  `rtp_idtarget_c`        VARCHAR(36)  NOT NULL,
  `rtp_idvalidatoruser_c` VARCHAR(36) DEFAULT NULL,
  `rtp_order_n`           INT(11)      NOT NULL,
  `rtp_createdate_d`      DATETIME     NOT NULL,
  `rtp_enddate_d`         DATETIME    DEFAULT NULL,
  `rtp_deletedate_d`      DATETIME    DEFAULT NULL,
  `rtp_transitions_c`     TEXT,
  PRIMARY KEY (`rtp_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:52
