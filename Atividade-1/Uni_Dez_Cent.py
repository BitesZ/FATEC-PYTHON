#3. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
#dezenas e unidades do mesmo. Exemplo:
# 123 = 1 centena(s), 2 dezena(s) e 3 unidade(s)
# 12 = 1 dezena(s) e 2 unidade(s)

num1 = int(input("Digite um número menor que 1000"));

if num1 < 1000:
    cent = num1 // 100;
    dez = (num1 % 100) // 10;
    uni = num1 % 10;
    
    print(cent ," Centena");
    print(dez ," Dezena");
    print(uni ," Unidade")
else:
    print ("Número é maior que 1000, tente novamente.");