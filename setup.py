#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for kvk_url_finder.

    This file was generated with PyScaffold 3.0.3.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: http://pyscaffold.org/
"""

import sys
from setuptools import setup

# Add here console scripts and other entry points in ini-style format
entry_points = """
[console_scripts]
kvk_url_finder = kvk_url_finder.kvk_url_finder_main:_run
url_to_kvk = kvk_url_finder.url_to_kvk_main:_run
kvk_plotter = kvk_url_finder.kvk_plotter:_run
# For example:
# fibonacci = kvk_url_finder.skeleton:run
"""


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['pyscaffold>=3.0a0,<3.1a0'] + sphinx,
          entry_points=entry_points,
          use_pyscaffold=True)


if __name__ == "__main__":
    setup_package()
