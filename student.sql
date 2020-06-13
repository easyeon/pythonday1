/*
SQLyog 企业版 - MySQL GUI v8.14
MySQL - 5.1.40-community : Database - easy
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`easy` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `easy`;

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `s_id` varchar(20) NOT NULL DEFAULT '',
  `s_name` varchar(20) NOT NULL DEFAULT '',
  `s_birth` varchar(20) NOT NULL DEFAULT '',
  `s_sex` varchar(10) NOT NULL DEFAULT '',
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `student` */

insert  into `student`(`s_id`,`s_name`,`s_birth`,`s_sex`) values ('01','赵雷','1990-01-01','男'),('02','钱电','1990-12-21','男'),('03','孙风','1990-05-20','男'),('04','李云','1990-08-06','男'),('05','周梅','1991-12-01','女'),('06','吴兰','1992-03-01','女'),('07','郑竹','1989-07-01','女'),('08','王菊','1990-01-20','女');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
