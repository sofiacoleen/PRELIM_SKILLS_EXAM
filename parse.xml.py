import xml.etree.cElementTree as et 
import csv

tree = et.parse ("covid_cases_xml.xml")
root = tree.getroot()
Date_reported = []
Countries_territories = []
Cases_number = []
Death_number = []

for date in root.iter("dateRep"):
    Date_reported.append (date.text)
for countries in root.iter("countries"):
    Countries_territories.append (countries.text)
for cases in root.iter("cases"):
    Cases_number.append (cases.text)
for deaths in root.iter("deaths"):
    Death_number.append (deaths.text)

covid_cases = open("covid_cases_parse", "w")
writer = csv.writer(covid_cases)
writer.writerow(["Date_reported","Countries_territories", "Cases_number", "Death_number"])
for i in range (len(Date_reported)):
    writer.writerow([Date_reported[i], Countries_territories[i], Cases_number[i], Death_number[i]])
    