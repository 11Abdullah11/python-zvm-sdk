# Copyright 2017 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import datetime
import jwt
import mock
import unittest

from zvmsdk import exception
from zvmsdk.sdkwsgi.handlers import image
from zvmsdk.sdkwsgi import util


FAKE_UUID = '00000000-0000-0000-0000-000000000000'


class FakeReq(object):
    def __init__(self):
        self.headers = {}
        self.environ = {}

    def __getitem__(self, name):
        return self.headers


class HandlersImageTest(unittest.TestCase):

    def setUp(self):
        expired_elapse = datetime.timedelta(seconds=100)
        expired_time = datetime.datetime.utcnow() + expired_elapse
        payload = jwt.encode({'exp': expired_time}, 'username')

        self.req = FakeReq()
        self.req.headers['X-Auth-Token'] = payload

    @mock.patch.object(image.ImageAction, 'create')
    def test_image_create(self, mock_create):
        body_str = '{"image": {"uuid": "1234"}}'
        self.req.body = body_str

        image.image_create(self.req)
        body = util.extract_json(body_str)
        mock_create.assert_called_once_with(body=body)

    def test_image_create_invalidname(self):
        body_str = '{"image": {"version": ""}}'
        self.req.body = body_str

        self.assertRaises(exception.ValidationError, image.image_create,
                          self.req)
