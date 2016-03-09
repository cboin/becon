#!/usr/bin/env python3

import argparse
import os
from sys import stderr

def initializeParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action='version', version='%(prog)s 1.0')
    parser.add_argument("account", type=str, nargs=1,
                        help="connect to the account or create it")
    parser.add_argument("-d", "--delete", action="store_true",
                        help="delete an account")
    parser.add_argument("-m", "--modify", action="store_true",
                        help="modify the master password")
    return parser.parse_args()

if __name__ == "__main__":
    args = initializeParser()
    if (args.delete and args.modify):
        print(os.path.basename(__file__) + ":", "error: there can be only one argument",
              file=stderr)
    elif (args.delete):
        print("deleting the account:", args.account)
    elif (args.modify):
        print("modifying the account:", args.account)
    else:
        print("connecting to the account:", args.account)

    
