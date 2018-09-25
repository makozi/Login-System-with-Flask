from flask import Flask, render_template 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Hello World!"
 

 
@app.route("/login")
def about():
     return render_template("login.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)