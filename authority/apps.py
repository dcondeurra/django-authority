from django.apps import AppConfig
from django.contrib.auth import user_logged_in
from accounts.signal_handlers import set_language

__author__ = 'dniel'


class AuthorityConfig(AppConfig):
    """Class that used to configure the module.

    """
    name = 'authority'
