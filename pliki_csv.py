path = 'C:\\Users\\vdi-student\\Desktop\\rozliczenie.csv'
mode = 'r'
#wypisanie zawartości

with open(path, mode) as plik:
    content = plik.readlines()
print(content)

for i in range(len(content)):
    print(content[i])
    content[i] = content[i].split(',')
print(content[i])
print(content[2][2])

#obliczanie sredniej wypłaty

total = 0
for i in range(1, len(content)):
    print(content[i][1])
    total = total + int(content[i][1])
print('Suma wynagrodzeń;', total)

#średnia wypłata
average = total / (len(content)-1)
print(average)
print('Srednia wynagrodzeń', round(average, 2))

#ilość kobiet na macierzyńskim

total = 0
for i in range(1, len(content)):
    #print(content[i])
    content[i][4] = content[i][4].replace('\n', '')
    if content[i][4] == 't' and content[i][3] == 'k':
        total += 1
print(total)





