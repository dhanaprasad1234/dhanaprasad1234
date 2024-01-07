from flask import *
from  rrr.con  import getCon
from rrr.connect import fetchdata
app=Flask(__name__)
@app.route("/")
def gun():
    return render_template('form.html')

@app.route("/user",methods=["get"])
def user():
    name = request.args.get("text")
    email = request.args.get("email")
    age = request.args.get("age")
    password = request.args.get("password")
    mobile = request.args.get("tel")


    return render_template("form1.html",name=name,email=email,age=age,password=password,mobile=mobile)

    my=getCon('python_db')
    mycursor=my.cursor()
    query="insert into register_tab values(%s,%s,%d,%s,%d)"
    valves=("prasad","ballumec143@gmail.com",23,"venkat",9999999999)
    mycursor.execute(query,valves)




if __name__=="__main__":
    app.run()