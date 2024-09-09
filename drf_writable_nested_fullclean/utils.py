import inspect

from django.conf import settings

def get_base_classes(instance):
    # https://stackoverflow.com/questions/1401661/list-all-base-classes-in-a-hierarchy-of-given-class
    class_type = type(instance)
    return list(inspect.getmro(class_type))


def remove_many_to_many(serializer, validated_data, **kwargs):
    for field in serializer.Meta.model._meta.many_to_many:
        if field.name in validated_data:
            del validated_data[field.name]
    return validated_data


# DEBUG
def print_debug(message):
    drf_full_clean = getattr(settings, 'DRF_WRITABLE_NESTED_FULLCLEAN', {})
    if not drf_full_clean.get('DEBUG', False):
        return
    print('\nDRF_WRITABLE_NESTED_FULLCLEAN -> {}'.format(message))
    

def get_is_allowed_partial_instances(serializer_obj):
    drf_full_clean = getattr(settings, 'DRF_WRITABLE_NESTED_FULLCLEAN', {})
    
    allow_partial_instances_serializer_meta = getattr(serializer_obj.Meta, 'allow_partial_instances', None)
    if isinstance(allow_partial_instances_serializer_meta, bool):
        return allow_partial_instances_serializer_meta
    else:
        return drf_full_clean.get('ALLOW_PARTIAL_INSTANCES', True)