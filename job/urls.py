from django.urls import include, path

from . import views
from . import api

app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    # before slug => so can access add like link
    path('add', views.add_job, name='add_job'),
    # path('<int:job_id>', views.job_detail, name='job_detail'),
    path('<str:title_slug>', views.job_detail, name='job_detail'),

    # api
    path('api/jobs', api.job_list_api, name='job_list_api'),
    path('api/jobs/<int:job_id>', api.job_detail_api, name='job_detail_api'),

    ## class based view 
    path('api/v2/jobs', api.JobListApi.as_view(), name='JobListApi'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view(), name='JobDetail'),
]
