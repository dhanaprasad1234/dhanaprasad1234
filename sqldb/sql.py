import mysql.connector
b=mysql.connector.connect(host='localhost',user='root',password='Venkatprasad')
c=b.cursor()
q='create database Prasad_db'
c.execute(q)