import sqlite3
import unittest
from testsqlite import *

#
# OLD TESTING CODE HERE
#


class testeBD(unittest.TestCase):
    def test_bd_connection(self):
        self.assertTrue(connection('users.db'), sqlite3.Connection)

    def test_bd_create_table(self):
        self.assertTrue(create_table(
            'user', 'id INTEGER PRIMARY KEY AUTOINCREMENT', 'name TEXT', 'age INTEGER'))

    def test_bd_insert(self):
        self.assertTrue(insert_data('user', 'jorja', '145'))

    def test_bd_update(self):
        self.assertTrue(update_data(
            'teste', 'jorjim', 'jorja', 'id', 1))

    def test_bd_read(self):
        self.assertTrue(read_data('user', 'name', 'jorjim'))
        self.assertTrue(read_data('user', 'age', '145'))

        self.assertTrue(read_column('user', 'name'))
        self.assertTrue(read_column('user', 'age'))

    def test_bd_drop(self):
        self.assertTrue(drop_value('user', 'name', 'jorja'))
        self.assertTrue(drop_column('user', 'age'))
        self.assertTrue(drop_table('teste'))


if __name__ == '__main__':
    unittest.main()
