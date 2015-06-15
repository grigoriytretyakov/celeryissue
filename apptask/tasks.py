import logging

from celery import shared_task
from datetime import datetime


logger = logging.getLogger('capybara.tasks')


@shared_task
def every_day():
    logger.info('Fire: %s', datetime.today())
