from django.urls import path
from LogApp.views import process_log_files

urlpatterns = [
    path('process-logs/', process_log_files, name='process_logs'),
]
