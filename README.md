# Image Recognition

## Objective: 
In this lab, you will learn about Face Recogntion (seeing if two pictures contain the same person) & Pytesseract (Identifying text from images). This lab contains two sections, choose your path!  

By the end of this lab, you will either have a login containing Face Recognition or a website that translates text from an image.  

> Before we start, make sure to fork the repo, and clone the code to your machine.

## Face Recognition
### Instructions:

In this lab, we'll be creating a signin/signup using face recognition!  
We have provided you with some frontend and backend (signup) code already, so make sure to clone the repo!  

1. Pip install the required library: `face-recognition`

2. Create and set up a new Firebase project:
    1. Go to https://console.firebase.google.com/
    2. Create a new project and name it whatever you'd like.
    3. Go to authentication and set it up.
    4. Go to Realtime Database and create a database.
    5. Go to rules and change false to true.

3. Connect the Firebase project to your Flask app:
    1. In your Firebase project:
        - Go to project setting and create a web app.
        - Copy the firebaseconfig lines.
    2. In the app.py file:
        - Paste the copied lines in the config dictionary (make sure to fix the syntax errors).


4. Go over the `signup` route and `signup.html`, understand the code and the purpose of the function.
        
5. When the user logs in:
    - In `login.html` we have 3 inputs: email, password & face (file).
    - When the form is submitted:
        - Log in the user using **authentication** and save it in the `login_session` (don't forget to use try & except).
        - Retrieve the user's information from the database using the `user's id`, and store it in a dictionary.
    - Face Recognition:
        - load the images the user filled in the form and the one stored in the database using the face_recognition library.
        - Run the `face_encodings` function on both images.
        - Use `compare_faces` to see if the person in each image is the same.
        - If the images are the same **redirect** to home, otherwise stay in `login.html`.


6. The home page:
    - In the home route retrieve the logged in user's infromation from the db.
    - Display in `home.html` the user's email and image.
    

## Pytesseract
### Instructions:

##### Call an Instructor/TA to check your completed tasks
 
###### make sure you commit and push your code.



