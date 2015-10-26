# Lengow Orders App

This project is a simple app to parse, and manage orders, from XML files as well as user input. The project benefits both from the power of Django, as well as Django-REST-Framework XML and offers managements via a web interface and an API.

## Getting Started

To get you started you can simply clone the lengow repository, create a virtual env and install the dependencies:

### Prerequisites

You need **git** to clone the angular-seed repository. You can get git from http://git-scm.com/.

You need also **pip** to install the requirements of the project. It is recommended to have as well **virtualenv** to setup requirements specific to the project in a new virtual environment as well as **virtualenvwrapper** to easily switch between virtual envs. You can get them from http://docs.python-guide.org/en/latest/dev/virtualenvs/

### Clone django-rest-framework-seed

Clone the django-rest-framework-seed repository using git:
```sh
$ git clone https://github.com/o5k/lengow.git
$ cd lengow
```

### Create and activate a virtual environment

```sh
$ mkvirtualenv lengow
$ workon lengow
```
### Install Dependencies

Provided that you have all the prerequisites, and you have activated your virtual env, to install dependencies of the project do the following inside the project directory:
```sh
$ pip install -r requirements.txt
```

### Setup Database
```sh
$ ./manage.py makemigrations
$ ./manage.py migrate
```
### Run the project

The simplest way to run the project is by using the built-in Django development server:
```sh
$ ./manage.py runserver
```
Now browse to the app at http://localhost:8000/

You can also visit the API at http://localhost:8000/api/ and go through /orders/ and so on..
## Contributions

Please feel free to fork the repo and make a pull request or simply create an issue if you find a bug.

## License

This project is licensed under the terms of the [MIT] license.

## Contact
To get in touch about this project feel free to contact me via http://oussamakrifa.com

[Django]: https://docs.djangoproject.com/
[Django REST Framework XML]: https://github.com/jpadilla/django-rest-framework-xml
[Django REST Framework]: http://django-rest-framework.org
[MIT]: http://opensource.org/licenses/MIT