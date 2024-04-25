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
The file contains global settings for the planisphere.
"""

from math import pi, sin, cos, atan2, asin
from typing import Dict, Tuple

# Units
dots_per_inch: float = 200

unit_m: float = 1.
unit_cm: float = 1. / 100
unit_mm: float = 1. / 1000

# Angle conversion
unit_deg: float = float(pi / 180)
unit_rev: float = 2 * pi

# Margins around output
margin_fraction: float = 1.02

# Font size
font_size_base: float = 2.6 * unit_mm
line_width_base: float = 0.2 * unit_mm

# Outer radius of planisphere
r_1: float = 8.0 * unit_cm

# Outer rim width with dates marked
r_gap: float = 1.1 * unit_cm

# Gap between edge of disk and fold in paper
fold_gap: float = 0.2 * unit_cm

# Radius of hole in middle of planisphere
central_hole_size: float = 0.1 * unit_cm

# Inclination of the ecliptic
inclination_ecliptic: float = 23.5

r_2: float = r_1 - r_gap


def radius(dec: float, latitude: float) -> float:
    dec_span: float = (90 + (90 - latitude)) * 1.125
    if latitude >= 0:
        return (90 - dec) / dec_span * r_2
    else:
        return (90 + dec) / dec_span * r_2


def transform(alt: float, az: float, latitude: float) -> Tuple[float, float]:
    alt *= unit_deg
    az *= unit_deg
    l: float = (90 - latitude) * unit_deg
    x: float = cos(alt) * sin(az)
    y: float = cos(alt) * cos(az)
    z: float = sin(alt)
    x2: float = x * cos(l) - z * sin(l)
    y2: float = y
    z2: float = x * sin(l) + z * cos(l)
    ra: float = atan2(x2, y2)
    dec: float = asin(z2)

    # Put south pole at the centre of southern planispheres
    if latitude < 0:
        dec = -dec
    return ra, dec


def pos(r: float, t: float) -> Dict[str, float]:
    return {'x': r * cos(t), 'y': -r * sin(-t)}
