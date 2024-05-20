-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 20, 2024 at 10:14 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id` int(4) NOT NULL,
  `isbn` bigint(20) DEFAULT NULL,
  `bname` varchar(90) DEFAULT NULL,
  `qty` int(4) DEFAULT NULL,
  `rented` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `isbn`, `bname`, `qty`, `rented`) VALUES
(1, 9777471189, '1984', 25, 0),
(2, 8590579984, 'Tempest', 29, 2),
(3, 3872540062, 'Adventures Of Sherlock Holmes', 54, 2),
(4, 5314561553, 'Crime And Punishment', 15, 3),
(5, 7938721315, 'The Subtle Art Of Not Caring', 41, 0),
(6, 8902669900, 'Ikigai', 68, 0);

-- --------------------------------------------------------

--
-- Table structure for table `librarian`
--

CREATE TABLE `librarian` (
  `id` int(11) NOT NULL,
  `uname` varchar(30) DEFAULT NULL,
  `exp` int(4) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `librarian`
--

INSERT INTO `librarian` (`id`, `uname`, `exp`, `pin`) VALUES
(1, 'Inmon', 78, 78906799),
(2, 'Xenon', 86, 99064678),
(3, 'Usopp', 65, 1123456);

-- --------------------------------------------------------

--
-- Table structure for table `readers`
--

CREATE TABLE `readers` (
  `cid` bigint(20) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `cbr` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `readers`
--

INSERT INTO `readers` (`cid`, `name`, `cbr`) VALUES
(431126959, 'tirth', 4),
(441694828, 'poyo', 3),
(753803023, 'coby', 0),
(815908637, 'star', 0);

-- --------------------------------------------------------

--
-- Table structure for table `reader_coby_rented`
--

CREATE TABLE `reader_coby_rented` (
  `cid` bigint(20) DEFAULT NULL,
  `bname` varchar(50) DEFAULT NULL,
  `isbn` bigint(20) DEFAULT NULL,
  `rent_count` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reader_poyo_rented`
--

CREATE TABLE `reader_poyo_rented` (
  `cid` bigint(20) NOT NULL,
  `bname` varchar(50) NOT NULL,
  `isbn` bigint(20) NOT NULL,
  `rent_count` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reader_poyo_rented`
--

INSERT INTO `reader_poyo_rented` (`cid`, `bname`, `isbn`, `rent_count`) VALUES
(441694828, 'Crime And Punishment', 5314561553, 1),
(441694828, 'Tempest', 8590579984, 2);

-- --------------------------------------------------------

--
-- Table structure for table `reader_star_rented`
--

CREATE TABLE `reader_star_rented` (
  `cid` bigint(20) DEFAULT NULL,
  `bname` varchar(50) DEFAULT NULL,
  `isbn` bigint(20) DEFAULT NULL,
  `rent_count` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `reader_tirth_rented`
--

CREATE TABLE `reader_tirth_rented` (
  `cid` bigint(20) NOT NULL,
  `bname` varchar(50) NOT NULL,
  `isbn` bigint(20) NOT NULL,
  `rent_count` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reader_tirth_rented`
--

INSERT INTO `reader_tirth_rented` (`cid`, `bname`, `isbn`, `rent_count`) VALUES
(431126959, 'Adventures Of Sherlock Holmes', 3872540062, 2),
(431126959, 'Crime And Punishment', 5314561553, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `isbn` (`isbn`);

--
-- Indexes for table `librarian`
--
ALTER TABLE `librarian`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uname` (`uname`);

--
-- Indexes for table `readers`
--
ALTER TABLE `readers`
  ADD PRIMARY KEY (`cid`),
  ADD UNIQUE KEY `cid` (`cid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `librarian`
--
ALTER TABLE `librarian`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
