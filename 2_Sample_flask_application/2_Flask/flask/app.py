from flask import Flask 

'''
It creates an instance of the Flask class,
 Which will be your WSGI (Web Server Gateway Interface) application.
'''

# WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welocome to this flask course.AI Is Good"

@app.route("/index")
def welcome2():
    return "welocome to index page"

if __name__=="__main__":
    app.run(debug=True,port=8080) # runs the app


# ==========================================================================================================

"""

1️⃣ Importing Flask

from flask import Flask

Flask is a lightweight web framework in Python used to build web applications.
You import the Flask class from the flask module.

2️⃣ Creating a Flask app (WSGI application)
python

app = Flask(__name__)

Here, you create an instance of the Flask class.
The __name__ variable is a special Python variable that represents the name of the current module.
It tells Flask whether your app is being run directly or imported as a module.
Why is this needed?
Flask uses this to:

Locate resources (like templates or static files).
Set up routes properly.
This app instance is your WSGI application — it handles requests and responses between the client (browser) and the server.

3️⃣ Defining routes (URL paths)
Route 1: Root route (/)
python

@app.route("/")
def welcome():
    return "welocome to this flask course.AI Is Good"

The @app.route() decorator tells Flask to map this function to the given URL route.
Here, "/" represents the root URL (http://localhost:8080/).
When a user visits this URL, Flask will execute the welcome() function and return the text.
Route 2: /index route
python

@app.route("/index")
def welcome2():
    return "welocome to index page"
    
The /index route maps to the welcome2() function.
Visiting http://localhost:8080/index will trigger this function and return a simple text response.
4️⃣ Running the Flask app
python

if __name__ == "__main__":
    app.run(debug=True, port=8080)
if __name__ == "__main__": ensures the app runs only when the script is executed directly (not when it's imported as a module).
app.run() starts the Flask development server.
Options:

debug=True:

Enables debug mode — useful for development.
Automatically restarts the server when you change the code.
Shows detailed error messages in the browser.
port=8080:

Sets the port number for the web server.
By default, Flask runs on port 5000 — here, you’ve changed it to 8080.*/"

""""