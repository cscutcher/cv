# -*- coding: utf-8 -*-
"""Setupfile for building nx6_cv"""
from setuptools import setup, find_packages
setup(
    name="nx6_cv",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'argh',
        'sh',
        'mako',
        'dateparser',
    ],
    entry_points={
        'console_scripts': [
            'nx6-cv = nx6_cv.cli:APP',
        ]
    },
    package_data={
        'nx6_cv': [
            'resume_schema.json',
            'resume.json',
            'latex/*',
        ],
    }
)
