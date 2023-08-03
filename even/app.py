from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is Even Page of Round Robin.</h1>"