-- adatbázis létrehozása

CREATE DATABASE `kiralyok`
DEFAULT CHARACTER SET utf8
COLLATE utf8_hungarian_ci;
USE `kiralyok`;

-- hivatal

CREATE TABLE `hivatal` (
  `azon` int(11) NOT NULL,
  `uralkodo_az` int(11) NOT NULL,
  `mettol` int(11) NOT NULL,
  `meddig` int(11) NOT NULL,
  `koronazas` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

INSERT INTO `hivatal` (`azon`, `uralkodo_az`, `mettol`, `meddig`, `koronazas`) VALUES
(1, 1, 1000, 1038, 1000),
(2, 2, 1038, 1041, 1038),
(3, 3, 1041, 1044, 1044),
(4, 2, 1044, 1046, NULL),
(5, 4, 1046, 1060, 1046),
(6, 5, 1060, 1063, 1060),
(7, 6, 1063, 1074, 1063),
(8, 7, 1074, 1077, 1075),
(9, 8, 1077, 1095, 1081),
(10, 9, 1095, 1116, 1095),
(11, 10, 1116, 1131, 1116),
(12, 11, 1131, 1141, 1131),
(13, 12, 1141, 1162, 1141),
(14, 13, 1162, 1172, 1162),
(15, 14, 1172, 1196, 1173),
(16, 15, 1196, 1204, 1194),
(17, 16, 1204, 1205, 1204),
(18, 17, 1205, 1235, 1205),
(19, 18, 1235, 1270, 1235),
(20, 19, 1270, 1272, 1270),
(21, 20, 1272, 1290, 1272),
(22, 21, 1290, 1301, 1290),
(23, 22, 1301, 1305, 1301),
(24, 23, 1305, 1307, 1305),
(25, 24, 1308, 1342, 1301),
(26, 25, 1342, 1382, 1342),
(27, 26, 1382, 1385, 1382),
(28, 27, 1385, 1386, 1385),
(29, 26, 1386, 1395, NULL),
(30, 28, 1387, 1437, 1387),
(31, 29, 1437, 1439, 1438),
(32, 30, 1440, 1457, 1440),
(33, 31, 1440, 1444, 1440),
(34, 32, 1458, 1490, 1464),
(35, 33, 1490, 1516, 1490),
(36, 34, 1516, 1526, 1508),
(37, 35, 1526, 1540, 1526),
(38, 36, 1540, 1571, NULL),
(39, 37, 1526, 1564, 1527),
(40, 38, 1564, 1576, 1563),
(41, 39, 1576, 1608, 1572),
(42, 40, 1608, 1619, 1608),
(43, 41, 1618, 1637, 1618),
(44, 42, 1637, 1657, 1625),
(45, 43, 1647, 1654, 1647),
(46, 44, 1657, 1705, 1655),
(47, 45, 1705, 1711, 1687),
(48, 46, 1711, 1740, 1712),
(49, 47, 1740, 1780, 1712),
(50, 48, 1780, 1790, NULL),
(51, 49, 1790, 1792, 1790),
(52, 50, 1792, 1835, 1792),
(53, 51, 1835, 1848, 1830),
(54, 52, 1848, 1916, 1867),
(55, 53, 1916, 1918, 1916);

-- --------------------------------------------------------

-- uralkodo

CREATE TABLE `uralkodo` (
  `azon` int(11) NOT NULL,
  `nev` varchar(30) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `ragnev` varchar(30) COLLATE utf8mb4_hungarian_ci DEFAULT NULL,
  `szul` int(11) NOT NULL,
  `hal` int(11) NOT NULL,
  `uhaz_az` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--

INSERT INTO `uralkodo` (`azon`, `nev`, `ragnev`, `szul`, `hal`, `uhaz_az`) VALUES
(1, 'I. István', 'Szent István', 969, 1038, 1),
(2, 'Péter', 'Orseolo Velencei Péter', 1011, 1059, 1),
(3, 'Sámuel', 'Aba Sámuel', 990, 1044, 1),
(4, 'I. András', 'Fehér András', 1015, 1060, 1),
(5, 'I. Béla', 'Bajnok Béla', 1015, 1063, 1),
(6, 'Salamon', NULL, 1053, 1087, 1),
(7, 'I. Géza', 'Magnus Géza', 1040, 1077, 1),
(8, 'I. László', 'Szent László', 1040, 1095, 1),
(9, 'Kálmán', 'Könyves Kálmán', 1074, 1116, 1),
(10, 'II. István', NULL, 1101, 1131, 1),
(11, 'II. Béla', 'Vak Béla', 1108, 1141, 1),
(12, 'II. Géza', NULL, 1130, 1162, 1),
(13, 'III. István', NULL, 1147, 1172, 1),
(14, 'III. Béla', 'Nagy Béla', 1148, 1196, 1),
(15, 'Imre', NULL, 1174, 1204, 1),
(16, 'III. László', NULL, 1200, 1205, 1),
(17, 'II. András', 'Jeruzsálemi András', 1176, 1235, 1),
(18, 'IV. Béla', 'Második honalapító', 1206, 1270, 1),
(19, 'V. István', NULL, 1239, 1272, 1),
(20, 'IV. László', 'Kun László', 1262, 1290, 1),
(21, 'III. András', 'Velencei András', 1265, 1301, 1),
(22, 'Vencel', 'Cseh Vencel', 1289, 1306, 2),
(23, 'Ottó', 'Bajor Ottó', 1261, 1312, 3),
(24, 'I. Károly', 'Károly Róbert', 1288, 1342, 4),
(25, 'I. Lajos', 'Nagy Lajos', 1326, 1382, 4),
(26, 'Mária', NULL, 1371, 1395, 4),
(27, 'II. Károly', 'Kis Károly', 1345, 1386, 4),
(28, 'Zsigmond', 'Luxemburgi Zsigmond', 1368, 1437, 5),
(29, 'Albert', 'Habsburg Albert', 1397, 1439, 6),
(30, 'V. László', 'Utószülött László', 1440, 1457, 6),
(31, 'I. Ulászló', 'Várnai Ulászló', 1424, 1444, 7),
(32, 'I. Mátyás', 'Corvin Mátyás', 1443, 1490, 8),
(33, 'II. Ulászló', 'Dobzse László', 1456, 1516, 7),
(34, 'II. Lajos', NULL, 1506, 1526, 7),
(35, 'I. János', NULL, 1487, 1540, 9),
(36, 'II. János', 'János Zsigmond', 1540, 1571, 9),
(37, 'I. Ferdinánd', NULL, 1503, 1564, 6),
(38, 'Miksa', NULL, 1527, 1576, 6),
(39, 'Rudolf', NULL, 1552, 1612, 6),
(40, 'II. Mátyás', NULL, 1557, 1619, 6),
(41, 'II. Ferdinánd', NULL, 1578, 1637, 6),
(42, 'III. Ferdinánd', NULL, 1608, 1657, 6),
(43, 'IV. Ferdinánd', NULL, 1633, 1654, 6),
(44, 'I. Lipót', NULL, 1640, 1705, 6),
(45, 'I. József', NULL, 1687, 1711, 6),
(46, 'III. Károly', NULL, 1685, 1740, 6),
(47, 'Mária Terézia', NULL, 1717, 1780, 6),
(48, 'II. József', 'A kalapos király', 1741, 1790, 10),
(49, 'II. Lipót', NULL, 1747, 1792, 10),
(50, 'I. Ferenc', NULL, 1768, 1835, 10),
(51, 'V. Ferdinánd', 'Jóságos Ferdinánd', 1793, 1875, 10),
(52, 'I. Ferenc József', NULL, 1830, 1916, 10),
(53, 'IV. Károly', 'Boldog Károly', 1887, 1922, 10);

-- --------------------------------------------------------

-- uralkodohaz

CREATE TABLE `uralkodohaz` (
  `azon` int(11) NOT NULL,
  `nev` varchar(30) COLLATE utf8mb4_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

INSERT INTO `uralkodohaz` (`azon`, `nev`) VALUES
(1, 'Árpád-ház'),
(2, 'Přemysl-ház'),
(3, 'Wittelsbach-ház'),
(4, 'Anjou-ház'),
(5, 'Luxemburgi-ház'),
(6, 'Habsburg-ház'),
(7, 'Jagelló-ház'),
(8, 'Hunyadi-ház'),
(9, 'Szapolyai-ház'),
(10, 'Habsburg–Lotaringiai-ház');

--
-- Indexek 
--
ALTER TABLE `hivatal`
  ADD PRIMARY KEY (`azon`),
  ADD KEY `uralkodo_az` (`uralkodo_az`);

ALTER TABLE `uralkodo`
  ADD PRIMARY KEY (`azon`),
  ADD KEY `uhaz_az` (`uhaz_az`);

ALTER TABLE `uralkodohaz`
  ADD PRIMARY KEY (`azon`);

-- Megkötések
--
ALTER TABLE `hivatal`
  ADD CONSTRAINT `hivatal_ibfk_1` FOREIGN KEY (`uralkodo_az`) REFERENCES `uralkodo` (`azon`);
--
ALTER TABLE `uralkodo`
  ADD CONSTRAINT `uralkodo_ibfk_1` FOREIGN KEY (`uhaz_az`) REFERENCES `uralkodohaz` (`azon`);
COMMIT;

