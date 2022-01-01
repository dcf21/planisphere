#!/usr/bin/python3
# holder.py
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
Render the holder for the planisphere.
"""

from math import pi, sin, cos, atan2, asin, hypot

from numpy import arange

from constants import radius, transform, pos
from constants import unit_deg, unit_rev, unit_cm, unit_mm, r_1, r_2, fold_gap, central_hole_size, line_width_base
from graphics_context import BaseComponent
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

    def bounding_box(self, settings):
        """
        Return the bounding box of the canvas area used by this component.

        :param settings:
            A dictionary of settings required by the renderer.
        :return:
         Dictionary with the elements 'x_min', 'x_max', 'y_min' and 'y_max' set
        """

        h = r_1 + fold_gap

        return {
            'x_min': -r_1 - 4 * unit_mm,
            'x_max': r_1 + 4 * unit_mm,
            'y_min': -r_2 - h - 4 * unit_mm,
            'y_max': h + 1.2 * unit_cm
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

        # Draw dotted line for folding the bottom of the planisphere
        context.begin_path()
        context.move_to(x=-r_1, y=0)
        context.line_to(x=r_1, y=0)
        context.stroke(dotted=True)

        # Draw the rectangular back and lower body of the planisphere
        context.begin_path()
        context.move_to(x=-r_1, y=a)
        context.line_to(x=-r_1, y=-a)
        context.move_to(x=r_1, y=a)
        context.line_to(x=r_1, y=-a)
        context.stroke(dotted=False)

        # Draw the curved upper part of the body of the planisphere
        theta = unit_rev / 2 - atan2(r_1, h - a)
        context.begin_path()
        context.arc(centre_x=0, centre_y=-h, radius=r_2, arc_from=-theta - pi / 2, arc_to=theta - pi / 2)
        context.move_to(x=-r_2 * sin(theta), y=-h - r_2 * cos(theta))
        context.line_to(x=-r_1, y=-a)
        context.move_to(x=r_2 * sin(theta), y=-h - r_2 * cos(theta))
        context.line_to(x=r_1, y=-a)
        context.stroke()

        # Shade the viewing window which needs to be cut out
        x0 = (0, h)
        context.begin_path()
        for i, az in enumerate(arange(0, 360.5, 1)):
            pp = transform(alt=0, az=az, latitude=latitude)
            r = radius(dec=pp[1] / unit_deg, latitude=latitude)
            p = pos(r=r, t=pp[0])
            if i == 0:
                context.move_to(x0[0] + p['x'], -x0[1] + p['y'])
            else:
                context.line_to(x0[0] + p['x'], -x0[1] + p['y'])
        context.stroke()
        context.fill(color=(0, 0, 0, 0.2))

        # Display instructions for cutting out the viewing window
        instructions = text[language]["cut_out_instructions"]
        context.set_color(color=(0, 0, 0, 1))
        context.text_wrapped(text=instructions,
                             width=4 * unit_cm, justify=0,
                             x=0, y=-h - r_1 * 0.35,
                             h_align=0, v_align=0, rotation=0)

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

            context.text(text=dir, x=x0[0] + p['x'], y=-x0[1] + p['y'],
                         h_align=0, v_align=1, gap=unit_mm, rotation=tr)

        # Write the cardinal points around the horizon of the viewing window
        context.set_font_style(bold=True)

        txt = text[language]['cardinal_points']['w']
        cardinal(txt, 180 if not is_southern else 0)

        txt = text[language]['cardinal_points']['s']
        cardinal(txt, 270 if not is_southern else 90)

        txt = text[language]['cardinal_points']['e']
        cardinal(txt, 0 if not is_southern else 180)

        txt = text[language]['cardinal_points']['n']
        cardinal(txt, 90 if not is_southern else 270)

        context.set_font_style(bold=False)

        # Clock face, which lines up with the date scale on the star wheel
        theta = unit_rev / 24 * 7  # 5pm -> 7am means we cover 7 hours on either side of midnight
        dash = unit_rev / 24 / 4  # Draw fat dashes at 15 minute intervals

        # Outer edge of dashed scale
        r_3 = r_2 - 2 * unit_mm

        # Inner edge of dashed scale
        r_4 = r_2 - 3 * unit_mm

        # Radius of dashes for marking hours
        r_5 = r_2 - 4 * unit_mm

        # Radius of text marking hours
        r_6 = r_2 - 5.5 * unit_mm

        # Inner and outer curves around dashed scale
        context.begin_path()
        context.arc(centre_x=0, centre_y=-h, radius=r_3, arc_from=-theta - pi / 2, arc_to=theta - pi / 2)
        context.begin_sub_path()
        context.arc(centre_x=0, centre_y=-h, radius=r_4, arc_from=-theta - pi / 2, arc_to=theta - pi / 2)
        context.stroke()

        # Draw a fat dashed line with one dash every 15 minutes
        for i in arange(-theta, theta, 2 * dash):
            context.begin_path()
            context.arc(centre_x=0, centre_y=-h, radius=(r_3 + r_4) / 2, arc_from=i - pi / 2, arc_to=i + dash - pi / 2)
            context.stroke(line_width=(r_3 - r_4) / line_width_base)

        # Write the hours
        for hr in arange(-7, 7.1, 1):
            txt = "{:.0f}{}".format(hr if (hr > 0) else hr + 12,
                                    "AM" if (hr > 0) else "PM")
            if language == "fr":
                txt = "{:02d}h00".format(int(hr if (hr > 0) else hr + 24))
            if hr == 0:
                txt = ""
            t = unit_rev / 24 * hr * (-1 if not is_southern else 1)

            # Stroke a dash and write the number of the hour
            context.begin_path()
            context.move_to(x=r_3 * sin(t), y=-h - r_3 * cos(t))
            context.line_to(x=r_5 * sin(t), y=-h - r_5 * cos(t))
            context.stroke(line_width=1)
            context.text(text=txt, x=r_6 * sin(t), y=-h - r_6 * cos(t), h_align=0, v_align=0, gap=0, rotation=t)

        # Back edge
        b = unit_cm
        t1 = atan2(h - a, r_1)
        t2 = asin(b / hypot(r_1, h - a))
        context.begin_path()
        context.move_to(x=-r_1, y=a)
        context.line_to(x=-b * sin(t1 + t2), y=h + b * cos(t1 + t2))
        context.move_to(x=r_1, y=a)
        context.line_to(x=b * sin(t1 + t2), y=h + b * cos(t1 + t2))
        context.arc(centre_x=0, centre_y=h, radius=b, arc_from=unit_rev / 2 - (t1 + t2) - pi / 2,
                    arc_to=unit_rev / 2 + (t1 + t2) - pi / 2)
        context.stroke(line_width=1)

        # For latitudes not too close to the pole, we have enough space to fit instructions onto the planisphere
        if latitude < 56:
            # Big bold title
            context.set_font_size(3.0)
            txt = text[language]['title']
            context.set_font_style(bold=True)
            context.text(
                text="%s %d\u00B0%s" % (txt, latitude, "N" if not is_southern else "S"),
                x=0, y=-4.8 * unit_cm,
                h_align=0, v_align=0, gap=0, rotation=0)
            context.set_font_style(bold=False)

            # First column of instructions
            context.set_font_size(2)
            context.text(
                text="1",
                x=-5.0 * unit_cm, y=-4.0 * unit_cm,
                h_align=0, v_align=0, gap=0, rotation=0)
            context.set_font_size(1)
            context.text_wrapped(
                text=text[language]['instructions_1'],
                x=-5.0 * unit_cm, y=-3.4 * unit_cm, width=4.5 * unit_cm, justify=-1,
                h_align=0, v_align=1, rotation=0)

            # Second column of instructions
            context.set_font_size(2)
            context.text(
                text="2",
                x=0, y=-4.0 * unit_cm,
                h_align=0, v_align=0, gap=0, rotation=0)
            context.set_font_size(1)
            context.text_wrapped(
                text=text[language]['instructions_2'].format(cardinal="north" if not is_southern else "south"),
                x=0, y=-3.4 * unit_cm, width=4.5 * unit_cm, justify=-1,
                h_align=0, v_align=1, rotation=0)

            # Third column of instructions
            context.set_font_size(2)
            context.text(
                text="3",
                x=5.0 * unit_cm, y=-4.0 * unit_cm,
                h_align=0, v_align=0, gap=0, rotation=0)
            context.set_font_size(1)
            context.text_wrapped(
                text=text[language]['instructions_3'],
                x=5.0 * unit_cm, y=-3.4 * unit_cm, width=4.5 * unit_cm, justify=-1,
                h_align=0, v_align=1, rotation=0)
        else:
            # For planispheres for use at high latitudes, we don't have much space, so don't show instructions.
            # We just display a big bold title
            context.set_font_size(3.0)
            txt = text[language]['title']
            context.set_font_style(bold=True)
            context.text(
                text="%s %d\u00B0%s" % (txt, latitude, "N" if not is_southern else "S"),
                x=0, y=-1.8 * unit_cm,
                h_align=0, v_align=0, gap=0, rotation=0)
            context.set_font_style(bold=False)

        # Write explanatory text on the back of the planisphere
        context.set_font_size(1.1)
        context.text_wrapped(
            text=text[language]['instructions_4'],
            x=0, y=5.5 * unit_cm, width=12 * unit_cm, justify=-1,
            h_align=0, v_align=1, rotation=0.5 * unit_rev)

        # Display web link and copyright text
        txt = text[language]['more_info']
        context.set_font_size(0.9)
        context.text(text=txt, x=0, y=-0.5 * unit_cm, h_align=0, v_align=0, gap=0, rotation=0)
        context.set_font_size(0.9)
        context.text(text=txt, x=0, y=0.5 * unit_cm, h_align=0, v_align=0, gap=0, rotation=pi)

        # Draw central hole
        context.begin_path()
        context.circle(centre_x=0, centre_y=h, radius=central_hole_size)
        context.stroke()


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
