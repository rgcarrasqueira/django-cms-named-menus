# -*- coding: utf-8 -*-
from django.apps import AppConfig


class CMSNamedMenusConfig(AppConfig):
    name = 'cms_named_menus'
    verbose_name = 'Django-CMS Named Menus'

    def ready(self):
        import cms_named_menus.signals

