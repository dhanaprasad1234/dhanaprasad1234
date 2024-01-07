from flask import *

wed=Flask(__name__)

@wed.route("/user")
def user():
    return render_template('myweb2.html',content=['ML','DL'])

if __name__=="__main__":
    wed.run()
