#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Dan Flettre
# Copyright (c) 2015 Dan Flettre
#
# License: MIT
#

"""This module exports the SemifourStandard plugin class."""

from SublimeLinter.lint import NodeLinter


class SemifourStandard(NodeLinter):

    """Provides an interface to semifour-standard."""

    syntax = ('javascript', 'html', 'javascriptnext', 'javascript 6to5', 'javascript (babel)')
    cmd = 'semifour-standard --stdin --verbose'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 4.0.3'
    regex = r'^\s.+:(?P<line>\d+):(?P<col>\d+):(?P<message>.+)'
    selectors = {
        'html': 'source.js.embedded.html'
    }
