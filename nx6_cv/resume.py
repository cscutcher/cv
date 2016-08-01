# -*- coding: utf-8 -*-
"""Parsing code for resume."""
import logging
import json
import pkg_resources
import dateparser

DEV_LOGGER = logging.getLogger(__name__)


class AttrDict(dict):
    """Wraps dict but allows lookup by attribute."""
    def __getattr__(self, name):
        return self[name]


class Resume(AttrDict):
    """Wrap resume data."""
    def get_keywords_iter(self):
        for skill in self.skills:
            yield from skill.keywords


def _format_pair(key, value):
    if "Date" in key:
        value = dateparser.parse(value)

    return key, value


def _resume_decode_pairs_hook(pairs):
    pairs = [_format_pair(key, value) for key, value in pairs]
    return AttrDict(pairs)




def get_resume():
    """Get resume data from json."""
    return Resume(json.loads(
        pkg_resources.resource_string(__name__, "resume.json").decode("UTF8"),
        object_pairs_hook=_resume_decode_pairs_hook,
    ))
