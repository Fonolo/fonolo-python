#
# This file is part of the Fonolo Python Wrapper package.
#
# (c) Foncloud, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#

import re

from .exception.exception import FonoloException
from .api.requesthandler import RequestHandler

from .api.callback import CallBack
from .api.call import Call
from .api.calls import Calls
from .api.optin import Optin
from .api.optins import Optins
from .api.profile import Profile
from .api.profiles import Profiles
from .api.realtime import Realtime
from .api.pending import Pending
from .api.scheduled import Scheduled
from .api.timezones import Timezones

class Client(object):

    def __init__(self, _account_sid, _api_token):

        #
        # Python library version
        #
        self.version = '1.0.2'

        #
        # validate account SID
        #
        if re.match(r'^[A-Z]{2}[0-9a-f]{32}$', _account_sid):
            self.account_sid = _account_sid
        else:
            raise FonoloException('ERROR: invalid API acount sid provided: ' + _account_sid)

        #
        # validate the APi token
        #
        if re.match(r'^[0-9a-f]{64}$', _api_token):
            self.api_token = _api_token
        else:
            raise FonoloException('ERROR: invalid API access token provided: ' + _api_token)

        #
        # the default API settings
        #
        self.options = {
            'url': 'https://api.fonolo.com/3.0/',
            'verify_ssl': True
        }

        self.request = RequestHandler(self.account_sid, self.api_token, self.options);

        self.calls      = Calls(self.request);
        self.optins     = Optins(self.request);
        self.realtime   = Realtime(self.request);
        self.pending    = Pending(self.request);
        self.scheduled  = Scheduled(self.request);
        self.profiles   = Profiles(self.request);
        self.timezones  = Timezones(self.request);

    #
    # quick function to override the endpoint URL for development
    #
    def endpoint(self, _endpoint_url):
        self.options['url'] = _endpoint_url;

    #
    # turn on/off SSL verification- for testing
    #
    def verify_ssl(self, _verify):
        self.options['verify_ssl'] = _verify;

    #
    # call-back
    #
    def callback(self, _call_id=''):
        return CallBack(self.request, _call_id);

    #
    # calls
    #
    def call(self, _call_id):
        return Call(self.request, _call_id);

    #
    # optins
    #
    def optin(self, _optin_id):
        return Optin(self.request, _optin_id);

    #
    # profiles
    #
    def profile(self, _profile_id):
        return Profile(self.request, _profile_id);
