try:
    from config.settings.local import *
except ImportError as e:
    from config.settings.default import *
