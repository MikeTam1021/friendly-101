# Friendly 101

Friendly 101 is a tutorial and hands-on workshop by the [Friendly Django](https://friendlydjango.org/) Meetup group. It acts as an introduction to the [Django](https://www.djangoproject.com/) web framework for beginners.

## Documentation

[https://friendly-101.readthedocs.org/](https://friendly-101.readthedocs.org)

You will likely simply want to [read the tutorial](https://friendly-101.readthedocs.org/), but keep reading if you're curious about generating it for yourself.

The documentation was written in [reStructuredText](http://docutils.sourceforge.net/rst.html), built with [Sphinx](http://sphinx-doc.org/), and saved to [Read the Docs](https://readthedocs.org/). Read the Docs will [create a build of the documentation](https://read-the-docs.readthedocs.org/en/latest/getting_started.html#import-your-docs) based on an OAuth authorization to your GitHub account and the GitHub project repository URL.

Prerequisites: [Python](https://www.python.org/), [pip](https://pip.pypa.io/), [virtualenv](http://virtualenv.readthedocs.org/), [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/), [Git](http://git-scm.com/).

```
mkdir -p ~/Sites/ && cd ~/Sites/
git clone git@github.com:friendlydjango/friendly-101.git
mkvirtualenv friendly-101
cd friendly-101
pip install -r requirements.txt
cd docs/
make html
cd _build/html/
python -m SimpleHTTPServer
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). Kill with `Ctrl+C`.

Or run `sphinx-autobuild` to watch for changes to your docs and automatically recreate a build when a change occurs. Magic!

```
sphinx-autobuild docs docs/_build/html
```

## Deployed application

[https://friendly-101.herokuapp.com/](https://friendly-101.herokuapp.com)

The sample application from the tutorial is included in the repository. Although you should probably follow the tutorial for full effect, to run the project in development:

```
mkdir -p ~/Sites/ && cd ~/Sites/
git clone git@github.com:friendlydjango/friendly-101.git
mkvirtualenv friendly-101
cd friendly-101
pip install -r requirements.txt
cd friendly101
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). Kill with `Ctrl+C`.

The sample application is also [deployed to Heroku](https://friendly-101.herokuapp.com/). Although care was taken to mirror the project resulting from the tutorial as closely as possible, the nature of Heroku necessitated changes. Where possible, these are commented in the project's source code.
