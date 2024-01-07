from flask import render_template,url_for,jsonify,request,redirect,Flask,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import bcrypt

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Venkatprasad@localhost:3306/python_db'
app.config['SECRET_KEY']="1234"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
'''engine=db.create_engine('mysql+pymysql://root:Venkatprasad@localhost:3306/python_db')
connection=engine.connect()
metadata=db.MetaData()
Session=sessionmaker(bind=engine)
session=Session()'''

class User(db.Model):
    id=db.Column('id',db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(200))

    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

app.app_context().push()

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/adduser',methods=['POST','GET'])
def adduser():
    if request.method=="POST":
        name=request.form['uname']
        email=request.form['uemail']
        password=request.form['upassword']
        user=User(name,email,password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('/login'))

@app.route('/checklogin',methods=['POST','GET'])
def checklogin():
    if request.method=='POST':
        print("in check")
        email=request.form['uemail']
        password=request.form['upassword']
        print(password)

        user=User.query.filter_by(email=email).first()
        print(user)
        if user and user.check_password(password):
            session['email']=user.email
            print("in check",user.email)
            return render_template("index.html")
        else:
            print("in else")
            return render_template("error.html")
    return render_template("login.html")

@app.route('/logout')
def logout():
    print("logout successfully")
    session.pop('email',None)
    return redirect(url_for('login'))


if __name__=='__main__':
    app.run(debug=True)
