# -*- coding: utf-8 -*-
#

import io
import os
import re
import sys
import platform
from setuptools import setup
from distutils.core import Command, Extension

try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise


setup(
    cmake_install_dir='.',
    #cmake_args=["-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",],
)
