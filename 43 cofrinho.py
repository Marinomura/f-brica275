#Dani tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu poupar.
# Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor total economizado, em reais.
# Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real.
# Não havendo moeda de um tipo, a quantidade respectiva é zero. ​
valor = int(input(" Qual as moedas depositas: "))
vinte_cinco=int(valor//25)
valor= valor - (vinte_cinco*25)
cinquenta = int(valor//50)
valor = valor - (cinquenta*50)
dez = int(valor//10)
valor = valor - (dez*10)
cinco = int (valor//5)
valor = valor - (cinco*5)
hum = valor

print('Moedas de R$ 0,25 = ',vinte_cinco)
print('Moedas de R$ 0,50 = ', cinquenta)
print('Moedas de R$ 10,00 = ', dez)
print("Moedas de R$ 5,00 = ", cinco)
print('Moedas de R$ 1,00 = ', hum)
