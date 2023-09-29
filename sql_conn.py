import pyodbc

server = 'dozealserver.database.windows.net'
database = 'DozealBeta'
username = 'Dozeal'
password = 'Open@2812'
conn = None
cursor = None
status = False


class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)


def get_sql_conn():
    global conn, cursor
    if conn is not None and cursor is not None:
        return conn, cursor
    else:
        connect_to_database()
        return conn, cursor


def connect_to_database():
    global conn, cursor, status
    connection_string = (
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';'
                                 'DATABASE=' + database + ';'
                                                          'UID=' + username + ';'
                                                                              'PWD=' + password
    )
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        status = True
        # print("Connected Successfully!")
    except Exception as e:
        raise CustomError(f"Database connection failed. Please contact the administrator.\n {e}")
