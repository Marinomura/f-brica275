#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:​

#Tabuada de 5:​
#5 X 1 = 5​
#5 X 2 = 10​
#...​
#5 X 10 = 50​

num = int(input('Digite qual tabuada você deseja: '))
print('*'*20, 'TABUADA DO',num, "*"*20)
for i in range(1,11):
    print(f'{num} x {i} = {num*i}')
    