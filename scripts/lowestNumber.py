def highestByAntoni(List):
    greatest = 0
    for i in List:
        for j in List:
            if i!=j and i > j and i > greatest:
                greatest = i
    print('The highest number is ' + str(greatest))

print ('Please enter an amount of numbers to compare:', end=' ')
amount = int(input())
Numbers = []

for i in range(1, amount + 1, 1):
    Numbers.append(int(input()))

highestByAntoni(Numbers)