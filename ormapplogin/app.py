from flask import Flask,render_template,url_for,request,redirect
from  flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Venkatprasad@localhost:3306/python_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False;
app.config['SECRET_KEY']="1234"

db=SQLAlchemy(app)



class Store(db.Model):
    # __tablename__="productstore"
    p_id=db.Column('id',db.Integer,primary_key=True)
    p_name=db.Column(db.String(50))
    p_model = db.Column(db.String(50))
    p_price = db.Column(db.Float(50))

    def __init__(self,name,model,price):
        self.p_name=name
        self.p_model=model
        self.p_price=price

app.app_context().push()
# db.create_all()


@app.route("/index")
def index():
    data=Store.query.all()
    return render_template("index.html",record=data)

@app.route('/add',methods=['POST'])
def addproduct():
    if request.method=='POST':
        name=request.form["pname"]
        model=request.form["model"]
        price=request.form["price"]
        data=Store(name,model,price)
        db.session.add(data)
        db.session.commit()


    return redirect(url_for("index"));

@app.route('/updateproduct',methods=['post'])
def updateproduct():
    if request.method=="POST":
        id=request.form['p_id']
        mydata = Store.query.get(id)
        print(mydata)
        mydata.p_name=request.form['pname']
        mydata.p_model = request.form['model']
        mydata.p_price = request.form['price']
        db.session.commit()
        return redirect(url_for("index"))

@app.route("/delete/<id>")
def delete(id):
    mydata = Store.query.get(id)
    db.session.delete(mydata)
    db.session.commit()
    return redirect(url_for("index"))









if __name__=="__main__":
    app.run()
