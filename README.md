# Notes
A simple note-taking app in Django that allows for creating, editing, and removing notes.

There is a password field associated with each note, however there is no password validation for accessing notes currently.

# Functionality
1. Creating notes - allows for creating a new note with a title, content, an expiration date, and a password.
2. Setting a note expiration time - allows for picking a day on which the note will expire, and will no longer be accessible for users(it will stay in the database).
3. Modifying existing notes - allows for modifying the title, content, expiration date, and the password associated with a note.
4. Deleting notes - allows for removing notes from the database, making them entirely inaccessible.

# Running
To run the application:
1. Clone the repo
2. Run `python manage.py migrate`
3. Run `python manage.py runserver`
4. Voila! Application should be up at 127.0.0.1:8000/

# Demo
A video demo of the application can be seen [here](https://streamable.com/vqxqvr) 
