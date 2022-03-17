Vetor = [0,0,0,0,0,0,0,0,0,0]
a = int(input())

for i in range(len(Vetor)):
  Vetor[i] = a
  a = a * 2
  print('Vetor[{}] = {}'.format(i, Vetor[i]))