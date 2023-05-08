import sys  # noqa: F401

try:
    from .local import * # noqa: F403, F401, E261
except ImportError:
    from .base import * # noqa: F403, F401, E261

# if 'test' in sys.argv:
#     from .tests import *
