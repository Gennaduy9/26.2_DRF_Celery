import stripe

from config.settings import STRIPE_SECRET_API_KEY

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
        # product_data={"name": product['name']},
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
