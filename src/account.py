#!/usr/bin/env python3

import sqlite3

# Connexion database
database = "../data/storage.sq3"
connexion = sqlite3.connect(database)
cursor = connexion.cursor()

def check_exsting_tables(t1, t2):
    for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+ t2 +"' AND name='"+ t2 +"';"):
        print(row)
        if ("users" not in row): 
            cursor.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nickname VARCHAR(55), fullname VARCHAR(128), password VARCHAR(255), email VARCHAR(128))")
        elif ("password" not in row):
            cursor.execute("CREATE TABLE password(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, host VARCHAR(255), user_id INTEGER, password VARCHAR(255), dt datetime DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(user_id) REFERENCES users(id));")

    connexion.commit()
    connexion.close()

