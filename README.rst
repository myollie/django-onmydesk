.. image:: https://travis-ci.org/knowledge4life/django-onmydesk.svg?branch=develop
       :target: https://travis-ci.org/knowledge4life/django-onmydesk
.. image:: https://readthedocs.org/projects/django-onmydesk/badge/?version=latest
       :target: http://django-onmydesk.readthedocs.io/en/latest/?badge=latest
       :alt: Documentation Status
.. image:: https://badge.fury.io/py/django-onmydesk.svg
       :target: https://badge.fury.io/py/django-onmydesk
.. image:: https://img.shields.io/github/issues/knowledge4life/django-onmydesk.svg
       :target: https://github.com/knowledge4life/django-onmydesk/issues
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
       :target: https://raw.githubusercontent.com/knowledge4life/django-onmydesk/develop/LICENSE
.. image:: https://coveralls.io/repos/github/knowledge4life/django-onmydesk/badge.svg?branch=master
       :target: https://coveralls.io/github/knowledge4life/django-onmydesk?branch=master



Django - OnMyDesk
===================

A Django app to build reports in a simple way.

App focused on developers with an easy way to retrieve information from application or any other source making it available to be shared.

Main features:

- Easy way to create reports by developers.
- Easy way to make reports available to users by a screen on admin.
- Possibility to use raw SQL queries or Django ORM to extract information.
- Possibility of retrieving informations from third party systems that enable some kind of integration (like an API).
- Easy way to give parameters from users on report creation.
- Possibility to schedule report creation with e-mail notification.

Installation
------------

With pip::

  pip install django-onmydesk

Add 'onmydesk' to your INSTALLED_APPS::

  INSTALLED_APPS = [
      # ...
      'onmydesk',
  ]

Run `./manage.py migrate` to create **OnMyDesk** models.

Quickstart
-----------

To create reports we need to follow just two steps:

    1. Create a report class in our django app.
    2. Add this report class to a config in you project settings to enable **OnMyDesk** to see your reports.

So, let's do it!

Create a module called *reports.py* in you django app with the following content:

myapp/reports.py::

    from onmydesk.core import reports

    class UsersReport(reports.SQLReport):
        name = 'Users report'
        query = 'SELECT * FROM auth_user'

On your project settings, add the following config::

    ONMYDESK_REPORT_LIST = [
    'myapp.reports.UsersReport',
    ]

Each new report must be added to this list. Otherwise, it won't be shown on admin screen.

Now, access your **OnMyDesk** admin screen and you'll see your **Users report** available on report creation screen.


After you create a report, it'll be status settled up as 'Pending', to process it you must run `process` command. E.g::

  $ ./manage.py process
  Found 1 reports to process
  Processing report #29 - 1 of 1
  Report #29 processed

Collaboration
-------------

There are many ways of improving and adding more features, so feel free to collaborate with ideas, issues and/or pull requests.

Let us know!
-------------

We'd be really happy if you sent us links to your projects where you use our component. Just create an issue and let us know if you have any questions or suggestion regarding the library.

Licence | License |
--------------

Please see `LICENSE <https://github.com/knowledge4life/django-onmydesk/LICENSE>`_.

.. |License| image:: http://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
