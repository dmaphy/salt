# -*- coding: utf-8 -*-
'''
Simple module for creating temporary directories and files

This is a thin wrapper around Pythons tempfile module

.. versionadded:: Beryllium

'''
from __future__ import absolute_import

import logging
import tempfile

log = logging.getLogger(__name__)


def dir(suffix='', prefix='tmp', parent=None):
    '''
    Create a temporary directory

    CLI Example:

    .. code-block:: bash

        salt '*' temp.dir
        salt '*' temp.dir prefix='mytemp-' parent='/var/run/'
    '''
    return tempfile.mkdtemp(suffix, prefix, parent)


def file(suffix='', prefix='tmp', parent=None):
    '''
    Create a temporary file

    CLI Example:

    .. code-block:: bash

        salt '*' temp.file
        salt '*' temp.file prefix='mytemp-' parent='/var/run/'
    '''
    return tempfile.mkstemp(suffix, prefix, parent)[1]
