# theme.py
# -*- coding: utf-8 -*-
#
# The python script in this file defines the available themes for the planisphere.
#
# Copyright (C) 2019 André Werlang <dcf21-www@dcford.org.uk>
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

themes = {
    "default":
        {
            "background": (1, 1, 1, 0),
            "date": (0, 0, 0, 1),
            "edge": (0, 0, 0, 1),
            "shading": (0.9, 0.9, 0.9, 1),
            "grid": (0.75, 0.75, 0.75, 1),
            "stick": (0.25, 0.25, 0.25, 1),
            "star": (0, 0, 0, 1),
            "constellation": (0, 0, 0, 1)
        },
    "dark":
        {
            "background": (0.2, 0.25, 0.45, 1),
            "date": (1, 1, 1, 1),
            "edge": (0.45, 0.45, 0.45, 1),
            "shading": (0.1, 0.1, 0.1, 1),
            "grid": (0.3, 0.3, 0.3, 1),
            "stick": (0.28, 0.35, 0.55, 1),
            "star": (1, 1, 1, 1),
            "constellation": (0.6, 0.5, 0.65, 1)
        }
}
