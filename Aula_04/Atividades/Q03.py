numero = float(input("Digite o número de maças compradas: "))

if numero < 12:
    print("O valor total da sua compra é: R$", numero * 1.3)
else:
    print("O valor total da sua compra é: R$", float(numero * 1))
