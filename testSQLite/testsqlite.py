import sqlite3
import logging
from rich import print

"""
THIS PROJECT IS A TEST OF BASIC C.R.U.D. OPERATIONS WITH SQLITE 3
AND SOME UNIT TESTING WITH UNITTEST LIBRARY.
"""


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - \
                    %(levelname)s - %(message)s', datefmt='%d/%M/%Y %H:%M:%S')

handler = logging.StreamHandler()
file = logging.FileHandler('arq.log')

handler.setLevel(logging.WARNING)
file.setLevel(logging.ERROR)

formato = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formato)
file.setFormatter(formato)

logger.addHandler(handler)
logger.addHandler(file)

# CONNECT AND CREATE
# ================================================================


# DataBase Connection
def connection(db_name) -> sqlite3.Connection:
    """
    Connection to a database
    :param db_name: name of the database
    :return:        connection to the database
    """
    try:
        connectionSQLite = sqlite3.connect(db_name)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}'.format(e))
        return None
    else:
        print('Connected to {}'.format(connectionSQLite))
        logger.info('Connected to {}'.format(connectionSQLite))
        return connectionSQLite


# Table creation
def create_table(db_name, t_name, *args) -> bool:
    """
    Create a table
    :param name: name of the table
    :param args: list of columns
    :return:     True if the table is created
    """
    line = 'CREATE TABLE IF NOT EXISTS {}'.format(t_name)
    fields = []
    for arg in args:
        fields.append(arg)
    line += '({})'.format(', '.join(fields))
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logging.info('Line executed {} in {}: '.format(line, t_name, db_name))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logger.info('Table {} created'.format(t_name))
    finally:
        connectionSQLite.close()
        return True


