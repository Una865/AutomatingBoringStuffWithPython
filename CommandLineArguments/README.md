# Command line arguments using argparse

## argparse is a command-line parsing module in Python
Examples of use of argparse:

 - **replaceWords.py** : the python script takes one argument from command line which represents the text file (in my case **test.txt**) from which it needs to extract text which will be processed. The code is replacing every occurence of **ADJECTIVE, NOUN or VERB** with words from the user input. The processed text then write in a text file **results.txt** (one example is written).
 - **pw.py** - not very safe password software. In this python script you can write your passwords for different accounts (which I would not reccomend, it is just for practice) as a dictionary. For example passwords['email'] would return password for your email. Executing this script through command line with one argument as a name of the account, this script will copy to clipboard your password for that accound. It does that using the passed argument from command line.  
- **multiclipboard.py** : python script for saving text from the clipboard under specified keywords. Sometimes we need to fill out texts forms and we need multiple things saved on clipboard, but unfortunately it is not possible. Calling this script from terminal and using appropriate keywords (you can find help for usage at the beginning of the script) you can instantly save all the text from the clipboard under desired keyword. Each piece of text is saved under keywords and if the user forgets what he/she saved, there is a list command to show all saved keywords.


Additional notes: in **multiclipboard.py** I used shelve module. It is used for persistent data storage that your program can later restore to variables. It is a dictionary-like object.
