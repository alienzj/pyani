# -*- coding: utf-8 -*-
"""anim_parser.py

Provides parser for anim subcommand

(c) The James Hutton Institute 2016-2019
Author: Leighton Pritchard

Contact:
leighton.pritchard@hutton.ac.uk

Leighton Pritchard,
Information and Computing Sciences,
James Hutton Institute,
Errol Road,
Invergowrie,
Dundee,
DD2 5DA,
Scotland,
UK

The MIT License

Copyright (c) 2016-2019 The James Hutton Institute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from argparse import ArgumentDefaultsHelpFormatter

from pyani import pyani_config
from pyani.scripts import subcommands


def build(subps, parents=None):
    """Return a command-line parser for the anim subcommand."""
    parser = subps.add_parser(
        "anim", parents=parents, formatter_class=ArgumentDefaultsHelpFormatter
    )
    # Required positional arguments: input and output directories
    parser.add_argument(
        action="store", dest="indir", default=None, help="input genome directory"
    )
    parser.add_argument(
        action="store",
        dest="outdir",
        default=None,
        help="output analysis results directory",
    )
    # Optional arguments
    parser.add_argument(
        "--dbpath",
        action="store",
        dest="dbpath",
        default=".pyani/pyanidb",
        help="path to pyani database",
    )
    parser.add_argument(
        "--nucmer_exe",
        dest="nucmer_exe",
        action="store",
        default=pyani_config.NUCMER_DEFAULT,
        help="path to NUCmer executable",
    )
    parser.add_argument(
        "--filter_exe",
        dest="filter_exe",
        action="store",
        default=pyani_config.FILTER_DEFAULT,
        help="path to delta-filter executable",
    )
    parser.add_argument(
        "--maxmatch",
        dest="maxmatch",
        action="store_true",
        default=False,
        help="override MUMmer to allow all NUCmer matches",
    )
    parser.add_argument(
        "--nofilter",
        dest="nofilter",
        action="store_true",
        default=False,
        help="do not use delta-filter for 1:1 NUCmer matches",
    )
    parser.set_defaults(func=subcommands.subcmd_anim)