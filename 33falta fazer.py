#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))
operacao = input("Digite a operação que deseja realizar: [+, -, /, *]: ")
par =(n1 or n2 /2)
#Se diferente de 0 e divisivel por 2 (' Então o número é par')
