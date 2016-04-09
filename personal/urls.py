from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact/contact_success/$', views.contact_success, name='contact_success'),
    url(r'^diy/$', views.diy, name='diy'),
    url(r'^about/$', views.about, name='about'),
    url(r'^cookies/$', views.cookies, name='cookies'),
    ]
