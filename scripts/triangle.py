def triangle(number):
    if number == 0:
        print ('The number must be greater than 0')
    for i in range(number + 1):
        if i != 0:
            print ('*' * i)

triangle(5)