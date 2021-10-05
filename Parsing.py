import xml.etree.cElementTree as et 
import csv

tree = et.parse ("covid_cases_xml.xml")
root = tree.getroot()
Date_reported = []
countries.