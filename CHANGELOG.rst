v0.3.1 (2020-10-27)
-------------------
- Bump version. [Andreas van Cranenburgh]
- Change package name for pypi. [Andreas van Cranenburgh]


v0.3 (2020-10-27)
-----------------
- Bump version. [Andreas van Cranenburgh]
- Merge pull request #14 from yoav-orca/master. [Andreas van
  Cranenburgh]

  Support building wheels automatically using github actions
- Creating github actions for building wheels. [Yoav Alon]
- Created pyproject.toml. [Yoav Alon]

  Poetry and other modern build system need to know which build-tools to
  install prior to calling setup.py. added a pyproject.toml to specify
  cython as a dependency.
- Add contains() method. [Andreas van Cranenburgh]

  - contains() works like match() but returns a bool to avoid creating a
    Match object. see #12
  - add wrapper for re.Pattern so that contains() and count() methods are
    also available when falling back to re.
- Disable dubious tests. [Andreas van Cranenburgh]

  - All tests pass.
  - Don't test for exotic/deprecated stuff such as non-initial flags in
    patterns and octal escapes without leading 0 or triple digits.
  - Known corner cases no longer reported as failed tests.
  - support \b inside character class to mean backspace
  - use re.error instead of defining subclass RegexError; ensures that
    exceptions can be caught both in re2 and in a potential fallback to re.
- Disable failing test for known corner case. [Andreas van Cranenburgh]
- Remove tests with re.LOCALE flag since it is not allowed with str in
  Python 3.6+ [Andreas van Cranenburgh]
- Decode named groups even with bytes patterns; fixes #6. [Andreas van
  Cranenburgh]
- Make -std=c++11 the default; fixes #4. [Andreas van Cranenburgh]
- Merge pull request #5 from mayk93/master. [Andreas van Cranenburgh]

  Adding c++ 11 compile flag on Ubuntu
- Adding c++ 11 compile flag on Ubuntu. [Michael]
- Merge pull request #3 from podhmo/macports. [Andreas van Cranenburgh]

  macports support
- Macports support. [podhmo]
- Use STL map for unicodeindices. [Andreas van Cranenburgh]
- Only translate unicode indices when needed. [Andreas van Cranenburgh]
- Update README. [Andreas van Cranenburgh]
- Add -std=c++11 only for clang, because gcc on CentOS 6 does not
  support it. [Andreas van Cranenburgh]
- Disable non-matched group tests; irrelevant after dad49cd. [Andreas
  van Cranenburgh]
- Merge pull request #2 from messense/master. [Andreas van Cranenburgh]

  Fix groupdict decode bug
- Fix groupdict decode bug. [messense]
- Merge pull request #1 from pvaneynd/master. [Andreas van Cranenburgh]

  Ignore non-matched groups when replacing with sub
- Ignore non-matched groups when replacing with sub. [Peter Van Eynde]

  From 3.5 onwards sub() and subn() now replace unmatched groups with
  empty strings. See:

  https://docs.python.org/3/whatsnew/3.5.html#re

  This change removes the 'unmatched group' error which occurs when using
  re2.
- Fix setup.py unicode error. [Andreas van Cranenburgh]
- Add C++11 param; update URL. [Andreas van Cranenburgh]
- Fix bugs; ensure memory is released; simplify C++ interfacing;
  [Andreas van Cranenburgh]

  - Fix bug causing zero-length matches to be returned multiple times
  - Use Latin 1 encoding with RE2 when unicode not requested
  - Ensure memory is released:
    - put del calls in finally blocks
    - add missing del call for 'matches' array
  - Remove Cython hacks for C++ that are no longer needed;
    use const keyword that has been supported for some time.
    Fixes Cython 0.24 compilation issue.
  - Turn _re2.pxd into includes.pxi.
  - remove some tests that are specific to internal Python modules _sre and sre
