from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>welcome to the Flask<h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)


#===================================================================================================
"""
1️⃣ Importing Flask and render_template
from flask import Flask, render_template
Flask is the main class for creating the web app.
render_template is a Flask function that loads and renders HTML files from a templates folder — essential for dynamic web pages.

2️⃣ Initializing the Flask app
app = Flask(__name__)
Creates an instance of the Flask class.
__name__ lets Flask know the current file’s name, helping it locate resources (like templates).

3️⃣ Route definitions
Root route (/)

@app.route("/")
def welcome():
    return "<html><h1>welcome to the Flask<h1><html>"

The root route (/) maps to the welcome() function.
It returns a simple HTML string directly — this is useful for quick testing but not ideal for complex pages.
When you visit http://localhost:5000/, you’ll see:
welcome to the Flask


/index route


@app.route("/index")
def index():
    return render_template('index.html')

Maps the /index route to the index() function.
Instead of raw HTML, it uses render_template() to serve the index.html file.
Flask will look for index.html inside the templates folder (which should be structured like this):

/your_project/
│
├── /templates/
│   ├── index.html
│   ├── about.html
│
└── app.py
/about route

@app.route('/about')
def about():
    return render_template('about.html')
Similar to /index, the /about route serves about.html.
Visiting http://localhost:5000/about will load about.html.
4️⃣ Running the Flask app

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__": ensures the app only runs if the script is executed directly (not imported as a module).
app.run(debug=True):
Starts the Flask development server on port 5000 by default.
Debug mode:
Automatically restarts the server if you change code.
Shows a detailed error page if something breaks.
How to run this Flask app:
Save this code in app.py.
Ensure you have the templates folder and HTML files (index.html and about.html).

Run the app:

python app.py
Open your browser and visit:
http://localhost:5000/ → shows "welcome to the Flask"
http://localhost:5000/index → loads index.html
http://localhost:5000/about → loads about.html """
