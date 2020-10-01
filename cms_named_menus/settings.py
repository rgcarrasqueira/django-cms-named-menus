# -*- coding: utf-8 -*-
'''
Created on Jan 30, 2017

@author: jakob
'''
from django.conf import settings

CACHE_DURATION = getattr(settings, 'CMS_NAMED_MENUS_CACHE_DURATION', 3600)
ALLOWED_NAMESPACES = getattr(settings, 'CMS_NAMED_MENUS_NAMESPACES', ['CMSMenu',])
REMOVE_UNAVAILABLE_PAGES = getattr(settings, 'CMS_NAMED_MENUS_REMOVE_UNAVAILABLE_PAGES', True)