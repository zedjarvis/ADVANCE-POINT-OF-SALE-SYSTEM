# -*- encoding: utf-8 -*-
"""
__author__ = Cedrouseroll Omondi
__email__ = omondicedo@gmail.com
"""

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.pos'
    verbose_name = _('point of sale')
