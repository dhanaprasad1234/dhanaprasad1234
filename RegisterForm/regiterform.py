from flask import *
app=Flask(__name__)

app.secret_key="meowmeow"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    if "name" in session:
        session.pop("name",None)
        return render_template("logout.html")
    else:
        return "<h1>User Already Logout</h1><a href='/login'>please login>"

@app.route("/user",methods=["post"])
def user():
    if request.method=="POST":
        name=request.form['name'];
        password=request.form['password'];
    if password=="tech":
        resp=make_response(render_template('userdetails.html',name=name))
        #resp.set_cookie("name",name)
        session['name']=name
        return resp
    else:
        return redirect(url_for("error"))
@app.route("/error")
def error():
    return "<h1 align='center' style=color:red;'>Invalid password/name ,Please check<h2 align='center'><a href='/login'>LOGIN AGAIN</a></h1>"

@app.route("/profile")
def viewprofile():
    if 'name' in session:
        name1=session['name']
        resp=make_response(render_template('userdetails.html',name=name1))
        return resp
    else:
        return "<p align='center' style='color:red'>Please Login First</p><br><a href='/login'>login here</a>"

if __name__=="__main__":
    app.run()