- Fix Match repr. [Andreas van Cranenburgh]
- Add tests for bug with \\b. [Andreas van Cranenburgh]
- Document support syntax &c. [Andreas van Cranenburgh]

  - add reference of supported syntax to main docstring
  - add __all__ attribute defining public members
  - add re's purge() function
  - add tests for count method
  - switch order of prepare_pattern() and _compile()
  - rename prepare_pattern() to _prepare_pattern() to signal that it is
    semi-private
- Add count method. [Andreas van Cranenburgh]

  - add count method, equivalent to len(findall(...))
  - use arrays in utf8indices
  - tweak docstrings
- Move functions around. [Andreas van Cranenburgh]
- Improve substitutions, Python 3 compatibility. [Andreas van
  Cranenburgh]

  - when running under Python 3+, reject unicode patterns on
    bytes data, and vice versa, in according with general Python 3 behavior.
  - improve Match.expand() implementation.
  - The substitutions by RE2 behave differently from Python (character escapes,
    named groups, etc.), so use Match.expand() for anything but simple literal
    replacement strings.
  - make groupindex of pattern objects public.
  - add Pattern.fullmatch() method.
  - use #define PY2 from setup.py instead of #ifdef hack.
  - debug option for compilation.
  - use data() instead of c_str() on C++ strings, and always supply length,
    so that strings with null characters are supported.
  - bump minimum cython version due to use of bytearray typing
  - adapt tests to Python 3; add b and u string prefixes where needed, &c.
  - update README
- Add flags parameter to toplevel functions. [Andreas van Cranenburgh]
- Update performance table / missing features. [Andreas van Cranenburgh]
- Workaround for sub(...) with count > 1. [Andreas van Cranenburgh]
- Handle named groups in replacement string; &c. [Andreas van
  Cranenburgh]

  - handle named groups in replacement string
  - store index of named groups in Pattern object instead of Match object.
  - use bytearray for result in _subn_callback
- Pickle Patterns; non-char buffers; &c. [Andreas van Cranenburgh]

  - support pickling of Pattern objects
  - support buffers from objects that do not support char buffer (e.g.,
    integer arrays); does not make a lot of sense, but this is what re does.
  - enable benchmarks shown in readme by default; fix typo.
  - fix typo in test_re.py
- New buffer API; precompute groups/spans; &c. [Andreas van Cranenburgh]

  - use new buffer API
    NB: even though the old buffer interface is deprecated from Python 2.6,
    the new buffer interface is only supported on mmap starting from
    Python 3.
  - avoid creating Match objects in findall()
  - precompute groups and spans of Match objects, so that possibly encoded
    version of search string (bytestr / cstring) does not need to be kept.
  - in _make_spans(), keep state for converting utf8 to unicode indices;
    so that there is no quadratic behavior on repeated invocations for
    different Match objects.
  - release GIL in pattern_Replace / pattern_GlobalReplace
  - prepare_pattern: loop over pattern as char *
  - advertise Python 3 support in setup.py, remove python 2.5
- Properly translate pos, endpos indices with unicode, &c. [Andreas van
  Cranenburgh]

  - properly translate pos, endpos indices with unicode
  - keep original unicode string in Match objects
  - separate compile.pxi file
- Re-organize code. [Andreas van Cranenburgh]
- Minor changes. [Andreas van Cranenburgh]
- Python 2/3 compatibility, support buffer objects, &c. [Andreas van
  Cranenburgh]

  - Python 2/3 compatibility
  - support searching in buffer objects (e.g., mmap)
  - add module docstring
  - some refactoring
  - remove outdated Cython-generated file
  - modify setup.py to cythonize as needed.
- Implement finditer as generator. [Andreas van Cranenburgh]
- Merge pull request #31 from sunu/master. [Michael Axiak]

  Add Python 3 support.
- Add Python 3 support. [Tarashish Mishra]
- Version bump. [Michael Axiak]


