# This is Python version 3.8.3

Copyright (c) 2001-2020 Python Software Foundation.  All rights reserved.

See the end of this file for further copyright and license information.

## General Information

- Website: https://www.python.org
- Source code: https://github.com/python/cpython
- Issue tracker: https://bugs.python.org
- Documentation: https://docs.python.org
- Developer's Guide: https://devguide.python.org/

## Contributing to CPython

For more complete instructions on contributing to CPython development,
see the `Developer Guide`_.

.. _Developer Guide: https://devguide.python.org/

## Using Python

Installable Python kits, and information about using Python, are available at
`python.org`_.

.. _python.org: https://www.python.org/

## Build Instructions

On Linux:

    meson builddir
    ninja -C builddir

## What's New

We have a comprehensive overview of the changes in the `What's New in Python
3.8 <https://docs.python.org/3.8/whatsnew/3.8.html>`_ document.  For a more
detailed change log, read `Misc/NEWS
<https://github.com/python/cpython/blob/3.8/Misc/NEWS.d>`_, but a full
accounting of changes can only be gleaned from the `commit history
<https://github.com/python/cpython/commits/3.8>`_.

If you want to install multiple versions of Python, see the section below
entitled "Installing multiple versions".

## Documentation

`Documentation for Python 3.8 <https://docs.python.org/3.8/>`_ is online,
updated daily.

It can also be downloaded in many formats for faster access.  The documentation
is downloadable in HTML, PDF, and reStructuredText formats; the latter version
is primarily for documentation authors, translators, and people with special
formatting requirements.

For information about building Python's documentation, refer to `Doc/README.rst
<https://github.com/python/cpython/blob/3.8/Doc/README.rst>`_.

## Converting From Python 2.x to 3.x

Significant backward incompatible changes were made for the release of Python
3.0, which may cause programs written for Python 2 to fail when run with Python
3.  For more information about porting your code from Python 2 to Python 3, see
the `Porting HOWTO <https://docs.python.org/3/howto/pyporting.html>`_.


## Testing

To test the interpreter, type ``make test`` in the top-level directory.  The
test set produces some output.  You can generally ignore the messages about
skipped tests due to optional features which can't be imported.  If a message
is printed about a failed test or a traceback or core dump is produced,
something is wrong.

By default, tests are prevented from overusing resources like disk space and
memory.  To enable these tests, run ``make testall``.

If any tests fail, you can re-run the failing test(s) in verbose mode.  For
example, if ``test_os`` and ``test_gdb`` failed, you can run::

    ninja -C builddir test

If the failure persists and appears to be a problem with Python rather than
your environment, you can `file a bug report <https://bugs.python.org>`_ and
include relevant output from that command to show the issue.

See `Running & Writing Tests <https://devguide.python.org/runtests/>`_
for more on running tests.

## Installing multiple versions

On Unix and Mac systems if you intend to install multiple versions of Python
using the same installation prefix (``--prefix`` argument to the configure
script) you must take care that your primary python executable is not
overwritten by the installation of a different version.  All files and
directories installed using ``make altinstall`` contain the major and minor
version and can thus live side-by-side.  ``make install`` also creates
``${prefix}/bin/python3`` which refers to ``${prefix}/bin/pythonX.Y``.  If you
intend to install multiple versions using the same prefix you must decide which
version (if any) is your "primary" version.  Install that version using ``make
install``.  Install all other versions using ``make altinstall``.

For example, if you want to install Python 2.7, 3.6, and 3.8 with 3.8 being the
primary version, you would execute ``make install`` in your 3.8 build directory
and ``make altinstall`` in the others.

## Issue Tracker and Mailing List

Bug reports are welcome!  You can use the `issue tracker
<https://bugs.python.org>`_ to report bugs, and/or submit pull requests `on
GitHub <https://github.com/python/cpython>`_.

You can also follow development discussion on the `python-dev mailing list
<https://mail.python.org/mailman/listinfo/python-dev/>`_.

## Proposals for enhancement

If you have a proposal to change Python, you may want to send an email to the
comp.lang.python or `python-ideas`_ mailing lists for initial feedback.  A
Python Enhancement Proposal (PEP) may be submitted if your idea gains ground.
All current PEPs, as well as guidelines for submitting a new PEP, are listed at
`python.org/dev/peps/ <https://www.python.org/dev/peps/>`_.

.. _python-ideas: https://mail.python.org/mailman/listinfo/python-ideas/


## Copyright and License Information

Copyright (c) 2001-2020 Python Software Foundation.  All rights reserved.

Copyright (c) 2000 BeOpen.com.  All rights reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.  All
rights reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum.  All rights reserved.

See the file "LICENSE" for information on the history of this software, terms &
conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.

This Python distribution contains *no* GNU General Public License (GPL) code,
so it may be used in proprietary projects.  There are interfaces to some GNU
code but these are entirely optional.

All trademarks referenced herein are property of their respective holders.
