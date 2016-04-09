# [Revision 200](https://code.google.com/p/snapboard/source/detail?r=200) #

  * `related_name` attributes were added to fields related to external models. Those that existed were changed for consistency. All are now prefixed with 'sb' so as to avoid potential conflict with other applications.
  * The Post model now has an `is_private` field, a boolean which indicates whether there are private recipients. This removes the need to perform a db query or join every time an authenticated user wants to display a non-private post.

# [Revision 193](https://code.google.com/p/snapboard/source/detail?r=193) #

  * [django-pagination](http://code.google.com/p/django-pagination/) is now an external dependency.

# [Revision 182](https://code.google.com/p/snapboard/source/detail?r=182) #

  * As of [r182](https://code.google.com/p/snapboard/source/detail?r=182), integrated registration has been removed.  We recommend using an actively maintained and more full-featured registration application (such as django-registration).

  * The middleware classes for User and IP address bans are now 'snapboard.middleware.ban.IPBanMiddleware' and 'snapboard.middleware.ban.UserBanMiddleware'.
> The models to support those bans have changed.

  * The SnapboardProfile model has been changed to UserSettings, which only holds the user's preferences for board navigation.

  * The SNAP\_PREFIX setting has disappeared in favor of the more flexible named urls (http://docs.djangoproject.com/en/dev/topics/http/urls/#id2).