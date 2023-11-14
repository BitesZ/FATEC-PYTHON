#Leitura de notas indefinidas

notas = []

i = 0;

while i != 1:
    nota = float(input(Digite nota: ))
    if nota > 0 and nota < 11:
        notas.append(nota)
    else:
        i+1
        break

print("\n---------Resultados---------\n")

#Exibir todos os valores e quantidade de valores lidos

cont = int(0)

for x in notas:
    cont = cont + 1


print(notas)
print("Numero de notas lida: ", cont)

#Exibir o maior e o menor valor

min = float(10)
max = float(0)

for nota in notas:
    if nota < min:
        min = nota
    elif nota > max:
        max = nota

print("Maior nota: ", max)
print("Menor nota: ", min)

#Calcular e mostrar a média das notas

total = float(0)

for nota in notas:
    if nota > total:
        total = nota
    else:
        total = total + nota

total = total / cont

print("Média da nota: {:.1f}".format(total))

#Mostrar valores acima da media calculada
maiornota = []

for nota in notas:
    if nota > total:
        maiornota.append(nota)

print("Notas maiores que a média: ",maiornota)
#Alterar todas as notas 5 para 6
i = 0

while i < cont:
    if notas[i] == 5:
        notas[i] = 6
    i = i + 1

#Exibir todos os valores após modificações

print(notas)
