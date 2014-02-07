#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import base_handler
import webapp2

from data import adjustments
from data import players
from data import stats

TEMPLATE = 'html/not_implemented.html'

class AdjustHandicapHandler(base_handler.BaseHandler):
    def get(self):
        context = {
                'page_title': 'Adjust a Handicap',
                'page_message': 'Click <a href="/admin">here</a> to go back to the admin page.',
                }
        self.render_response(TEMPLATE, **context)


app = webapp2.WSGIApplication([(r'/.*', AdjustHandicapHandler)],
    debug=True,
    config=base_handler.CONFIG)
