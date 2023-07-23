from .settings import *

# mongodb://root:example@147.135.165.171:27017/?tls=false
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / env('DB_NAME'),
    },
    'mongodb': {
        'ENGINE': 'djongo',
        'NAME': 'huge',
        'CLIENT': {
            'host': '147.135.165.171',
            'port': 27017,
            'username': 'root',
            'password': 'example',
        }
    }
}
