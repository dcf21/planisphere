# text.py
# -*- coding: utf-8 -*-
#
# The python script in this file makes the various parts of a model planisphere.
#
# Copyright (C) 2014-2019 Dominic Ford <dcf21-www@dcford.org.uk>
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

# A list of text strings, which we can render in various languages

text = {
    "en":
        {
            "title": "PLANISPHERE",
            "instructions_1": "Turn the starwheel until you find the point around its edge where today's date is marked, and line this point up with the current time. The viewing window now shows all of the constellations that are visible in the sky.",
            "instructions_2": "Go outside and face {cardinal}. Holding the planisphere up to the sky, the stars marked at the bottom of the viewing window should match up with those that you see in the sky in front of you.",
            "instructions_3": """Turn to face east or west, and rotate the planisphere so that the word "East" or "West" is at the bottom of the window. Once again, the stars at the bottom of the viewing window should match up with those that you see in the sky in front of you.""",
            "instructions_4": (
                r"A planisphere is a simple hand-held device which shows a map of which stars are visible in the night sky at any particular time. By rotating the star wheel, it shows how stars move across the sky through the night, and how different constellations are visible at different times of year.",
                "",
                r"The constellations of the night sky revolve around the celestial poles once every 23 hour and 56 minutes. The idea of representing the night sky as a flat map, which is turned to emulate the night sky's rotation, dated back to the ancient Greek astronomer Hipparchus (circa 150 BC). The fact that this rotation takes four minutes less than the length of a day means that stars rise four minutes earlier each day, or half-an-hour earlier each week. Through the year, new constellations become visible in the pre-dawn sky, and disappear into evening twilight."),
            "more_info": "For more information, see https://in-the-sky.org/planisphere       \u00A9 Dominic Ford 2019.",
            "glue_here": "GLUE HERE",
            "cut_out_instructions": (
                "Cut out this shaded area with scissors.",
                "",
                "It will become a viewing window through which to look at the star wheel behind."
            ),
            "cardinal_points": {"n": "NORTH", "s": "SOUTH", "w": "WEST", "e": "EAST"},
            "months": [
                [31, "JANUARY"],
                [28, "FEBRUARY"],
                [31, "MARCH"],
                [30, "APRIL"],
                [31, "MAY"],
                [30, "JUNE"],
                [31, "JULY"],
                [31, "AUGUST"],
                [30, "SEPTEMBER"],
                [31, "OCTOBER"],
                [30, "NOVEMBER"],
                [31, "DECEMBER"]
            ],
            "constellation_translations": {
            }
        },
    "fr":
        {
            "title": r"CHERCHE-ÉTOILES",
            "instructions_1": r"Tournez le disque de la carte du ciel jusqu'à trouver sur son pourtour le point où est inscrite la date du jour et alignez ce point avec l'heure actuelle. La fenêtre de visualisation montre maintenant toutes les constellations visibles dans le ciel.",
            "instructions_2": r"""Allez dehors et tournez-vous de manière à faire face au nord. Avec le cherche-étoiles tenu à bout de bras et le ciel en arrière-plan, les étoiles figurant au bas de la fenêtre de visualisation doivent co\"incider avec celles que vous voyez dans le ciel devant vous.""",
            "instructions_3": r"Tournez-vous vers l'est ou l'ouest, et faites pivoter le cherche-étoiles de sorte que le mot ``Est'' ou ``Ouest'' soit en bas de la fenêtre. Là encore, les étoiles dans la partie inférieure de la fenêtre de visualisation doivent correspondre à celles que vous voyez devant vous dans le ciel.",
            "instructions_4": (
                r"Un cherche-étoiles est un accessoire de poche simple fournissant une carte des étoiles visibles dans le ciel à un instant donné. Au moyen d'un disque rotatif, il montre comment les étoiles se déplacent dans le ciel pendant la nuit et la manière dont différentes constellations sont visibles selon la période de l'année.",
                "",
                r"Dans le ciel nocturne, les constellations accomplissent une révolution autour des pôles célestes toutes les 23 heures et 56 minutes. L'idée de représenter le ciel nocturne à plat sous la forme d'une carte que l'on tourne pour imiter la rotation du ciel date de l'astronome grec de l'Antiquité Hipparque (150 av. J.-C. env.). Le fait que cette rotation s'effectue en quatre minutes de moins que ce que dure une journée signifie que les étoiles se lèvent quatre minutes plus tôt chaque jour, ou une demi-heure plus tôt chaque semaine. Tout au long de l'année, de nouvelles constellations deviennent visibles dans le ciel avant l'aurore, et disparaissent dans le crépuscule en fin de journée."),
            "more_info": "Pour plus d'informations, voir https://in-the-sky.org/planisphere       \u00A9 Dominic Ford 2019.",
            "glue_here": "COLLER ICI",
            "cut_out_instructions": (
                r"Découpez cette zone grisée.",
                "",
                r"Vous pourrez voir la carte du ciel à travers cette fenêtre de visualisation."
            ),
            "cardinal_points": {"n": "NORD", "s": "SUD", "w": "OUEST", "e": "EST"},
            "months": [
                [31, "JANVIER"],
                [28, "FÉVRIER"],
                [31, "MARS"],
                [30, "AVRIL"],
                [31, "MAI"],
                [30, "JUIN"],
                [31, "JUILLET"],
                [31, "AOÛT"],
                [30, "SEPTEMBRE"],
                [31, "OCTOBRE"],
                [30, "NOVEMBRE"],
                [31, "DÉCEMBRE"]
            ],
            "constellation_translations": {
                "Andromeda": "Andromède",
                "Antlia": "Antlia",
                "Apus": "Apus",
                "Aquarius": "Verseau",
                "Aquila": "Aigle",
                "Ara": "Autel",
                "Aries": "Bélier",
                "Auriga": "Cocher",
                "Boötes": "Bouvier",
                "Caelum": "Burin",
                "Camelopardalis": "Girafe",
                "Cancer": "Cancer",
                "Canes_Venatici": "Chiens_de_chasse",
                "Canis_Major": "Grand_Chien",
                "Canis_Minor": "Petit_Chien",
                "Capricornus": "Capricorne",
                "Carina": "Carène",
                "Cassiopeia": "Cassiopée",
                "Centaurus": "Centaure",
                "Cepheus": "Céphée",
                "Cetus": "Baleine",
                "Chamaeleon": "Chamaeleon",
                "Circinus": "Circinus",
                "Columba": "Colombe",
                "Coma_Berenices": "Chevelure_de_Bérénice",
                "Corona_Australis": "Couronne_australe",
                "Corona_Borealis": "Couronne_boréale",
                "Corvus": "Corbeau",
                "Crater": "Coupe",
                "Crux": "Croix_du_Sud",
                "Cygnus": "Cygne",
                "Delphinus": "Dauphin",
                "Dorado": "Dorado",
                "Draco": "Dragon",
                "Equuleus": "Petit_Cheval",
                "Eridanus": "Éridan",
                "Fornax": "Fourneau",
                "Gemini": "Gémeaux",
                "Grus": "Grue",
                "Hercules": "Hercule",
                "Horologium": "Horloge",
                "Hydra": "Hydre",
                "Hydrus": "Hydrus",
                "Indus": "Indien",
                "Lacerta": "Lézard",
                "Leo": "Lion",
                "Leo_Minor": "Petit_Lion",
                "Lepus": "Lièvre",
                "Libra": "Balance",
                "Lupus": "Loup",
                "Lynx": "Lynx",
                "Lyra": "Lyre",
                "Mensa": "Mensa",
                "Microscopium": "Microscope",
                "Monoceros": "Licorne",
                "Musca": "Musca",
                "Norma": "Règle",
                "Octans": "Octans",
                "Ophiuchus": "Serpentaire",
                "Orion": "Orion",
                "Pavo": "Pavo",
                "Pegasus": "Pégase",
                "Perseus": "Persée",
                "Phoenix": "Phénix",
                "Pictor": "Peintre",
                "Pisces": "Poissons",
                "Piscis_Austrinus": "Poisson_austral",
                "Puppis": "Poupe",
                "Pyxis": "Boussole",
                "Reticulum": "Réticule",
                "Sagitta": "Flèche",
                "Sagittarius": "Sagittaire",
                "Scorpius": "Scorpion",
                "Sculptor": "Sculpteur",
                "Scutum": "Écu_de_Sobieski",
                "Serpens": "Serpent",
                "Sextans": "Sextant",
                "Taurus": "Taureau",
                "Telescopium": "Télescope",
                "Triangulum": "Triangle",
                "Triangulum_Australe": "Triangulum_Australe",
                "Tucana": "Toucan",
                "Ursa_Major": "Grande_Ourse",
                "Ursa_Minor": "Petite_Ourse",
                "Vela": "Voiles",
                "Virgo": "Vierge",
                "Volans": "Volans",
                "Vulpecula": "Petit_Renard"
            }
        }
}
