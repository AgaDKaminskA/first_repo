path = 'C: \\Users\\vdi-student\\Pulpit\\ rozliczenie.csv'
mode = 'r'

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



