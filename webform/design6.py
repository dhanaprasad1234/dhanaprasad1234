from flask import *
from  rrr.con  import getCon
app=Flask(__name__)
@app.route("/")
def gun():
    return render_template('form.html')

@app.route("/user",methods=["POST"])
def user():
    '''name = request.args.get("text")
    email = request.args.get("email")
    age = request.args.get("age")
    password = request.args.get("password")
    mobile = request.args.get("tel")'''
    data=request.form;

    return render_template("form1.html",data=data)
    '''my=getCon('python_db')
    mycursor=my.cursor()'''


if __name__=="__main__":
    app.run()