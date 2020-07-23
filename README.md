# Setup
* "insert steps for installing virtualenvwrapper here"
* mkvirtualenv teleskwela
* cd teleskwela_api
* pip install -r requirements.txt
* create local_settings.py file. Follow the example shown in local_settings.py.example

# To run locally:
* python manage.py runserver

# To run tests
* python manage.py test

# Notes
* always make a pull request when merging to dev or master. These pull requests will be used to document our design decisions


## Branches
* master - source code in production
* dev - branch out from master. stable version but needs last round of testing before merging to master (production)
* feature/fix/hotfix - branch out from dev when working on new feature
