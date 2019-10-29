# Testing Python's JSON module with the PokeAPI

#! python3

# Importing the needed modules
import sys, requests, json, pyperclip

# Asking for the pokemon to look for in case it wasn't given
if len(sys.argv) < 2:
    print('Please enter the pokemon to search: ', end='')
    sys.argv.append(input())

# Displaying information about the pokemon
def giveData(response):
    # Requesting the pokemon data
    pokemon = str(' '.join(sys.argv[1:])).lower()
    res = requests.get('https://pokeapi.co/api/v2/pokemon/%s' %(pokemon))

    # Working with a valid pokemon
    if res.text == 'Not Found':
        print('Pokemon %s not found.' %(pokemon))
        sys.exit()
    else:
    # Loading the JSON data
        pokeData = json.loads(res.text)

    # Putting the data on the screen or pasting it to the clipboard
    if response.lower() == 's':
        # Basic info
        print('Basic info')
        print('-'*20)
        print('Name: %s' % (str(pokeData['name']).capitalize()))
        print('Height: %s m' % (str(pokeData['height']/10).capitalize()))
        print('Weight: %s kg' % (str(pokeData['weight']/10).capitalize()))

        # Abilities
        print('\nAbilities')
        print('-'*20)
        for abilityIdx in range(len(pokeData['abilities'])):
            print('%s' % (str(pokeData['abilities'][abilityIdx]['ability']['name']).capitalize()))

        # Moves
        print('\nMoves')
        print('-'*20)
        for moveIdx in range(len(pokeData['moves'])):
            print('%s' % (str(pokeData['moves'][moveIdx]['move']['name']).capitalize()))
    elif response.lower() == 'c':
        clipData = []
        # Basic info
        clipData.append('Basic info')
        clipData.append('-'*20)
        clipData.append('Name: %s' % (str(pokeData['name']).capitalize()))
        clipData.append('Height: %s m' % (str(pokeData['height']/10).capitalize()))
        clipData.append('Weight: %s kg' % (str(pokeData['weight']/10).capitalize()))

        # Abilities
        clipData.append('\nAbilities')
        clipData.append('-'*20)
        for abilityIdx in range(len(pokeData['abilities'])):
            clipData.append('%s' % (str(pokeData['abilities'][abilityIdx]['ability']['name']).capitalize()))

        # Moves
        clipData.append('\nMoves')
        clipData.append('-'*20)
        for moveIdx in range(len(pokeData['moves'])):
            clipData.append('%s' % (str(pokeData['moves'][moveIdx]['move']['name']).capitalize()))
        
        # Pasting to the clipboard
        pyperclip.copy('\n'.join(clipData))
        print('Done.')

# Giving the option to have the information on screen or to the clipboard
while True:
    try:
        print('Would you like the information on screen or pasted to the clipboard? (S/C): ', end='')
        response = input()
        if response.lower() not in ('s','c'):
            raise Exception('Please enter a valid option Screen(S) or Clipboard(C).')
        giveData(response)
        break
    except Exception as err:
        print (err)