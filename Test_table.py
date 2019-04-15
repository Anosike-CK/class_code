import pymysql.cursors



connection = pymysql.connect(host = 'localhost',
                            user = 'root',
                            password = '',
                            db = 'first_database',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor)


test_types = ['physics', 'maths', 'biology']
with connection.cursor() as cursor:

    # sql = """ CREATE TABLE TEST(id int(3) unique auto_increment, type VARCHAR(20) )"""
    for types in test_types:
        sql = f"""INSERT INTO TEST (type) VALUES('{types}')"""
    
    
        cursor.execute(sql)
        connection.commit()