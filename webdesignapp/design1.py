from flask import Flask
web=Flask(__name__)

def about():
    return "we with you"
web.add_url_rule("/about","about",about)

if __name__=="__main__":
    web.run()