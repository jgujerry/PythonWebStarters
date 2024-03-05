from django.urls import path

from app.views import index, sync_run_modeling_job, async_run_modeling_job


urlpatterns = [
    path("", index, name="index"),
    path('sync-run-modeling-job/', sync_run_modeling_job),
    path('async-run-modeling-job/', async_run_modeling_job)
]
