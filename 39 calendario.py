#Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano.
#Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias. ​
mes=30
ano=365

dia=input('Digite uma data: ')
mes=input('Digite o mês desejado: ')
inicio_ano = 2023
print('Quantos dias se passam desde o inicio do ano? ')
calc_dia= dia 
calc_mes = int(mes-1)*30 
print ('\n')
print ('Data informada: ',(dia), 'de', (mes), 'de ', (inicio_ano))
if mes != 0 or 12:
    print ('INVALIDO')

