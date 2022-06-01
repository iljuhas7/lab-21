#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# Создание соединения

con_db = sqlite3.connect('test.db')
print(type(con_db))
