# -*- coding: utf-8 -*-
"""
    mdonline.settings
    ~~~~~~~~~~~~~~~~~

    App config.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""

import os


DEBUG = False
# Detect environment by whether debug named file exists or not
if os.path.exists(os.path.join(os.path.dirname(__file__), 'debug')):
    DEBUG = True

