-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2023 at 10:22 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dw`
--

-- --------------------------------------------------------

--
-- Table structure for table `country`
--

CREATE TABLE `country` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `landArea` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `countrydata`
--

CREATE TABLE `countrydata` (
  `id` int(11) NOT NULL,
  `year` int(11) DEFAULT NULL,
  `countryId` int(11) DEFAULT NULL,
  `healthcareDataId` int(11) DEFAULT NULL,
  `environmentalDataId` int(11) DEFAULT NULL,
  `financialDataId` int(11) DEFAULT NULL,
  `educationalDataId` int(11) DEFAULT NULL,
  `populationDataId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Fact/Maintable';

-- --------------------------------------------------------

--
-- Table structure for table `educationaldata`
--

CREATE TABLE `educationaldata` (
  `id` int(11) NOT NULL,
  `GrossPrimaryEducationEnrollment` float DEFAULT NULL,
  `GrossTertiaryEducationEnrollment` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `environmentaldata`
--

CREATE TABLE `environmentaldata` (
  `id` int(11) NOT NULL,
  `Co2Emmission` float DEFAULT NULL,
  `forestedArea` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `financialdata`
--

CREATE TABLE `financialdata` (
  `id` int(11) NOT NULL,
  `armedForcesSize` int(11) DEFAULT NULL,
  `CPI` float DEFAULT NULL,
  `gasolinePrice` float DEFAULT NULL,
  `GDP` int(11) DEFAULT NULL,
  `minimumWage` float DEFAULT NULL,
  `outOfPocketHealthExpenditure` float DEFAULT NULL,
  `taxRevenue` float DEFAULT NULL,
  `totalTaxRate` float DEFAULT NULL,
  `unemploymentRate` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `happinesreportscore`
--

CREATE TABLE `happinesreportscore` (
  `id` int(11) NOT NULL,
  `countryId` int(11) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `score` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Fact/Maintable';

-- --------------------------------------------------------

--
-- Table structure for table `healthcaredata`
--

CREATE TABLE `healthcaredata` (
  `id` int(11) NOT NULL,
  `birthRate` float DEFAULT NULL,
  `fertilityRate` float DEFAULT NULL,
  `infantMortaloty` float DEFAULT NULL,
  `lifeExpectancy` int(11) DEFAULT NULL,
  `maternalMortality` float DEFAULT NULL,
  `physicianPerThousand` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `populationdata`
--

CREATE TABLE `populationdata` (
  `id` int(11) NOT NULL,
  `density` int(11) DEFAULT NULL,
  `population` int(11) DEFAULT NULL,
  `laborForceParticipant` float DEFAULT NULL,
  `urbanPopulation` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `country`
--
ALTER TABLE `country`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `countrydata`
--
ALTER TABLE `countrydata`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `educationaldata`
--
ALTER TABLE `educationaldata`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `environmentaldata`
--
ALTER TABLE `environmentaldata`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `financialdata`
--
ALTER TABLE `financialdata`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `happinesreportscore`
--
ALTER TABLE `happinesreportscore`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `healthcaredata`
--
ALTER TABLE `healthcaredata`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `populationdata`
--
ALTER TABLE `populationdata`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
