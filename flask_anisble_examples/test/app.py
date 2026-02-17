from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/') # http://127.0.0.1:5000
def index():
    return render_template("my.html")
    #return "<h1>helloworld</h1>"

@app.route('/showMessage',methods=['POST'])
def message():
    #data = request.get_json()
    #name = data.get('name','')
    playbook =  request.form['playbook']
    password = request.form['password']
    return f"<h1>Playbook - {playbook} and Password = {password}</h1>"
    #return f"<h1>Welcoem flask user {name}</h1>"

if __name__ == "__main__":
    app.run()
