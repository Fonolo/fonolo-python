#
# This file is part of the Fonolo Python Wrapper package.
#
# (c) Foncloud, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#

import re

from .requesthandler import RequestHandler
from ..exception.exception import FonoloException

class Optin(object):

    def __init__(self, _handler, _optin_id):
        self.handler = _handler;
        self.optin_id = _optin_id;

    def get(self):
        return self.handler.get('optin/' + self.optin_id);
