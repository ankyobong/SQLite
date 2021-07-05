#!/usr/bin/env python
# coding=utf8
"""
====================================
 :mod:`argoslabs.data.sqlite`
======0==============================
.. moduleauthor:: Kyobong An <akb0930@argos-labs.com>
.. note:: ARGOS-LABS License

Description
===========
ARGOS LABS plugin module for sqlite
"""
#
# Authors
# ===========
#
# * Kyobong An
#
# Change Log
# --------
#  * [2021/07/05]
#   start


################################################################################
import sys
import sqlite3
from alabs.common.util.vvargs import ModuleContext, func_log, \
    ArgsError, ArgsExit, get_icon_path


@func_log
def do_sqlite(mcxt, argspec):
    mcxt.logger.info('>>>starting...')


# ##########################################################
def _main(*args):
    with ModuleContext(
            owner='ARGOS-LABS',
            group='4', # Data Science
            version='1.0',
            platform=['windows', 'darwin', 'linux'],
            output_type='text',
            display_name='SQLite',
            icon_path=get_icon_path(__file__),
            description='SQLite plugin',
    ) as mcxt:
        # ##################################### for app dependent options
        # ----------------------------------------------------------------------
        mcxt.add_argument('--select',
                          display_name='SELECT',
                          input_group='Search',
                          help='choose method')
        # ##################################### for app dependent parameters
        # ----------------------------------------------------------------------
        mcxt.add_argument('open', nargs='?',
                          display_name='Open CSV',
                          input_method='filewrite',
                          input_group='CREATE',
                          help='open db')
        argspec = mcxt.parse_args(args)
        return do_sqlite(mcxt, argspec)


################################################################################
def main(*args):
    try:
        return _main(*args)
    except ArgsError as err:
        sys.stderr.write('Error: %s\nPlease -h to print help\n' % str(err))
    except ArgsExit as _:
        pass