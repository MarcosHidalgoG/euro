import csv
data = []
with open('./docs/EURO.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append({'date' : row['DATE'], 'n1': row['N1'], 'n2': row['N2'], 'n3': row['N3'], 'n4': row['N4'], 'n5': row['N5'], 'star1': row['STAR1'], 'star2': row['STAR2']})
print(data)