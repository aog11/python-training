def factorial(number):
    result = 1
    for i in reversed(range(number + 1)):
        if i == 0:
            break
        result *= i
    print ('The factorial of ' + str(number) + ' is ' + str(result))

print ('Please enter a number ', end='')
inNumber = int(input())
factorial(inNumber)
