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
from aliyunsdkram.endpoint import endpoint_data

class UpdateUserRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ram', '2015-05-01', 'UpdateUser','Ram')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_NewUserName(self): # String
		return self.get_query_params().get('NewUserName')

	def set_NewUserName(self, NewUserName):  # String
		self.add_query_param('NewUserName', NewUserName)
	def get_NewMobilePhone(self): # String
		return self.get_query_params().get('NewMobilePhone')

	def set_NewMobilePhone(self, NewMobilePhone):  # String
		self.add_query_param('NewMobilePhone', NewMobilePhone)
	def get_NewEmail(self): # String
		return self.get_query_params().get('NewEmail')

	def set_NewEmail(self, NewEmail):  # String
		self.add_query_param('NewEmail', NewEmail)
	def get_NewDisplayName(self): # String
		return self.get_query_params().get('NewDisplayName')

	def set_NewDisplayName(self, NewDisplayName):  # String
		self.add_query_param('NewDisplayName', NewDisplayName)
	def get_NewComments(self): # String
		return self.get_query_params().get('NewComments')

	def set_NewComments(self, NewComments):  # String
		self.add_query_param('NewComments', NewComments)
	def get_UserName(self): # String
		return self.get_query_params().get('UserName')

	def set_UserName(self, UserName):  # String
		self.add_query_param('UserName', UserName)
