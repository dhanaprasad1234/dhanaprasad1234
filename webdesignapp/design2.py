from flask import Flask

wed=Flask(__name__)

@wed.route("/user/<name>")
def user(name):
    return f"<h1>Be With You {name}</h1>"

if __name__=="__main__":
    wed.run()