# Column creation
def create_column(db_name, table, column_name, *type) -> bool:
    """
    Create a new column
    :param table:       table to add a new column
    :param column_name: string name of the column
    :param type:        type of the column
    :return:            True if successful, False otherwise
    """
    line = 'ALTER TABLE {} ADD COLUMN {} {}'.format(table, column_name)
    for t in type:
        line += ' {}'.format(t)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logging.info('Line executed {} in {}: {}'.format(
            line, column_name, table))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logging.error('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logging.info('Column {} created in {}'.format(column_name, table))
    finally:
        connectionSQLite.close()
        return True


# READ FUNCTIONS
# ================================================================

# Read DataBase value
def read_data(db_name, table, column, value) -> list:
    """
    Read data from a table
    :param table:   table name
    :param column:  column name
    :param value:   value to read from the column
    :return:        data from the table
    """
    line = 'SELECT * FROM {} WHERE {} = {}'.format(table, column, value)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logging.info('Line executed {} in {}'.format(line, table))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logging.error('Error: {}'.format(e))
    else:
        connectionSQLite.close()
        logging.info('Data read from {}'.format(table))
        return cursor.fetchall()


# Read a Column
def read_column(db_name, table, column):
    """
    Read a column
    :param table:       table name
    :param column:      column name to read
    :return:            data from the column
    """
    line = 'SELECT {} FROM {}'.format(column, table)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logging.info('Line executed {} in {}: {}'.format(line, column, table))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logging.error('Error: {}'.format(e))
    else:
        connectionSQLite.close()
        logging.info('Data read from {}'.format(column))
        return cursor.fetchall()


# READ ALL
def readAll(db_name, table) -> list:
    """
    Read all data from a table
    :param table: table name
    :return:      data from the table
    """
    line = 'SELECT * FROM {}'.format(table)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logging.info('Line executed {} in {}'.format(line, table))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logging.error('Error: {}'.format(e))
    else:
        connectionSQLite.close()
        logging.info('Data read from {}'.format(table))
        return cursor.fetchall()


# UPDATE/INSERT FUNCTIONS
# ================================================================

# Insertion in DataBase
def insert_data(db_name, table, **kwargs) -> bool:
    """
    Insert data into a table
    :param table:   table name
    :param kwargs:  additional parameters
    :return:        True if successful, False otherwise
    """
    line = 'INSERT INTO {}'.format(table)
    fields = []
    values = []
    for key, value in kwargs.items():
        fields.append(key)
        values.append(value)
    line += '({})'.format(', '.join(fields))
    line += 'VALUES ({})'.format(', '.join(values))

    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logging.info('Line executed {} in {}: {}'.format(line, table, db_name))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logging.error('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logging.info('Data inserted in {}'.format(table))
    finally:
        connectionSQLite.close()
        return True


# Insert Many Data
def insert_line(db_name, table, *args) -> bool:
    """
    Insert a line data into the table
    :param table:       table name
    :param kwargs:      additional parameters
    :return:            True if successful, False otherwise
    """
    line = 'INSERT INTO {}'.format(table)
    values = []
    for arg in args:
        values.append(arg)
    line += 'VALUES ({})'.format(', '.join(values))

    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.executemany(line)
        logging.info('Line executed {} in {}: {}'.format(line, table, db_name))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logging.error('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logging.info('Data inserted in {}'.format(table))
    finally:
        connectionSQLite.close()
        return True


# Update Many Data
def update_data(db_name, table, **kwargs) -> bool:
    """
    Update data in a table
    :param table:   table name
    :param kwargs:  additional parameters
    :return:        True if successful, False otherwise
    """
    line = 'UPDATE {}'.format(table)
    fields = []
    values = []
    for key, value in kwargs.items():
        fields.append(key)
        values.append(value)
    line += 'SET {}'.format(', '.join(fields))
    line += 'WHERE {}'.format(values)

    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.executemany(line)
        logging.info('Line executed {} in {}: {}'.format(line, table, db_name))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logging.error('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logging.info('Data updated in {}'.format(table))
    finally:
        connectionSQLite.close()
        return True


# DELETE FUNCTIONS
# ================================================================

# Delete Table
def drop_table(db_name, name) -> bool:
    """
    Drop a table
    :param name: table to delete
    :return:     True if table was successfully dropped, False otherwise
    """
    line = 'DROP TABLE IF EXISTS {}'.format(name)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logging.info('Line executed {} in {}: {}'.format(line, name, db_name))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logging.error('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logging.info('Table {} dropped'.format(name))
    finally:
        connectionSQLite.close()
        return True


# Delete Column
def drop_column(db_name, table, column) -> bool:
    """
    Delete a column
    :param table:  table name
    :param column: column name to delete
    :return:       True if column was successfully dropped, False otherwise
    """
    line = 'ALTER TABLE {} DROP COLUMN {}'.format(table, column)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logging.info('Line executed {} in {}: {}'.format(line, column, table))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logging.error('Error: {}'.format(e))
        return False
    else:
        print('Column {} deleted from {}'.format(column, table))
        logging.info('Column {} deleted from {}'.format(column, table))
        connectionSQLite.commit()
    finally:
        print('Connection closed')
        connectionSQLite.close()
        return True


# Delete Value
def drop_value(db_name, column, table, value) -> bool:
    """
    Delete a value in a column
    :param column:      column name
    :param table:       table name
    :param value:       value to delete
    :return:            True if value was successfully deleted, False otherwise
    """
    line = 'DELETE FROM {} WHERE {} = {}'.format(table, column, value)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logging.info('Line executed {} in {}: {}'.format(line, column, table))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logging.error('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logging.info('Value {} deleted from {}'.format(value, column))
    finally:
        connectionSQLite.close()
        return True

# ==============================================================================


# helper function to execute a query in the database
def execute_query(db_name, query) -> list:
    """
    Execute a query
    :param query:
    :return:
    """
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(query)
        logging.info('Query executed: {}'.format(query))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logging.error('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.close()
        return cursor.fetchall()
