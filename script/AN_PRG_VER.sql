CREATE TABLE `AN_PRG_VER` (
  `PRG_ID` varchar(100) NOT NULL,
  `PRG_VER` varchar(100) NOT NULL,
  `PRG_LINK` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`PRG_ID`,`PRG_VER`),
  CONSTRAINT `AN_PRG_VER_FK` FOREIGN KEY (`PRG_ID`) REFERENCES `AN_PRG` (`PRG_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8