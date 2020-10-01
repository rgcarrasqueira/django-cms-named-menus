# -*- coding: utf-8 -*-
from django.contrib.auth.models import AnonymousUser
from menus.menu_pool import menu_pool


def anonymous_request(f):
    def decorator(request, *args, **kwargs):
        auth_user = None
        if request.user.is_authenticated:
            auth_user = request.user
            request.user = AnonymousUser()
        try:
            result = f(request, *args, **kwargs)
        finally:
            if auth_user is not None:
                request.user = auth_user
        return result

    return decorator


def filter_nodes(nodes):
    return [node for node in nodes if not node.attr.get('cms_named_menus_hidden', False) and
            node.attr.get("is_page", False)]


@anonymous_request
def get_nodes(request, namespace=None, root_id=None):

    # Set the menu renderer to force use of the anonymous version
    menu_renderer = menu_pool.get_renderer(request)

    nodes = menu_renderer.get_nodes(namespace, root_id, breadcrumb=False)

    nodes = filter_nodes(nodes)

    return nodes, menu_renderer

