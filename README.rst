the_pci_data
===============

This app can be installed and used in your django project by:

.. code-block:: bash

    $ pip install the_pci_data


Edit your `settings.py` file to include `'the_pci_data'` in the `INSTALLED_APPS`
listing.

.. code-block:: python

    INSTALLED_APPS = [
        ...

        'the_pci_data',
    ]

    # ------------------------------------------------------
    # django-otp
    # ------------------------------------------------------
    OTP_TOTP_ISSUER = 'sample pci data app'
    OTP_ENTRY_URL = '/twofactor/'



    MIDDLEWARE = [
        ...
   
    ]

     

 

Edit your project `urls.py` file to import the URLs:


.. code-block:: python

    url_patterns = [
        ...

        path('', include('the_pci_data.urls')),
    ]


Finally, add the models to your database:


.. code-block:: bash

    $ ./manage.py makemigrations the_pci_data


The "project" Branch
--------------------

The `master branch <https://github.com/realpython/django-receipts/tree/master>`_ contains the final code for the PyPI package. There is also a `project branch <https://github.com/realpython/django-receipts/tree/project>`_ which shows the "before" case -- the Django project before the app has been removed.


 