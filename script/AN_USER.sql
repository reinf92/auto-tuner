CREATE TABLE `AN_USER` (
  `USER_ID` varchar(100) NOT NULL,
  `USER_NM` varchar(100) DEFAULT NULL,
  `USER_IP` varchar(100) DEFAULT NULL,
  `USER_MAC_ADDR` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`USER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8