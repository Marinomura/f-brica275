#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor = int(input(" Valor a ser sacado que deve ser entre R$10 e R$600: "))
cem = int(valor//100)
valor = valor - (cem*100)
cinquenta = int(valor//50)
valor = valor - (cinquenta*50)
dez = int(valor//10)
valor = valor - (dez*10)
cinco = int (valor//5)
valor = valor - (cinco*5)
hum = valor

print('Notas de R$ 100,00 = ',cem)
print('Notas de R$ 50,00 = ', cinquenta)
print('Notas de R$ 10,00 = ', dez)
print("Notas de R$ 5,00 = ", cinco)
print('Notas de R$ 1,00 = ', hum)

#v_min =>10
#v_max =<600