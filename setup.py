# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='litepolis',
    version="1.0.2",
    description='The package manager of a Customizable e-democracy opinion collection and insight mining system.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Yuan XU',
    author_email='dev.source@outlook.com',
    url='https://github.com/NewJerseyStyle/LitePolis',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['fastapi', 'ray[serve]', 'GitPython', 'click'],
    entry_points={
        'console_scripts': [
            'litepolis-cli=litepolis.core:main',
        ],
    },
    extras_require={
        'demo': [
            'litepolis-router-database',
            'litepolis-router-example',
            'litepolis-middleware-example',
            'litepolis-ui-example'
        ],
    },
)
