# Flashcards
## Author  
  
### Titans Group 

* Derrick Nyongesa
* Kenneth Mwangi
* Victor Kigen
  
# Description  
This is a flashcard django application intended to be used as an aid in memorization.
  
##  Live Link  
 Click [View Site](https://moringa-flash.herokuapp.com/)  to visit the site
 


## User Story  
  
* A user must be authenticated to see his flashcards.
* A user's flash card can contain a title with some notes.
* Flashcards should be organized according to subjects/courses.
* A user can delete or update a flash card he has created.
* A user should see when the flash card was created and when it was last updated.
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/kigensky/FLASHCARDS
```
##### Navigate into the folder and install requirements  
 ```bash 
cd FLASHCARDS pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations flashcards
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.2.2](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [vickigen@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/kigensky/pic-galery/blob/main/LICENCE)  
* Copyright (c) 2021 **Victor Kigen**