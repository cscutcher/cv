# -*- coding: utf-8 -*-
"""CLI for building CV."""
from pathlib import Path
import re
import json
import logging
import os.path
import tempfile

import argh
import mako.template
import pkg_resources
import sh

DEV_LOGGER = logging.getLogger(__name__)


def get_resume():
    """Get resume data from json."""
    return json.loads(
        pkg_resources.resource_string(__name__, "resume.json").decode("UTF8"))


APP = argh.EntryPoint()


@APP
def build_latex_pdf(output_filename):
    """Build latex style pdf."""
    resume = get_resume()
    output_stream = Path(output_filename).open('wb')

    with tempfile.TemporaryDirectory(prefix="nx6_cv_latex_") as tmpdir:
        tmpdir = Path(tmpdir)

        # Copy latex sources
        for path in pkg_resources.resource_listdir(__name__, "latex"):
            (tmpdir / path).open('wb').write(
                pkg_resources.resource_string(
                    __name__, os.path.join("latex", path)))

        template_raw = (tmpdir / 'cv.tex.mako').open().read()

        # Stop mako nuking '//' in tex
        template_raw = re.sub(
            r"\\$",
            r"\\\\" + "\n",
            template_raw,
            flags=re.MULTILINE)

        # Render and write template
        template = mako.template.Template(template_raw)
        tex = template.render_unicode(cv=resume)
        (tmpdir / 'cv.tex').open('w').write(tex)

        # Add gitrevision tex
        (tmpdir / 'gitrevision.tex').open('w').write("NOTSET")

        sh.make("-C", str(tmpdir.resolve()))
        output_stream.write((tmpdir / 'cv.pdf').open('rb').read())
