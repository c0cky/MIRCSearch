from django.conf.urls import patterns, url

from mirc import views

urlpatterns = patterns('',
   url(r'^$', views.index, name='name'),
   url(r'^ajax/', views.ajax, name='ajax'),
   url(r'^search/', views.search, name='search'),
   url(r'^noresults/', views.noresults, name='noresults'),
   url(r'^rearrange/', views.rearrange, name ='rearrange')
)
