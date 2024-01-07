from flask  import *
from model.dbconnection import Database
import os
from werkzeug.utils import secure_filename

app=Flask(__name__)
db=Database()
UPLOAD_FOLDER='static/photos'
ALLOWED_EXTENSIONS=set(['txt','pdf','png','jpg','jpeg','gif'])
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER


@app.route("/home")
def home():
    return render_template("regform.html")

@app.route("/index")
def index():
    data=db.read(None)
    return render_template("index.html",data=data)

@app.route("/register",methods=["post"])
def register():
    if request.method=="POST":
        data=request.form
        file=request.files['file']
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        status=db.insert(data,filename)
        if status:
            return redirect(url_for("index"))

        else:
            return redirect(url_for("home"))

@app.route("/edit/<id>")
def editStudent(id):
    data=db.read(id)
    return render_template("success.html",data=data)
    print(data)
@app.route("/update",methods=["POST"])
def updateStudent():
   if request.method=="POST":
       data=request.form
       status=db.update(data)
       if status:
            print("success")
            return redirect(url_for("index"))
       else:
            return "fail"


   # return render_template("update.html",data=data)

@app.route("/delete/<int:id>")
def deleteStudent(id):
    status=db.delete(id)
    if status:
        return "Successfully deleted"
    else:
        return "Fail"


if __name__=="__main__":
     app.run()