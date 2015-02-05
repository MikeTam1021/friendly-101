Command line
============

After a good text editor, the next tool a developer needs to become familiar with is the `command-line interface <https://en.wikipedia.org/wiki/Command-line_interface>`_.

You won't break your computer
-----------------------------

A **command-line interface** is a program that allows developers to interact with a computer by running commands that are typed. The functionality between a command-line interface and the more familiar graphical user interface, known in OS X as the Finder, are identical.

Beginning developers often have a fear of the command line, thinking they will "break their computer" if they even open the application. Others think it's an old, archaic tool that can't possibly be useful to write modern software. Both ideas can be right, and both ideas can be wrong. As you'll discover, command-line interfaces have advantages and disadvantages just as graphical user interfaces do. Understanding the strengths and weaknesses of one's tools is one of the hallmarks of a good developer.

You can be bashful now
----------------------

The command-line interface we'll work with is **Bash**. Bash is a shell, which is a category of program that loads command-line interfaces, much like Chrome is a web browser. Bash is the most popular shell today and the default shell inside the `Terminal <https://en.wikipedia.org/wiki/Terminal_(OS_X)>`_ application on OS X. It's worthy to note that shells other than Bash can be loaded inside of Terminal--a feat that web browsers can't and will likely never do.

Open a Finder window, navigate to the Applications folder, then the Utilities folder, and open the Terminal application. It might look something like this, which shows a whole lot of white.

.. figure:: img/command_line-terminal.png
   :alt: Terminal

The first line tells me when I last started a Bash session (``Last login: Mon Feb 5 09:58:08``) and on which `Teletypes <http://en.wikipedia.org/wiki/Teleprinter>`_ (``ttys000``), although today the equivalent is simply a tab in Terminal, much like a tab in a web browser. The second line tells me the name of my computer on the network (``Rich``), my current directory (``~``, which is my home directory), the name of my user account (``rich``), and the symbol indicating a prompt for user input (``$``).

Feel free to trick it out in the Preferences. I like to make mine look like `The Matrix <http://www.imdb.com/media/rm541630976/tt0133093>`_.

.. figure:: img/command_line-terminal_matrix.png
   :alt: Terminal from the Matrix

I also recommend dragging the Terminal icon from the Applications folder `into your Dock <http://support.apple.com/kb/PH18815>`_ for easy access in the future.

Common Bash commands
--------------------

I will provide all of the commands you should run and the reason why, but it helps to remember the most commonly used commands and symbols. Each command or symbol is preceded by a comment, which is a line starting with a hash (``#``) and represents code that is merely explanatory. Also note that the prompt, represented by the dollar sign (``$``), is meant only to communicate that the line is a Bash command and is not meant to be included as part of the command.

Commands for directory manipulation (``<directory>`` represents the name of a directory):

.. code-block:: bash

   # Display (print) the path of the current (working) directory
   $ pwd

   # List the contents of a directory
   $ ls <directory>
   
   # Change the current directory
   $ cd <directory>
   
   # Make a directory
   $ mkdir <directory>

   # Open a directory in Finder
   $ open <directory>

Symbols for directory traversal:

.. code-block:: bash

   # The parent directory
   ../

   # The parent's parent directory
   ../../

   # The root directory
   /

   # The current directory
   .

These commands and others can be combined in interesting ways that would be difficult to replicate in a graphical user interface.

.. code-block:: bash

   # List the contents of the parent directory
   ls ../

   # Change to the parent's parent directory
   cd ../../

   # Make a directory in the root directory
   mkdir /<directory>

   # Open the current directory in Finder
   open .

If you feel like you need additional guidance, `The Command Line Crash Course <http://cli.learncodethehardway.org/book/>`_ by Zed Shaw is excellent.

Terminal, meet Sublime
----------------------

Let's run our first command, a helpful trick that will connect Terminal to Sublime Text. Note that you might need to enter your OS X password. Take care not to copy and paste the ``$`` and adjacent space.

.. code-block:: bash

   $ sudo ln -s "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl

This command will create a `symbolic link <http://en.wikipedia.org/wiki/Symbolic_link>`_, which is the equivalent of an alias or shortcut in the Finder. From now on, when we type ``subl`` and the name of a directory or file in Terminal, that same directory or file will pop up in Sublime Text, ready for us to edit!

Just like text editors, people have varying opinions on shells. `Bash <https://en.wikipedia.org/wiki/Bash_(Unix_shell)>`_ is most popular, but some developers claim `Z shell <https://en.wikipedia.org/wiki/Z_shell>`_ can be more productive. Terminal comes with OS X, but some swear by `iTerm2 <http://iterm2.com/>`_. Get comfortable with what's most accessible and when you feel confident, explore what else is out there.
