from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
from PIL import Image
import pytesseract
import requests
import requests

url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

payload = {
    "q": "Hello World!",
    "source": "en",
    "target": "es"
}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "a2dcccc4c8msh8daf10df609f621p198cfcjsncb56e4cf657e",
    "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

app.config['SECRET_KEY'] = "Your_secret_string"

def translate(text , lang):
    payload = {
    "q": lang,
    "source": "en",
    "target": lang
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return response["data"]["translations"]["translatedText"]

@app.route('/')
def form():
    if request.method == 'POST':
        lang = request.form['lang']
        pic = request.files['pic']
        img = Image.open(pic)
        result = pytesseract.image_to_string(img, lang = lang)
        r = translate(img , lang)
        print(result )
        return render_template("translated.html" , r = r)
    else:
        return render_template('form.html')
    


@app.route('/translated', methods=['GET', 'POST'])
def translated():
    return render_template('translated.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        debug=True
    )
