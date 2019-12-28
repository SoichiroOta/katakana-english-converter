#!/usr/bin/env python

"""Tests for `katakana_english_converter` package."""


import unittest
from click.testing import CliRunner

from katakana_english_converter import katakana_english_converter
from katakana_english_converter import cli


class TestKatakana_english_converter(unittest.TestCase):
    """Tests for `katakana_english_converter` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'katakana_english_converter.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
