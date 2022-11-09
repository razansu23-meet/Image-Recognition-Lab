from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
from PIL import Image
import pytesseract
import requests


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

app.config['SECRET_KEY'] = "Your_secret_string"


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/translated', methods=['GET', 'POST'])
def translated():
    return render_template('translated.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        debug=True
    )
