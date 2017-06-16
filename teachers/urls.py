from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.teacher_list, name = "teacher_list"),
    url(r'^detail/$', views.teacher_detail, name = "teacher_detail"),
    url(r'^add/$', views.teacher_add, name ="teacher_add"),
]
