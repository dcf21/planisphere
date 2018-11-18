#!/usr/bin/python3
# starwheel.py
# -*- coding: utf-8 -*-
#
# The python script in this file makes the various parts of a model planisphere.
#
# Copyright (C) 2014-2018 Dominic Ford <dcf21-www@dcford.org.uk>
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
Render the star wheel for the planisphere.
"""

from math import pi, sin, cos, atan2, hypot
import re
import calendar

from bright_stars_process import fetch_bright_star_list
from constants import unit_deg, unit_rev, unit_mm, unit_cm, r_1, r_gap, central_hole_size, radius
from graphics_context import BaseComponent
from numpy import arange
from settings import fetch_command_line_arguments
from text import text


class StarWheel(BaseComponent):
    """
    Render the star wheel for the planisphere.
    """

    def default_filename(self):
        """
        Return the default filename to use when saving this component.
        """
        return "star_wheel"

    def bounding_box(self, settings):
        """
        Return the bounding box of the canvas area used by this component.

        :param settings:
            A dictionary of settings required by the renderer.
        :return:
         Dictionary with the elements 'x_min', 'x_max', 'y_min' and 'y_max' set
        """
        return {
            'x_min': -r_1 - 4 * unit_mm,
            'x_max': r_1 + 4 * unit_mm,
            'y_min': -r_1 - 4 * unit_mm,
            'y_max': r_1 + 4 * unit_mm
        }

    def do_rendering(self, settings, context):
        """
        This method is required to actually render this item.

        :param settings:
            A dictionary of settings required by the renderer.
        :param context:
            A GraphicsContext object to use for drawing
        :return:
            None
        """

        is_southern = settings['latitude'] < 0
        language = settings['language']
        latitude = abs(settings['latitude'])

        context.set_font_size(1.2)

        r_2 = r_1 - r_gap
        r_3 = r_1 * 0.1 + r_2 * 0.9
        r_4 = r_1 * 0.2 + r_2 * 0.8
        r_5 = r_1
        r_6 = r_1 * 0.4 + r_2 * 0.6

        context.begin_path()
        context.circle(centre_x=0, centre_y=0, radius=r_1)  # Outer edge of planisphere
        context.begin_sub_path()
        context.circle(centre_x=0, centre_y=0, radius=central_hole_size)  # White out central hole
        context.stroke()
        context.clip()

        for dec in arange(-80, 85, 15):
            r = radius(dec=dec, latitude=latitude)
            if r > r_2:
                continue
            context.begin_path()
            context.circle(centre_x=0, centre_y=0, radius=r)
            context.stroke(color=(0.75, 0.75, 0.75, 1))

        # Draw constellation stick figures
        for line in open("raw_data/constellation_stick_figures.dat", "rt"):
            line = line.strip()

            # Ignore blank lines and comment lines
            if (len(line) == 0) or (line[0] == '#'):
                continue

            # Split line into words
            [name, ra1, dec1, ra2, dec2] = line.split()

            if is_southern:
                ra1 = -float(ra1)
                ra2 = -float(ra2)
                dec1 = -float(dec1)
                dec2 = -float(dec2)

            r_point_1 = radius(dec=float(dec1), latitude=latitude)
            if r_point_1 > r_2:
                continue

            r_point_2 = radius(dec=float(dec2), latitude=latitude)
            if r_point_2 > r_2:
                continue

            p1 = (-r_point_1 * cos(float(ra1) * unit_deg), -r_point_1 * sin(float(ra1) * unit_deg))
            p2 = (-r_point_2 * cos(float(ra2) * unit_deg), -r_point_2 * sin(float(ra2) * unit_deg))

            # Impose a maximum length of 4 cm on constellation stick figures; they get quite distored at the edge
            if hypot(p2[0] - p1[0], p2[1] - p1[1]) > 4 * unit_cm:
                continue

            context.begin_path()
            context.move_to(x=p1[0], y=p1[1])
            context.line_to(x=p2[0], y=p2[1])
            context.stroke(color=(0.25, 0.25, 0.25, 1), line_width=1, dotted=True)

        # Draw stars from Yale Bright Star Catalogue
        for star_descriptor in fetch_bright_star_list()['stars'].values():
            [ra, dec, mag] = star_descriptor[:3]

            # Discard stars fainter than mag 4
            if mag == "-" or float(mag) > 4.0:
                continue

            ra = float(ra)
            dec = float(dec)
            if is_southern:
                ra *= -1
                dec *= -1

            r = radius(dec=dec, latitude=latitude)
            if r > r_2:
                continue
            context.begin_path()
            context.circle(centre_x=-r * cos(ra * unit_deg), centre_y=-r * sin(ra * unit_deg),
                           radius=0.18 * unit_mm * (5 - mag))
            context.fill(color=(0, 0, 0, 1))

        # Write constellation names
        context.set_font_size(0.7)
        context.set_color(r=0, g=0, b=0)

        for line in open("raw_data/constellation_names.dat"):
            line = line.strip()

            # Ignore blank lines and comment lines
            if (len(line) == 0) or (line[0] == '#'):
                continue

            # Split line into words
            [name, ra, dec] = line.split()[:3]

            # Translate constellation name, if required
            if name in text[language]['constellation_translations']:
                name = text[language]['constellation_translations'][name]

            ra = float(ra) * 360. / 24
            dec = float(dec)

            if is_southern:
                ra = -ra
                dec = -dec

            name2 = re.sub("@", " ", name)
            r = radius(dec=dec, latitude=latitude)
            if r > r_2:
                continue
            p = (-r * cos(ra * unit_deg), -r * sin(ra * unit_deg))
            a = atan2(p[0], p[1])
            context.text(text=name2, x=p[0], y=p[1], h_align=0, v_align=0, gap=0, rotation=unit_rev / 2 - a)

        # Calendar ring counts clockwise in northern hemisphere; anticlockwise in southern hemisphere
        s = -1 if not is_southern else 1

        def theta2014(d):
            """
            Convert Julian Day into a rotation angle of the sky about the NCP at midnight, relative to spring equinox.

            :param d:
                Julian day
            :return:
                Rotation angle, radians
            """
            return (d - calendar.julian_day(year=2014, month=3, day=20, hour=16, minute=55, sec=0)) / 365.25 * unit_rev

        # Write month names
        context.set_font_size(1.8)
        context.set_color(r=0, g=0, b=0)
        for mn, (mlen, name) in enumerate(text[language]['months']):
            theta = s * theta2014(calendar.julian_day(year=2014, month=mn+1, day=mlen // 2, hour=12, minute=0, sec=0))

            # We supply circular_text with a negative radius here, as a fudge to orientate the text with bottom-inwards
            context.circular_text(text=name, centre_x=0, centre_y=0, radius=-(r_1 * 0.65 + r_2 * 0.35),
                                  azimuth=theta / unit_deg + 180,
                                  spacing=1, size=1)

        # Write day ticks
        for mn, (mlen, name) in enumerate(text[language]['months']):
            # Tick marks
            for d in range(1, mlen + 1):
                theta = s * theta2014(calendar.julian_day(year=2014, month=mn+1, day=d, hour=0, minute=0, sec=0))
                R = r_3 if (d % 5) else r_4  # Multiples of 5 get longer ticks
                if d == mlen:
                    R = r_5
                context.begin_path()
                context.move_to(x=r_2 * cos(theta), y=-r_2 * sin(theta))
                context.line_to(x=R * cos(theta), y=-R * sin(theta))
                context.stroke(line_width=1, dotted=False)

            # Numeric labels
            for d in [10, 20, mlen]:
                theta = s * theta2014(calendar.julian_day(year=2014, month=mn+1, day=d, hour=0, minute=0, sec=0))
                context.set_font_size(1.0)
                theta2 = theta + 0.15 * unit_deg
                context.text(text="%d" % (d / 10), x=r_6 * cos(theta2), y=-r_6 * sin(theta2),
                             h_align=1, v_align=0,
                             gap=0,
                             rotation=-theta + pi/2)
                theta2 = theta - 0.15 * unit_deg
                context.text(text="%d" % (d % 10), x=r_6 * cos(theta2), y=-r_6 * sin(theta2),
                             h_align=-1, v_align=0,
                             gap=0,
                             rotation=-theta + pi/2)

        context.begin_path()
        context.circle(centre_x=0, centre_y=0, radius=r_2)
        context.stroke(color=(0, 0, 0, 1), line_width=1, dotted=False)


# Do it right away if we're run as a script
if __name__ == "__main__":
    # Fetch command line arguments passed to us
    arguments = fetch_command_line_arguments(default_filename=StarWheel().default_filename())

    # Render the star wheel for the planisphere
    StarWheel(settings={
        'latitude': arguments['latitude'],
        'language': 'en'
    }).render_to_file(
        filename=arguments['filename'],
        img_format=arguments['img_format'],

    )
