"""
    mdonline.views
    ~~~~~~~~~~~~~~

    Register your actions.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""
import os

from flask import abort, render_template

from mdonline import app


@app.route('/')
def index():
    if os.path.exists(app.markdown_path):
        markdowns = os.listdir(app.markdown_path)
    else:
        markdowns = []

    return render_template('index.html', markdowns=markdowns)


@app.route('/<path:path>')
def detail(path):
    filename = os.path.basename(path)
    path = os.path.join(app.markdown_path, path)
    if not os.path.exists(path):
        abort(404)
    markdown = open(path, 'r').read()
    return render_template('detail.html', title=filename, markdown=markdown)
