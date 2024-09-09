from rest_framework import serializers

from .mixins import NestedFullCleanCreateMixin, NestedFullCleanUpdateMixin


class WritableNestedFullCleanModelSerializer(NestedFullCleanCreateMixin, NestedFullCleanUpdateMixin,
                                    serializers.ModelSerializer):
    pass