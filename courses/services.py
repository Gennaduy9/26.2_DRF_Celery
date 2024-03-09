import stripe
import os

from config.settings import STRIPE_SECRET_API_KEY
from courses.models import Course

API_KEY = STRIPE_SECRET_API_KEY


def get_session(payment):
    """ Функция возвращает сессию для оплаты """
    stripe.api_key = API_KEY

    product = stripe.Product.create(
        name=f'{payment.name}'
    )

    price = stripe.Price.create(
        currency='eur',
        unit_amount=payment.price_amount,
        product=f'{product.id}',
        #product_data={"name": product['name']},
    )

    session = stripe.checkout.Session.create(
        # success_url="http://example.com/success",
        success_url="http://127.0.0.1:8000/",
        line_items=[
            {
                'price': f'{price.id}',
                'quantity': 1,
            }
        ],
        mode='payment',
        # customer_email=f'{instance.user.email}'

    )
    # return session
    return session.url

# def create_stripe_price(payment):
#     stripe.api_key = API_KEY
#
#     stripe_product = stripe.Product.create(
#         name=payment.paid_course.name
#     )
#
#     stripe_price = stripe.Price.create(
#         currency="rub",
#         unit_amount=payment.payment_amount*100,
#         product_data={"name": stripe_product['name']},
#     )
#
#     return stripe_price['id']
#
#
# def create_stripe_session(stripe_price_id):
#     stripe.api_key = API_KEY
#     stripe_session = stripe.checkout.Session.create(
#         line_items=[{
#             'price': stripe_price_id,
#             'quantity': 1
#         }],
#         mode='payment',
#         success_url='https://example.com/success',
#     )
#
#     return stripe_session['url'], stripe_session['id']
