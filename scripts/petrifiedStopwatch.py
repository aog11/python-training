# Chapter 15
# Petrified Stopwatch project

#! python3

# Importing the needed modules
import time, pyperclip

# Display the program's instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press CTRL-C to quit.')
input() # press Enter to begin

# List with the output of the stopwatch
outputLaps = []
outputLaps.append('Started')

print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        # Formatting the output and appending it to the list
        output = 'Lap #%s: %s (%s)' %(str(lapNum).rjust(1), str(totalTime).rjust(5), str(lapTime).rjust(5))
        outputLaps.append(output)
        print(output, end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Pasting the output to the clipboard
    outputLaps.append('Done.')
    pyperclip.copy('\n'.join(outputLaps))
    # Handle the CTRL-C exception to keep its error message from displaying
    print('\nDone.')