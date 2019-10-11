  #Dividindo o imperio

#a entrada está pronta
#criar um dicionario com as chaves sendo cada cidade e o valor sendo a quantidade de vezes que ela aparece(qtd de ligacoes)
#criar um loop que passa por cada cidade e subtrair o total de cidades pela qantidade de vezes que ela aparece

entrada = int(input())
l = []
for i in range(entrada):
  a,b = map(int,input().split())
  l += [(a,b)]
d = {}
for i in l:
  d[i[0]] = l.count(i[0])

#for i in range(1,entrada+1):
 # for j in l:


