CREATE TABLE `contract` (
  `ID_card` varchar(13) NOT NULL,
  `Contract_Num` int NOT NULL,
  `Contract_Date` varchar(100),
  `Finish_Date` varchar(100),
  `Start_Date` varchar(100),
  `Deposit` int,
  PRIMARY KEY (`ID_card`)
);