# main.py
# Steven Tsang May 2022
# Description: A python script that will print out all words inside a given textfile.

from pynput.keyboard import Key, Controller
import keyboard
import ctypes  # An included library with Python install.   
import time

start_time = time.time()
fileName = "listOfWords.txt" # please separate words using ","
countDown = 5

def typer(phrase):
    for word in myPhrase:
        num = 0
        for letter in word:
            if (keyboard.is_pressed('Esc')):
                return()
            if (letter != ' ' and num != 0):
                key.press(letter)
                key.release(letter)
            elif (letter == ' ' and num != 0):
                key.press(letter)
                key.release(letter)

            num+=1

        key.press(Key.enter)
        key.release(Key.enter)
        time.sleep(0.5)

print("Starting in", countDown, "seconds...")

for i in range(countDown):
    print(countDown-i)
    time.sleep(1)

textFile = open(fileName)

key = Controller()

myPhrase = textFile.readline().split(",")

typer(myPhrase)

time_took = (round(time.time() - start_time, 3))
ctypes.windll.user32.MessageBoxW(0, "Program finished running at: " + str(time_took) + " seconds." , "Finished!", 0)
