# learn_python_with_5_box_quiz

This web app has been developed by three people using the Django framework. Our motivation, was to build this project so that we can learn about Django and increase our skillset. It is also part of our training to learn Python. We had three weeks to make the project run.

The goal is to learn Python through 100 repeating flashcards. Instructions: Click „Start” to begin the quiz. When you see the question, read it carefully. If you know the answear, click the"I know" button and the correct answer will appear, confirming that you are right. If you are not certain about the correct answear, choose the "Next question" button so the flashcard will wait for another try.

## Basic Features of the App

### QUIZ PART

1. You can display a random flashcard from database - use db.sqlite3
2. Clicking "I know" button will cause the correct answear to appear
3. Clicking "Next" button leads you to the next question without seeing the answer to the previous one
4. If you finish the quiz, the certficiate with congratulations in pdf format will show up

### USER MANAGEMENT

1. Register - Users can register and create a new profile
2. Proper language validation - during registration all fields except password are validated for using improper language (word base only in english)
2. Login - Registered users can login using username and password
3. User profile - Once logged in, users can create and update additional information such as bio in the profile page
4. Update profile - Users can update their information such as username, email, password and bio
5. Remember me - Cookie option, users don`t have to provide credentials every time they hit the site
6. Admin panel - admin can CRUD users

### HOW TO RUN THE PROJECT

To get this project up and running locally on your computer follow these steps.

1. Set up a python virtual environment
2. Make sure You have the fixtures.json file - there You can find the questions and anwears
3. Run the following commands:

$ pip install -r requirements.txt

$ python manage.py makemigrations

$ python manage.py migrate

4. Connect data base from DBeaver
5. Run the following commands:

$ python manage.py runserver

$ python manage.py loaddata fixtures.json

$ python manage.py createsuperuser

$ python manage.py runserver

6. Open a browser and go to http://localhost:8000/

### CHALLENGES WE FACED AND FEATURES WE HOPE TO IMPLEMENT IN THE FUTURE

The main design assumptions where to do the quiz according to the instruction from Leitner system.
The goal is to learn Python through repeating 100 flashcards, five times each run. How? Imagine five boxes. At the beginning all questions are inside the first box.
If You see the question think carefully. If you know the answear click "I know" button and check the answear. The question will move to the second box.
If You are not sure about the correct answear choose "Next question" button so the flashcard will stay in the first box for another try. Repaet these steps until each question go through five boxes.

We hope to improve the project to achieve the design assumptions so be welcome to come back in the future. 
