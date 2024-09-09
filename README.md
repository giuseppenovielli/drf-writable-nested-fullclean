# drf-writable-nested-fullclean
![PyPI - Version](https://img.shields.io/pypi/v/drf-writable-nested-fullclean)
![PyPI - Downloads](https://img.shields.io/pypi/dm/drf-writable-nested-fullclean)

**Call django Model.full_clean(exclude=None, validate_unique=True) when validate WritableNestedModelSerializer**

## Installation
```
pip install drf-writable-nested-fullclean
```

## Configuration
Add the following code into settings.py
```
DRF_FULL_CLEAN = {
    "DEBUG" : False #set True if you want to see debug print
}
```
