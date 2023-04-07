# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
import json

class CreateApiDestinationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'CreateApiDestination')
		self.set_method('POST')

	def get_ConnectionName(self): # String
		return self.get_query_params().get('ConnectionName')

	def set_ConnectionName(self, ConnectionName):  # String
		self.add_query_param('ConnectionName', ConnectionName)
	def get_Description(self): # String
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # String
		self.add_query_param('Description', Description)
	def get_HttpApiParameters(self): # Struct
		return self.get_query_params().get('HttpApiParameters')

	def set_HttpApiParameters(self, HttpApiParameters):  # Struct
		self.add_query_param("HttpApiParameters", json.dumps(HttpApiParameters))
	def get_ApiDestinationName(self): # String
		return self.get_query_params().get('ApiDestinationName')

	def set_ApiDestinationName(self, ApiDestinationName):  # String
		self.add_query_param('ApiDestinationName', ApiDestinationName)
