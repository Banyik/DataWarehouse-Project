CREATE TABLE `HappinesReportScore` (
  `id` integer,
  `countryId` integer,
  `year` integer,
  `score` float
);

CREATE TABLE `Country` (
  `id` integer,
  `name` string,
  `landArea` integer
);

CREATE TABLE `CountryData` (
  `id` integer,
  `year` integer,
  `countryId` integer,
  `healthcareDataId` integer,
  `environmentalDataId` integer,
  `financialDataId` integer,
  `educationalDataId` integer,
  `populationDataId` integer
);

CREATE TABLE `PopulationData` (
  `id` integer,
  `density` integer,
  `population` integer,
  `laborForceParticipant` float,
  `urbanPopulation` integer
);

CREATE TABLE `FinancialData` (
  `id` integer,
  `armedForcesSize` integer,
  `CPI` float,
  `gasolinePrice` float,
  `GDP` integer,
  `minimumWage` float,
  `outOfPocketHealthExpenditure` float,
  `taxRevenue` float,
  `totalTaxRate` float,
  `unemploymentRate` float
);

CREATE TABLE `EducationalData` (
  `id` integer,
  `GrossPrimaryEducationEnrollment` float,
  `GrossTertiaryEducationEnrollment` float
);

CREATE TABLE `EnvironmentalData` (
  `id` integer,
  `Co2Emmission` float,
  `forestedArea` float
);

CREATE TABLE `HealthcareData` (
  `id` integer,
  `birthRate` float,
  `fertilityRate` float,
  `infantMortaloty` float,
  `lifeExpectancy` integer,
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
