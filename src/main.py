#!/usr/bin/env python3

import argparse
import os
from sys import stderr
from getpass import getpass
import src.file as bfile
from Crypto.Cipher import AES

def initialize_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action='version', version='%(prog)s 1.0')
    parser.add_argument("account", type=str, nargs=1,
                        help="connect to the account or create it")
    parser.add_argument("-d", "--delete", action="store_true",
                        help="delete an account")
    parser.add_argument("-m", "--modify", action="store_true",
                        help="modify the master password")
    return parser.parse_args()

def encrypt(master, host, data):
    encryption_suite = AES.new(master, AES.MODE_CBC, host)
    return encryption_suite.encrypt(data)

def decrypt(master, host, data):
    decryption_suite = AES.new(master, AES.MODE_CBC, host)
    return decryption_suite.decrypt(data)

def delete_account(account_name):
    file_path = bfile.dir_config + "/" + account_name
    if os.path.isfile(file_path):
        print("Deleting the account:", account_name)
        confirm = input("Are you sure ? [y/N] ")
        if (confirm == "" or confirm.lower() == 'n'):
            print("Canceled")
        else:
            os.remove(file_path)
            print("The account {} is now removed".format(account_name))
    else:
        print("The account {} doesn't exists".format(account_name))
        
def create_account(account_name):
    print("Create the account:", account_name)
    while(True):
        # TODO : crypt the password
        pw = getpass("Your master password: ")
        if getpass("Verify password: ") == pw:
            with open(bfile.dir_config + "/" + account_name, 'x') as acc_file:
                acc_file.write(pw)
            return
        else:
            print("error: password do not match", end="\n\n")
                    
def main():
    args = initialize_parser()
    if (args.delete and args.modify):
        print(os.path.basename(__file__) + ":", "error: there can be only one argument",
              file=stderr)
    elif (args.delete):
        delete_account(args.account[0])
    elif (args.modify):
        print("Modifying the account:", args.account)
        # TODO
    else:
        if not os.path.exists(bfile.dir_config):
            bfile.mkdir(bfile.dir_config)

        file_path = bfile.dir_config + "/" + args.account[0]
        if os.path.isfile(file_path):
            print("Connecting the account:", args.account)
            # TODO
        else:
            create_account(args.account[0])
