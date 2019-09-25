#Chapter 6
#Table Printer practice project

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

'''
#Old code
for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        print(str(tableData[j][i]).rjust(10),end='')
    print('')
'''
#New code
def printTable(table):
    columnWidth = []
    justWidth = []
    rowWidth = len(table)

    for i in table:
        columnWidth.append(len(i))
    columnWidth.sort()
    columnWidth = columnWidth[-1]

    for i in table:
        for j in i:
            justWidth.append(len(j))
    justWidth.sort()
    justWidth = justWidth[-1]

    for i in range(columnWidth):
        for j in range(rowWidth):
            print(str(table[j][i]).rjust(justWidth),end='')
        print('')

printTable(tableData)