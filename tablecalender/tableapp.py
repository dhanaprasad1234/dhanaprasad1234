from flask import *
web=Flask(__name__)
@web.route("/")
def home():
    return render_template("home.html")

@web.route("/tableform")
def tableform():
    return render_template("tableform.html")

@web.route("/tablevalues",methods=["GET"])
def tablevalues():
    content=int(request.args.get("number"))
    return render_template("tablevalues.html",content=content)

if __name__=="__main__":
    web.run()
