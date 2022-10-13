from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import date, datetime
import os

# Constants
CURRENT_YEAR = datetime.now().year

# Set up Flask app
app = Flask(__name__)
Bootstrap(app)


# Home Page
@app.route('/')
def home():
    return render_template('index.html', year=CURRENT_YEAR)


if __name__ == "__main__":
    app.run(debug=True)
