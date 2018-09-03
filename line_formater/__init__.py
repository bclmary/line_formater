#!/usr/bin/env python3
# -*-coding:utf-8 -*

"""
A collection of text line formaters.

::

    ┏━━by━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃░░░░░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓████████░░░░░░░░░░░░░░░░░░┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃░░░░░░░░░░░░░░░░░░██▒▒▓▓▓▓▓▓▓▓▓▓▓▓████▓▓██░░░░░░░░░░░░░░░░┃
    ┃░░░░░░░░░░░░░░░░░░██▒▒▓▓▓▓░░      ▓▓▓▓  ██░░░░░░░░░░░░░░░░┃
    ┃                  ██▒▒▓▓░░    ████░░██  ██                ┃
    ┃                    ██▓▓░░    ████░░██  ██                ┃
    ┃                  ████▓▓░░░░      ░░  ░░██                ┃
    ┃              ████▒▒▒▒██▓▓░░████████░░██████              ┃
    ┃            ██▓▓▒▒▒▒▒▒▒▒██░░░░░░░░░░██▒▒▒▒▓▓██            ┃ 
    ┃            ██▓▓▓▓▒▒▒▒▒▒▒▒██████████▒▒▒▒▓▓▓▓██            ┃
    ┃          ██▓▓▓▓▓▓▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▓▓▓▓▓▓██          ┃
    ┃          ██▓▓▓▓██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▓▓▓▓██          ┃
    ┃          ██▓▓▓▓▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓██          ┃
    ┃░░░░░░░░░░██▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓██░░░░░░░░░░┃
    ┃░░░░░░░░░░░░██████░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░██████░░░░░░░░░░░░┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃░░░░░░░░░░░░░░░░██▓▓▓▓▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▓▓██░░░░░░░░░░░░░░░░┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▒▒██▒▒██▒▒▓▓▓▓▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒██████████████████▒▒▒▒▒▒██████████████████▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━bclmary━━┛

"""

from line_formater.line_formater import LineFormater

__all__ = [
    "LineFormater",
    ]
