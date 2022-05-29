# n >= 2 (anterior impar e posterior par)

numentrada = int(input(''))
impar = 0
par = 0

if numentrada >= 2:
  if numentrada % 2 == 0:
    impar = numentrada - 1
    par = numentrada + 2
  else:
    impar = numentrada - 2
    par = numentrada + 1 

  print(impar,par)