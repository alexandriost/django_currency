from .settings import * # noqa: F401,F403,E261

DEBUG = False
CELERY_TASK_ALWAYS_EAGER = True

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}
