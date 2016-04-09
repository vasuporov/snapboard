**This page is deprecated.  Please see the official documentation for setup instructions.**

http://snapboard.deadpuck.net/docs/

For comments, questions and concerns, please see the Google [Group](http://groups.google.com/group/snapboard-discuss).

So you've got some Django project up and running - well, adding snapboard is a snap!  You just need to make a few symbolic links and minor changes to your Django settings and URLs.

# Recommended Setup #

Check out a copy of snapboard and make a symbolic link to the application in your project directory.
```
$ svn checkout http://snapboard.googlecode.com/svn/trunk/ snapboard_trunk
$ ln -s `pwd`/snapboard_trunk/snapboard /path/to/django/exampleproject
```

Create a symbolic link your media directory pointing to snapboard media files.
```
$ ln -s `pwd`/snapboard_trunk/media /path/to/django/media/snapboard
```

## urls.py ##
Edit your project urls (exampleproject/url.py) so the the following tuple is included:
```
    (r'^snapboard/', include('exampleproject.snapboard.urls')),
```

## settings.py ##
Tell snapboard where the media files are:
```
SNAP_MEDIA_PREFIX = MEDIA_URL + '/media/snapboard'
```

Modify `MIDDLEWARE_CLASSES` to include snapboard middleware:
```
MIDDLEWARE_CLASSES = (
    ...
    # SNAPboard middleware
    'exampleproject.snapboard.middleware.threadlocals.ThreadLocals',
)
```

You then need to modify the `TEMPLATE_CONTEXT_PROCESSORS` setting<sup>1</sup>:
```
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",

    # SNAPboard processors
    "examplesite.snapboard.views.snapboard_default_context",
)
```

> <sup>1</sup> There is a gotcha here; the default template context processors are `auth`, `debug`, `i18n`, and `request`.  When you set `TEMPLATE_CONTEXT_PROCESSORS` in your project settings file, the defaults are no longer applied.  At a _minimum_, you need `auth` and `request`.  For more information see the Djano settings [documentation](http://www.djangoproject.com/documentation/settings/#template-context-processors).

Finally, add `examplesite.snapboard` to the list of `INSTALLED_APPS`.

## Voila! ##

At this point, you can sync up and deploy.
```
$ cd /path/to/exampleproject; python manage.py syncdb
```


# Extras #

## Account Registration ##
Optionally, if you want the snapboard account registration application, you can create a symbolic link in your project directory pointing to the `sbreg` application.
```
$ ln -s /path/to/snapboard_trunk/sbreg /path/to/django/exampleproject
```

Add `sbreg` to your urls (`urls.py`):
```
    (r'^accounts/', include('sbreg.urls')),
```

And add it to your list of installed applications (`settings.py`):
```
    'examplesite.sbreg',
```

## URLs ##
You don't have to use `/snapboard` as your base URL.  A good alternative is:
```
    (r'^forum/', include('examplesite.snapboard.urls')),
    (r'^forums/', include('examplesite.snapboard.urls')),
```

In this case, you need to set an additional snapboard variable in `settings.py`, e.g. for the urls above, you would need to set `SNAP_PREFIX` such that
```
SNAP_PREFIX = '/forums'    # note the lack of a trailing slash
```

## Media Files ##
snapboard will accept a setting to specify a custom media location.  The default is:
```
SNAP_MEDIA_PREFIX = MEDIA_URL + '/media'
```
If that's okay, you don't need to do anything.  If you've moved the media files somewhere special, just set the above variable.

## Templates ##
**This section is incomplete**
SNAPboard templates are designed to be as flexible as possible.  It is very easy to override them.  We've tried to use the same template block variable names as the admin templates, so you should be comfortable doing small customizations.  Larger changes like layout changes should also be relatively straightforward.

# Credits #
Thanks to johnnie.pittman for contributing to this page.