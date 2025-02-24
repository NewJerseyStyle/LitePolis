# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='litepolis',
    version="v0.0.1",
    description='Replicating `civictechto/polis`, built using Python and optimized for scalability and performance.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Yuan XU',
    author_email='dev.source@outlook.com',
    url='https://github.com/NewJerseyStyle/LitePolis',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    # install_requires=['pydantic', 'ollama'],
    # entry_points={
    #     'console_scripts': [
    #         'ollama-tools=ollama_tools.server:main',
    #     ],
    # },
    # extras_require={
    #     'full': ['fastapi', 'uvicorn'],
    # },
)
