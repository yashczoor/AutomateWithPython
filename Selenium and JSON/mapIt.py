#! python3
#mapIt.py - launches a map in the browser using an address from the command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #get address from cl
    address = ' '.join(sys.argv[1:])

    #adddress from clipboard
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
