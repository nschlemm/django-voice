from django.conf import settings

BRAND_VIEW = getattr(settings, 'VOICE_BRAND_VIEW', 'djangovoice_home')
