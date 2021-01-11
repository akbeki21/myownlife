import mysql.connector

my_db = mysql.connector.connect(
    host='localhost', 
    user='db_test_user',
    password='Python8!',
    database='db_connect'
)

# print(my_db)

my_cursor = my_db.cursor()
# print(dir(my_cursor))

# my_cursor.execute("CREATE DATABASE db_connect")

# my_cursor.execute('SHOW DATABASES')
# my_cursor.close()
# print(my_cursor.fetchall())

# for x in my_cursor:
#     print(x)
# print(my_cursor)


# my_cursor.execute("CREATE TABLE posts(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, title VARCHAR(30) NOT NULL)")



# my_cursor.execute("INSERT INTO posts (id, title) VALUES (%s, %s)", (2, 'python makers'))
# my_db.commit()



# query = "INSERT INTO posts (id, title) VALUES (%s, %s)"
# params = [
#     (1, 'Hello world')
# ]
# my_cursor.executemany(query, params)
# my_db.commit()