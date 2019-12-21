-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_user`
--

DROP TABLE IF EXISTS `ike_doc_user`;
CREATE TABLE `ike_doc_user` (
  `use_id_c`             VARCHAR(36) NOT NULL,
  `use_idrole_c`         VARCHAR(36)  DEFAULT NULL,
  `use_username_c`       VARCHAR(50) NOT NULL,
  `use_password_c`       VARCHAR(60)  DEFAULT NULL,
  `use_email_c`          VARCHAR(100) DEFAULT NULL,
  `use_createdate_d`     DATETIME    NOT NULL,
  `use_deletedate_d`     DATETIME     DEFAULT NULL,
  `use_privatekey_c`     VARCHAR(100) DEFAULT NULL,
  `use_storagequota_n`   BIGINT(20)   DEFAULT NULL,
  `use_storagecurrent_n` BIGINT(20)   DEFAULT NULL,
  `use_totpkey_c`        VARCHAR(100) DEFAULT NULL,
  `use_disabledate_d`    DATETIME     DEFAULT NULL,
  PRIMARY KEY (`use_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:55
