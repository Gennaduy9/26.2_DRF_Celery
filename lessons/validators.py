import re
from rest_framework.serializers import ValidationError


class UrlLinkCheckValidator:

    def __init__(self, field):
        self.base = field

    def __call__(self, value):
        url_link_check = dict(value).get(self.base)
        if url_link_check:
            if bool(re.match(r'https://www.youtube.com/', url_link_check)) is False:
                raise ValidationError('Нельзя использовать стороннюю ссылку кроме youtube')

# def validator_scam_url(value):
#     """Валидация ссылки на материал"""
#
#     for link in value.split():
#         parsed_url = urlparse(link)
#         if parsed_url.netloc != 'youtube.com':
#             raise ValidationError(f"Вы используете запрещенную ссылку: '{parsed_url.netloc}', только 'youtube.com'")
