# Hashem Barudi
# Web Server Gateway Interface (WSGI) for python Django

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "bulletin_board_core.settings"
)
application = get_wsgi_application()
