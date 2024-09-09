import os
import re
from io import open

from setuptools import find_packages, setup

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('drf_writable_nested_fullclean')

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
with open('LICENSE', "r", encoding="utf-8") as f:
    license = f.read()
    
    
setup(
    name="drf-writable-nested-fullclean",
    version=version,
    author="Giuseppe Novielli",
    author_email="novielligiuseppe@gmail.com",
    description="Call django model full_clean() when validate WritableNestedModelSerializer",
    long_description=long_description,
    license=license,
    long_description_content_type="text/markdown",
    url="https://github.com/giuseppenovielli/drf-writable-nested-fullclean",
    keywords=['django-rest-framework', 'model-serializer', 'validate', 'full_clean', 'writable-nested', 'writable-nested-serializer', 'writable-nested-fullclean', 'writable-nested-fullclean-serializer'],
    install_requires=["djangorestframework>=3.0.0", 'drf-writable-nested==0.7.0', 'drf-fullclean'],
    packages=find_packages(exclude=['tests*']),
    project_urls={
        'Documentation': 'https://github.com/giuseppenovielli/drf-writable-nested-fullclean?tab=readme-ov-file#drf-writable-nested-fullclean',
        'Funding': 'https://buymeacoffee.com/giuseppedev',
        'Source': 'https://github.com/giuseppenovielli/drf-writable-nested-fullclean',
        'Tracker': 'https://github.com/giuseppenovielli/drf-writable-nested-fullclean/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
    ],
    python_requires='>=3.7',
)