Because snapboard runs on the Django framework, a host of installation options (database selection, CGI/mod\_python, etc) are available.  This document does not attempt to be a comprehensive guide on all the options available to you to run snapboard.  For that, a careful reading of the [Django installation document](http://www.djangoproject.com/documentation/install/) is a good start.

[Common server arrangements](http://code.djangoproject.com/wiki/ServerArrangements) are covered on the Django Wiki.

# Test Driving SNAPboard #
An example site is included in.  If you have Django and sqlite3 installed already, you can test-drive snapboard by simply running Django's built-in web server:

If you use MySQL or PostgreSQL, simply tweak `examplsite.settings`

When you run `syncdb` on the examplesite, you have the option of seeding the forum with garbage threads and posts.

```
$ cd /PATH/TO/SNAPBOARD
$ cd examplesite
$ python manage.py syncdb
$ python manage.py runserver
```

SNAPboard will install a temporary database at `/tmp/examplesite.db`.  If you use MySQL or PostgreSQL, simply tweak `examplsite.settings`.

Point your browser to http://localhost:8000/snapboard to see it in action!

# Debian Etch #
I use Etch - it's easy to get an environment to test things out:

```
$ apt-get install python-imaging subversion python-pysqlite2
```

Then [install Django](http://www.djangoproject.com/documentation/install/).