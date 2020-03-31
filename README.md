# MusicApp
Spotify like website with basic CRUD and song listings using Django. The screenshots of the project on my machine are provided at https://github.com/Jain-Aditya/MusicApp/tree/master/Screenshots

Steps to run locally:
You should have Python3 installed on your computer

1. Run `pip3 install -r requirements.txt`. This will install all the dependencies
2. Run `Python3 manage.py makemigrations`
3. Run `Python3 manage.py migrate`
4. Run `Python3 manage.py createsuperuser` and provide relevant information. This will provide access to admin panel at /admin route.
5. Run `Python3 manage.py runserver` and you would be able to access the App at `http://127.0.0.1:8000/`
6. You can create few songs from the UI itself after creating some Artists. The sample Artworks for songs are provided at https://github.com/Jain-Aditya/MusicApp/tree/master/Images%20of%20songs%20sample(for%20your%20testing)
7. To rate a song, you should be logged-in.
