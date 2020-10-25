# Brief of the application
Flask are used in python to build a web application. The application makes use of libraries such as the Jinja templating library and WTForms. 


# Installation via requirements.txt

```shell
$ cd MOVIE-web-app
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

Setting the virtual environment in Pycharm using 'File'->'Settings' and select 'Project:MOVIE-web-app' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 



# Run the application

In the activated virtual environment

````shell
$ flask run
```` 


# Layout

Needed variables and values in MovieCenter/.env file/.
* `FLASK_APP`: Entry point of the application (should always be `wsgi.py`).
* `FLASK_ENV`: The environment in which to run the application (either `development` or `production`).
* `SECRET_KEY`: Secret key used to encrypt session data.
* `TESTING`: Set to False for running the application. Overridden and set to True automatically when testing the application.
* `WTF_CSRF_SECRET_KEY`: Secret key used by the WTForm library.
