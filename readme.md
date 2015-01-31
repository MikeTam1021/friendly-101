# Django 101

Django 101 is a tutorial and hands-on workshop by the [Friendly Django](https://friendlydjango.org/) Meetup group. It acts as an introduction to the [Django](https://www.djangoproject.com/) web framework for beginners.

The code was written in [reStructuredText](http://docutils.sourceforge.net/rst.html), built with [Sphinx](http://sphinx-doc.org/), and saved to [Read the Docs](https://readthedocs.org/). Wikipedia's article on [reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText) will make you more tolerable of the language.

You will likely simply want to [read the documentation](https://friendly-django-101.readthedocs.org/), but keep reading if you're curious about generating it for yourself.

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

The original [reStructuredText docs](http://read-the-docs.readthedocs.org/en/latest/getting_started.html#in-rst) are automatically sent to [Read the Docs](http://read-the-docs.readthedocs.org/) via a [Webhook](http://read-the-docs.readthedocs.org/en/latest/webhooks.html) whenever a `git push` happens. Read the Docs will impressively [create the static build](http://read-the-docs.readthedocs.org/en/latest/builds.html) on its own servers after [receiving only](http://read-the-docs.readthedocs.org/en/latest/getting_started.html#import-your-docs) OAuth authorization to the GitHub account and a specific GitHub project repository URL.
