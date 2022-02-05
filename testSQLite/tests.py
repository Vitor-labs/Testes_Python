import sqlite3
import unittest
from testsqlite import *

# FALTA: TESTAR O RETORNO DAS LEITURAS


class testeBD(unittest.TestCase):
    # CREATE FUNCTIONS
    def test_bd_connection(self):
        self.addTypeEqualityFunc(connection('test.db'), sqlite3.Connection)

    def test_bd_creates(self):
        self.assertTrue(create_table(
            'test.db', 'test_table', ['name TEXT', 'age INTEGER']))
        self.assertTrue(create_column('test.db', 'test_table', 'cpf TEXT'))
    # =====================================================================

    # UPDATE/INSERT FUNCTIONS
    def test_bd_inserts(self):
        self.assertTrue(insert_data('test.db', 'test_table',
                        {'name': "'jorja'", 'age': '145', 'cpf': "'321.321.321-33'"}))
        self.assertTrue(insert_line('test.db', 'test_table',
                        ["'jorjim'", '145', "'121.121.212-21'"]))

    def test_bd_updates(self):
        self.assertTrue(update_data('test.db', 'test_table', "'jorjim'", {
                        'name': "'jorjim'", 'age': '21', 'cpf': "'123.123.123-31'"}))
    # ================================================================

    # READ FUNCTIONS
    def test_bd_read_databases(self):
        self.addTypeEqualityFunc(list, read_data)

        # self.assertEqual(read_data('test.db', 'test_table',
        #                  'name', "'jorjim'"), [('jorjim', 21, '123.123.123-31')], msg='[(\'jorjim\', 21, \'123.123.123-31\')]')

    def test_bd_read_column(self):
        self.addTypeEqualityFunc(list, read_column)
#        self.assertEqual(read_column('test.db','test_table', 'name'), ['jorjim'])
#        self.assertEqual(read_column('test.db','test_table', 'age'), [145])

    def test_bd_read_all(self):
        self.addTypeEqualityFunc(list, read_all)
        #self.assertEqual(read_all('test.db', 'test_table'), [['id', 'name', 'age'], [1, 'jorjim', 145]])
    # =====================================================================

    # DELETE FUNCTIONS
    def test_bd_drops(self):
        self.assertTrue(drop_value(
            'test.db', 'test_table', 'name', "'jorjim'"))
        self.assertTrue(drop_column('test.db', 'test_table', 'name'))
        self.assertTrue(drop_table('test.db', 'test_table'))
    # ================================================================


if __name__ == '__main__':
    tests = testeBD()
    tests.test_bd_connection()
    tests.test_bd_creates()
    tests.test_bd_inserts()
    tests.test_bd_updates()
    # tests.test_bd_read_databases()
    # tests.test_bd_read_column()
    # tests.test_bd_read_all()
    tests.test_bd_drops()
