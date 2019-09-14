#Robô linear
#Questão 1 e questão 2
entrada = input('Digite a sequencia de comandos para o robô: ').lower()
metros_andados = 0
for letra in entrada:
  if letra == 'f':
    metros_andados += 1
  else:
    metros_andados -= 1
if metros_andados < 0:
  metros_andados *= (-1)
print(metros_andados)
if metros_andados != 0:
  print('Com essa sequencia a posição final do robô não é igual a sua posição inicial: %s'%entrada)