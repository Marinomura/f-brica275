#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))
op = input("Digite a operação: ")

match(op):
    case '+':
        soma =n1+n2
        print(f'{n1}+{n2} = {soma}')

    case '-':
        sub = n1-n2
        print(f'{n1}-{n2}= {sub}')

    case '*':
        multi = n1*n2
        print(f'{n1}*{n2}= {multi}')

    case '/' :
        div = n1/n2
        print(f'{n1}/{n2} = {div}')

#Se diferente de 0 e divisivel por 2 (' Então o número é par')
