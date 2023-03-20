from flask import Flask,render_template, request, redirect, url_for
import tweepy

app = Flask(__name__)

client = tweepy.Client(
    consumer_key = "",
    consumer_secret = "",
    access_token = "",
    access_token_secret = ""
)

@app.route('/')
def home():
    render_template("index.html")

@app.route('/sendtweet', methods=['GET','POST'])
def sendtweet():
    if request.method == 'POST':
        content = request.form['content']
        client.create_tweet(text=content)
        return redirect(url_for('home'))
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()