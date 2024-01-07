def fetchdata(query,cursor):
    cursor.execute(query)
    result=cursor.fetchall()

    for database in result:
        print(database)