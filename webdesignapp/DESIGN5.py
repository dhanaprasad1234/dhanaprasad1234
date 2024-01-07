from flask import *
app=Flask(__name__)
@app.route("/my")
def user():
    return "welcome"
@app.route("/home")
def home():
    return "hi"
@app.route("/nam/<name>")
def jam(name):
    if name=='home':
        return redirect(url_for("home"))
    if name=='user':
        return redirect(url_for("my"))

if __name__=="__main__":
    app.run()







