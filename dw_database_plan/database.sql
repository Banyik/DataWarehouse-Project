CREATE TABLE `HappinesReportScore` (
  `id` int,
  `countryId` int,
  `year` int,
  `score` float
);

CREATE TABLE `Country` (
  `id` int,
  `name` varchar(100),
  `landArea` int
);

CREATE TABLE `CountryData` (
  `id` int,
  `year` int,
  `countryId` int,
  `healthcareDataId` int,
  `environmentalDataId` int,
  `financialDataId` int,
  `educationalDataId` int,
  `populationDataId` int
);

CREATE TABLE `PopulationData` (
  `id` int,
  `density` int,
  `population` int,
  `laborForceParticipant` float,
  `urbanPopulation` int
);

CREATE TABLE `FinancialData` (
  `id` int,
  `armedForcesSize` int,
  `CPI` float,
  `gasolinePrice` float,
  `GDP` int,
  `minimumWage` float,
  `outOfPocketHealthExpenditure` float,
  `taxRevenue` float,
  `totalTaxRate` float,
  `unemploymentRate` float
);

CREATE TABLE `EducationalData` (
  `id` int,
  `GrossPrimaryEducationEnrollment` float,
  `GrossTertiaryEducationEnrollment` float
);

CREATE TABLE `EnvironmentalData` (
  `id` int,
  `Co2Emmission` float,
  `forestedArea` float
);

CREATE TABLE `HealthcareData` (
  `id` int,
  `birthRate` float,
  `fertilityRate` float,
  `infantMortaloty` float,
  `lifeExpectancy` int,
  `maternalMortality` float,
  `physicianPerThousand` float
);

ALTER TABLE `HappinesReportScore` COMMENT = 'Fact/Maintable';

ALTER TABLE `CountryData` COMMENT = 'Fact/Maintable';

ALTER TABLE `CountryData` ADD FOREIGN KEY (`populationDataId`) REFERENCES `PopulationData` (`id`);

ALTER TABLE `CountryData` ADD FOREIGN KEY (`financialDataId`) REFERENCES `FinancialData` (`id`);

ALTER TABLE `CountryData` ADD FOREIGN KEY (`educationalDataId`) REFERENCES `EducationalData` (`id`);

ALTER TABLE `CountryData` ADD FOREIGN KEY (`environmentalDataId`) REFERENCES `EnvironmentalData` (`id`);

ALTER TABLE `CountryData` ADD FOREIGN KEY (`healthcareDataId`) REFERENCES `HealthcareData` (`id`);

ALTER TABLE `Country` ADD FOREIGN KEY (`id`) REFERENCES `HappinesReportScore` (`countryId`);

ALTER TABLE `Country` ADD FOREIGN KEY (`id`) REFERENCES `CountryData` (`countryId`);
