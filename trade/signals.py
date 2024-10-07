# signals.py
import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import task_send_email_new_trade
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from .models import TradeModel
from .services import get_payment_method, get_shipping_method

@receiver(post_save, sender=TradeModel)
def send_email_new_trade(sender, instance, created, **kwargs) -> None:
    """ catch the signal from TradeModel on post_save, and send email confirmation to book.owner and trade.user """
    if created:
        try:
            payment = get_payment_method(trade=instance)

            shipping = get_shipping_method(trade=instance)
            shipping_estimate_price = shipping.calculate_price_shipping()

            book = instance.book

            task_send_email_new_trade.delay(
                email=book.owner.email,
                user_name=book.owner.full_name,
                request_owner_name = instance.user.full_name,
                book_to_trade=instance.book.title,
                payment_value=payment.trade_value,
                estimate_price = shipping_estimate_price,
            )   
        

        except ObjectDoesNotExist as error:
            print('erro ao pegar o objeto no signals: ', error)

        except Exception as error:
            print('error no signals: ', error)

    return None

