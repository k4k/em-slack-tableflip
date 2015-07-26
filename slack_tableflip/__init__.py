#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# EM Slack Tableflip
# Copyright (c) 2015 Erin Morelli
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
'''
Module: slack_tableflip

    - Sets up Flask application and module constants
'''

import os
from flask import Flask
from datetime import date
from pkginfo import Installed
from pkg_resources import get_provider


# =============================================================================
#  App Constants
# =============================================================================

# Set module name
__module__ = "slack_tableflip.{0}".format(__file__)


# Get module info
def set_project_info():
    ''' Set project information from setup tools installation
    '''

    # CUSTOMIZE THIS VALUE FOR YOUR OWN INSTALLATION
    base_url = 'http://dev.erinmorelli.com/slack/flip'

    # Get app info from the dist
    app_name = 'slack_tableflip'
    provider = get_provider(app_name)
    dist = Installed(app_name).__dict__

    # Set extra info
    dist.update({
        'name_full': 'EM Slack Tableflip',
        'author_url': 'http://www.erinmorelli.com',
        'version_int': 0.101,
        'package_path': provider.module_path,
        'copyright': str(date.today().year),
        'base_url': base_url,
        'auth_url': '{0}/authenticate'.format(base_url),
        'valid_url': '{0}/validate'.format(base_url)
    })

    return dist

# Project info
PROJECT_INFO = set_project_info()

# Set the template directory
TEMPLATE_DIR = os.path.join(PROJECT_INFO['package_path'], 'templates')

# Set required args
REQUIRED_ARGS = [
    'command',
    'team_id',
    'user_id',
    'channel_id'
]

# Allowed slash commands
ALLOWED_COMMANDS = [
    '/flip',
    '/fliptable',
    '/tableflip',
    '/flip_table',
    '/table_flip'
]

# Allowed flip types
# Sources:
#   http://www.emoticonfun.org/flip/
#   http://emojicons.com/table-flipping
ALLOWED_TYPES = {
    'classic': "(╯°□°)╯︵ ┻━┻",
    'rage': "(ﾉಥ益ಥ）ﾉ﻿ ┻━┻",
    'whoops': "┬──┬﻿ ¯\_(ツ)",
    'two': "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    'relax': "┬─┬ノ( º _ ºノ)",
    'teeth': "(ノಠ益ಠ)ノ彡┻━┻",
    'monocle': "(╯ಠ_ರೃ)╯︵ ┻━┻",
    'person': "(╯°□°）╯︵ /(.□. \)",
    'jake': "(┛❍ᴥ❍﻿)┛彡┻━┻",
    'owl': "(ʘ∇ʘ)ク 彡 ┻━┻",
    'laptop': "(ノÒ益Ó)ノ彡▔▔▏",
    'strong': "/(ò.ó)┛彡┻━┻",
    'yelling': "(┛◉Д◉)┛彡┻━┻",
    'shrug': "┻━┻ ︵﻿ ¯\(ツ)/¯ ︵ ┻━┻",
    'pudgy': "(ノ ゜Д゜)ノ ︵ ┻━┻",
    'battle': "(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)",
    'return': "(ノ^_^)ノ┻━┻ ┬─┬ ノ( ^_^ノ)",
    'cry': "(╯'□')╯︵ ┻━┻",
    'freakout': "(ﾉಥДಥ)ﾉ︵┻━┻･/",
    'people': "(/ .□.)\ ︵╰(゜Д゜)╯︵ /(.□. \)",
    'force': "(._.) ~ ︵ ┻━┻",
    'bear': "ʕノ•ᴥ•ʔノ ︵ ┻━┻",
    'magic': "(/¯◡ ‿ ◡)/¯ ~ ┻━┻",
    'robot': "┗[© ♒ ©]┛ ︵ ┻━┻",
    'opposite': "ノ┬─┬ノ ︵ ( \o°o)\\",
    'cute': "┻━┻ ︵ ლ(⌒-⌒ლ)"
}

# Flipped character mapping
FLIPPED_CHARS = {
    " ": " ",
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ı",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "q",
    "C": "Ɔ",
    "D": "p",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "ʞ",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "ɹ",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    ",": "'",
    "!": "¡",
    "?": "¿",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    ".": "˙",
    '"': ",,",
    "'": ","
}

# =============================================================================
# Flask App Configuration
# =============================================================================

# Initalize flask app
APP = Flask(
    'em-slack-tableflip',
    template_folder=TEMPLATE_DIR,
    static_folder=TEMPLATE_DIR
)

# Set up flask config
# SET THESE ENV VALUES FOR YOUR OWN INSTALLATION
APP.config.update({
    'SQLALCHEMY_DATABASE_URI': os.environ['EMST_DATABASE_URI'],
    'SECRET_KEY': os.environ['EMST_SECRET_KEY']
})
