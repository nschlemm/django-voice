from django.contrib.sites.models import Site
from settings import BRAND_VIEW


def djangovoice_extra_context(method):
    """
    Adds djangovoice extra contexts to view context variable params.
    """
    def wrapped(self, **kwargs):
        context = method(self, **kwargs)

        for c_key, c_value in get_djangovoice_extra_context().items():
            context.setdefault(c_key, c_value)

        return context
    return wrapped


def get_djangovoice_extra_context():
    """
    Gets extra context for djangovoice.

    :return: a context dict.
    """
    if Site._meta.installed:
        current_site = Site.objects.get_current()

    else:
        current_site = None

    context = {
        'site': current_site,
        'brand_view': BRAND_VIEW
    }

    return context
