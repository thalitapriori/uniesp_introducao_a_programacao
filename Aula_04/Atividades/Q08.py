def verificar_saldo_positivo(X):
    if X >= 0 :
        return True
    return False

quantAtualEstoque  = float(input("Digite a quantidade atual em estoque do produto: "))
quantMaximaEstoque = float(input("Digite a quantidade máxima em estoque do produto: "))
quantMinimaEstoque = float(input("Digite a quantidade mínima em estoque do produto: "))

quantMediaEstoque = (quantMaximaEstoque + quantMinimaEstoque) / 2

if quantAtualEstoque >= quantMediaEstoque:

    print('Não efetuar compra')
else:

    print('Efetuar compra')
