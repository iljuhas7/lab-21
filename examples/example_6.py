#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# Обновление данных в таблицах

con = sqlite3.connect('test.db')


def sql_update(con):
    cursor_obj = con.cursor()
    cursor_obj.execute(
        "UPDATE employees SET name = 'Rogers' where id = 2"
    )

    con.commit()


sql_update(con)
