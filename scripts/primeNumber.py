for i in range(1,101,1):
    contador = 0
    for j in range(1,i + 1,1):
        if i%j == 0:
            contador += 1
    if contador == 2:
        print (str(i) + ' is a prime number.')