from django.conf.urls import patterns, url

urlpatterns = patterns(
    'hello.views',
    url(r'^tasks/$', 'task_list', name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', 'task_detail', name='task_detail'),
    url(r'^water/$', 'water_list', name='water_list'),
    url(r'^water/(?P<pk>[0-9]+)$', 'water_detail', name='water_detail'),
)