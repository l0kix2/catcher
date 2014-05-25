# coding: utf-8
from setuptools import setup
from pip.req import parse_requirements

requirements = [
    str(ir.req)
    for ir in parse_requirements('requirements.txt')
]

setup(
    name='catcher',
    version='0.1.0',
    install_requires=requirements,
)
