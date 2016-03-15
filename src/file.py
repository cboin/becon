#!/usr/bin/env python3
# coding: utf8

import os.path
import pyperclip
from os.path import expanduser

home = expanduser("~")

dir_config = home + "/.config/becon"

def mkdir(path):
    if not (os.path.exists(path)):
        os.makedirs(path)

def touch(path, f):
    if not (os.path.isfile(path + "/" + f)):
        open(path + "/" + f, 'a').close()

def add_account(host, user, password, f):
    db = open(f, 'r')
    found = False
    account = host + ":" + user + ":" + password

    for line in db.readlines():
        if account in line:
            found = True

    if not found:
        db = open(f, 'a')
        db.write(account + "\n")

def get(host, f):
    found = False
    for line in open(f, 'r'):
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

def list(f):
    for line in open(f, 'r'):
        account = line.split(":")
        print(account[0])

