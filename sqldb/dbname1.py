import rrr.con as mc1
import rrr.connect as mc2
try:
    con1=mc1.getCon('shopping_details')
    mycursor=con1.cursor()
    query="delete from presonal_details where id_person=1"
    mycursor.execute(query)
    print(mycursor.rowcount,'recorded deleted')
    #result1=mc2.fetchdata(query,mycursor)

except:
    print('Please Check The Query')