from flask import Flask
from flask import render_template,request
app = Flask(__name__)
# home page
@app.route("/")
def home():
    print('Loading Home page')
    return render_template("web.html")
# form page
@app.route("/register", methods=["GET","POST"])
def form():
    print('Loading Registration page')
    if request.method == "POST":
        Name=request.form["name"]
        Email = request.form["email"]
        Password = request.form["password"]
        return render_template(loginsuccess.html,name=Name,email=Email)
    else:
        Name=request.form["name"]        
        Email = request.form["email"]
        Password = request.form["password"]
        return render_template(loginsuccess.htm,name=Name,email=Email)
if __name__ == "__main__":
    app.run(debug=True)
    print('web service started')
else:
    print('web service Stopped')
     
