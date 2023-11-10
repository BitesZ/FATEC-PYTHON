#4. Faça um Programa que leia os 3 lados de um triângulo. O programa deverá informar se os valores
#podem ser um triângulo. Se sim, calcule e mostre a área do triângulo.

l1 = float(input("Lado 1 do Triangulo: "));
l2 = float(input("Lado 2 do Triangulo: "));
l3 = float(input("Lado 3 do Triangulo: "));


if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print("É um triangulo.");
    s = (l1 + l2 + l3) / 2;
    area = (s * (s - l1) * (s - l2) * (s - l3)) * 0.5;
    print("Area do triangulo: ", area);
else:
    print("Não é um triangulo.");