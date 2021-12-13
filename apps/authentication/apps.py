# -*- encoding: utf-8 -*-
"""
__author__ = Cedrouseroll Omondi
__email__ = omondicedo@gmail.com
"""

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.authentication'
    verbose_name = _('authentication')

    def ready(self):
        import apps.authentication.signals
