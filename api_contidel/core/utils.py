# myapp/utils.py

from rest_framework.authtoken.models import Token

def default_create_token(token_model, user):
    token, _ = token_model.objects.get_or_create(user=user)
    return token
