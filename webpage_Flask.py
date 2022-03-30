from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/About")
def About():
    return render_template("Layout.html")

@app.route("/Contact")
def Contactus():
    return render_template("Contact.html")

if __name__=="__main__":
    app.run(port=5001,debug=True)