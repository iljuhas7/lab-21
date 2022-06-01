#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# Курсор SQLite3

con = sqlite3.connect('test.db')
cursor_obj = con.cursor()

print(cursor_obj)
