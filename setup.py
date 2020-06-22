# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from setuptools.command.test import test

import os
import sys

if sys.version_info < (3, 7):
    sys.exit("Sorry, Python < 3.7 is not supported")

sys.executable = "/bin/env python"

version_path = os.path.join(os.path.dirname(__file__), "SimpleWebserviceMapper", "_version.py",)

with open(version_path) as version_file:
    env = {}
    exec(version_file.read(), env)
    VERSION = env["VERSION"]

setup(
    name="interstate_love_song.SimpleWebserviceMapper",
    version=VERSION,
    packages=find_packages(),
    author="Eric Hermelin, Simon Otter, Fredrik Brännbacka",
    author_email="eric.hermelin@ilpvfx.com, simon.otter@ilpvfx.com, fredrik.brannbacka@ilpvfx.com",
    python_requires=">3.6",
    entry_points={
        "interstate_love_song.plugins": "SimpleWebserviceMapper = SimpleWebserviceMapper"
    },
    install_requires = [
        "interstate_love_song>=2,<3"
    ]
)
