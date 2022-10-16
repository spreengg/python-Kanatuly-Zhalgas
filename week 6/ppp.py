import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'dbnew'
username = 'postgres'
pwd = '1212'
port_id = 5432
conn = None



try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS users')

            create_script = ''' CREATE TABLE IF NOT EXISTS users (
                                    id      int PRIMARY KEY,
                                    name    text,
                                    age  int,
                                    gender text,
                                    nationality text) '''
            cur.execute(create_script)

            insert_script  = 'INSERT INTO users (id, name, age, gender, nationality) VALUES (%s, %s, %s, %s, %s)'
            insert_values = [(1, 'Askar', 23, 'Male', 'Kazakh'), (2, 'Zhanna', 33, 'Female', 'Kazakh'), (3, 'Hasan', 20, 'Male', 'Turkish')]
            for record in insert_values:
                cur.execute(insert_script, record)



             

            create_script = ''' CREATE TABLE IF NOT EXISTS comments (
                                    id      int PRIMARY KEY,
                                    text    text ,
                                    user_id   int,
                                    post_id int ) '''
            cur.execute(create_script)

            insert_script  = 'INSERT INTO comments (id, text, user_id, post_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'AAAAA', 1, 1), (2, 'BBBBB', 2, 2), (3, 'CCCCC', 3, 3)]
            for record in insert_values:
                cur.execute(insert_script, record)

             

            create_script = ''' CREATE TABLE IF NOT EXISTS likes (
                                    id      int PRIMARY KEY,
                                    user_id   int,
                                    post_id int ) '''
            cur.execute(create_script)

            insert_script  = 'INSERT INTO likes (id, user_id, post_id) VALUES (%s, %s, %s)'
            insert_values = [(1, 1, 2), (2, 3, 3), (3, 1, 1)]
            for record in insert_values:
                cur.execute(insert_script, record)


           

            create_script = ''' CREATE TABLE IF NOT EXISTS posts (
                                    id      int PRIMARY KEY,
                                    title    text ,
                                    description   text,
                                    user_id int ) '''
            cur.execute(create_script)

            insert_script  = 'INSERT INTO posts (id, title, description, user_id) VALUES (%s, %s, %s)'
            insert_values = [(1, 'Happy,I am feeling very happy today', 'aaa', 2 ), (2, 'Hot Weather', 'The weather is very hot today', 3 ), (3, 'Help', 'I need some help with my work'), 3]
            for record in insert_values:
                cur.execute(insert_script, record)





                
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
