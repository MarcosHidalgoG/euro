from collections import defaultdict
import csv

data = []

#--------------APERTURA Y LECTURA DE FICHERO E INSERCION A DATA-----------------#
with open('./docs/EURO.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append({'date' : row['DATE'], 'n1': row['N1'], 'n2': row['N2'], 'n3': row['N3'], 'n4': row['N4'], 'n5': row['N5'], 'star1': row['STAR1'], 'star2': row['STAR2']})
#------------./APERTURA Y LECTURA DE FICHERO E INSERCION A DATA-----------------#
# crear un diccionario para contar la frecuencia de cada número
counts = defaultdict(int)
countsStar = defaultdict(int)
for d in data:
    for k, v in d.items():
        if k.startswith('n'):
            counts[v] += 1
        elif k.startswith('star'):
            countsStar[v] += 1

# ordenar el diccionario por frecuencia y obtener los números más repetidos
most_commonNumbers = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10] 
most_arrayNumber = [k for k, v in most_commonNumbers]
most_arrayNumber.sort()

most_commonStars = sorted(countsStar.items(), key=lambda x: x[1], reverse=True)[:4]
most_arrayStar = [k for k, v in most_commonStars]
most_arrayStar.sort()

print("\tResultado más probable para el siguiente euromillón\n\t\t", most_arrayNumber, "*", most_arrayStar)


