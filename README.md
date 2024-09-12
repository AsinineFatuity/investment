## Investment REST API Application
This is a django rest framework backend api that simulates user's investment account types

## To Run The Project 
1. Clone the repo 
2. Create a `.env` file at the root folder (same location as `manage.py` file) and add values as described in `.env.example` file
3. Create a postgres database for serving the app as indicated in the `.env.example`
    ### Python Dependency Management (Pipenv)
   1. This project supports both [pip](https://pypi.org/project/pip/) and [pipenv](https://pypi.org/project/pipenv/)
   2. To create/activate a virtual env with pipenv:
     * Run `pip install pipenv`
     * Navigate to project root directory (where `manage.py` file is) and run `pipenv shell`
   3. To install a package run `pipenv install package-name`
   4. To install from a `requirements.txt` file run `pipenv install -r requirements.txt` or `pipen install -r requirements-dev.txt --dev`
   5. To install from the `Pipfile` run `pipenv install`
   6. For more details on pipenv read [the documentation](https://pipenv.pypa.io/en/latest/#install-pipenv-today)
   ### Python Dependency Management (Pip)
   1.  Create a virtual environment folder outside the root project folder(where git is initialized) by running `python3 -m venv name_of_env`
       **NB**: *You may create the virtual environment folder inside the root project folder folder but you have to update the .gitignore to ignore the folder*
   2. Activate your virtual environment by running `source name_of_env/bin/activate`
   3. Install packages by running `pip install -r requirements.txt`
4. To start the local host server run `python3 manage.py runserver`
5. To run migrations run the command `python3 manage.py migrate`

## To Run Unit Tests
* The first time/whenever you have created new migrations run `python3 manage.py test`
* Subsequently you run `python3 manage.py test --keepdb`
* Find more arguments you can pass to django's test api [here](https://docs.djangoproject.com/en/5.0/topics/testing/overview/)