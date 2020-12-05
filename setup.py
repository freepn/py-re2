# -*- coding: utf-8 -*-
#

import io
import os
import re
import sys
import platform
from setuptools import setup
from distutils.core import Command, Extension

MINIMUM_CYTHON_VERSION = '0.20'
BASE_DIR = os.path.dirname(__file__)
PY2 = sys.version_info[0] == 2
DEBUG = False

class TestCommand(Command):
    description = 'Run packaged tests'
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from tests import re2_test
        re2_test.testall()


def majorminor(version):
    return [int(x) for x in re.match(r'([0-9]+)\.([0-9]+)', version).groups()]

cmdclass = {'test': TestCommand}

ext_files = []
if '--cython' in sys.argv or not os.path.exists('src/re2.cpp'):
    # Using Cython
    try:
        sys.argv.remove('--cython')
    except ValueError:
        pass
    from Cython.Compiler.Main import Version
    if majorminor(MINIMUM_CYTHON_VERSION) >= majorminor(Version.version):
        raise ValueError('Cython is version %s, but needs to be at least %s.'
                % (Version.version, MINIMUM_CYTHON_VERSION))
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize
    cmdclass['build_ext'] = build_ext
    use_cython = True
else:
    # Building from C
    ext_files.append('src/re2.cpp')
    use_cython = False


# Locate the re2 module
_re2_prefixes = ['/usr', '/usr/local', '/opt/', '/opt/local', os.environ.get('HOME', '') + '/.local']

re2_prefix = ''
for a in _re2_prefixes:
    if os.path.exists(os.path.join(a, 'include', 're2')):
        re2_prefix = a
        break

def get_long_description():
    with io.open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf8') as inp:
        return inp.read()

def get_authors():
    author_re = re.compile(r'^\s*(.*?)\s+<.*?\@.*?>', re.M)
    authors_f = open(os.path.join(BASE_DIR, 'AUTHORS'))
    authors = [match.group(1) for match in author_re.finditer(authors_f.read())]
    authors_f.close()
    return ', '.join(authors)

def main():
    os.environ['GCC_COLORS'] = 'auto'
    include_dirs = [os.path.join(re2_prefix, 'include')] if re2_prefix else []
    libraries = ['re2']
    library_dirs = [os.path.join(re2_prefix, 'lib')] if re2_prefix else []
    runtime_library_dirs = [os.path.join(re2_prefix, 'lib')
            ] if re2_prefix else []
    extra_compile_args = ['-O0', '-g'] if DEBUG else [
            '-O3', '-march=native', '-DNDEBUG']
    # Older GCC version such as on CentOS 6 do not support C++11
    if not platform.python_compiler().startswith('GCC 4.4.7'):
        extra_compile_args.append('-std=c++11')
    ext_modules = [
        Extension(
            're2',
            sources=['src/re2.pyx' if use_cython else 'src/re2.cpp'],
            language='c++',
            include_dirs=include_dirs,
            libraries=libraries,
            library_dirs=library_dirs,
            runtime_library_dirs=runtime_library_dirs,
            extra_compile_args=['-DPY2=%d' % PY2] + extra_compile_args,
            extra_link_args=['-g'] if DEBUG else ['-DNDEBUG'],
        )]
    if use_cython:
        ext_modules = cythonize(
            ext_modules,
            language_level=3,
            annotate=True,
            compiler_directives={
                'embedsignature': True,
                'warn.unused': True,
                'warn.unreachable': True,
            })
    setup(
        name='py-re2',
        version='0.3.1-1',
        description='Python wrapper for Google\'s RE2 using Cython',
        long_description=get_long_description(),
	long_description_content_type='text/x-rst',
        author=get_authors(),
        license='New BSD License',
        author_email='andreas@unstable.nl',
        url='https://github.com/andreasvc/pyre2',
        ext_modules = ext_modules,
        cmdclass=cmdclass,
        zip_safe=False,
        classifiers = [
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Cython',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 3.3',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        )

if __name__ == '__main__':
    main()
