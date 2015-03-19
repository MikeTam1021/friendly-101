from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    """
    Django should display the "It worked!" page without editing the project
    URLconf, which originally shows the admin and comments out the homepage:

    # url(r'^$', 'friendly101.views.home', name='home'),

    However, Heroku seems to change this default behavior and returns a
    404 not found for the homepage. Therefore, I explicitly set the
    the URL for home to the "It worked!" `default_urlconf` view.
    """
    '',

    url(r'^$', 'django.views.debug.default_urlconf', name='home'),

    url(r'^admin/', include(admin.site.urls)),

)
