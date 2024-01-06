import mysql.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DB = "dw"

# Connect to MySQL
def connect():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )


def add_happines_report_score(id, country_id, year, score):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO HappinesReportScore (id, countryId, year, score) VALUES (%s, %s, %s, %s)"
    values = (id, country_id, year, score)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

def add_country(name, land_area):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Country (name, landArea) VALUES (%s, %s)"
    values = (name, land_area)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

def add_country_data(id, year, country_id, healthcare_data_id, environmental_data_id, educational_data_id, population_data_id):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Country (id, year, countryId, healthcareDataId, environmentalDataId, financialDataId, educationalDataId, populationDataId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (id, year, country_id, healthcare_data_id, environmental_data_id, educational_data_id, population_data_id)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

def add_population_data(id, density, population, labor_force_participant, urban_population):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Country (id, density, population, laborForceParticipant, urbanPopulation) VALUES (%s, %s, %s, %s, %s)"
    values = (id, density, population, labor_force_participant, urban_population)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

def add_financial_data(id, armed_forces_size, cpi, gasoline_price, gdp, minimum_wage, out_of_pocket_health_expenditure, tax_revenue, total_tax_rate, unemployment_rate):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Country (id, armedForcesSize, CPI, gasolinePrice, GDP, minimumWage, outOfPocketHealthExpenditure, taxRevenue, totalTaxRate, unemploymentRate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (id, armed_forces_size, cpi, gasoline_price, gdp, minimum_wage, out_of_pocket_health_expenditure, tax_revenue, total_tax_rate, unemployment_rate)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

def add_educational_data(id, gross_primary_education_enrollment, gross_tertiary_education_enrollment):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Country (id, GrossPrimaryEducationEnrollment, GrossTertiaryEducationEnrollment) VALUES (%s, %s, %s)"
    values = (id, gross_primary_education_enrollment, gross_tertiary_education_enrollment)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

def add_environmental_data(id, co2_emission, forested_area):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Country (id, Co2Emmission, forestedArea) VALUES (%s, %s, %s)"
    values = (id, co2_emission, forested_area)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

def add_healthcare_data(id, birth_rate, fertility_rate, infant_mortaloty, life_expectancy, maternal_morality, physician_per_thousand):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Country (id, birthRate, fertilityRate, infantMortaloty, lifeExpectancy, maternalMortality,physicianPerThousand) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (id, birth_rate, fertility_rate, infant_mortaloty, life_expectancy, maternal_morality, physician_per_thousand)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid