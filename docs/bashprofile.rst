Bash profile
============

You probably notice that when you turn on your computer that some applications start up along with it. Some applications are required by the operating system, and some you installed yourself. And some can make your computer's fan sound like an airplane taking off.

Some of these applications are in the "Login Items" tab of the "Users & Groups" section of your System Preferences.

.. figure:: img/bash_profile-login_items.png
   :alt: OS X Login items

And some applications have their own application-specific login items, which run only when that specific application is opened. We're going to use Terminal's login items feature to make web development easier.

What is a Bash profile?
-----------------------

The **Bash profile** is a file on your computer that Terminal runs every time a new Terminal session is created. This is important because we need to run certain code every time before starting to work.

OS X doesn't include a Bash profile by default, but if you already have one, it lives in your OS X home directory with the name ``.bash_profile``. And if you had one, you probably never saw it  because its name starts with a period, and the Finder hides all folders and files starting with a period. The folders and files are hidden to protect the casual user from harming the operating system--but because you're a developer now, we're going to create or edit a Bash profile file now!

Creating your Bash profile
--------------------------

Open Terminal, copy and paste the following command (remembering not to include the ``$`` and adjacent space character), and hit ``Return``:

.. code-block:: bash

   $ subl ~/.bash_profile

The tilda (``~``) tells Terminal to start traversing the file system from one's home directory. In my personal case, an equivalent command would have been ``subl /Users/Rich/.bash_profile``, with ``~`` acting as equivalent of ``/Users/Rich``. Using ``~`` is a shortcut that also makes it generic and usable for everybody to understand and use.

Your Bash profile will pop up in a Sublime Text window.

Understanding your PATH
-----------------------

The first edit to your Bash profile is to correct your |PATH|_. ``PATH`` is an **environment variable**, which means that it simply represents some small bit of data while you use Terminal. Specifically, ``PATH`` contains a list of file system paths where OS X can find programs to run.

.. |PATH| replace:: ``PATH``
.. _PATH: http://en.wikipedia.org/wiki/PATH_%28variable%29

When a developer runs a program from Terminal, the computer will sequentially look for the program in each of the paths that ``PATH`` contains, starting with the first path listed. If the computer can't find the program in the first path, it looks for the same program in the second path, and so on, until either eventually finding and running the program or returning an error if the program couldn't be found.

``PATH`` contains paths that are delimited by a colon (``:``). Therefore, the value of ``PATH`` might look something like:

.. code-block:: bash

   /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

You can see that ``/usr/local/bin`` is the first path, and ``/usr/bin`` is the second path. ``/usr/local/bin`` is where all programs *local* to your use of the operating system are located. Storing programs for your personal use in ``/usr/local/bin`` is a best practice and highly encouraged. Therefore, the path listed earlier is correct.

Likewise, storing programs in ``/usr/bin`` allows programs to be globally accessible by other users. Although storing programs globally can sometimes be desirable, in general it's discouraged and likely to cause confusion.

Correcting your PATH
--------------------

In versions of OS X prior to Yosemite, Apple mistakenly switched the order of the paths, placing ``/usr/bin`` ahead of ``/usr/local/bin``, causing much disruption and angst. Apple has since corrected the issue, but it's still worth changing because doing so won't harm the operating system and will prevent problems from occuring again.

Copy and paste the following into your text editor:

.. code-block:: bash

   # Paths
   export PATH=/usr/local/bin:$PATH

The first line, which begins with a hash (``#``) is a comment and merely exists to help you remember your edits. The right portion of the second line begins ``/usr/local/bin``, which is the path we want to prioritize, followed by ``:``, which concatenates paths, and finally ``$PATH``, which calls the value of the existing ``PATH``. By appending ``$PATH`` we can change ``PATH`` without destroying the original value, making everything nice and tidy!

Next we assign the value ``/usr/local/bin:$PATH`` to ``PATH`` and export it at the same time. Exporting ``PATH`` ensures that the variable is loaded into memory and accessible.

.. figure:: img/bash_profile-code.png
   :alt: OS X Login items

Save and close the file.

Sourcing Bash profile
---------------------

Although we edited our Bash profile, it is critical to remember that Terminal runs the code in Bash profile only when a *new Terminal session is created*, which is called **sourcing**. Therefore, for our changes to take effect, you should quit Terminal and open it again to make sure that ``PATH`` is in fact exported. When Terminal is open again, you can check the value of ``PATH`` by running the ``echo`` command:

.. code-block:: bash

   $ echo $PATH

The output might look like one of the two:

.. code-block:: bash

   /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

.. code-block:: bash

   /usr/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

Ensure that ``/usr/local/bin`` is listed prior to ``/usr/bin``.

.. note::

   Although Terminal allows a Bash profile to be sourced by command without restarting--``source ~/.bash_profile``--I have found it to be unreliable.

``PATH`` is just one variable we changed in our Bash profile. We will edit our Bash profile to run more important code in the future.
