from django.conf.urls import url
from . import views

app_name = 'students'
urlpatterns = [
    url(r'^$', views.student_list, name = 'student_list'),
    url(r'^detail/$', views.detail, name = 'detail'),
    url(r'^add/$', views.students_add, name = 'students_add'),

]
