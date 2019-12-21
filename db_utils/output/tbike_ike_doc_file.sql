-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_file`
--

DROP TABLE IF EXISTS `ike_doc_file`;
CREATE TABLE `ike_doc_file` (
  `fil_id_c`            VARCHAR(36) NOT NULL,
  `fil_iddoc_c`         VARCHAR(36)          DEFAULT NULL,
  `fil_iduser_c`        VARCHAR(36) NOT NULL,
  `fil_mimetype_c`      VARCHAR(100)         DEFAULT NULL,
  `fil_createdate_d`    DATETIME             DEFAULT NULL,
  `fil_deletedate_d`    DATETIME             DEFAULT NULL,
  `fil_order_n`         INT(11)              DEFAULT NULL,
  `fil_content_c`       LONGTEXT,
  `fil_name_c`          VARCHAR(200)         DEFAULT NULL,
  `fil_version_n`       INT(11)     NOT NULL,
  `fil_idversion_c`     VARCHAR(36)          DEFAULT NULL,
  `fil_latestversion_b` INT(11)     NOT NULL DEFAULT '1',
  PRIMARY KEY (`fil_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:55
