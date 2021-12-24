import sqlite3

"""
THIS PROJECT IS A TEST OF BASIC C.R.U.D. OPERATIONS WITH SQLITE 3
AND SOME UNIT TESTING WITH UNITTEST LIBRARY.
"""

# CONNECT AND CREATE
# ================================================================

# DataBase Connection


def connection(db_name) -> sqlite3.Connection:
    """
    Connection to a database
    :param db_name:
    :return connection:
    """
    try:
        connectionSQLite = sqlite3.connect(db_name)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        return None
    else:
        print('Connected to {}'.format(connectionSQLite))
        return connectionSQLite


# Table creation
def create_table(name, *args) -> bool:
    """
    Create a table
    :param name:
    :param args:
    :return:
    """
    line = 'CREATE TABLE IF NOT EXISTS {}'.format(name)
    fields = []
    for arg in args:
        fields.append(arg)
    line += '({})'.format(', '.join(fields))
    try:
        connectionSQLite = connection('test.db')
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
    finally:
        connectionSQLite.close()
        return True


# READ FUNCTION
# ================================================================

# Read DataBase value
def read_data(table, column, value):
    """
    Read data from a table
    :param table:
    :param column:
    :param value:
    :return:
    """
    line = 'SELECT * FROM {} WHERE {} = {}'.format(table, column, value)
    try:
        connectionSQLite = connection('test.db')
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.close()
        return cursor.fetchall()


def read_column(table, column):
    """
    Read a column
    :param table:
    :param column:
    :return:
    """
    line = 'SELECT {} FROM {}'.format(column, table)
    try:
        connectionSQLite = connection('test.db')
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.close()
        return cursor.fetchall()


# UPDATE FUNCTIONS
# ================================================================

# Insertion in DataBase
def insert_data(table, **kwargs) -> bool:
    """
    Insert data into a table
    :param table:
    :param kwargs:
    :return:
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
        connectionSQLite = connection('test.db')
        cursor = connectionSQLite.cursor()
        cursor.executemany(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
    finally:
        connectionSQLite.close()
        return True


# Update DataBase
def update_data(table, **kwargs) -> bool:
    """
    Update data in a table
    :param table:
    :param kwargs:
    :return:
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
        connectionSQLite = connection('test.db')
        cursor = connectionSQLite.cursor()
        cursor.executemany(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
    finally:
        connectionSQLite.close()
        return True


# DELETE FUNCTIONS
# ================================================================

# Delete Table
def drop_table(name) -> bool:
    """
    Drop a table
    :param name:
    :return:
    """
    line = 'DROP TABLE IF EXISTS {}'.format(name)
    try:
        connectionSQLite = connection('test.db')
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
    finally:
        connectionSQLite.close()
        return True


# Delete Column
def drop_column(table, column) -> bool:
    """
    Delete a column
    :param table:
    :param column:
    :return:
    """
    line = 'ALTER TABLE {} DROP COLUMN {}'.format(table, column)
    try:
        connectionSQLite = connection('test.db')
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        return False
    else:
        print('Column {} deleted from {}'.format(column, table))
        connectionSQLite.commit()
    finally:
        print('Connection closed')
        connectionSQLite.close()
        return True


# Delete Value
def drop_value(column, table, value) -> bool:
    """
    Delete a value in a column
    :param column:
    :param table:
    :param value:
    :return:
    """
    line = 'DELETE FROM {} WHERE {} = {}'.format(table, column, value)
    try:
        connectionSQLite = connection('test.db')
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.commit()
    finally:
        connectionSQLite.close()
        return True

# ==============================================================================


# helper function to execute a query in the database
def execute_query(query):
    """
    Execute a query
    :param query:
    :return:
    """
    try:
        connectionSQLite = connection('test.db')
        cursor = connectionSQLite.cursor()
        cursor.execute(query)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.close()
        return cursor.fetchall()
