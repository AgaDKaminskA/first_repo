path = 'C:\Users\vdi-student\Desktop\\rozliczenie.csv'
mode = 'r'
#zapis danych w odpowiedniej postaci

with open(path, mode) as plik:
    content = plik.readlines()

print(content)
for i in range(len(content)):
    content[i] = content[i].split(',')
print(content)
print(content[3][3])

#obliczanie sredniej wypłaty

total = 0
for i in range (1,len(content)):
    total = total + int(content[i][1])
average = total / (len(content)-1)
print = (rounde(average, 2))

#ilość kobiet na macierzyńskim

for i in range (1,len(content)):
    if content[i][3] =='k' and content[i][4] == 't':
        total += 1
print(total)





