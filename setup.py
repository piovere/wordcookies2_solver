#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'nltk'
]

test_requirements = [
    'pytest'
]

setup(
    name='wordcookies2_solver',
    version='0.1.0',
    description="Quick solver for WordCookies2 game using NLTK",
    long_description=readme + '\n\n' + history,
    author="J.R. Powers-Luhn",
    author_email='jpowersl@vols.utk.edu',
    url='https://github.com/piovere/wordcookies2_solver',
    packages=[
        'wordcookies2_solver',
    ],
    package_dir={'wordcookies2_solver':
                 'wordcookies2_solver'},
    entry_points={
        'console_scripts': [
            'wordcookies2_solver=wordcookies2_solver.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='wordcookies2_solver',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
