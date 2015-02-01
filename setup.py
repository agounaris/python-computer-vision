# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('bootstrap/bootstrap.py').read(),
    re.M
).group(1)

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="python-computer-vision",
    packages=["bootstrap"],
    entry_points={
        "console_scripts": ['bootstrap = bootstrap.bootstrap:main']
    },
    version=version,
    description="Python command line application to test computer vision scripts",
    long_description=long_descr,
    author="Argyrios Gounaris",
    author_email="agounaris@gmail.com",
    url="http://agounaris.github.io",
)
