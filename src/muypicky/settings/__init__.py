from .base import *

from .production import *

try:
    from .local import *
except:
    pass

# Currently it is loading local as a setting file
