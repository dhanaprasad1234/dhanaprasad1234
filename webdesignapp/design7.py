from flask import *

app=Flask(__name__)
@app.route("/")
def gun():
    return render_template('myform2.html')

@app.route("/user",methods=["POST","GET"])
def user():
    if request.method == "POST":
        user1=request.form["text"]
        session["login"] = user1
        return redirect(url_for("login"))
    return render_template("form.html")

@app.route("/logout")
def logout():
    pass

@app.route("/login")
def login():
    if 'login' in session:
        user1=session['user']
        return f"hello {user1}"
    else:
        return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True)