# Hashem Barudi
# Asynchronous Server Gateway Interface (ASGI) for python Django

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "bulletin_board_core.settings"
)
application = get_asgi_application()
