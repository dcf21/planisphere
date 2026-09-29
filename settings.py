# settings.py
# -*- coding: utf-8 -*-
#
# The python script in this file makes the various parts of a model planisphere.
#
# Copyright (C) 2014-2024 Dominic Ford <https://dcford.org.uk/>
#
# This code is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# You should have received a copy of the GNU General Public License along with
# this file; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA  02110-1301, USA

# ----------------------------------------------------------------------------

"""
Define a common command-line interface which is shared between all the scripts.
"""

import argparse

from typing import Dict, Union


def fetch_command_line_arguments(default_filename: str = '') -> Dict[str, Union[int, str]]:
    """
    Read input parameters from the command line

    :return:
        Dictionary of command-line arguments
    """

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--latitude', dest='latitude', type=int, default=52,
                        help="The latitude to create a planisphere for.")
    parser.add_argument('--format', dest='img_format', choices=["pdf", "png", "svg"], default="png",
                        help="The image format to create.")
    parser.add_argument('--output', dest='filename', default=default_filename,
                        help="Filename for output, without a file type suffix.")
    parser.add_argument('--theme', dest='theme', choices=["default", "dark"], default="default",
                        help="Color theme to be used in the planisphere.")
    parser.add_argument('--time-format', dest='time_format', choices=["auto", "12h", "24h"], default="auto",
                        help="Clock format on the planisphere holder: 12-hour (AM/PM) or 24-hour. "
                             "'auto' picks a format based on the language.")
    parser.add_argument('--dst', dest='dst', action='store_true',
                        help="Additionally print daylight saving time (+1 hour) in brackets after each hour.")
    args = parser.parse_args()

    return {
        "latitude": args.latitude,
        "img_format": args.img_format,
        "filename": args.filename,
        "theme": args.theme,
        "time_format": args.time_format,
        "dst": args.dst
    }
