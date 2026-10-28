valores = input().split()

lista = []
for i in valores:
    lista.append(int(i))

lista_ordenada = sorted(lista)

for i in lista_ordenada:
    print(i)

print("")

for i in lista:
    print(i)