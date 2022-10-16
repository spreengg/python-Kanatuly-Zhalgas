import psycopg2
from config import host,user,password,db_name
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    with connection.cursor() as cursor:
        cursor.execute("""
        #     SQL CODE
        """
        )
        connection.commit()
        connection.close()
except Exception as ex:
    print("ERR with postgresql: ", ex)
