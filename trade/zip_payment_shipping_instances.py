from .payment import Payment, PaymentFactory
from main.models import UserModel
from .shipping import Shipping, ShippingFacotry
from .models import TradeModel

def zip_payment_shipping_instances(trades: list,  user: UserModel) -> list:
    """ return a zip list with tuple (trade_object, {payment, shipping}) """
    payments = list(map(
        lambda trade: (
            trade,
            Payment(
                payment_method=PaymentFactory.create_payment_method(method_key=trade.payment_method),
                user=user,
                book=trade.book,
                trade=trade),
            Shipping(
                shipping=ShippingFacotry.get_shipping_instance(trade.shipping_method)
            )
        ),
        trades
    ))
    return payments