#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tracker',
      version='0.1.0',
      description='Track all the monies',
      author='Lindy Helfman',
      author_email='ljh@torsion.org',
      #packages=find_packages(),
      packages=['tracker'],
      entry_points={
        'console_scripts':[
          'tracker = tracker.__main__:main'
        ]
     },
     )
