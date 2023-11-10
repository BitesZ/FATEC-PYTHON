#2. Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, 
#mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. 
#Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, 
#o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor. 

vendedornm = str("Pedro Ricardo");

numvendas = int(5);

valvenda = float(2500.00);

salvendedor = float(3000.00);

comiss = float (250.00) + (valvenda * 0.05);

comisstotal = comiss * numvendas;

print("Vendedor: ", vendedornm)
print("Número de vendas: ", numvendas);
print("Comissão por venda: ", comiss);
print("Comissão total: ", comisstotal);
print("Salário inicial: ", salvendedor);


print("Valor total das vendas: ", valvenda * numvendas);

print("Salário total: ", salvendedor + comisstotal);