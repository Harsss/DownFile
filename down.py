
import webbrowser as web

import keyboard
import time
def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

f=open('lik.txt','r')
for a in f:
    c,b=(findOccurrences(a,'"'))
    k=(a[c+1:b])
    web.open(k)
    time.sleep(2)

    keyboard.press_and_release('s') 
    keyboard.press_and_release('ctrl+w') # Change accordin to Mac 
    