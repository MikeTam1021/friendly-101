# Django 101

Django 101 is a tutorial and hands-on workshop by the [Friendly Django](https://friendlydjango.org/) Meetup group. It acts as an introduction for beginners to the [Django](https://www.djangoproject.com/) web framework.

The code was written in [reStructuredText](http://docutils.sourceforge.net/rst.html), exported with [Sphinx](http://sphinx-doc.org/), and uploaded to [Read the Docs](https://readthedocs.org/). Wikipedia's article on [reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText) will make you less sad.

You will likely simply want to [read the documentation](https://friendly-django-101.readthedocs.org/), but read on if you're curious about generating it for yourself.

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

Or run `sphinx-autobuild` to watch for changes to your docs and automatically recreate a build when a change occurs. Magic!

```
sphinx-autobuild docs docs/_build/html
```
