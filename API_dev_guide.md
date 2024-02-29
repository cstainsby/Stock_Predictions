# API Development Guide

## Important Links 
Any links to documentation or other that were used to help build this project are found here.
1. [Flask - A simple api framework for Python](https://flask.palletsprojects.com/en/3.0.x/)
1. [Jinja - templating engine used to make developing html pages easier](https://jinja.palletsprojects.com/en/3.1.x/)
1. [Venv - A virtual environment module](https://docs.python.org/3/library/venv.html)
1. [Github Development Workflow - How to work on a git project](https://uidaholib.github.io/get-git/3workflow.html)

## Development Cycle
In order to develop this project, you will need to follow some steps in order to successfully prepare your environment, run the application, and save you work. This includes:

### Starting Development
In this project, we will be using venv, python's virtual environment manager. This tool allows us to isolate the modules we download to its own "project" and make sure what works on your device also works on mine. Read more about how it works [here](#important-links)

**Start the Environment:**
You will need to make sure you load into your environment before working.

    source venv/bin/activate

**Update your Packages:**
In case someone else made changes to the dependancy requirements, run:

    pip install -r requirements.txt

After that you will be good to go.


### Running the Project 
The api is being run through a Flask app which is stored in *api.py*. In order to boot it up run:

    python3 apy.py

### Closing Down
Make sure to exit the running api using 'Cntl+C'. Then deactivate your Venv envrionment by running:

    deactivate

*NOTE: I did not include git commands. Please ensure you are on the right branch and then save your work to it. Read about it here: [Github Workflow Link](#important-links)*