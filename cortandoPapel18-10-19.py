n = int(input()) #numero de retângulos
alturas = [int(i) for i in input().split()] #entrada desse jeito: 1 2 3 4. O split retorna uma lista onde cada numero da entrada representa um elemento dessa lista. Cada elemento da lista é convertido para inteiro.
alturas_ordenadas = sorted([(alturas[i],i+1) for i in range(n)]) # "range" de 0 até o numero de retangulos(passando pelos indices). Tupla é criada com cada numero da lista acima e seu respectivo indice+1. A lista com as tuplas é ordenada

colunas = [1 for i in range(n+2)] #lista com len de n+2 só com o número 1
colunas[0],colunas[-1] = 0, 0#primeiro e último elementos passam a ser 0

melhor_corte, variavel = 2, 2 #numero mínimo possível de papéis após o corte na horizontal.
for i in alturas_ordenadas:
  altura, indice = i
  colunas[indice] = 0
  if variavel > melhor_corte:
    melhor_corte = variavel
  if colunas[indice+1] == 0 and colunas[indice-1] == 0:#retangulos adj menores
    variavel -= 1
  if colunas[indice+1] == 1 and colunas[indice-1] == 1:#retangulos adj maiores
    variavel += 1

print(melhor_corte)