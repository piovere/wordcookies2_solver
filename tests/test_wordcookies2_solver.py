#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_wordcookies2_solver
----------------------------------

Tests for `wordcookies2_solver` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from wordcookies2_solver import wordcookies2_solver
from wordcookies2_solver import cli


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'wordcookies2_solver.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_easy_words():
    l = wordcookies2_solver.wordlist('abc')
    c = ['cab', 'bac']
    assert set(l) == set(c)
