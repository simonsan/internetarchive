# -*- coding: utf-8 -*-
"""
Internetarchive Library
~~~~~~~~~~~~~~~~~~~~~~~

Internetarchive is a python interface to archive.org.
usage:

    >>> import internetarchive
    >>> item = internetarchive.Item('govlawgacode20071')
    >>> item.exists
    True

:copyright: (c) 2013 by Jacob M. Johnson.
:license: GPL, see LICENSE for more details.

"""

__title__ = 'internetarchive'
__version__ = '0.5.1'
__author__ = 'Jacob M. Johnson'
__license__ = 'GPL'
__copyright__ = 'Copyright 2013 Jacob M. Johnson'

from .item import Item, File
from .service import Search, Catalog
from .api import *


# Set default logging handler to avoid "No handler found" warnings.
import logging
try: # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
