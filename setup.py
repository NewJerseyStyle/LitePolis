# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='litepolis',
    version="v0.0.2",
    description='The package manager and core module for LitePolis',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Yuan XU',
    author_email='dev.source@outlook.com',
    url='https://github.com/NewJerseyStyle/LitePolis',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['fastapi', 'ray[serve]'],
    entry_points={
        'console_scripts': [
            'litepolis-cli=litepolis.core:main',
        ],
    },
    extras_require={
        'demo': [
            'litepolis-router-example',
            'litepolis-middleware-example',
            'litepolis-ui-example'
        ],
    },
)
