# import Flask
from flask import Flask, render_template

# Create an app, being sure to pass __name__
app = Flask(__name__, template_folder="templates")


# Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return render_template('home.html')

# Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("***ALERT***Client is on about page! Server received request for 'About' page...")
    return "Flask is cool! I love running my own servers"


if __name__ == "__main__":
    app.run(debug=True)