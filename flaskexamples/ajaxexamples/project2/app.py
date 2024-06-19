from flask import Flask,render_template,url_for,redirect,request,jsonify
import pymysql
 
 
app=Flask(__name__)
con=pymysql.connect(host="localhost",user="root",password="rps@123",db="demodb_1",cursorclass=pymysql.cursors.DictCursor)
 
@app.route('/')
def hello():
    return render_template('index.html')
 
@app.route('/userDetails',methods=['GET','POST'])
def getvalue():
    id=request.form["userID"]
    print(id)
    cur=con.cursor()
    cur.execute("select username,useremail from loginusers where id={}".format(id))
    user=cur.fetchall()
    return jsonify(user)
 
 
if __name__=="__main__":
    app.run()
