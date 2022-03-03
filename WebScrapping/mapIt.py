#! python3
# mapIt - Launches a map in the browser using an address from
# the command line or clipboard

import argparse
import pyperclip
import webbrowser


ap = argparse.ArgumentParser()
ap.add_argument('street', action = 'store' , nargs = '*')
args = vars(ap.parse_args())
print(type(args['street']))

streetAdr  = ''

if args['street'] == None:
    streetAdr = pyperclip.paste()
else:
    streetAdr = ' '.join(args['street'])

webbrowser.open('https://www.google.com/maps/place/'+streetAdr)








