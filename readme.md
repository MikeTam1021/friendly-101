# Django 101

This repository contains the source code and documentation of the [Friendly Django](https://friendlydjango.org/) Meetup group's introductory tutorial to installing [Django](https://www.djangoproject.com/) for beginners.

The code was written in [reStructuredText](http://docutils.sourceforge.net/rst.html), exported with [Sphinx](http://sphinx-doc.org/), and uploaded to [Read the Docs](https://readthedocs.org/). Wikipedia's article on [reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText) will make you less sad.

You will likely simply want to read the documentation instead of generating it for yourself, but read on if you're curious.

## Installation

Prerequisites:

- [Python](https://www.python.org/)
- [pip](https://pip.pypa.io/)
- [virtualenv](http://virtualenv.readthedocs.org/)
- [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)
- [Git](http://git-scm.com/)

```
mkdir -p ~/Sites/ && cd ~/Sites/
git clone git@github.com:friendlydjango/friendly-django-101.git
mkvirtualenv friendly-django-101
cd friendly-django-101
pip install -r requirements.txt
cd docs/
make html
cd _build/html/
python -m SimpleHTTPServer
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). Kill with `Ctrl+C`.

If you're in a hurry, running one command to go up the directories, create a build, go back down the directories, and run the server will work.

```
cd ../../ && make html && cd _build/html/ && python -m SimpleHTTPServer
```

If you're interested in generating documentation for your own project from scratch, you can follow the same spirit of the instructions above, but with `pip install sphinx`, `pip install sphinx-rtd-theme`, and `sphinx-quickstart`. There is a lot more in the [Sphinx tutorial](http://sphinx-doc.org/tutorial.html). The source code of your project doesn't even need to be in Python to use Sphinx and Read the Docs!
