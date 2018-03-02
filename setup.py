#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="capybara",
    version="0.1",
    packages=find_packages(),
    py_modules=['app', 'app.api', 'app.config', 'app.device', 'app.sensor_cable'],

    #Include .yaml file in app dir
    package_data={
        'app': ['*.yaml','handle_error.py']
    },

    #Information
    author="Jonathan srary",
    author_email="jonathan.sarry@edu.turkuamk.fi",

    description="Building Energy IoT Client",
    long_description=open('README.md').read(),
    url="https://github.com/dopyoman/capybara",
)

