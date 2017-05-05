import os
import sqlite3
from libs import globs as gl

class SqliteDB:
    def __init__(self):
        self.parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.db_path = gl.dbp
        self.db_connection = sqlite3.connect(self.db_path)
        self.db_cursor = self.db_connection.cursor()

    def execute(self, query, args=''):
        return self.db_cursor.execute(query, args)

    def commit(self):
        self.db_connection.commit()

    def close(self):
        self.db_connection.close()