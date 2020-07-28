#! //anaconda3/bin/python3
# 此為程式腳本script
# to operate the script, we must write the path of the interpreter (type “which python3” to obtain the address in terminal)
# mapIt.py (launches a map in the browser using an address from the command line or clipboard.)

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # web address is given in the terminal
    address = ' '.join(sys.argv[1:])
else:
    # web address is given in the clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com.tw/maps/place/' + address)