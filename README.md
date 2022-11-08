# Image Recognition

## Objective: 
In this lab, you will learn about Face Recogntion (seeing if two pictures contain the same person) & Pytesseract (Identifying text from images). This lab contains two sections, choose your path!  

By the end of this lab, you will either have a login containing Face Recognition or a website that translates text from an image.  

> Before we start, make sure to fork the repo, and clone the code to your machine.

## Face Recognition
### Instructions:

In this lab, we'll be creating our very own meet profile with your users uploading the images!  
We have provided you with some frontend and backend code already, so make sure to clone the repo!  

1. Create and set up a new Firebase project:
    1. Go to https://console.firebase.google.com/
    2. Create a new project and name it whatever you'd like.
    3. Go to Realtime Database and create a database.
    4. Go to rules and change false to true.

2. Connect the Firebase project to your Flask app:
    1. In your Firebase project:
        - Go to project setting and create a web app.
        - Copy the firebaseconfig lines.
    2. In the app.py file:
        - Create a dictionary called config and paste the copied lines (make sure to fix the syntax errors).
        - Intialize the firebase using pyrebase.
        - Intialize db using the firebase object.

3. In `add_post.html`, you have a form that contains an input called caption and a submit button:
    - **Add** the required line to the form tag to be able to accept images.
    - **Create** an input that you can upload images to.
        
4. Check the `UPLOAD_FOLDER` and see if the needed folder in static are there, if no create them.

5. Uploading images to our directory:
    - Make sure to copy the functions that upload to the directory from the slides.
    - In the `/add_post` route get the inputs from the form and upload the image.

6. Saving images in the Realtime Database:
    - after uploading the image, create a dictionary for the post inputs.
    - **Push** the dictionary under the child `"Posts"`.

Now, after you're done with uploading posts, let's them!

7. Dispalying the posts:
    - In the `/` route get all the posts under the `"Posts"` child, and pass the posts to the html page.
    - Using a **for loop** display all the posts.


##### Call an Instructor/TA to check your completed tasks
 
###### make sure you commit and push your code.



