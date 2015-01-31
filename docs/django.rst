Django
======

.. code-block:: bash

   $ mkdir -p ~/Sites/ && cd ~/Sites/
   $ mkvirtualenv myproject
   $ pip install django
   $ django-admin startproject myproject
   $ cd myproject
   $ python manage.py migrate
   $ python manage.py runserver
   $ deactivate
