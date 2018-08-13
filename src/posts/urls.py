from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_politics_list,
	post_events_list,
	post_gist_list,
	post_celeby_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
)

urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^politics/$', post_politics_list, name='politis'),
	url(r'^events/$', post_events_list, name='event'),
	url(r'^gist/$', post_gist_list, name='gist'),
	url(r'^celebs/$', post_celeby_list, name='celes'),
	url(r'^create/$', post_create),
	url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
	url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
	url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name="delete"),
]

