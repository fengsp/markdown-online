"""
    mdonline.app
    ~~~~~~~~~~~~

    One simple WSGI app.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""
import os
from flask import Flask
app = Flask(__name__)
from mdonline import settings
app.config.from_object(settings)
app.markdown_path = os.path.join(app.root_path, 'markdowns')

import mdonline.views
