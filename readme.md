# INSTAGRAM_CLONE

## Author
### [BINAMIN HUSSEIN](https://github.com/Binamin-hussein100)
## Description
Instagram_clone is a clone made of the actual social media.

## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running

   ```bash
   git clone https://github.com/Binamin-hussein100/instagram_clone.git
   ```
 or download a zip file of the project from github


Navigate to the project directory
```bash
cd Personal-django
```

##### 2. Create a virtual environment
 Install `Virtualenv`

   ```prettier
   python3 -m venv venv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   python3 -m venv Virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```
##### 3. Create a django and create django projects
 Install django
 ```bash
 pip install django
  ```
  Create django project
  ```bash
  django-admin startproject instagram.
```
create an app
 ```bash
 django-admin startapp news
 ```



##### 5. Create a database
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```insta```
   ```
   # create database picha
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python manage.py makemigrations insta_clone
```


then run the command below;

 ```bash
 python manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine,

    python3 manage.py runserver

## Technologies Used
* Django
* Cloudinary
* Html
* Css
* Bootstrap3
* Django-Admin


## User stories
>As a user I should be able to:

* log in as a user
* able to post a picture with a caption
* view my profile as a user
* make search using username and post title



## Bugs
There are afew bugs. 

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2021 

# Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

# Contacts
binamin.h.hassan14@gmail.com