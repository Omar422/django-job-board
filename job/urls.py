from django.urls import include, path

from . import views

app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    # before slug => so can access add like link
    path('add', views.add_job, name='add_job'),
    # path('<int:job_id>', views.job_detail, name='job_detail'),
    path('<str:title_slug>', views.job_detail, name='job_detail'),
]
