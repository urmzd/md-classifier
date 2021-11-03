#!/usr/bin/env python

from distutils.core import setup

setup(
    name="md-nlp",
    version="1.0",
    author="Urmzd Mukhammadnaim & Ben MacDonald",
    author_email="urmzd@dal.ca, ben.macdonald@dal.ca",
    package_dir={"": "src"},
    data_files=[("resources/*", ["*.csv"])],
    include_package_data=True,
    module_dir=["scraper"],
)
