from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class TokenManager:
    @staticmethod
    def generate_token(user):
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        return token

    @staticmethod
    def verify_token(user, token):
        token_generator = PasswordResetTokenGenerator()
        return token_generator.check_token(user, token)
