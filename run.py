
import configparser
from flask import Flask, render_template

# Read configuration from file
config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/news', methods=['GET', 'POST'])
def news():
    return render_template("news.html")

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(**config['app'])

