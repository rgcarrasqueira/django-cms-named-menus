# -*- coding: utf-8 -*-
from cms_named_menus import cache
from cms_named_menus.models import CMSNamedMenu

from cms.models.titlemodels import Title
from django.db.models.signals import post_save, post_delete
from django.dispatch.dispatcher import receiver


@receiver(post_save, sender=CMSNamedMenu, dispatch_uid='clear_cache_named_menu_saved')
def clear_cache_named_menu_saved(sender, instance, **kwargs):
    cache.delete(instance.slug)


@receiver(post_delete, sender=CMSNamedMenu, dispatch_uid='clear_cache_named_menu_deleted')
def clear_cache_named_menu_deleted(sender, instance, **kwargs):
    cache.delete(instance.slug)


@receiver(post_save, sender=Title, dispatch_uid='clear_cache_title_saved')
def clear_cache_title_saved(sender, instance, **kwargs):
    cache.delete_by_page_id(instance.page.id)


@receiver(post_delete, sender=Title, dispatch_uid='clear_cache_title_deleted')
def clear_cache_title_deleted(sender, instance, **kwargs):
    cache.delete_by_page_id(instance.page.id)
