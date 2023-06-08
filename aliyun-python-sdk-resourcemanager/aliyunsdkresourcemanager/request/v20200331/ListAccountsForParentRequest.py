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
from aliyunsdkresourcemanager.endpoint import endpoint_data

class ListAccountsForParentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ResourceManager', '2020-03-31', 'ListAccountsForParent','resourcemanager')
		self.set_protocol_type('https')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_QueryKeyword(self): # String
		return self.get_query_params().get('QueryKeyword')

	def set_QueryKeyword(self, QueryKeyword):  # String
		self.add_query_param('QueryKeyword', QueryKeyword)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_ParentFolderId(self): # String
		return self.get_query_params().get('ParentFolderId')

	def set_ParentFolderId(self, ParentFolderId):  # String
		self.add_query_param('ParentFolderId', ParentFolderId)
	def get_IncludeTags(self): # Boolean
		return self.get_query_params().get('IncludeTags')

	def set_IncludeTags(self, IncludeTags):  # Boolean
		self.add_query_param('IncludeTags', IncludeTags)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Tag(self): # Array
		return self.get_query_params().get('Tag')

	def set_Tag(self, Tag):  # Array
		for index1, value1 in enumerate(Tag):
			if value1.get('Value') is not None:
				self.add_query_param('Tag.' + str(index1 + 1) + '.Value', value1.get('Value'))
			if value1.get('Key') is not None:
				self.add_query_param('Tag.' + str(index1 + 1) + '.Key', value1.get('Key'))
