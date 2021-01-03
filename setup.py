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


extra_cmake_args = ['-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON']
cmake_toolchain_file = os.environ.get('CMAKE_TOOLCHAIN_FILE', '')

if cmake_toolchain_file:
    extra_cmake_args += ['-DCMAKE_TOOLCHAIN_FILE={}'.format(cmake_toolchain_file)]


setup(
    cmake_install_dir='.',
    cmake_args=extra_cmake_args,
)
