from django.urls import path, include
from . import views
from . import api

app_name  = 'job'

urlpatterns = [
    path('', views.job_list, name = 'job-list'),
    path('add/', views.add_job, name='add-job'),
    path('<str:slug>/', views.job_detail, name='job-detail'),

    #API V1
    path('api/jobs', api.jobs_api, name='joblistapi'),
    path('api/jobs/<int:id>', api.job_detail_api, name='jobdetailapi'),

    #API V2 Class Based Views
    path('api/v2/jobs', api.JobListApi.as_view(), name='joblistapi'),
    path('api/v2/jobs/<int:id>', api.JobDetailApi.as_view(), name='joblistapi'),
    

]


