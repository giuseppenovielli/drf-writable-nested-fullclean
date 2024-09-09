__title__ = 'DRF writable nested with Model.fullclean() validation'
__version__ = '0.0.1'
__author__ = 'beda.software, giuseppe novielli' 
__license__ = 'MIT'
__copyright__ = 'Copyright 2014-2022 beda.software, Copyright 2024 giuseppe novielli'

# Version synonym
VERSION = __version__


from .mixins import (
    NestedFullCleanCreateMixin,
    NestedFullCleanUpdateMixin,
)
from .serializers import WritableNestedFullCleanModelSerializer
