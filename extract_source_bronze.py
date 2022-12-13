#Script para realizar extracción desde el origen de datos y almacenar en la zona bronze

import csv
import io
import urllib.request

url = "https://raw.github.com/datasets/gdp/master/data/gdp.csv"
webpage = urllib.request.urlopen(url)
datareader = csv.reader(io.TextIOWrapper(webpage))

for row in datareader:
    print(row)