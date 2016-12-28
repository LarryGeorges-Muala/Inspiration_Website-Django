from django.conf.urls import url
from . import views

app_name = 'inspiration'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<author_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^about/$', views.about, name='about'),
]