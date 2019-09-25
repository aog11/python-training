#Chapter 6
#Table Printer practice project

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        print(str(tableData[j][i]).rjust(10),end='')
    print('')