from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>welcome to the Flask<h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')



if __name__=="__main__":
    app.run(debug=True)


# ==========================================================================================================
'''
1️⃣ Importing libraries

from flask import Flask, render_template, request
Flask: The core library used to create the web application.
render_template: Used to render HTML templates (like index.html, about.html, etc.).
request: Helps in handling incoming HTTP requests — like reading data sent via forms.

2️⃣ Initialize the Flask app

app = Flask(__name__)
Flask(__name__): Creates an instance of the Flask class.
__name__: A special Python variable that represents the name of the current module.
Flask uses it to know where to look for templates, static files, etc.
                                   
3️⃣ Define routes (URL mappings)
Home Route ("/")

@app.route("/")
def welcome():
    return "<html><h1>welcome to the Flask<h1></html>"
@app.route("/"): Maps the root URL (/) to the welcome() function.
welcome(): Returns a simple HTML message directly as a string.
✅ Access this by visiting:
http://localhost:5000/

Index Route ("/index")

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')
@app.route("/index", methods=['GET']): Maps the /index URL.
methods=['GET']: Specifies that only HTTP GET requests are allowed.
render_template('index.html'): Renders the index.html file — Flask will look for this file inside the templates folder.

✅ Access this by visiting:
http://localhost:5000/index

About Route ("/about")

@app.route('/about')
def about():
    return render_template('about.html')
Similar to /index, it renders the about.html template.
✅ Access this by visiting:
http://localhost:5000/about

Form Route ("/form")

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')
methods=['GET', 'POST']: Allows both GET and POST requests.
request.method: Checks the type of request (GET or POST).
request.form['name']: Retrieves the value of the form field named name (useful for handling form submissions).
If POST: It processes the form data and returns a greeting.
If GET: It shows the form (via form.html).
✅ Access this by visiting:
http://localhost:5000/form

4️⃣ Running the app

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":: Ensures the app only runs when the script is executed directly (not imported as a module).
app.run(debug=True):
Starts the Flask development server.
debug=True: Automatically restarts the server when code changes (useful for development).'''