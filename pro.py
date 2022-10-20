# this intro my web site
from flask import Flask , render_template

# this home page 
my_cv = Flask(__name__)

# this a path to home page

@my_cv.route('/')
def home():
    return render_template("/home.html" , ptitle="CV")
