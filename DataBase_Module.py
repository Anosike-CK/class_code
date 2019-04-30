import pymysql

connection = pymysql.connect(host = 'localhost',
                            user = 'root',
                            password = '',
                            db = 'first_database',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor)

def create_table():

    with connection.cursor() as cursor:

        sql = """ CREATE TABLE Bank(id INT(3) NOT NULL AUTO_INCREMENT PRIMARY KEY, Bank_Name VARCHAR(100), Bank_Code INT(9))"""

        cursor.execute(sql)
        connection.commit()

def insert_into_tables():

    with connection.cursor() as cursor:

        sql = """ INSERT INTO """


        cursor.execute(sql)
        connection.commit()

def retrieve():

        with connection.cursor() as cursor:

            sql = """ FROM """