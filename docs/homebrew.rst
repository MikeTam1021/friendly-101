Homebrew
========

Several years ago, compiling one's software was a `messy and complicated process <http://hivelogic.com/articles/installing-ruby-on-rails-on-tiger>`_. `Some <https://www.macports.org/>`_ `tried <http://www.finkproject.org/>`_ to create solutions, but it wasn't until **Homebrew** had arrived and made compiling source code a breeze.

What's Hombrew?
---------------

Compiling software involves several implied steps: download the zipped source code file, unzip the file, compile the source code, move the binaries to correct locations, arrange the symbolic links, delete the downloaded file, perform any other cleanup or special tasks, determine any dependencies, and do the whole process over again if dependencies exist. Don't forget about updating and uninstalling.

Homebrew handles all of these tasks as "the missing package manager for OS X" and "installs the stuff you need that Apple didn't," according to `its website <http://brew.sh/>`_. A package manager is simply a program that automates the steps listed earlier. Homebrew can manage `thousands of packages <https://github.com/Homebrew/homebrew/tree/master/Library/Formula>`_, each of which has a unique set of installation instructions called "formula."

Homebrew installs all software to the ``/usr/local/Cellar/`` directory and creates symbolic links in ``/usr/local/bin/`` and ``/usr/local/lib/`` that point back to your "Cellar." It's a very clean way to manage packages and automates an `existing best practice <http://hivelogic.com/articles/using_usr_local/>`_. And because we edited the ``$PATH`` environment variable in :ref:`understanding_your_path` to prioritize ``/usr/local/bin/``, all of the software Homebrew installs will take precedence. Perfect!

Although Homebrew is written in Ruby, it can be used to compile almost any other software, including Python. In doing so, Homebrew depends on the pre-installed version of Ruby that came with OS X.

It's possible to avoid installing Homebrew packages by visiting the respective websites of `Python <https://www.python.org/>`_, `SQLite <http://www.sqlite.org/>`_, and others, and installing each DMG (or worse, compiling manually), but I highly recommend using Homebrew for of its convenience and ease of use.

.. warning::

   Homebrew is a package manager for larger "general purpose" packages, such as Python, SQLite, MySQL, PostgreSQL, or Git. Do not install packages whose languages have package managers of their own. For example, packages written in Python should be installed not with Homebrew but with pip, which will be explained in a future lesson.

Let's start brewing
-------------------

As a precaution, set the ownership of your ``/usr/local`` directory to yourself. Correct ownership ensures Homebrew will be able to install packages in the correct directory on your behalf without errors. You should already have ownership, but sometimes an erroneous permission can slip through.

.. code-block:: bash

   $ sudo chown -R `whoami` /usr/local

Now install Homebrew.

.. code-block:: bash

   $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

You should run ``brew doctor`` and any other additional instructions to make sure Homebrew is up to date and error free.

.. code-block:: bash

   $ brew doctor

Time to pop open a few brewskies
--------------------------------

OS X comes with a pre-installed version of Python, which is located at ``/usr/bin/python``, but because we want to use the latest version, we are going to use Homebrew.

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

.. note::

   Homebrew prevents multiple versions of Python to be installed at the same time. `pyenv <https://github.com/yyuu/pyenv>`_ is a program that manages different versions of Python, much like the popular `rbenv <http://rbenv.org/>`_ and `RVM <https://rvm.io/>`_ managers for Ruby. But because Homebrew installs Python 2.7.9 by default, which is also the `last 2.x.x version of the language <https://www.python.org/dev/peps/pep-0404/>`_, and because Python 3 is installed with the unique ``brew install python3``, I don't recommend needing to install pyenv.

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

My brews need updating
----------------------

Although Homebrew has a `troubleshooting checklist <https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Troubleshooting.md>`_, in general the following commands are most useful in keeping your brews so fresh and so clean:

.. code-block:: bash

   # Update existing formulae files
   $ brew update

   # Install new versions of installed packages
   $ brew upgrade

   # Delete the old versions of packages
   $ brew cleanup

   # Delete and stray symbolic links
   $ brew prune

   # Check all packages for installation integrity
   $ brew doctor
