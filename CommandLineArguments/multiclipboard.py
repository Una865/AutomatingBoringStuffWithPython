#! python3
#multiclipboard.py - saves,loads an deletes text from and onto the clipboard
#Usage: python multiclipboard.py save <keyword> - saves clipboard to keyword
#       python multiclipboard.py <keyword> - loads text for that keyword to clipboard
#       python multiclipboard.py list - loads all keywords to a clipboard
#       python multiclipboard.py delete <keyword> - delete keyword and text specified for it

import shelve
import pyperclip
import sys
import argparse

multiclipShelf = shelve.open('multiclip')

ap = argparse.ArgumentParser()
ap.add_argument('cmd', action =  'store')
ap.add_argument('keyword', action = 'store',nargs='?')
args = vars(ap.parse_args())

if args['cmd'].lower() == 'save':
    if args['keyword'] is not None:
        multiclipShelf[args['keyword']] = pyperclip.paste()
elif args['cmd'] == 'delete':
    if args['keyword'] is not None:
      del multiclipShelf[args['keyword']]
    else:
        multiclipShelf.clear()
elif args['keyword'] is None:
    if args['cmd'].lower() == 'list':
        pyperclip.copy(str(list(multiclipShelf.keys())))
        print('List of keywords copied to the clipboard.')
    else:
        pyperclip.copy(multiclipShelf[args['cmd']])
        print('Value under the keyword is copied to the clipboard.')

multiclipShelf.close()
