from celery import task
from celery.utils.log import get_task_logger
from .email import send_review_email

logger = get_task_logger(__name__)

@task
def send_review_email_task(name, email, review):
    logger = get_task_logger(__name__)  # Import the "get_task_logger" function and assign it to the "logger" variable
    logger.info("Sent review email")
    return send_review_email(name, email, review)

    
      
    
 