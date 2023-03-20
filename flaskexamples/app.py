# install flask
# pip install flask
# flask templates are rendered using jinja2 templating module

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')                               # / - http://localhost:5000
def home():
    #msg = "A message from flask method"
    #return render_template("index.html",message = msg)
    #list_of_names = ['tom','pat','sam','bob']
    list_of_names = [{'name':'tom'},{'name':'pat'},{'name':'sam'},{'name':'bob'}]
    return render_template("index.html",names = list_of_names)
    #return "My First Web page from flask"     # /playVideo - http://localhost:5000/playVideo

@app.route('/getParams', methods=['GET','POST'])
def getParams():
    if request.method == "POST":
        username = request.form['username']
        email = request.form["useremail"]
        print(username,email)
    return "Another Web page from flask"

if __name__ == '__main__':
    app.run()
