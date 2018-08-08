import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="PyFrac",

    description="Fractal flame generation tools",

    author="Sean Pope",

    packages=find_packages(exclude=['images','examples','docs']),

    long_description=read('README.md'),
)