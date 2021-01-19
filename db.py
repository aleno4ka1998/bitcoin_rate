import sqlite3

from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE rate(id integer PRIMARY KEY, date text, salary real, department text, position text, hireDate text)")
    con.commit()

con = sql_connection()
sql_table(con)

