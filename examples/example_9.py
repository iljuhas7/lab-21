#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# Проверка существования таблицы

con = sqlite3.connect('test.db')


def sql_fetch(con):
    cursor_obj = con.cursor()
    cursor_obj.execute(
        "CREATE TABLE IF NOT EXISTS projects(id INTEGER, name TEXT)")
    con.commit()


sql_fetch(con)
