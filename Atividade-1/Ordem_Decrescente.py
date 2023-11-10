#5. Faça um programa para ler 3 valores inteiros e escrevê-los em ordem decrescente.

v1 = int(input("Digite Valor 1: "));
v2 = int(input("Digite Valor 2: "));
v3 = int(input("Digite Valor 3: "));


valores = [v1, v2, v3];
valores.sort(reverse=True);

print("Valores em ordem decrescente: ", valores);