nºconta = input("Digite o numero da conta")
saldo = float(input("Digite saldo"))
debito = float(input("Digite o valor débito"))
credito = float(input("Digite o valor crédito"))
Saldoatual = saldo-debito+credito

if Saldoatual <=0:
    print("O saldo atual é Negativo")
else:
    print("O saldo é Positivo")
