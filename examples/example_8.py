#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# Получение списка таблиц

con = sqlite3.connect('test.db')

def sql_fetch(con):
    cursor_obj = con.cursor()
    cursor_obj.execute("SELECT name from sqlite_master where type='table'")
    print(cursor_obj.fetchall())

sql_fetch(con)