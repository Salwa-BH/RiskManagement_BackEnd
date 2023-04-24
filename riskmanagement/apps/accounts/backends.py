from django.conf import settings
from django.contrib.auth import get_user_model

class EmailOrUsernameModelBackend(object):
    """
    This is a ModelBacked that allows authentication with either a username or an email address.

    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("authentication sliw")
        if '@' in username:
            kwargs = {'email': username}
            print("connect with email")
        else:
            kwargs = {'username': username}
            print("connect with username")
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
#########################################################################################
    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None

    def get_user_model(self):
        """
        By default, this will return the model class configured by
        AUTH_USER_MODEL. Subclasses may wish to override it and return a proxy
        model.
        """
        return get_user_model()