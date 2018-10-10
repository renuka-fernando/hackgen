# Copyright (c) 2018 Renuka Fernando
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import setup, find_packages

with open("README", "r") as fh:
    long_description = fh.read()

setup(
    name="hackgen",
    version="1.0.0",
    author="Renuka Fernando",
    author_email="renukapiyumal@gmail.com",
    license="MIT",
    description="HackerRank Test-Case Generator",
    long_description=long_description,
    url="https://github.com/renuka-fernando/hackgen",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
