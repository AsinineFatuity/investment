## Investment REST API Application
This is a django rest framework backend api that simulates user's investment account types

## To Run The Project 
1. Clone the repo by running `git clone https://github.com/AsinineFatuity/investment.git`
2. Create a `.env` file at the root folder (same location as `manage.py` file) and add values as described in `.env.example` file
3. Create a postgres database for serving the app as indicated in the `.env.example`
    ### Python Dependency Management (Pipenv)
   1. This project supports both [pip](https://pypi.org/project/pip/) and [pipenv](https://pypi.org/project/pipenv/)
   2. To create/activate a virtual env with pipenv:
     * Run `pip install pipenv`
     * Navigate to project root directory (where `manage.py` file is) and run `pipenv shell`
   3. To install a package run `pipenv install package-name`
   4. To install from the `requirements.txt` file run `pipenv install -r requirements.txt`
   5. To install from the `Pipfile` run `pipenv install` (recommended)
   6. For more details on pipenv read the [documentation](https://pipenv.pypa.io/en/latest/#install-pipenv-today)
   ### Python Dependency Management (Pip)
   7.  Create a virtual environment folder outside the root project folder (where git is initialized) by running `python3 -m venv name_of_env`
      * **NB**: *You may create the virtual environment folder inside the root project folder folder but you have to update the `.gitignore` file to ignore the folder*
   8. Activate your virtual environment by running `source name_of_env/bin/activate` or system equivalent
   9. Install packages by running `pip install -r requirements.txt`
4. To start the local host server run `python manage.py runserver`
5. To run migrations run the command `python manage.py migrate`

## Unit Tests
### Running Tests
* The first time/whenever you have created new migrations run ` manage.py test`
* Subsequently you run `python manage.py test --keepdb`
* Find more arguments you can pass to django's test api [here](https://docs.djangoproject.com/en/5.0/topics/testing/overview/)
### Test Coverage
1. This project uses [coverage](https://coverage.readthedocs.io/en/7.6.1/) to gauge effectiveness of tests
2. To get a test coverage report:
   * Run `coverage run manage.py test --keepdb`
   * Generate report by running `coverage report`
## Additional Dev Notes
### Code Quality (Linting)
1. This project uses [black code formatter](https://black.readthedocs.io/en/stable/) to achieve consistency in formatting code in line with [PEP 8](https://peps.python.org/pep-0008/) standards
2. Whenever changes are made to code, run `black .` to format the changed files
3. This project also uses [flake8](https://pypi.org/project/flake8/) to enforce `PEP8` standards. Run `flake8` whenever you make changes to a file so as to detect non conformant code
### Typehinting
1. This project prefers type hinting as a way of documenting code hence always type hint your functions to improve readability
2. As of the moment the project does not enforce types but this can be configured with the tools available
