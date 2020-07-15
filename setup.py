# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in service_agent/__init__.py
from service_agent import __version__ as version

setup(
	name='service_agent',
	version=version,
	description='Service Agent for Travel and Student Register ',
	author='Omar',
	author_email='qeqwe@asda.asd',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
