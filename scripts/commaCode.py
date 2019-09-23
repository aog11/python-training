def commaString(values):
    result = ''
    counter = 0
    for i in values:
        if i == values[-1]:
            result += ' and ' + i
        elif i == values[-2]:
            result += '' + i
        else:
            result += i + ', '
        counter += 1
    print (result)

spam = ['Anne','Louis','Herb','Thomas','Peter','Lucas','Bill']
commaString(spam)
