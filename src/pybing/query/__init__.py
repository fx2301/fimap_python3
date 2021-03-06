from __future__ import absolute_import
# This file is part of PyBing (http://pybing.googlecode.com).
# 
# Copyright (C) 2009 JJ Geewax http://geewax.org/
# All rights reserved.
# 
# This software is licensed as described in the file COPYING.txt,
# which you should have received as part of this distribution.

# Mixins
from .mixin import QueryMixin
from .pagable import Pagable

# Base Query
from .query import BingQuery

# Concrete Queries
from .web import WebQuery
