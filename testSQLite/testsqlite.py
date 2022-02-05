import sqlite3
import logging
from rich import print

"""
THIS PROJECT IS A TEST OF BASIC C.R.U.D. OPERATIONS WITH SQLITE 3
AND SOME UNIT TESTING WITH UNITTEST LIBRARY.
"""


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%M/%Y %H:%M:%S')

handler = logging.StreamHandler()
file = logging.FileHandler('testSQLite/arq.log')

handler.setLevel(logging.DEBUG)
file.setLevel(logging.DEBUG)

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
        connectionSQLite = sqlite3.connect('testSQLite/{}'.format(db_name))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}'.format(e))
        return None
    else:
        #print('Connected to {}'.format(connectionSQLite))
        #logger.info('Connected to {}'.format(connectionSQLite))
        return connectionSQLite


# Table creation
def create_table(db_name, t_name, *args) -> bool:
    """
    Create a table
    :param name: name of the table
    :param args: list of columns
    :return:     True if the table is created
    """
    logger.info('Creating table {}'.format(t_name))
    line = 'CREATE TABLE IF NOT EXISTS {}'.format(t_name)
    for arg in args:
        line += '({})'.format(', '.join(arg))
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logger.info('Line executed {} in {}: '.format(line, t_name, db_name))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}\n'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logger.info('Table {} createdzn'.format(t_name))
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
    logger.info("Creating column {} in {}".format(column_name, table))
    line = 'ALTER TABLE {} ADD COLUMN {}'.format(table, column_name)
    for t in type:
        line += ' {}'.format(t)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logger.info('Line executed {} in {}: {}'.format(
            line, column_name, table))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}\n'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logger.info('Column "{}" created in {}\n'.format(column_name, table))
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
    logger.info('Reading data from {}'.format(table))
    line = 'SELECT * FROM {} WHERE {} = {}'.format(table, column, value)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        logger.info('Line executed "{}" in {}'.format(line, table))
        cursor.execute(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}\n'.format(e))
    else:
        data = cursor.fetchall()
        logger.info(
            'Data read from {}->{}: {} ({})\n'.format(table, column, data, value))
        connectionSQLite.close()
        return data


# Read a Column
def read_column(db_name, table, column):
    """
    Read a column
    :param table:       table name
    :param column:      column name to read
    :return:            data from the column
    """
    logger.info('Reading column {} from {}'.format(column, table))
    line = 'SELECT {} FROM {}'.format(column, table)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logger.info('Line executed "{}" in {}: {}'.format(line, column, table))
    except sqlite3.OperationalError as e:
        print('Error: {}\n'.format(e))
        logger.error('Error: {}'.format(e))
    else:
        connectionSQLite.close()
        data = cursor.fetchall()
        logger.info('Data read from {}: {}\n'.format(column, data))
        return data


# READ ALL
def read_all(db_name, table) -> list:
    """
    Read all data from a table
    :param table: table name
    :return:      data from the table
    """
    logger.info('Reading all data from {}'.format(table))
    line = 'SELECT * FROM {}'.format(table)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logger.info('Line executed {} in {}'.format(line, table))
    except sqlite3.OperationalError as e:
        print('Error: {}\n'.format(e))
        logger.error('Error: {}'.format(e))
    else:
        connectionSQLite.close()
        data = cursor.fetchall()
        logger.info('Data read from {}: {}\n'.format(table, data))
        return data


# UPDATE/INSERT FUNCTIONS
# ================================================================

# Insertion in DataBase
def insert_data(db_name, table, dict_data) -> bool:
    """
    Insert data into a table
    :param table:   table name
    :param values:  additional parameters
    :return:        True if successful, False otherwise
    """
    logger.info('Inserting data into {}'.format(table))
    line = 'INSERT INTO {} ('.format(table)
    fields = []
    values = []
    for key, value in dict_data.items():
        fields.append(key)
        values.append(value)

    line += ', '.join(fields) + ') VALUES (' + \
        ', '.join(values) + ')'

    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        logger.info('Line executed {} in {}: {}'.format(line, table, db_name))
        cursor.execute(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}\n'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logger.info('Data inserted in {}\n'.format(table))
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
    logger.info('Inserting data line into {}'.format(table))
    line = 'INSERT INTO {} VALUES ('.format(table)
    for arg in args:
        line += '{}'.format(', '.join(arg))
    line += ')'

    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        logger.info('Line executed {} in {}: {}'.format(line, table, db_name))
        cursor.execute(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.info('Error: {}\n'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logger.info('Data inserted in {}\n'.format(table))
    finally:
        connectionSQLite.close()
        return True


# Update Many Data
def update_data(db_name, table, id, data_dict) -> bool:
    """
    Update data in a table
    :param table:   table name
    :param kwargs:  additional parameters
    :return:        True if successful, False otherwise
    """
    logger.info('Updating data in {}'.format(table))
    line = 'UPDATE {} SET '.format(table)
    fields = []
    values = []
    for key, value in data_dict.items():
        fields.append(key)
        values.append(value)

    for field, value in zip(fields, values):
        line += '{} = {}'.format(field, value) + ', '

    line = line[:-2] + ' WHERE name = {}'.format(id)

    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        logger.info('Line executed {} in {}: {}'.format(line, table, db_name))
        cursor.execute(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}\n'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logger.info('Data updated in {}\n'.format(table))
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
    logger.info('Deleting table {}'.format(name))
    line = 'DROP TABLE IF EXISTS {}'.format(name)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logger.info('Line executed {} in {}: {}'.format(line, name, db_name))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}\n'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logger.info('Table {} dropped\n'.format(name))
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
    logger.info('Deleting column {} from {}'.format(column, table))
    line = 'ALTER TABLE {} DROP COLUMN {}'.format(table, column)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        logger.info('Line executed {} in {}: {}'.format(line, column, table))
        cursor.execute(line)
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}\n'.format(e))
        return False
    else:
        print('Column {} deleted from {}'.format(column, table))
        logger.info('Column {} deleted from {}\n'.format(column, table))
        connectionSQLite.commit()
    finally:
        print('Connection closed')
        connectionSQLite.close()
        return True


# Delete Value
def drop_value(db_name, table, column, value) -> bool:
    """
    Delete a value in a column
    :param column:      column name
    :param table:       table name
    :param value:       value to delete
    :return:            True if value was successfully deleted, False otherwise
    """
    logger.info('Deleting value {} in {}'.format(value, column))
    line = 'DELETE FROM {} WHERE {} = {}'.format(table, column, value)
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(line)
        logger.info('Line executed {} in {}: {}'.format(line, column, table))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}\n'.format(e))
        return False
    else:
        connectionSQLite.commit()
        logger.info(
            'Value {} deleted from {} -> {}\n'.format(table, value, column))
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
    logger.info('Executing query: {}'.format(query))
    try:
        connectionSQLite = connection(db_name)
        cursor = connectionSQLite.cursor()
        cursor.execute(query)
        logger.info('Query executed: {}'.format(query))
    except sqlite3.OperationalError as e:
        print('Error: {}'.format(e))
        logger.error('Error: {}'.format(e))
        return False
    else:
        connectionSQLite.close()
        logger.info('\n')
        return cursor.fetchall()
