import mysql.connector
import database_config

mydb = mysql.connector.connect(
  host=database_config.host,
  user=database_config.user,
  password=database_config.password,
  port=database_config.port,
  database=database_config.database
)

file = open("Country.csv")
lines = file.readlines()
file.close()
cursor = mydb.cursor()
cursor.execute("truncate table country")
first = True
for line in lines:
  if first:
    first = False
    continue
  line = line.replace("\n","").split(",")
  stmnt=f"insert into country(id, name, landArea) values ({line[0]}, \"{line[1]}\", \"{line[2]}\")"
  cursor.execute(stmnt)
  print(stmnt)
mydb.commit()

file = open("HappinesReportScore.csv")
lines = file.readlines()
file.close()
cursor = mydb.cursor()
cursor.execute("truncate table happinesreportscore")
first = True
i = 1
for line in lines:
  if first:
    first = False
    continue
  line = line.replace("\n","").split(",")
  print(line)
  stmnt=f"insert into happinesreportscore(id, countryId, year, score) values ({i}, {line[0]}, {line[1]}, {line[2]})"
  i+=1
  cursor.execute(stmnt)
  print(stmnt)
mydb.commit()

file = open("EnvironmentalData.csv")
lines = file.readlines()
file.close()
cursor = mydb.cursor()
cursor.execute("truncate table environmentaldata")
first = True
i = 1
for line in lines:
  if first:
    first = False
    continue
  line = line.replace("\n","").split(",")
  print(line)
  stmnt=f"insert into environmentaldata(id, Co2Emmission, forestedArea) values ({line[0]}, {line[1]}, {line[2]})"
  i+=1
  cursor.execute(stmnt)
  print(stmnt)
mydb.commit()

file = open("EducationalData.csv")
lines = file.readlines()
file.close()
cursor = mydb.cursor()
cursor.execute("truncate table educationaldata")
first = True
i = 1
for line in lines:
  if first:
    first = False
    continue
  line = line.replace("\n","").split(",")
  print(line)
  stmnt=f"insert into educationaldata(id, GrossPrimaryEducationEnrollment, GrossTertiaryEducationEnrollment) values ({line[0]}, {line[1]}, {line[2]})"
  i+=1
  cursor.execute(stmnt)
  print(stmnt)
mydb.commit()


file = open("FinanciallData.csv")
lines = file.readlines()
file.close()
cursor = mydb.cursor()
cursor.execute("truncate table financialdata")
first = True
i = 1
for line in lines:
  if first:
    first = False
    continue
  line = line.replace("\n","").split(",")
  print(line)
  stmnt=f"insert into financialdata values ({line[0]}, {line[1]}, {line[2]},{line[3]},{line[4]}, {line[5]},{line[6]},{line[7]},{line[8]},{line[9]})"
  i+=1
  cursor.execute(stmnt)
  print(stmnt)
mydb.commit()


file = open("HealthcareData.csv")
lines = file.readlines()
file.close()
cursor = mydb.cursor()
cursor.execute("truncate table healthcaredata")
first = True
i = 1
for line in lines:
  if first:
    first = False
    continue
  line = line.replace("\n","").split(",")
  print(line)
  stmnt=f"insert into healthcaredata values ({line[0]}, {line[1]}, {line[2]},{line[3]},{line[4]}, {line[5]},{line[6]})"
  i+=1
  cursor.execute(stmnt)
  print(stmnt)
mydb.commit()

file = open("PopulationData.csv")
lines = file.readlines()
file.close()
cursor = mydb.cursor()
cursor.execute("truncate table populationdata")
first = True
i = 1
for line in lines:
  if first:
    first = False
    continue
  line = line.replace("\n","").split(",")
  print(line)
  i+=1
  stmnt=f"insert into populationdata values ({line[0]}, {line[1]}, {line[2]},{line[3]},{line[4]})"
  cursor.execute(stmnt)
  print(stmnt)
mydb.commit()


cursor = mydb.cursor()
cursor.execute("truncate table countrydata")
for index in range(i):
  stmnt=f"insert into countrydata values ({index}, {2023}, {index},{index},{index}, {index}, {index}, {index})"
  cursor.execute(stmnt)
  print(stmnt)
  mydb.commit()


mydb.close()
