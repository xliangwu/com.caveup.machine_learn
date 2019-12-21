-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_doc_document`
--

DROP TABLE IF EXISTS `ike_doc_document`;
CREATE TABLE `ike_doc_document` (
  `doc_id_c`          VARCHAR(36)  NOT NULL,
  `doc_iduser_c`      VARCHAR(36)  NOT NULL,
  `doc_title_c`       VARCHAR(100) NOT NULL,
  `doc_description_c` TEXT,
  `doc_createdate_d`  DATETIME              DEFAULT NULL,
  `doc_deletedate_d`  DATETIME              DEFAULT NULL,
  `doc_language_c`    VARCHAR(7)            DEFAULT NULL,
  `doc_subject_c`     TEXT,
  `doc_identifier_c`  TEXT,
  `doc_publisher_c`   TEXT,
  `doc_format_c`      TEXT,
  `doc_source_c`      TEXT,
  `doc_type_c`        TEXT,
  `doc_coverage_c`    TEXT,
  `doc_rights_c`      TEXT,
  `doc_updatedate_d`  DATETIME     NOT NULL,
  `doc_idfile_c`      VARCHAR(36)           DEFAULT NULL,
  `event_mark`        INT(11)      NOT NULL DEFAULT '0',
  `announcement_mark` INT(11)      NOT NULL DEFAULT '0',
  PRIMARY KEY (`doc_id_c`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8 ROW_FORMAT = DYNAMIC;

-- Dump completed on 2019-05-28 13:58:57
