from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
    return  render_template('home.html')

@app.route("/contact")
def contact():
    return "<h1>contact<h1>"

@app.route("/about")
def about():
    return "<h1>about<h1>"

@app.route("/saludo/<name>")
def saludo(name):
    return  render_template('saludo.html', name=name)

@app.route("/drinks")
def drinks():
    drinks=["Agua","juago","coca"]
    return render_template('drinks.html', drinks=drinks)
   
if __name__== '__main__' :
    app.run(debug=True)