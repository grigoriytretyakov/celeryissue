# -*- coding: utf-8 -*-

import celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryissue.settings')
from django.conf import settings

celery_app = celery.Celery('celeryissue')
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
