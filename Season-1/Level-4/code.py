'''
Please note:

The first file that you should run in this level is tests.py for database creation, with all tests passing.
Remember that running the hack.py will change the state of the database, causing some tests inside tests.py
to fail.

If you like to return to the initial state of the database, please delete the database (level-4.db) and run 
the tests.py again to recreate it.
'''

import sqlite3
import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    DB_CRUD_ops().get_stock_info(request.args["input"])
    DB_CRUD_ops().get_stock_price(request.args["input"])
    DB_CRUD_ops().update_stock_price(request.args["input"])
    DB_CRUD_ops().exec_multi_query(request.args["input"])
    DB_CRUD_ops().exec_user_script(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class Connect:
    def create_connection(self, path):
        try:
            return sqlite3.connect(path)
        except sqlite3.Error as e:
            print(f"ERROR: {e}")
            return None

class Create:
    def __init__(self):
        con = Connect()
        path = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(path, 'level-4.db')
        db_con = con.create_connection(db_path)
        if db_con is None:
            return
        cur = db_con.cursor()

        table_exists = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='stocks'").fetchall()
        if not table_exists:
            cur.execute("CREATE TABLE stocks (date TEXT, symbol TEXT, price REAL)")
            cur.execute("INSERT INTO stocks VALUES ('2022-01-06', 'MSFT', 300.0)")
            db_con.commit()

        db_con.close()

class DB_CRUD_ops:
    def get_stock_info(self, stock_symbol):
        db = Create()
        con = Connect()
        path = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(path, 'level-4.db')
        db_con = con.create_connection(db_path)
        if db_con is None:
            return "Database connection failed"

        cur = db_con.cursor()
        res = "[METHOD EXECUTED] get_stock_info\n"
        query = f"SELECT * FROM stocks WHERE symbol = '{stock_symbol}'\n"
        res += "[QUERY] " + query

        restricted_chars = ";%&^!#-'"
        if any(char in stock_symbol for char in restricted_chars):
            res += "CONFIRM THAT THE ABOVE QUERY IS NOT MALICIOUS TO EXECUTE"
        else:
            cur.execute(query)
            query_outcome = cur.fetchall()
            for result in query_outcome:
                res += "[RESULT] " + str(result) + "\n"
        
        db_con.close()
        return res

    def get_stock_price(self, stock_symbol):
        db = Create()
        con = Connect()
        path = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(path, 'level-4.db')
        db_con = con.create_connection(db_path)
        if db_con is None:
            return "Database connection failed"

        cur = db_con.cursor()
        res = "[METHOD EXECUTED] get_stock_price\n"
        query = f"SELECT price FROM stocks WHERE symbol = '{stock_symbol}'\n"
        res += "[QUERY] " + query

        cur.execute(query)
        query_outcome = cur.fetchall()
        for result in query_outcome:
            res += "[RESULT] " + str(result) + "\n"

        db_con.close()
        return res

    def update_stock_price(self, stock_symbol, price):
        db = Create()
        con = Connect()
        path = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(path, 'level-4.db')
        db_con = con.create_connection(db_path)
        if db_con is None:
            return "Database connection failed"

        cur = db_con.cursor()
        res = "[METHOD EXECUTED] update_stock_price\n"
        query = f"UPDATE stocks SET price = '{price}' WHERE symbol = '{stock_symbol}'\n"
        res += "[QUERY] " + query

        cur.execute(query)
        db_con.commit()

        db_con.close()
        return res

    def exec_multi_query(self, queries):
        db = Create()
        con = Connect()
        path = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(path, 'level-4.db')
        db_con = con.create_connection(db_path)
        if db_con is None:
            return "Database connection failed"

        cur = db_con.cursor()
        res = "[METHOD EXECUTED] exec_multi_query\n"

        try:
            for query in filter(None, queries.split(';')):
                res += "[QUERY] " + query + "\n"
                cur.execute(query.strip())
                db_con.commit()
                query_outcome = cur.fetchall()
                for result in query_outcome:
                    res += "[RESULT] " + str(result) + " "
        except sqlite3.Error as e:
            res += f"ERROR: {e}"
        finally:
            db_con.close()

        return res

    def exec_user_script(self, query):
        db = Create()
        con = Connect()
        path = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(path, 'level-4.db')
        db_con = con.create_connection(db_path)
        if db_con is None:
            return "Database connection failed"

        cur = db_con.cursor()
        res = "[METHOD EXECUTED] exec_user_script\n"
        res += "[QUERY] " + query + "\n"

        try:
            cur.execute(query)
            db_con.commit()
            query_outcome = cur.fetchall()
            for result in query_outcome:
                res += "[RESULT] " + str(result) + "\n"
        except sqlite3.Error as e:
            res += f"ERROR: {e}"
        finally:
            db_con.close()

        return res
