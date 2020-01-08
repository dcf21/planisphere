# settings.py
# -*- coding: utf-8 -*-
#
# The python script in this file makes the various parts of a model planisphere.
#
# Copyright (C) 2014-2020 Dominic Ford <dcf21-www@dcford.org.uk>
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

# Units
dots_per_inch = 200

unit_m = 1.
unit_cm = 1. / 100
unit_mm = 1. / 1000

# Angle conversion
unit_deg = float(pi / 180)
unit_rev = 2 * pi

# Margins around output
margin_fraction = 1.02

# Font size
font_size_base = 2.6 * unit_mm
line_width_base = 0.2 * unit_mm

# Outer radius of planisphere
r_1 = 8.0 * unit_cm

# Outer rim width with dates marked
r_gap = 1.1 * unit_cm

# Gap between edge of disk and fold in paper
fold_gap = 0.2 * unit_cm

# Radius of hole in middle of planisphere
central_hole_size = 0.1 * unit_cm

# Inclination of the ecliptic
inclination_ecliptic = 23.5

r_2 = r_1 - r_gap


def radius(dec, latitude):
    dec_span = (90 + (90 - latitude)) * 1.125
    if latitude >= 0:
        return (90 - dec) / dec_span * r_2
    else:
        return (90 + dec) / dec_span * r_2


def transform(alt, az, latitude):
    alt *= unit_deg
    az *= unit_deg
    l = (90 - latitude) * unit_deg
    x = cos(alt) * sin(az)
    y = cos(alt) * cos(az)
    z = sin(alt)
    x2 = x * cos(l) - z * sin(l)
    y2 = y
    z2 = x * sin(l) + z * cos(l)
    ra = atan2(x2, y2)
    dec = asin(z2)

    # Put south pole at the centre of southern planispheres
    if latitude < 0:
        dec = -dec
    return [ra, dec]


def pos(r, t):
    return {'x': r * cos(t), 'y': -r * sin(-t)}
