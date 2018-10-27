# text.py
# -*- coding: utf-8 -*-
#
# The python script in this file makes the various parts of a model planisphere.
#
# Copyright (C) 2014-2018 Dominic Ford <dcf21-www_dcford.org.uk>
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
            "instructions_2": "Go outside and face %s. Holding the planisphere up to the sky, the stars marked at the bottom of the viewing window should match up with those that you see in the sky in front of you.",
            "instructions_3": """Turn to face east or west, and rotate the planisphere so that the word ``East'' or ``West'' is at the bottom of the window. Once again, the stars at the bottom of the viewing window should match up with those that you see in the sky in front of you.""",
            "instructions_4": r"A planisphere is a simple hand-held device which shows a map of which stars are visible in the night sky at any particular time. By rotating the star wheel, it shows how stars move across the sky through the night, and how different constellations are visible at different times of year. \\vspace{6mm}\n\n The constellations of the night sky revolve around the celestial poles once every 23 hour and 56 minutes. The idea of representing the night sky as a flat map, which is turned to emulate the night sky's rotation, dated back to the ancient Greek astronomer Hipparchus (circa 150~BC). The fact that this rotation takes four minutes less than the length of a day means that stars rise four minutes earlier each day, or half-an-hour earlier each week. Through the year, new constellations become visible in the pre-dawn sky, and disappear into evening twilight.",
            "more_info": "For more information, see http://in-the-sky.org/planisphere \kern2cm\ \copyright\ Dominic Ford 2018.",
            "glue_here": "GLUE HERE",
            "cut_out_instructions": "\centerline{Cut out this shaded area with scissors.}\centerline{It will become a viewing window through which}\centerline{to look at the star wheel behind.}",
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
            "zodiacal_constellations": [
                {"name": "Aries", "symbol": "\u2648"},
                {"name": "Taurus", "symbol": "\u2649"},
                {"name": "Gemini", "symbol": "\u264a"},
                {"name": "Cancer", "symbol": "\u264b"},
                {"name": "Leo", "symbol": "\u264c"},
                {"name": "Virgo", "symbol": "\u264d"},
                {"name": "Libra", "symbol": "\u264e"},
                {"name": "Scorpio", "symbol": "\u264f"},
                {"name": "Sagittarius", "symbol": "\u2650"},
                {"name": "Capricornus", "symbol": "\u2651"},
                {"name": "Aquarius", "symbol": "\u2652"},
                {"name": "Pisces", "symbol": "\u2653"},
            ],
            "constellation_translations": {
            }
        },
    "fr":
        {
            "title": r"CHERCHE-\'ETOILES",
            "instructions_1": r"Tournez le disque de la carte du ciel jusqu'\`a trouver sur son pourtour le point o\`u est inscrite la date du jour et alignez ce point avec l'heure actuelle. La fen\^etre de visualisation montre maintenant toutes les constellations visibles dans le ciel.",
            "instructions_2": r"""Allez dehors et tournez-vous de mani\`ere \`a faire face au nord. Avec le cherche-\'etoiles tenu \`a bout de bras et le ciel en arri\`ere-plan, les \'etoiles figurant au bas de la fen\^etre de visualisation doivent co\"incider avec celles que vous voyez dans le ciel devant vous.""",
            "instructions_3": r"Tournez-vous vers l'est ou l'ouest, et faites pivoter le cherche-\'etoiles de sorte que le mot ``Est'' ou ``Ouest'' soit en bas de la fen\^etre. L\`a encore, les \'etoiles dans la partie inf\'erieure de la fen\^etre de visualisation doivent correspondre \`a celles que vous voyez devant vous dans le ciel.",
            "instructions_4": r"Un cherche-\'etoiles est un accessoire de poche simple fournissant une carte des \'etoiles visibles dans le ciel \`a un instant donn\'e. Au moyen d'un disque rotatif, il montre comment les \'etoiles se d\'eplacent dans le ciel pendant la nuit et la mani\`ere dont diff\'erentes constellations sont visibles selon la p\'eriode de l'ann\'ee. \\vspace{6mm}\n\n Dans le ciel nocturne, les constellations accomplissent une r\'evolution autour des p\^oles c\'elestes toutes les 23 heures et 56 minutes. L'id\'ee de repr\'esenter le ciel nocturne \`a plat sous la forme d'une carte que l'on tourne pour imiter la rotation du ciel date de l'astronome grec de l'Antiquit\'e Hipparque (150 av. J.-C. env.). Le fait que cette rotation s'effectue en quatre minutes de moins que ce que dure une journ\'ee signifie que les \'etoiles se l\`event quatre minutes plus t\^ot chaque jour, ou une demi-heure plus t\^ot chaque semaine. Tout au long de l'ann\'ee, de nouvelles constellations deviennent visibles dans le ciel avant l'aurore, et disparaissent dans le cr\'epuscule en fin de journ\'ee.",
            "more_info": "Pour plus d'informations, voir http://in-the-sky.org/planisphere \kern2cm\ \copyright\ Dominic Ford 2018.",
            "glue_here": "COLLER ICI",
            "cut_out_instructions": r"""\centerline{D\'ecoupez cette zone gris\'ee.}\centerline{Vous pourrez voir la carte du ciel}\centerline{\`a travers cette fen\^etre de visualisation.}""",
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
            "zodiacal_constellations": [
                {"name": "Aries", "symbol": "\u2648"},
                {"name": "Taurus", "symbol": "\u2649"},
                {"name": "Gemini", "symbol": "\u264a"},
                {"name": "Cancer", "symbol": "\u264b"},
                {"name": "Leo", "symbol": "\u264c"},
                {"name": "Virgo", "symbol": "\u264d"},
                {"name": "Libra", "symbol": "\u264e"},
                {"name": "Scorpio", "symbol": "\u264f"},
                {"name": "Sagittarius", "symbol": "\u2650"},
                {"name": "Capricornus", "symbol": "\u2651"},
                {"name": "Aquarius", "symbol": "\u2652"},
                {"name": "Pisces", "symbol": "\u2653"},
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
