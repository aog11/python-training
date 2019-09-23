def collatz(number):
    if number%2 == 0:
        return (number // 2)
    else:
        return (3 * number + 1)

print ('Enter number:')
while True:
    try :
        result = collatz(int(input()))
        print (str(result))
        if result == 1:
            break;
    except ValueError:
        print ('Please input a valid integer')
    
