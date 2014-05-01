from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='django-csv',
      version=version,
      description="Some CSV Utilities for your django projects",
      long_description="""\
Some CSV Utilities for your django projects""",
      classifiers=['Development Status :: 5 - Production/Stable'], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='csv django',
      author='Bobby Steinbach',
      author_email='steinbach.rj@gmail.com',
      url='https://github.com/steinbachr/django-csv',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
