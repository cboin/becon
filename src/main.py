#!/usr/bin/env python3

import argparse
import os
from sys import stderr
from getpass import getpass
import src.file as bfile
from Crypto.Cipher import AES

list_cmd = ["list", "get", "add", "help"]

def initialize_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action='version', version='%(prog)s 1.0')
    parser.add_argument("account", type=str, nargs=1,
                        help="connect to the account or create it")
    parser.add_argument("-d", "--delete", action="store_true",
                        help="delete an account")
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

def help():
    print("\tlist - list all host")
    print("\tget <host> - copy host password into clipboard")
    print("\tadd <host> - add an host")
    print("\tdelete <host> - delete host")
    print("\thelp - print list of commands")
            
def loop(account_name):
    print("Connecting the account:", account_name)
    file_path = bfile.dir_config + "/" + account_name
    crypted_pw = None
    pw = None
    
    # Get the crypted pw
    with open(file_path, 'r') as f:
        crypted_pw = f.readline()
    crypted_pw = crypted_pw.rstrip()
        
    # Verifying the password
    while(True):
        pw = getpass("Your master password: ")
        # TODO : Crypt pw
        if pw == crypted_pw:
            break
        else:
            print("error: password do not match", end="\n\n")
            print(pw, crypted_pw)
    
    # Main loop
    while(True):
        print("For commands type 'help'", end="\n\n")
        cmd = input('> ').split(' ')
        if cmd[0] not in list_cmd:
            print("error: command not recognized")
            help()
        else:
            if cmd[0] == "list":
                bfile.list(file_path)
            elif cmd[0] == "help":
                print("List of commands:")
                help()
            elif cmd[0] == "get":
                if len(cmd) == 2 and cmd[1] != '':
                    bfile.get(cmd[1], file_path)
                else:
                    print("error: command not recognized")
                    help()
                
    
def main():
    args = initialize_parser()
    if (args.delete and args.modify):
        print(os.path.basename(__file__) + ":", "error: there can be only one argument",
              file=stderr)
    elif (args.delete):
        delete_account(args.account[0])
    else:
        if not os.path.exists(bfile.dir_config):
            bfile.mkdir(bfile.dir_config)

        file_path = bfile.dir_config + "/" + args.account[0]
        if os.path.isfile(file_path):
            loop(args.account[0])           
        else:
            create_account(args.account[0])
