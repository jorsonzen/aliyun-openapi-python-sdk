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
from aliyunsdkarms.endpoint import endpoint_data

class SearchAlertContactGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'SearchAlertContactGroup','arms')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ContactId(self):
		return self.get_query_params().get('ContactId')

	def set_ContactId(self,ContactId):
		self.add_query_param('ContactId',ContactId)

	def get_IsDetail(self):
		return self.get_query_params().get('IsDetail')

	def set_IsDetail(self,IsDetail):
		self.add_query_param('IsDetail',IsDetail)

	def get_ContactGroupName(self):
		return self.get_query_params().get('ContactGroupName')

	def set_ContactGroupName(self,ContactGroupName):
		self.add_query_param('ContactGroupName',ContactGroupName)

	def get_ContactName(self):
		return self.get_query_params().get('ContactName')

	def set_ContactName(self,ContactName):
		self.add_query_param('ContactName',ContactName)

	def get_ContactGroupIds(self):
		return self.get_query_params().get('ContactGroupIds')

	def set_ContactGroupIds(self,ContactGroupIds):
		self.add_query_param('ContactGroupIds',ContactGroupIds)