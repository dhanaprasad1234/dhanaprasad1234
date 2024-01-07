from rrr.con import getCon
from rrr.connect import fetchdata
try:
    con1=getCon('new1');

    mycursor=con1.cursor()
    query='show tables'
    fetchdata(query,mycursor)
except:
    print('Please check the data')
