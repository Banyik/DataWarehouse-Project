from fastapi import FastAPI, HTTPException
import json
import requests
from database import connect, add_country, add_country_data, add_educational_data, add_environmental_data, add_financial_data, add_happines_report_score, add_healthcare_data, add_population_data

app = FastAPI()
conn = connect()
cursor = conn.cursor

@app.get("/")
async def root_call():
    return {"message": "api server is running..."}

@app.post("/add/happiness-report-score")
async def happiness_report_score(id=int, country_id=int, year=int, score=float):
    new_happiness_report_score = add_happines_report_score(id, year, score)
    if new_happiness_report_score:
        return {"message": "success"}
    else:
        raise HTTPException(status_code=400, detail="bad request")
    
@app.post("/add/country")
async def country(name=str, land_area=int):
    if(len(name) > 100):
        raise HTTPException(status_code=400, detail="bad request")
    new_country = add_country(name, land_area)
    if new_country:
        return {"message": "success"}
    else:
        raise HTTPException(status_code=400, detail="bad request")
    
@app.post("/add/country-data")
async def country_data(id=int, year=int, country_id=int, healthcare_data_id=int, environmental_data_id=int, population_data_id=int):
    new_country_data = add_country_data(id, year, country_id, healthcare_data_id, environmental_data_id, population_data_id)
    if new_country_data:
        return {"message": "success"}
    else:
        raise HTTPException(status_code=400, detail="bad request")
    
@app.post("/add/population-data")
async def population_data(id=int, density=int, population=int, labor_force_participant=float, urban_population=int):
    new_population_data = add_population_data(id, density, population, labor_force_participant, urban_population)
    if new_population_data:
        return {"message": "success"}
    else:
        raise HTTPException(status_code=400, detail="bad request")
    
@app.post("/add/financial-data")
async def population_data(id=int, armed_forces_size=int, cpi=float, gasoline_price=float, gdp=int, minimum_wage=float, out_of_pocket_health_expenditure=float, tax_revenue=float, total_tax_rate=float, unemployment_rate=float):
    new_financial_data = add_financial_data(id, armed_forces_size, cpi, gasoline_price, gdp, minimum_wage, out_of_pocket_health_expenditure, tax_revenue, total_tax_rate, unemployment_rate)
    if new_financial_data:
        return {"message": "success"}
    else:
        raise HTTPException(status_code=400, detail="bad request")
    
@app.post("/add/educational-data")
async def educational_data(id=int, gross_primary_education_enrollment=float, gross_tertiary_education_enrollment=float):
    new_educational_data = add_educational_data(id, gross_primary_education_enrollment, gross_tertiary_education_enrollment)
    if new_educational_data:
        return {"message": "success"}
    else:
        raise HTTPException(status_code=400, detail="bad request")
    
@app.post("/add/environmental-data")
async def environmental_data(id=int, co2_emission=float, forested_area=float):
    new_environmental_data = add_environmental_data(id, co2_emission, forested_area)
    if new_environmental_data:
        return {"message": "success"}
    else:
        raise HTTPException(status_code=400, detail="bad request")
    
@app.post("/add/healthcare-data")
async def healthcare_data(id=int, birth_rate=float, fertility_rate=float, infant_mortaloty=float, life_expectancy=int, maternal_morality=float, physician_per_thousand=float):
    new_healthcare_data = add_healthcare_data(id, birth_rate, fertility_rate, infant_mortaloty, life_expectancy, maternal_morality, physician_per_thousand)
    if new_healthcare_data:
        return {"message": "success"}
    else:
        raise HTTPException(status_code=400, detail="bad request")