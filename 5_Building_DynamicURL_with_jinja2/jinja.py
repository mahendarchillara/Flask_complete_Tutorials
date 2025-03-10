# jinja2 template engine

'''
{{  }} expressions to print output in html
{%...%} conditions ,for loops
{#...#} this is for comments
'''



from flask import Flask,render_template,request,redirect,url_for

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



@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

#variable Rule
@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is "+ str(score)


@app.route('/resultscore/<int:scorevalue>')
def resultscore(scorevalue):
    res=""
    if scorevalue>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score ': score,"res":res}
    
    return render_template('result2.html',results=exp)

@app.route('/successif/<int:score>')
def successif(score):
    # res=""
    # if scorevalue>=50:
    #     res="PASSED"
    # else:
    #     res="FAILED"
    
    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    # res=""
    # if score>50:
    #     res="PASSED"
    # else:
    #     res="FAILED"
    
    return render_template('result.html',results=score)

@app.route('/submit_latest',methods=['POST','GET'])
def submit_latest():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    
    return redirect(url_for('successres',score=total_score))

if __name__=="__main__":
    app.run(debug=True)


#======================================================================================================

'''
📦 1. Importing libraries

from flask import Flask, render_template, request, redirect, url_for
Flask: Core library for creating the web app.
render_template: To render HTML templates using Jinja2.
request: To handle incoming data from forms (like POST requests).
redirect: To redirect users to another route.
url_for: To build dynamic URLs for routes.

🚀 2. Initializing Flask app

app = Flask(__name__)
This initializes the Flask app.
__name__ lets Flask know where to look for templates and static files.

📡 3. Basic routes
Home route

@app.route("/")
def welcome():
    return "<html><h1>welcome to the Flask<h1></html>"
@app.route("/"): Maps the root URL (/) to the welcome() function.
It returns a simple HTML string.
Index route

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')
/index route is linked to index.html (located in the templates folder).
Only GET requests are allowed.
About route

@app.route('/about')
def about():
    return render_template('about.html')
Renders about.html.

📬 4. Form submission

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')
GET request: Displays the form (via form.html).
POST request: Gets the form data using:

request.form['name']
Displays a simple greeting with the submitted name.

✅ Flow:

User visits /submit → GET request → shows form.
User submits the form → POST request → "Hello [name]!"
📏 5. Variable rules in routes
Simple variable rule

@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is " + str(score)
<int:score>: Captures the score as an integer.
URL example: /success/85 will output:

The marks you got is 85
Using Jinja2 templates
Basic pass/fail logic:

@app.route('/resultscore/<int:scorevalue>')
def resultscore(scorevalue):
    res = "PASSED" if scorevalue >= 50 else "FAILED"
    return render_template('result.html', results=res)
Logic:
If score is 50 or above → PASSED
Else → FAILED
Sends the result to result.html using Jinja2 templating.

✅ URL example:
/resultscore/70 → Passes "PASSED" to the template.

Sending dictionaries to Jinja2:

@app.route('/successres/<int:score>')
def successres(score):
    res = "PASSED" if score >= 50 else "FAILED"
    exp = {'score': score, "res": res}
    return render_template('result2.html', results=exp)
Dictionary is passed to result2.html.
Accessed in Jinja2 like this:

<p>Score: {{ results.score }}</p>
<p>Result: {{ results.res }}</p>

✅ Why use dictionaries?

Helps pass multiple related pieces of data at once, like score + result.
Conditional rendering with Jinja2:

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', results=score)
The score is sent to result.html.
You can use Jinja2 if statements in the template:

{% if results >= 50 %}
    <p>You Passed!</p>
{% else %}
    <p>You Failed!</p>
{% endif %}

🧮 6. Calculating total score from form data
Collect form data and redirect:

@app.route('/submit_latest', methods=['POST', 'GET'])
def submit_latest():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science) / 4
    else:
        return render_template('getresult.html')
    
    return redirect(url_for('successres', score=total_score))

✅ Flow:

GET request: Shows a form (via getresult.html) where users enter scores for:
Science
Maths
C
Data Science
POST request:
Retrieves scores via:

request.form['science']
Calculates the average score.
Redirects to /successres with the score using:

return redirect(url_for('successres', score=total_score))
✅ Why use redirect(url_for(...))?

Helps avoid form resubmission issues — if a user refreshes the result page, it won't re-submit the form.
Keeps URLs clean by dynamically generating them.
🎨 7. Jinja2 template engine
The comment at the top reminds us about Jinja2 syntax:


'''
#{{  }} expressions to print output in html
#{%...%} conditions ,for loops
#{#...#} this is for comments
'''
{{ ... }}: Outputs variables/expressions in HTML.
{% ... %}: Logic — like if/for loops.
{# ... #}: Comments (won’t be shown in HTML).
✅ Example in templates:


<h1>Your Score: {{ score }}</h1>

{% if score >= 50 %}
    <p>Congratulations! You passed.</p>
{% else %}
    <p>Sorry, you failed.</p>
{% endif %}

🚀 How to run the app
Save the code in a file (like app.py).
Ensure you have Flask installed:

pip install flask
Run the app:

python app.py
Visit http://localhost:5000/ in your browser!

✅ Summary
This Flask app:

Handles multiple routes (/, /index, /submit, etc.)
Uses Jinja2 to render HTML templates dynamically.
Supports GET and POST requests.
Processes form data and calculates scores.
Implements conditional rendering (pass/fail).
Redirects using url_for().

'''
