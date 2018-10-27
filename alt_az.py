#!/usr/bin/python3
# alt_az.py
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
Render the optional alt-az grid of the planisphere.
"""

from math import atan2

from constants import unit_deg, unit_rev, unit_cm, unit_mm, central_hole_size
from constants import radius, transform, pos
from graphics_context import BaseComponent
from numpy import arange
from settings import fetch_command_line_arguments
from text import text


class AltAzGrid(BaseComponent):
    """
    Render the optional alt-az grid of the planisphere.
    """

    def default_filename(self):
        """
        Return the default filename to use when saving this component.
        """
        return "alt_az_grid"

    def bounding_box(self):
        """
        Return the bounding box of the canvas area used by this component.

        :return:
         Dictionary with the elements 'x_min', 'x_max', 'y_min' and 'y_max' set
        """
        return {
            'x_min': -50 * unit_cm,
            'x_max': 50 * unit_cm,
            'y_min': -50 * unit_cm,
            'y_max': 50 * unit_cm
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

        latitude = abs(settings['latitude'])
        language = settings['language']

        context.set_font_size(0.9)

        # Draw horizon, and line to cut around edge
        for alt in (-10, 0):
            p = []
            for az in arange(0, 360.5, 1):
                p.append(transform(alt=alt, az=az, latitude=latitude))
            for i in range(1, len(p)):
                r_a = radius(dec=p[i - 1][1] / unit_deg, latitude=latitude)
                r_b = radius(dec=p[i][1] / unit_deg, latitude=latitude)
                context.move_to(**pos(r_a, p[i - 1][0]))
                context.line_to(**pos(r_b, p[i][0]))

        # Draw lines of constant altitude
        for alt in range(10, 85, 10):
            p = []
            for az in arange(0, 360.5, 1):
                p.append(transform(alt=alt, az=az, latitude=latitude))
            for i in range(1, len(p)):
                r_a = radius(dec=p[i - 1][1] / unit_deg, latitude=latitude)
                r_b = radius(dec=p[i][1] / unit_deg, latitude=latitude)
                # with col grey50
                context.move_to(**pos(r_a, p[i - 1][0]))
                context.line_to(**pos(r_b, p[i][0]))

        # Draw lines marking S,SSE,SE,ESE,E, etc
        for az in arange(0, 359, 22.5):
            p = []
            for alt in arange(0, 90.1, 1):
                p.append(transform(alt=alt, az=az, latitude=latitude))
            for i in range(1, len(p)):
                r_a = radius(dec=p[i - 1][1] / unit_deg, latitude=latitude)
                r_b = radius(dec=p[i][1] / unit_deg, latitude=latitude)
                # with col grey50
                context.move_to(**pos(r_a, p[i - 1][0]))
                context.line_to(**pos(r_b, p[i][0]))

        # Gluing labels
        def cardinal(dir, ang):
            pp = transform(az=0, alt=ang - 0.01, latitude=latitude)
            r = radius(dec=pp[1] / unit_deg, latitude=latitude)
            p = pos(r, pp[0])

            pp2 = transform(alt=0, az=ang + 0.01, latitude=latitude)
            r2 = radius(dec=pp2[1] / unit_deg, latitude=latitude)
            p2 = pos(r2, pp2[0])

            p3 = [p2[i] - p[i] for i in ('x', 'y')]
            tr = -unit_rev / 4 - atan2(p3[0], p3[1])
            context.text(text=dir, x=p['x'], y=p['y'], h_align=0, v_align=0, gap=unit_mm, rotation=tr)

        glue_text = text[language]["glue_here"]

        # set font bold here
        cardinal(glue_text, 0)
        cardinal(glue_text, 90)
        cardinal(glue_text, 180)
        cardinal(glue_text, 270)

        # White out central hole
        context.circle(centre_x=0, centre_y=0, radius=central_hole_size)  # w fillc white


# Do it right away if we're run as a script
if __name__ == "__main__":
    # Fetch command line arguments passed to us
    arguments = fetch_command_line_arguments(default_filename=AltAzGrid().default_filename())

    # Render the alt-az grid
    AltAzGrid(settings={
        'latitude': arguments['latitude'],
        'language': 'en'
    }).render_to_file(
        filename=arguments['filename'],
        img_format=arguments['img_format']
    )
