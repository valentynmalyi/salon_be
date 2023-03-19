from pathlib import Path

from environs import Env

env = Env()
BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(str(BASE_DIR.joinpath(".env")))


INSTALLED_APPS = [
    'apps.asd',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASS"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.int("DB_PORT"),
    },
}

TIME_ZONE = 'UTC'
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
