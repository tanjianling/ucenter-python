/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50540
Source Host           : 127.0.0.1:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50540
File Encoding         : 65001

Date: 2017-02-15 20:43:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `user_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT '',
  `password` varchar(32) DEFAULT '',
  `name` varchar(20) DEFAULT '',
  `email` varchar(30) DEFAULT '',
  `qq` varchar(12) DEFAULT '',
  `phone` varchar(11) DEFAULT '',
  `status` tinyint(1) DEFAULT '0',
  `login_count` int(11) DEFAULT '0',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', 'admin', '21232f297a57a5a743894a0e4a801fc3', '谭建领', '923825@qq.com', '9235578', '186296464', '1', '127');
INSERT INTO `users` VALUES ('3', 'zhangjie', '172a792213d4fedd5b3c2012242cab15', '张洁', '1588445@qq.com', '1088445', '150361490', '1', '52');
INSERT INTO `users` VALUES ('4', 'wanghaijuan', '74e307156d078a3d075fd414bb760158', '汪海娟', '237860@qq.com', '', '18728972', '1', '45');
INSERT INTO `users` VALUES ('5', 'zhangchaofeng', '0b11e7e824a456d75716258a65c7a08d', '张超峰', '4580201@qq.com', '451201', '1595481', '1', '35');
INSERT INTO `users` VALUES ('7', 'jiangchunjie', '47baf500083166c6940777a85b47b269', '姜春杰', '1195116@qq.com', '11957116', '150934028', '1', '36');
INSERT INTO `users` VALUES ('8', 'liman', '5fa2987984adbf47f57c327b3ac50845', '李曼', '608535@qq.com', '260635', '1862997', '1', '33');
INSERT INTO `users` VALUES ('9', 'qiuzhaojie', '9cc1c731bbd990e27762947455e77054', '邱兆杰', '29715543@qq.com', '29715543', '1560990', '1', '45');
INSERT INTO `users` VALUES ('11', 'wushijie', '4b7c8c8f34433aaf934553a5a812466f', '吴世杰', '405776@qq.com', '407736', '18575199', '1', '10');
INSERT INTO `users` VALUES ('12', 'zhuyunlong', '278e33ebd42933b6d68a13a9edc500e1', '祝运龙', 'xi00@vip.qq.com', '151950', '1119950', '1', '3');
INSERT INTO `users` VALUES ('14', 'lixiangyang', '4465a9c7f3e564411d808d787d787a71', '李向阳', '1292669@qq.com', '179929', '136708', '1', '5');
INSERT INTO `users` VALUES ('15', 'zhufengmei', 'ad3335a6902c7b65e5df5581d7258ee3', '朱凤梅', '5465978@qq.com', '54678', '1364881', '1', '7');
INSERT INTO `users` VALUES ('16', 'liuhong', 'da36cd13db4fb7d1c1f5a2a6c884bfbf', '刘宏', '1543413@qq.com', '154413', '181271', '1', '13');
INSERT INTO `users` VALUES ('17', 'weilinyu', '91183e1cb4e46961f86a2ef6287927ad', '魏琳宇', '466149@qq.com', '466549', '18627590', '1', '2');
INSERT INTO `users` VALUES ('20', 'zhoutingting', '24d323d5eec486538660445152410079', '周婷婷', '690018@qq.com', '690938', '13803138', '1', '7');
INSERT INTO `users` VALUES ('22', 'madandan', 'e706e34bf3e7085c1b1d1392e6d4c3e7', '马丹丹', '1490953@qq.com', '12490953', '13841262', '1', '2');
INSERT INTO `users` VALUES ('23', 'hanhuanhuan', 'd955864e0f902d36bf953f8de1076753', '韩欢欢', '8423511@qq.com', '2623511', '15801612', '1', '2');
INSERT INTO `users` VALUES ('24', 'hanlili', '2c8a39ab096b7edd2915da8423f69653', '韩丽丽', '2198520@qq.com', '2198580', '18745163', '1', '1');
