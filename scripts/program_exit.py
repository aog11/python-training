import sys

while True:
    print ('Type exit to exit')
    response = input()
    if response.lower() == 'exit':
        sys.exit()
    print ('You typed ' + response + '.')
