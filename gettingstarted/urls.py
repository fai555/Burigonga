from django.conf.urls import patterns, include, url
import hello.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
	'',
    url(r'^$', 'hello.views.login'),
	url(r'^accounts/login/$', 'hello.views.login'),
	url(r'^accounts/loading_main_page/$', 'hello.views.loading_main_page'),
	url(r'^accounts/loading_login_page/$', 'hello.views.loading_login_page'),
	url(r'^accounts/auth/$', 'hello.views.auth_view'),
	url(r'^accounts/logout/$', 'hello.views.logout'),
	url(r'^accounts/loggedin/$', 'hello.views.loggedin'),
	url(r'^accounts/invalid/$', 'hello.views.invalid_login'),
	url(r'^accounts/register/$', 'hello.views.register_user'),
	url(r'^accounts/register_success/$', 'hello.views.register_success'),
    url(r'^api/', include('hello.urls')),
    url(r'^admin/', include(admin.site.urls)),
)