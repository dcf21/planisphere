#!/usr/bin/python3
# holder.py
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
Render the holder for the planisphere.
"""

from math import sin, cos, atan2, asin, hypot

from constants import unit_deg, unit_rev, unit_cm, unit_mm, r_1, r_2, fold_gap, central_hole_size
from constants import radius, transform, pos
from graphics_context import BaseComponent
from numpy import arange
from settings import fetch_command_line_arguments
from text import text


class Holder(BaseComponent):
    """
    Render the holder for the planisphere.
    """

    def default_filename(self):
        """
        Return the default filename to use when saving this component.
        """
        return "holder"

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

        is_southern = settings['latitude'] < 0
        latitude = abs(settings['latitude'])
        language = settings['language']

        context.set_font_size(0.9)

        a = 6 * unit_cm
        h = r_1 + fold_gap
        context.move_to(x=-r_1, y=0)
        context.line_to(x=r_1, y=0)  # with lt 2)
        context.move_to(x=-r_1, y=-a)
        context.line_to(x=-r_1, y=a)
        context.move_to(x=r_1, y=-a)
        context.line_to(x=r_1, y=a)

        theta = unit_rev / 2 - atan2(r_1, h - a)
        context.arc(centre_x=0, centre_y=h, radius=r_2, arc_from=-theta, arc_to=theta)
        context.move_to(x=-r_2 * sin(theta), y=h + r_2 * cos(theta))
        context.line_to(x=-r_1, y=a)
        context.move_to(x=r_2 * sin(theta), y=h + r_2 * cos(theta))
        context.line_to(x=r_1, y=a)

        # Viewing window
        x0 = (0, h)
        for az in arange(0, 360.5, 1):
            pp = transform(alt=0, az=az, latitude=latitude)
            r = radius(dec=pp[1] / unit_deg, latitude=latitude)
            p = pos(r=r, t=pp[0])
            if az == 0:
                context.move_to(x0[0] + p['x'], x0[1] + p['y'])
            else:
                context.line_to(x0[0] + p['x'], x0[1] + p['y'])
        # polygon p with fillc grey80

        instructions = text[language]["cut_out_instructions"]
        context.text(text="\parbox{10cm}{%s}" % instructions,
                     x=0, y=h + r_1 * 0.4,
                     h_align=0, v_align=0, gap=0, rotation=0)

        # Cardinal points
        def cardinal(dir, ang):
            pp = transform(alt=0, az=ang - 0.01, latitude=latitude)
            r = radius(dec=pp[1] / unit_deg, latitude=latitude)
            p = pos(r, pp[0])

            pp2 = transform(alt=0, az=ang + 0.01, latitude=latitude)
            r2 = radius(dec=pp2[1] / unit_deg, latitude=latitude)
            p2 = pos(r=r2, t=pp2[0])

            p3 = [p2[i] - p[i] for i in ('x', 'y')]
            tr = -unit_rev / 4 - atan2(p3[0], p3[1])

            context.text(text=dir, x=x0[0] + p['x'], y=x0[1] + p['y'], h_align=0, v_align=0, gap=unit_mm, rotation=tr)

        # set font bold
        txt = text[language]['cardinal_points']['w']
        cardinal(txt, 180 if not is_southern else 0)

        txt = text[language]['cardinal_points']['s']
        cardinal(txt, 270 if not is_southern else 90)

        txt = text[language]['cardinal_points']['e']
        cardinal(txt, 0 if not is_southern else 180)

        txt = text[language]['cardinal_points']['n']
        cardinal(txt, 90 if not is_southern else 270)

        # Clock face
        theta = unit_rev / 24 * 7  # 5pm -> 7am
        dash = unit_rev / 24 / 4
        r_3 = r_2 - 2 * unit_mm
        r_4 = r_2 - 3 * unit_mm
        r_5 = r_2 - 4 * unit_mm
        r_6 = r_2 - 5 * unit_mm

        context.arc(centre_x=0, centre_y=h, radius=r_3, arc_from=-theta, arc_to=theta)
        context.arc(centre_x=0, centre_y=h, radius=r_4, arc_from=-theta, arc_to=theta)

        # with linewidth (r_4-r_3)/(0.2*mm)
        for i in arange(-theta, theta, 2 * dash):
            context.arc(centre_x=0, centre_y=h, radius=(r_3 + r_4) / 2, arc_from=i, arc_to=i + dash)

        for hr in arange(-7, 7.1, 1):
            txt = "{:.0f}{}".format(hr if (hr > 0) else hr + 12,
                                    "AM" if (hr > 0) else "PM")
            if language == "fr":
                txt = "{:02d}h00".format(int(hr if (hr > 0) else hr + 24))
            if hr == 0:
                txt = ""
            t = unit_rev / 24 * hr * (-1 if not is_southern else 1)
            context.move_to(x=r_3 * sin(t), y=h + r_3 * cos(t))
            context.line_to(x=r_5 * sin(t), y=h + r_5 * cos(t))
            context.text(text=txt, x=r_6 * sin(t), y=h + r_6 * cos(t), h_align=0, v_align=0, gap=0, rotation=-t)

        # Back edge
        b = unit_cm
        t1 = atan2(h - a, r_1)
        t2 = asin(b / hypot(r_1, h - a))
        context.move_to(x=-r_1, y=-a)
        context.line_to(x=-b * sin(t1 + t2), y=-h - b * cos(t1 + t2))
        context.move_to(x=r_1, y=-a)
        context.line_to(x=b * sin(t1 + t2), y=-h - b * cos(t1 + t2))
        context.arc(centre_x=0, centre_y=-h, radius=b, arc_from=unit_rev / 2 - (t1 + t2),
                    arc_to=unit_rev / 2 + (t1 + t2))

        # Title
        if latitude < 64:
            context.set_font_size(3.0)
            txt = text[language]['title']
            context.text(text="%s %d$^\circ$%s" % (txt, latitude, "N" if not is_southern else "S"),
                         x=0, y=4.8 * unit_cm,
                         h_align=0, v_align=0, gap=0, rotation=0)

            context.set_font_size(0.85)
            txt = text[language]['instructions_1']
            context.text(text="""\parbox{5.6cm}{\centerline{\Huge 1}\vspace{1mm}%s}""" % txt,
                         x=-5.0 * unit_cm, y=3.7 * unit_cm,
                         h_align=0, v_align=0, gap=0, rotation=0)

            context.set_font_size(0.85)
            txt = text[language]['instructions_2'].format(cardinal="north" if not is_southern else "south")
            context.text(text="""\parbox{5.6cm}{\centerline{\Huge 2}\vspace{1mm}%s}""" % txt,
                         x=0, y=3.7 * unit_cm,
                         h_align=0, v_align=0, gap=0, rotation=0)

            context.set_font_size(0.85)
            txt = text[language]['instructions_3']
            context.text(text="""\parbox{5.6cm}{\centerline{\Huge 3}\vspace{1mm}%s}""" % txt,
                         x=5.0 * unit_cm, y=3.7 * unit_cm,
                         h_align=0, v_align=0, gap=0, rotation=0)
        else:
            context.set_font_size(3.0)
            txt = text[language]['title']
            context.text(text="%s %d$^\circ$%s" % (txt, latitude, "N" if not is_southern else "S"),
                         x=0, y=2.4 * unit_cm,
                         h_align=0, v_align=0, gap=0, rotation=0)

        context.set_font_size(0.9)
        txt = text[language]['instructions_4']
        context.text(text="""\\begin{minipage}{12cm}%s\\end{minipage}""" % txt,
                     x=0, y=-6 * unit_cm,
                     h_align=0, v_align=0, gap=0, rotation=0.5 * unit_rev)

        txt = text[language]['more_info']
        context.set_font_size(0.8)
        context.text(text=txt, x=0, y=0.5 * unit_cm, h_align=0, v_align=0, gap=0, rotation=0)
        context.set_font_size(0.8)
        context.text(text=txt, x=0, y=-0.5 * unit_cm, h_align=0, v_align=0, gap=0, rotation=180)

        # White out central hole
        context.circle(centre_x=0, centre_y=-h, radius=central_hole_size)  # w fillc white


# Do it right away if we're run as a script
if __name__ == "__main__":
    # Fetch command line arguments passed to us
    arguments = fetch_command_line_arguments(default_filename=Holder().default_filename())

    # Render the holder for the planisphere
    Holder(settings={
        'latitude': arguments['latitude'],
        'language': 'en'
    }).render_to_file(
        filename=arguments['filename'],
        img_format=arguments['img_format']
    )
