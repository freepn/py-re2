#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Adapted from:
#   https://git.sr.ht/~cnx/palace/tree/main/item/setup.py
#   Copyright (C) 2019, 2020  Nguyễn Gia Phong
#   Copyright (C) 2020  Francesco Caliumi
#

import re
import sys

from distutils import log
from distutils.command.clean import clean
from distutils.dir_util import mkpath
from distutils.errors import DistutilsExecError, DistutilsFileError
from operator import methodcaller
from os import environ, unlink
from os.path import dirname, join
from platform import system
from subprocess import DEVNULL, PIPE, run, CalledProcessError

from Cython.Build import cythonize
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

CPPSTD = '/std:c++11' if system() == 'Windows' else '-std=c++11'
PY2 = sys.version_info[0] == 2
fallback_ver = '0.3.2'

try:
    TRACE = int(environ['CYTHON_TRACE'])
except KeyError:
    TRACE = 0
except ValueError:
    TRACE = 0


def src(file: str) -> str:
    """Return path to the given file in src."""
    return join(dirname(__file__), 'src', file)


class CMakeBuild(build_ext):
    """CMake extension builder and process runner."""
    def finalize_options(self) -> None:
        super().finalize_options()
        mkpath(self.build_temp)
        try:
            cmake = run(
                ['cmake', '../..'], check=True, stdout=DEVNULL, stderr=PIPE,
                cwd=self.build_temp, universal_newlines=True)
        except CalledProcessError as e:
            log.error(e.stderr.strip())
            raise DistutilsExecError(str(e))

        for key, value in map(methodcaller('groups'),
                              re.finditer(r'^re2_(\w*)=(.*)$',
                                          cmake.stderr, re.MULTILINE)):
            for ext in self.extensions:
                getattr(ext, key).extend(value.split(';'))


class CleanCpp(clean):
    """Remove Cython C++ outputs on clean command."""
    def run(self) -> None:
        for cpp in [src('re2.cpp')]:
            log.info(f'removing {cpp!r}')
            try:
                unlink(cpp)
            except OSError as e:
                raise DistutilsFileError(
                    f'could not delete {cpp!r}: {e.strerror}')
        super().run()


setup(cmdclass=dict(build_ext=CMakeBuild, clean=CleanCpp),
      ext_modules=cythonize(
          Extension(name='re2', sources=[src('re2.pyx')],
                    define_macros=[('CYTHON_TRACE', TRACE)],
                    extra_compile_args=[CPPSTD, '-DPY2=%d' % PY2],
                    libraries=['re2'],
                    language='c++'),
          compiler_directives={
              'binding': True,
              'linetrace': TRACE,
              'language_level': '3',
              'embedsignature': True,
              'warn.unused': True,
              'warn.unreachable': True
          }),
      use_scm_version={'root': '.',
          'relative_to': __file__,
          'fallback_version': fallback_ver,
          'version_scheme': 'post-release',
      },
      setup_requires=['setuptools_scm'],
)
