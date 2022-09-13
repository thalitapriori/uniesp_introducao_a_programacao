numeroConta  = int(input("Digite o número da conta: "))
saldoConta   = float(input("Digite o Saldo da Conta: "))
debitoConta  = float(input("Digite o valor a ser debitado na conta: "))
creditoConta = float(input("Digite o valor a ser creditado na conta: "))

saldoAtualConta = (saldoConta - debitoConta) + creditoConta

if saldoAtualConta >= 0:

    print('O saldo da sua conta de número', numeroConta, 'é Positivo. Valor do Saldo: R$', saldoAtualConta)
else:

    print('O saldo da sua conta de número', numeroConta, 'é Negativo. Valor do Saldo: R$', saldoAtualConta)
