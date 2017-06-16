from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lecture_list, name = 'lecture_list'),
    url(r'^detail/$', views.lecture_detail, name = 'lecture_detail'),
    url(r'^add/$', views.lecture_add, name = 'lecture_add'),
    
]
