from enum import Enum

from time_mama_brains.config.dev import config as config_dev
from time_mama_brains.config.prod import config as config_prod
from time_mama_brains.config.default import config as config_default


class ConfigEnv(Enum):
    DEV = 1
    TEST = 2
    PROD = 10


def configure(venv: ConfigEnv):
    ext_config = dict({})
    ext_config.update(config_default)
    if venv == ConfigEnv.PROD:
        ext_config.update(config_prod)
    else:
        ext_config.update(config_dev)

    return ext_config
