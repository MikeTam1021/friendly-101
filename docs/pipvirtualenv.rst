.. _`pip & virtualenv`:

pip & virtualenv
****************

If you were reading carefully in :ref:`installing_python` in the Homebrew lesson, you might have noticed the following lines in the success message.

.. code-block:: bash

   Setuptools and Pip have been installed. To update them
     pip install --upgrade setuptools
     pip install --upgrade pip

   You can install Python packages with
     pip install <package>

   They will install into the site-package directory
     /usr/local/lib/python2.7/site-packages

   See: https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md

**pip** is the community-favored package manager for Python software, and is the `successor <http://www.ianbicking.org/blog/2008/12/a-few-corrections-to-on-packaging.html>`_ to `Easy Install <https://pythonhosted.org/setuptools/easy_install.html>`_, which suffered from `several issues <http://www.b-list.org/weblog/2008/dec/14/packaging/>`_. Homebrew `installs pip automatically <https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md>`_ for you. Sweet!

It might seem strange to use a package manager to have downloaded, well, *another* package manager, but each tool has specific capabilities that take advantage of the language's unique strengths. To make one all-encompassing package manager for all platforms and all languages would be unwieldly at best. Think of it like using one web browser to download another preferred web browser.

pip installs...what?
====================

`pip <https://pip.pypa.io/>`_ is a `recursive acronym <https://en.wikipedia.org/wiki/Recursive_acronym>`_ for "pip installs packages" and is, in and of itself, a Python package. If Homebrew didn't install pip automatically, we would have installed pip with Easy Install. Some common commands you'll run with pip:

.. code-block:: bash

   # Search to see if a package is available
   $ pip search <package>

   # Display information about an installed package
   $ pip show <package>

   # Install a new package
   $ pip install <package>

   # Update an existing package
   $ pip install <package> --update

   # Install all packages from a requirements file
   $ pip install -r requirements.txt

   # Export a list of all currently installed packages to a requirements file
   $ pip freeze > requirements.txt

   # List all installed packages
   $ pip list

   # Uninstall a package
   $ pip uninstall <package>

pip downloads Django and other Python software packages from the `Python Package Index <https://pypi.python.org/pypi>`_, or PyPi (pronounced like "pie pie"), which is generally recognized by the community as the canonical source of Python software. 

We are VR
=========

If you installed packages solely with pip, pip would install them to ``/usr/local/lib/python2.7/site-packages``, which is "local" to your computer use but *does not* separate packages from the possibly several Django (or in general Pythonic) projects you could write. The result is an inability to cleanly share your code with others because your project's package dependencies are not cleanly separated. To solve this problem, the author of pip also created **virtualenv**.

`virtualenv <http://virtualenv.readthedocs.org/>`_ is a Python package that creates isolated development environments, preventing packages from colliding and conflicting with one another.

Some developers don't use it, but I also recommend `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/>`_, which is a collection of additional helpers that makes working with virtualenv easier. It's another layer of abstraction, but I think the returns come back fairly quickly. virtualenv and virtualenvwrapper can be installed with pip in just one command.

.. code-block:: bash

   $ pip install virtualenv virtualenvwrapper

pip installs virtualenv and virtualenvwrapper to ``/usr/local/lib/python2.7/site-packages``. virtualenvwrapper requires additional settings in your Bash profile to ensure that it is available on the command line. Open your Bash profile.

.. code-block:: bash

   $ subl ~/.bash_profile

Copy and paste the following lines, probably right after your ``PATH`` settings. Remember to restart Terminal.

.. code-block:: bash

   # virtualenvwrapper
   export WORKON_HOME=$HOME/.virtualenvs
   source /usr/local/bin/virtualenvwrapper.sh

The first line appends the hidden directory ``.virtualenvs`` to the path of the home directory ``$HOME``, assigns it to the variable ``WORKON_HOME``, and finally `exports it <http://virtualenvwrapper.readthedocs.org/en/latest/install.html?highlight=workon_home#shell-startup-file>`_. ``.virtualenvs`` is the name of the hidden directory in your OS X home folder where all of our virtual environments will be stored. ``workon`` will usually be the command to start working on a project.

It might make your head spin to think that a package's only job is to isolate other packages, but it's not very complicated. You should use pip to install virtualenv and virtualenvwrapper *globally* and only virtualenv and virtualenvwrapper globally. All other packages should be installed with pip but inside a virtual environment.

Making an environment
=====================

Let's make a new virtual environment.

.. code-block:: bash

   $ mkvirtualenv hello
   New python executable in hello/bin/python2.7
   Also creating executable in hello/bin/python
   Installing setuptools, pip...done.
   (hello)$ 

The name of my virtual environment was the ever-so creative ``hello``. You can see that I entered my environment because ``(hello)`` prepends the ``$`` Bash prompt. Now whenever I install a package, it installs to the site packages directory of my virtual environment, which is ``/Users/Rich/.virtualenvs/hello/lib/python2.7/site-packages``. Had I installed a package without being inside of my virtual environment, the package would have installed globally to ``/usr/local/lib/python2.7/site-packages``.

It is worth noting that virtualenvwrapper automatically puts you inside a virtual environment whenever creating a new one. You won't totally understand these virtualenvwrapper commands now, but they're worth pointing out because we'll use some of them in the future (``<env>`` or ``hello`` standing for the name of an environment).

.. code-block:: bash

   # List all virtual environments
   $ lsvirtualenv

   # Make and enter a virtual environment
   $ mkvirtualenv <env>

   # Enter a virtual environment
   $ workon <env>

   # Change to a virtual environment's directory
   # This would change you to ~/.virtualenvs/hello/
   (hello)$ cdvirtualenv

   # Change to a virtual environment's site packages directory
   # This would change you to ~/.virtualenvs/hello/lib/python2.7/site-packages/
   (hello)$ cdsitepackages

   # Set a project directory
   (hello)$ setvirtualenvproject <virtualenv directory> <project directory>

   # Change to the project directory
   (hello)$ cdproject

   # Add a directory to the virtual environment's Python path
   # Edits ~/.virtualenvs/hello/lib/python2.7/site-packages/_virtualenv_path_extensions.pth
   (hello)$ add2virtualenv <directory>

   # Exit a virtual environment
   (hello)$ deactivate

   # Remove a virtual environment
   $ rmvirtualenv <env>

There is a lot more in virtualenvwrapper's `command reference <http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html>`_, but you can see that the naming conventions are similar to :ref:`common_bash_commands`. For example, while your virtual environment is active, you can change into the virtual environment directory by running ``cdvirtualenv``, which, if you squint, kind of looks like the change directory command ``cd``. You could have just as easily run ``cd ~/.virtualenvs/hello/`` but the shortcut ``cdvirtualenv`` can be easier to remember. Beginners are often confused by the phrase "``cd`` into your virtual environment." Someone is telling you to run ``cdvirtualenv``---and not ``cd virtualenv``, which wouldn't make sense!

.. note::

   Virtual machine software like `VirtualBox <https://www.virtualbox.org/>`_ and `Vagrant <https://www.vagrantup.com/>`_ can be used with pip and virtualenv to further minimize differences between development and production environments. Their use is often how development is done at larger organizations. `Getting Started with Django <http://gettingstartedwithdjango.com/en/lessons/introduction-and-launch/>`_ by Kenneth Love has a great tutorial about using virtual machines with Django.
