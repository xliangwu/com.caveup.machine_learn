-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tbike
-- ------------------------------------------------------
-- Server version	8.0.11


--
-- Table structure for table `ike_product_category`
--

DROP TABLE IF EXISTS `ike_product_category`;
CREATE TABLE `ike_product_category` (
  `id`             VARCHAR(50) NOT NULL,
  `product_name`   VARCHAR(50)      DEFAULT NULL,
  `parent_id`      VARCHAR(50)      DEFAULT NULL,
  `level`          INT(11)          DEFAULT NULL,
  `enabled`        VARCHAR(1)       DEFAULT '1',
  `create_time`    TIMESTAMP   NULL DEFAULT NULL,
  `delete_time`    TIMESTAMP   NULL DEFAULT NULL,
  `create_user_id` VARCHAR(255)     DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE =InnoDB DEFAULT CHARSET = utf8;

-- Dump completed on 2019-05-28 13:58:52
