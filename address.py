import os
import webbrowser

# read selected text
sel = os.popen('xsel').read()
url = 'https://google.com/maps/search/' + sel

# open new tab from selected text url
webbrowser.open_new_tab(url)
