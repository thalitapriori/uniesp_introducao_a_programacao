valor1 = float(input("Digite a primeiro valor: "))
valor2 = float(input("Digite a segundo valor: "))

maior = 0
menor = 0

if(valor2 > valor1):
    maior = valor2
    menor = valor1
else:
    maior = valor1
    menor = valor2

print('Os números informados em ordem crescente: ', menor, ",", maior )
