#!/usr/bin/python3
# starwheel.py
# -*- coding: utf-8 -*-
#
# The python script in this file makes the various parts of a model planisphere.
#
# Copyright (C) 2014-2022 Dominic Ford <dcf21-www@dcford.org.uk>
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

import re
from math import pi, sin, cos, atan2, hypot

from numpy import arange

import calendar
from bright_stars_process import fetch_bright_star_list
from constants import unit_deg, unit_rev, unit_mm, unit_cm, r_1, r_gap, central_hole_size, radius
from graphics_context import BaseComponent
from settings import fetch_command_line_arguments
from text import text
from themes import themes


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
        theme = themes[settings['theme']]

        context.set_font_size(1.2)

        # Radius of outer edge of star chart
        r_2 = r_1 - r_gap

        # Radius of day-of-month ticks from centre of star chart
        r_3 = r_1 * 0.1 + r_2 * 0.9

        # Radius of every fifth day-of-month tick from centre of star chart
        r_4 = r_1 * 0.2 + r_2 * 0.8

        # Radius of lines between months on date scale
        r_5 = r_1

        # Radius for writing numeric labels for days of the month
        r_6 = r_1 * 0.4 + r_2 * 0.6

        # Shade background to month scale
        shading_inner_radius = r_1 * 0.55 + r_2 * 0.45
        context.begin_path()
        context.circle(centre_x=0, centre_y=0, radius=r_1)
        context.circle(centre_x=0, centre_y=0, radius=shading_inner_radius)
        context.fill(color=theme['shading'])

        # Draw the outer edge of planisphere
        context.begin_path()
        context.circle(centre_x=0, centre_y=0, radius=r_1)
        context.fill(color=theme['background'])

        # Draw the central hole in the middle of the planisphere
        context.begin_sub_path()
        context.circle(centre_x=0, centre_y=0, radius=central_hole_size)
        context.stroke(color=theme['edge'])

        # Combine these two paths to make a clipping path for drawing the star wheel
        context.clip()

        # Draw lines of constant declination at 15 degree intervals.
        for dec in arange(-80, 85, 15):
            # Convert declination into radius from the centre of the planisphere
            r = radius(dec=dec, latitude=latitude)
            if r > r_2:
                continue
            context.begin_path()
            context.circle(centre_x=0, centre_y=0, radius=r)
            context.stroke(color=theme['grid'])

        # Draw constellation stick figures
        for line in open("raw_data/constellation_stick_figures.dat", "rt"):
            line = line.strip()

            # Ignore blank lines and comment lines
            if (len(line) == 0) or (line[0] == '#'):
                continue

            # Split line into words.
            # These are the names of the constellations, and the start and end points for each stroke.
            [name, ra1, dec1, ra2, dec2] = line.split()

            # If we're making a southern hemisphere planisphere, we flip the sky upside down
            if is_southern:
                ra1 = -float(ra1)
                ra2 = -float(ra2)
                dec1 = -float(dec1)
                dec2 = -float(dec2)

            # Project RA and Dec into radius and azimuth in the planispheric projection
            r_point_1 = radius(dec=float(dec1), latitude=latitude)
            if r_point_1 > r_2:
                continue

            r_point_2 = radius(dec=float(dec2), latitude=latitude)
            if r_point_2 > r_2:
                continue

            p1 = (-r_point_1 * cos(float(ra1) * unit_deg), -r_point_1 * sin(float(ra1) * unit_deg))
            p2 = (-r_point_2 * cos(float(ra2) * unit_deg), -r_point_2 * sin(float(ra2) * unit_deg))

            # Impose a maximum length of 4 cm on constellation stick figures; they get quite distorted at the edge
            if hypot(p2[0] - p1[0], p2[1] - p1[1]) > 4 * unit_cm:
                continue

            # Stroke a line
            context.begin_path()
            context.move_to(x=p1[0], y=p1[1])
            context.line_to(x=p2[0], y=p2[1])
            context.stroke(color=theme['stick'], line_width=1, dotted=True)

        # Draw stars from Yale Bright Star Catalogue
        for star_descriptor in fetch_bright_star_list()['stars'].values():
            [ra, dec, mag] = star_descriptor[:3]

            # Discard stars fainter than mag 4
            if mag == "-" or float(mag) > 4.0:
                continue

            ra = float(ra)
            dec = float(dec)

            # If we're making a southern hemisphere planisphere, we flip the sky upside down
            if is_southern:
                ra *= -1
                dec *= -1

            r = radius(dec=dec, latitude=latitude)
            if r > r_2:
                continue

            # Represent each star with a small circle
            context.begin_path()
            context.circle(centre_x=-r * cos(ra * unit_deg), centre_y=-r * sin(ra * unit_deg),
                           radius=0.18 * unit_mm * (5 - mag))
            context.fill(color=theme['star'])

        # Write constellation names
        context.set_font_size(0.7)
        context.set_color(theme['constellation'])

        # Open a list of the coordinates where we place the names of the constellations
        for line in open("raw_data/constellation_names.dat"):
            line = line.strip()

            # Ignore blank lines and comment lines
            if (len(line) == 0) or (line[0] == '#'):
                continue

            # Split line into words
            [name, ra, dec] = line.split()[:3]

            # Translate constellation name into the requested language, if required
            if name in text[language]['constellation_translations']:
                name = text[language]['constellation_translations'][name]

            ra = float(ra) * 360. / 24
            dec = float(dec)

            # If we're making a southern hemisphere planisphere, we flip the sky upside down
            if is_southern:
                ra = -ra
                dec = -dec

            # Render name of constellation, with _s turned into spaces
            name2 = re.sub("_", " ", name)
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
            Convert Julian Day into a rotation angle of the sky about the north celestial pole at midnight,
            relative to spring equinox.

            :param d:
                Julian day
            :return:
                Rotation angle, radians
            """
            return (d - calendar.julian_day(year=2014, month=3, day=20, hour=16, minute=55, sec=0)) / 365.25 * unit_rev

        # Write month names around the date scale
        context.set_font_size(2.3)
        context.set_color(theme['date'])
        for mn, (mlen, name) in enumerate(text[language]['months']):
            theta = s * theta2014(calendar.julian_day(year=2014, month=mn + 1, day=mlen // 2, hour=12, minute=0, sec=0))

            # We supply circular_text with a negative radius here, as a fudge to orientate the text with bottom-inwards
            context.circular_text(text=name, centre_x=0, centre_y=0, radius=-(r_1 * 0.65 + r_2 * 0.35),
                                  azimuth=theta / unit_deg + 180,
                                  spacing=1, size=1)

        # Draw ticks for the days of the month
        for mn, (mlen, name) in enumerate(text[language]['months']):
            # Tick marks for each day
            for d in range(1, mlen + 1):
                theta = s * theta2014(calendar.julian_day(year=2014, month=mn + 1, day=d, hour=0, minute=0, sec=0))

                # Days of the month which are multiples of 5 get longer ticks
                R = r_3 if (d % 5) else r_4

                # The last day of each month is drawn as a dividing line between months
                if d == mlen:
                    R = r_5

                # Draw line
                context.begin_path()
                context.move_to(x=r_2 * cos(theta), y=-r_2 * sin(theta))
                context.line_to(x=R * cos(theta), y=-R * sin(theta))
                context.stroke(line_width=1, dotted=False)

            # Write numeric labels for the 10th, 20th and last day of each month
            for d in [10, 20, mlen]:
                theta = s * theta2014(calendar.julian_day(year=2014, month=mn + 1, day=d, hour=0, minute=0, sec=0))
                context.set_font_size(1.2)

                # First digit
                theta2 = theta + 0.15 * unit_deg
                context.text(text="%d" % (d / 10), x=r_6 * cos(theta2), y=-r_6 * sin(theta2),
                             h_align=1, v_align=0,
                             gap=0,
                             rotation=-theta + pi / 2)

                # Second digit
                theta2 = theta - 0.15 * unit_deg
                context.text(text="%d" % (d % 10), x=r_6 * cos(theta2), y=-r_6 * sin(theta2),
                             h_align=-1, v_align=0,
                             gap=0,
                             rotation=-theta + pi / 2)

        # Draw the dividing line between the date scale and the star chart
        context.begin_path()
        context.circle(centre_x=0, centre_y=0, radius=r_2)
        context.stroke(color=theme['date'], line_width=1, dotted=False)


# Do it right away if we're run as a script
if __name__ == "__main__":
    # Fetch command line arguments passed to us
    arguments = fetch_command_line_arguments(default_filename=StarWheel().default_filename())

    # Render the star wheel for the planisphere
    StarWheel(settings={
        'latitude': arguments['latitude'],
        'language': 'en',
        'theme': arguments['theme'],
    }).render_to_file(
        filename=arguments['filename'],
        img_format=arguments['img_format'],

    )
