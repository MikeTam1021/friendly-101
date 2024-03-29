.. _`Homebrew`:

Homebrew
********

Several years ago, compiling one's software was a `messy and complicated process <http://hivelogic.com/articles/installing-ruby-on-rails-on-tiger>`_. `Some <https://www.macports.org/>`_ `tried <http://www.finkproject.org/>`_ to create solutions, but it was said that the process was enough to `drive one to drink <https://news.ycombinator.com/item?id=1189274>`_ until **Homebrew** had arrived.

What's Hombrew?
===============

Compiling software involves several implied steps, much like downloading and installing a binary: Download the source code, often a `ZIP <https://en.wikipedia.org/wiki/Zip_(file_format)>`_ file of some kind, unzip the file, compile the source code, move the binaries to correct locations, arrange the symbolic links, delete the downloaded file, perform any other cleanup or special tasks, determine any dependencies, and do the whole process over again if dependencies do exist. Don't forget about updating and uninstalling.

`Homebrew <http://brew.sh/>`_ handles all of these tasks as "the missing package manager for OS X" and "installs the stuff you need that Apple didn't." A **package manager** is a program that automates the installation and maintenance of software libraries, which are self-contained bundles of code. Packages contain not only source code, but also the license, `README <https://en.wikipedia.org/wiki/README>`_, and other release notes. Homebrew manages `thousands of packages <https://github.com/Homebrew/homebrew/tree/master/Library/Formula>`_, each of which has a unique set of installation instructions called "formula."

Homebrew installs all software to the ``/usr/local/Cellar`` directory and creates symbolic links in ``/usr/local/bin`` and ``/usr/local/lib`` that point back to your "Cellar." It's a very clean way to manage packages and automates an `existing best practice <http://hivelogic.com/articles/using_usr_local/>`_. And because we edited the ``PATH`` environment variable in :ref:`understanding_your_path` to prioritize ``/usr/local/bin``, all of the software Homebrew installs will take precedence. Perfect!

Homebrew is written in Ruby, but it can be used to compile almost any other software, including Python. In doing so, Homebrew depends on the pre-installed version of Ruby that came with OS X.

.. warning::

   Homebrew is a package manager for larger "general purpose" packages, such as Python, SQLite, MySQL, PostgreSQL, or Git. Do not install packages whose languages have package managers of their own. For example, packages written in Python be installed not with Homebrew but with pip, a package manager for Python, and will be explained later.

Let's start brewing
===================

As a precaution, set the ownership of the ``/usr/local`` directory to yourself. Correct ownership ensures Homebrew will be able to install packages on your behalf without errors. You should already have ownership, but sometimes an erroneous permission can slip through.

.. code-block:: bash

   $ sudo chown -R `whoami` /usr/local

