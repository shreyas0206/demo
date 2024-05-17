from flask import Flask,render_template

app = Flask(__name__,static_url_path='/static')

# ------ simple hello task ---------
@app.route('/')
def hello():
    return '<h1>Hello Cyronics</h1>'
 
@app.route('/<name>')
def user(name):
    return f'<h1>Welcome to Cyronics <u>{name}</u></h1>'

# --------- using HTML,CSS ------------
@app.route('/home/<name>')
def home(name):
    return render_template('home.html',name=name)
if __name__== "__main__" :
    app.run(debug=True)
