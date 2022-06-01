#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

from sqlite3 import Error

# Создание базы данных

def sql_connection():
    try:
        con = sqlite3.connect(':memory:')
        print("Connection is established: Database is created in memory")
    except Error:
        print(Error)
    finally:
        con.close()


if __name__ == "__main__":
    sql_connection()