Please note that the `grave accent <https://en.wikipedia.org/wiki/Grave_accent>`_ or "backtick" (`````), are *not* single quotation marks. Backticks are to the left of the number ``1`` key on many keyboards. You could also use the environment variable ``$USER`` (assuming it wasn't overwritten) or type in your username manually, but backticks are the easiest and least error prone method.

Now install Homebrew.

.. code-block:: bash

   $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

You should run ``brew doctor`` and any other on-screen instructions to make sure Homebrew is up to date and error free.

.. code-block:: bash

   $ brew doctor

.. _installing_python:

Installing Python
=================

Django is written in the `Python <https://www.python.org/>`_ programming language, and as such `requires Python <https://docs.djangoproject.com/en/1.7/intro/install/#install-python>`_ to run. OS X comes with a pre-installed version of Python. Let's find out where that installation currently lives and which version it is.

.. code-block:: bash

   $ which python
   /usr/bin/python
   $ python --version
   Python 2.7.5

This version of Python is the globally accessible version and likely a little bit old by now. To remedy these issues, let's use Homebrew to install a newer version of Python.

.. code-block:: bash

   $ brew install python

The success message should look something like:

.. code-block:: bash

   python: stable 2.7.9 (bottled), HEAD
   https://www.python.org
   /usr/local/Cellar/python/2.7.9 (4855 files, 79M) *
     Poured from bottle
   From: https://github.com/Homebrew/homebrew/blob/master/Library/Formula/python.rb
   ==> Dependencies
   Build: pkg-config ✔
   Required: openssl ✔
   Recommended: readline ✔, sqlite ✔, gdbm ✔
   ==> Options
   --quicktest
    Run `make quicktest` after the build (for devs; may fail)
   --universal
    Build a universal binary
   --with-brewed-tk
    Use Homebrew's Tk (has optional Cocoa and threads support)
   --with-poll
    Enable select.poll, which is not fully implemented on OS X (http://bugs.python.org/issue5154)
   --without-gdbm
    Build without gdbm support
   --without-readline
    Build without readline support
   --without-sqlite
    Build without sqlite support
   --HEAD
    Install HEAD version
   ==> Caveats
   Setuptools and Pip have been installed. To update them
     pip install --upgrade setuptools
     pip install --upgrade pip

   You can install Python packages with
     pip install <package>

   They will install into the site-package directory
     /usr/local/lib/python2.7/site-packages

   See: https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md

   .app bundles were installed.
   Run `brew linkapps python` to symlink these to /Applications.

You don't need to run ``brew linkapps python`` in the success message.

Let's find out where our new installation of Python lives and what version it is.

.. code-block:: bash

   $ which python
   /usr/local/bin/python
   $ python --version
   Python 2.7.9

Excellent! Because we set precedence in our Bash profile to look for programs in ``/usr/local/bin``, and because Homebrew creates symbolic links to that location by default, we get our Homebrew installation whenever we reference Python from now on.

.. note::

   Homebrew prevents multiple versions of Python to be installed at the same time. `pyenv <https://github.com/yyuu/pyenv>`_ is a program that manages different versions of Python, much like the popular `rbenv <http://rbenv.org/>`_ and `RVM <https://rvm.io/>`_ managers for Ruby. But because Homebrew installs Python 2.7.x by default, and because Python 3 is installed with the unique ``brew install python3``, I don't recommend needing to install pyenv.

.. note::

   Python 3 is the next major version of the Python programming language. It is a backward-incompatible upgrade; however migration guides for `Python <https://docs.python.org/3/howto/pyporting.html>`_ and `Django <https://docs.djangoproject.com/en/1.7/topics/python3/>`_ exist. Updating code to Python 3 compatibility is a good idea in the long run, but Python 2 is excepted to be supported `until 2020 <https://www.python.org/dev/peps/pep-0373/>`_ at the time of this writing.

Installing SQLite
=================

Django also requires a `SQL database <https://docs.djangoproject.com/en/1.7/intro/install/#set-up-a-database>`_. `SQL <https://en.wikipedia.org/wiki/SQL>`_, which stands for Structured Query Language, is a category of programming languages that interact with `relational databases <http://en.wikipedia.org/wiki/Relational_database>`_.

`SQLite <http://www.sqlite.org/>`_ is a good candidate for beginning developers and development on your computer because it's easier to use than its more complex but robust peers, like `PostgreSQL <http://www.postgresql.org/>`_ and `MySQL <http://www.mysql.com/>`_. By default, Django expects SQLite because it helps start development quickly. Install SQLite with Hombrew.

.. code-block:: bash

   $ brew install sqlite

The success message should look something like:

.. code-block:: bash

   sqlite: stable 3.8.7.4 (bottled)
   http://sqlite.org/

   This formula is keg-only.
   Mac OS X already provides this software and installing another version in
   parallel can cause all kinds of trouble.

   OS X provides an older sqlite3.

   /usr/local/Cellar/sqlite/3.8.7.4 (9 files, 2.1M)
     Poured from bottle
   From: https://github.com/Homebrew/homebrew/blob/master/Library/Formula/sqlite.rb
   ==> Dependencies
   Recommended: readline ✔
   Optional: icu4c ✔
   ==> Options
   --universal
    Build a universal binary
   --with-docs
    Install HTML documentation
   --with-fts
    Enable the FTS module
   --with-functions
    Enable more math and string functions for SQL queries
   --with-icu4c
    Enable the ICU module
   --without-readline
    Build without readline support
   --without-rtree
    Disable the R*Tree index module

.. warning::

   Do not use SQLite in a production environment. SQLite supports a low number of concurrent database connections, which makes it a good candidate for development on your personal computer, but is not recommended for use on the web.

Troubleshooting Homebrew
========================

Homebrew has a `troubleshooting checklist <https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Troubleshooting.md>`_, but in general the following commands are the most helpful in keeping your brews up to date and trouble free.

.. code-block:: bash

   # Search to see if a package is available
   $ brew search <package>

   # Display information about an installed package
   $ brew info <package>

   # Install a new package
   $ brew install <package>

   # Update installed packages
   $ brew update

   # Update to new major versions of installed packages
   $ brew upgrade (<package>)

   # Remove the old (existing but unused) versions of packages
   $ brew cleanup (<package>)

   # Delete stray symbolic links
   $ brew prune

   # Check all packages for installation integrity
   $ brew doctor

It's possible to avoid installing Homebrew packages by visiting the respective websites of `Python <https://www.python.org/>`_, `SQLite <http://www.sqlite.org/>`_, and others, and installing each DMG (or worse, compiling manually), but I highly recommend  Homebrew for its convenience and ease of use.
