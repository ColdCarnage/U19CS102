from flask import Flask, render_template #importing flask and required functions

app = Flask(__name__)

@app.route("/") #displaying the home.html in the root directory of the website
def home():
    return render_template("home.html")#render template function is used to render html files in the template folder

@app.route("/about") #displaying the about page
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)#Running the web app
