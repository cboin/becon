#!/usr/bin/env python3
# coding: utf8

import os.path
from os.path import expanduser
try:
    import pyperclip
except ImportError:
    from sys import stderr
    print("error: you need pyperclip library to run the program", file=stderr)
    exit(1)

home = expanduser("~")
dir_config = home + "/.config/becon"

def mkdir(path):
    if not (os.path.exists(path)):
        os.makedirs(path)

def add_host(host, user, password, f):
    found = False
    with open(f, 'r') as db:
        account = host + ":" + user + ":" + password

        for line in db.readlines():
            if account in line:
                found = True

    if not found:
        with open(f, 'a') as db:
            db.write(account + "\n")

def get(host, f):
    found = False
    with open(f, 'r') as bfile:
        for line in bfile:
            if host in line:
                account = line.split(":")
                found = True
                if found:
                    print("Host: " + account[0])
                    print("Nickname: " + account[1])
                    pyperclip.copy(account[2])
                    print("Password has been copied to clipboard.")
                else:
                    print(host + " not found.")
