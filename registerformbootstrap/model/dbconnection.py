from mysql.connector import connect
class Database:
    def getconnection(self):
        return connect(host="localhost",user="root",password="Venkatprasad",database="python_db")

    def insert(self,data,filename):
        try:
            con=Database.getconnection(self)
            query="insert into register_tab(resigter_name,resigter_email,resigter_gender,resigter_course,images,resigter_address,resigter_country) values(%s,%s,%s,%s,%s,%s,%s)"
            val=(data["name"],data["email"],data["gender"],data["course"],filename,data["address"],data["country"])
            my=con.cursor()
            my.execute(query,val)
            con.commit()
            con.close()
            return True
        except:
            con.rollback()
            return False
    def read(self,id):
        try:
            if id==None:
                con=Database.getconnection(self)
                query="select * from  register_tab "
                my=con.cursor()
                my.execute(query)
                fetchdata= my.fetchall()


            else:
                con = Database.getconnection(self)
                query="select resigter_id,resigter_name,resigter_email,resigter_gender,resigter_course,images,resigter_address,resigter_country from register_tab where resigter_id=%s "
                val=(id,)
                my = con.cursor()
                my.execute(query,val)
                fetchdata=my.fetchall()

            return fetchdata

        except:
            return None

    def delete(self,id):
        try:
            con=Database.getconnection(self)
            query="delete from register_tab where resigter_id= %s"
            val=(id,)
            my = con.cursor()
            my.execute(query,val)
            con.commit()
            return True
        except :
            return False
    def update(self,data):
        try:
            con=Database.getconnection(self)
            query="update register_tab set resigter_name=%s,resigter_email=%s,resigter_gender=%s,resigter_course=%s,resigter_address=%s where resigter_id=%s"
            val=(data["name"],data["email"],data["gender"],data["course"],data["address"],data["id"],)
            my=con.cursor()
            my.execute(query,val)
            con.commit()
            con.close()
            return True
        except:
            con.rollback()
            return False











