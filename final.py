import csv
import pandas as pd

data1 = []
data2 = []

with open("brightstar.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data1.append(row)

with open("finaldstar.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data2.append(row)
        
header1 = data1[0]
star_data1 = data1[1:]

header2 = data2[0]
star_data2 = data2[1:]

headers = header1 + header2

star_data = []

for i in star_data1:
    star_data.append(i)

for j in star_data2:
    star_data.append(j)
    
with open("finaloutput.csv", "w", encoding= "utf8") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)

df = pd.read_csv("finaloutput.csv")
print(df.tail(8))
    