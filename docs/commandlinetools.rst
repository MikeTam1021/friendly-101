.. _`Command line tools`:

Command line tools
==================

Now that you're a little familiar with the command-line interface, we're going to install some additional tools to compile any software we might need.

What is compiling?
------------------

If you've downloaded software before, you're probably familiar with the song and dance by now: Go to the website, find the download link, click the download link, find the DMG, open it, open the mount, copy the application into the Applications folder, close the window, unmount the DMG, find the application, open the application, trash the DMG. *Whew*.

The DMG you downloaded is known as a **binary**, which was *compiled* from source code that other developers wrote, likely from many files into a single neat, tidy file ready for hungry downloaders. Not all software is compiled--especially development software that you might need--and because of that, I recommend learning the basics of compiling your own software. Fortunately, the ability to compile your own software has come a long way and is a lot easier than it used to be.

Installing the tools
--------------------

Compiling on OS X requires the `GNU Compiler Collection <https://en.wikipedia.org/wiki/GNU_Compiler_Collection>`_, or GCC, and is included in the **Command Line Tools** software by Apple. You can download Command Line Tools from the `Apple Developer website <https://developer.apple.com/downloads/>`_, but it is often more convenient to simply download and install it from the command line.

Open Terminal, copy and paste the following, and press ``Return``. Review the :ref:`Command line` lesson if necessary.

.. code-block:: bash

   $ xcode-select --install

Click ``Install``.

Once installed, confirm the installation:

.. code-block:: bash

   $ xcode-select --print-path
   /Library/Developer/CommandLineTools

Confirm GCC was installed:

.. code-block:: bash

   $ gcc --version
   Configured with: --prefix=/Library/Developer/CommandLineTools/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
   Apple LLVM version 6.0 (clang-600.0.54) (based on LLVM 3.5svn)
   Target: x86_64-apple-darwin14.0.0
   Thread model: posix

Do I need Xcode?
----------------

Previously Apple bundled Command Line Tools with `Xcode <https://developer.apple.com/xcode/>`_, a full suite of software development tools for developing native applications on OS X and iOS. The bundling forced developers to download the entire suite, which was about 2.5 GB in size.

Since the OS X release of Mavericks, developers can download Command Line Tools separately, which means developers do not *need* Xcode. However, if you downloaded Xcode before, then you will need to update it either in the App Store application or with Software Update.

If you verified the installation of Command Line Tools with Xcode installed, you will instead receive confirmation that Xcode was installed, which is perfectly fine.

.. code-block:: bash

   $ xcode-select --print-path
   /Applications/Xcode.app/Contents/Developer

.. code-block:: bash

   $ gcc --version
   Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
   Apple LLVM version 6.0 (clang-600.0.54) (based on LLVM 3.5svn)
   Target: x86_64-apple-darwin14.0.0
   Thread model: posix
