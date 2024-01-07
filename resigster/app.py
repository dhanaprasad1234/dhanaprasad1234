from flask import *
from dbconnection import connection

app=Flask(__name__)
app.secret_key="teachbird"

@app.route("/")
def home():
    return render_template("studentreg.html")

@app.route('/login')
def login():
    #response=make_response("<h1>cookie is set</h1>")
    #response.set_cookie("name","TeachBird")
    return render_template("login.html")
@app.route('/logout')
def logout():
    if 'name' in session:
        session.pop('name',None)
        return render_template('logout.html')
    else:
        return '<p>user already logged out</p>'

@app.route('/error')
def error():
    return "<h1 style='color:red' align='center'>Invalid Password/User Name ,please check</h1><br> <a href='/login' align='center'>login again</a>"

@app.route('/profile',methods=['post'])
def profile():
    if request.method=="POST":
     name=request.form['username'];
     pwd=request.form['password'];
    if pwd=="teach":
        resp=make_response(render_template('view-profile.html',name=name))
        #resp.set_cookie("name",name)
        session['name']=name
        return resp
    else:
        return redirect(url_for('error'))
@app.route("/viewprofile")
def viewProfile():

   if 'name' in session :
      name1=session['name']
      resp=make_response(render_template('view-profile.html',name=name1))
      return resp
   else:
       return "<p align='center' style='color:red'>Please Login First</p><br><a href='/login'>login here</a>"


