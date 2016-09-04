# -*- coding: utf-8 -*-
"""CLI for building CV."""
from pathlib import Path
import re
import logging
import os.path
import tempfile

import argh
import mako.template
import pkg_resources
import sh

import nx6_cv.resume

DEV_LOGGER = logging.getLogger(__name__)


APP = argh.EntryPoint()


@APP
def build_latex_pdf(output_filename="cscutcher_cv_latex.pdf"):
    """Build latex style pdf."""
    resume = nx6_cv.resume.get_resume()

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


def build_resume(output_filename, theme, format):
    """Helper to build resume with 'resume' tool"""
    resume_path = Path(
        pkg_resources.resource_filename(__name__, "resume.json")).parent

    orig_path = os.getcwd()
    os.chdir(str(resume_path))

    print(sh.resume.export(
        output_filename,
        format=format,
        theme=theme,
    ))

    os.chdir(orig_path)

    (resume_path / output_filename).rename(Path.cwd() / output_filename)

@APP
def build_html(output_filename="cscutcher_cv.html", theme="kendall"):
    """Build html style pdf."""
    build_resume(output_filename=output_filename, theme=theme, format='html')


@APP
def build_pdf(output_filename="cscutcher_cv.pdf", theme="modern"):
    """Build html style pdf."""
    build_resume(output_filename=output_filename, theme=theme, format='pdf')


@APP
def build(output_filename_prefix="cscutcher_"):
    """Build all CV styles."""
    build_latex_pdf(output_filename=output_filename_prefix + "cv_latex.pdf")
    build_html(output_filename=output_filename_prefix + "cv.html")
    build_pdf(output_filename=output_filename_prefix + "cv.pdf")
