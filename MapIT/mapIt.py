import webbrowser,sys,pyperclip
if len(sys.argv) > 0:
	address=' '.join(sys.argv[1:])
else:
	address=pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/'+address)
