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

class QueryDataRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'QueryData','2.2.0')
		self.set_method('POST')

	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_ReturnFields(self): # String
		return self.get_query_params().get('ReturnFields')

	def set_ReturnFields(self, ReturnFields):  # String
		self.add_query_param('ReturnFields', ReturnFields)
	def get_Conditions(self): # String
		return self.get_query_params().get('Conditions')

	def set_Conditions(self, Conditions):  # String
		self.add_query_param('Conditions', Conditions)
	def get_ApiId(self): # String
		return self.get_query_params().get('ApiId')

	def set_ApiId(self, ApiId):  # String
		self.add_query_param('ApiId', ApiId)
