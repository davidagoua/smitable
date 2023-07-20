from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    },
    'mongo': {
        'ENGINE': 'djongo',
        'NAME': 'smitable',
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
            'username': 'smitable',
        }
    }
}
