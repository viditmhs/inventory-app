from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^add', views.add, name='add'),
	url(r'^get', views.get, name='get'),
	url(r'^appendTrip', views.appendTrip, name='appendTrip'),
	url(r'^appendService', views.appendService, name='appendService'),
]