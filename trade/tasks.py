import os
from django.conf import settings
from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
from .models import TradeModel
from book.models import BookModel
from typing import Type, Optional, Union
from django.contrib.auth import get_user_model
from main.models import UserModel
from .shipping import Shipping
from .payment import Payment

 
logger = get_task_logger(__name__)
 
@shared_task()
def thirty_second_func(): #testando
    logger.info("I run every 30 seconds using Celery Beat")
    return "Done"
 

@shared_task
def task_send_email_new_trade(
        email: str, 
        user_name: Optional[Union[UserModel, str]], 
        request_owner_name: Optional[Union[UserModel, str]], 
        book_to_trade: str,
        payment_value: Optional[Union[int, BookModel]],  #points or other book
        estimate_price: Optional[Union[float, str]]
    ) -> Optional[str]:

    """ simple task to send booking email confirmation to celery worker """

    if isinstance(user_name, TradeModel):
        user_name = user_name.username
    if isinstance(request_owner_name, TradeModel):
        request_owner_name = request_owner_name        


    subject = "Confirmação de troca"
    from_email = str(os.environ.get('EMAIL_HOST_USER'))
    to_email = [email]
    deploy_host = os.environ.get('DEPLOY_HOST')
    link_to_confirmation = f"https://{deploy_host}/trade/trocas-solicitadas"

    context = {
        'user_name': user_name,
        'request_owner_name': request_owner_name,
        'book_trade': str(book_to_trade),
        'payment': {
            'trade_value': payment_value,
            },
        'link_to_confirmation': link_to_confirmation,
        'current_year': datetime.now().year,
        'estimate_price_shipping': estimate_price
    }   

    html_content = render_to_string('global/email/new_trade.html', context)
    text_content = strip_tags(html_content)

    email_msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email_msg.attach_alternative(html_content, "text/html")
    email_msg.send()
    print(f'Email para {email} enviado com sucesso')
    return "Done"

   
