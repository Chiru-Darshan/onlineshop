from celery import Celery
import os

#  Django settings module for 'celery' program 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineshop.settings')

app = Celery('onlineshop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()