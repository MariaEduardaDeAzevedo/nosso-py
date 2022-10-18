p=1
pasd=0
while (p<=100):
  atual=int(input())
  if(atual>pasd):
    pasd=atual
    posicao=p
  p+=1
print(pasd)
print(posicao)