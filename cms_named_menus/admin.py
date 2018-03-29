import json

from django.utils.functional import Promise
from django.utils.encoding import force_text

from django.conf import settings
from django.contrib import admin

from cms_named_menus.models import CMSNamedMenu
from cms_named_menus.nodes import get_nodes

class LazyEncoder(json.JSONEncoder):
    """Encodes django's lazy i18n strings.
        Used to serialize translated strings to JSON, because
        simplejson chokes on it otherwise. """

    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return obj


class CMSNamedMenuAdmin(admin.ModelAdmin):
    
    change_form_template = 'cms_named_menus/change_form.html'

    readoly_fields = ('pages_json',)

    def change_view(self, request, object_id, form_url='', extra_context={}):
        menu_pages = CMSNamedMenu.objects.get(id=object_id).pages
        extra_context = {
            'menu_pages': json.dumps(menu_pages),
            'available_pages': self.serialize_navigation(request),
            'debug': settings.DEBUG,
        }
        return super(CMSNamedMenuAdmin, self).change_view(request, object_id, form_url, extra_context)

    def serialize_navigation(self, request):
        nodes = get_nodes(request)
        cleaned = []
        for node in nodes:
            # Allow hiding from named menu selection
            if node.attr.get('cms_named_menus_hidden', False):
                continue
            node.children = None
            node.parent = None
            cleaned.append(node.__dict__)
        return json.dumps(cleaned, cls=LazyEncoder)


admin.site.register(CMSNamedMenu, CMSNamedMenuAdmin)
