from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
import face_recognition
import pyrebase
import os

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

config = {

}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app.config['SECRET_KEY'] = "Your_secret_string"
UPLOAD_FOLDER = 'static/images/faces'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']


@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == "POST":

		return redirect(url_for("home"))
	else:
  	return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        face = request.files['face']
        upload_file(face)
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            person = {"email": email, "face": face.filename}
            db.child("Users").child(login_session['user']['localId']).set(person)
            return redirect(url_for('login'))
        except:
            return render_template('signup.html')
    else:
        return render_template('signup.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def upload_file(file):
    if request.method == 'POST':
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(UPLOAD_FOLDER + "/" + filename)


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        debug=True
    )
