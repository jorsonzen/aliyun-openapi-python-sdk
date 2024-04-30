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
from aliyunsdkrds.endpoint import endpoint_data

class ModifyCustinsResourceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'ModifyCustinsResource','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_IncreaseRatio(self): # String
		return self.get_query_params().get('IncreaseRatio')

	def set_IncreaseRatio(self, IncreaseRatio):  # String
		self.add_query_param('IncreaseRatio', IncreaseRatio)
	def get_RestoreOriginalSpecification(self): # String
		return self.get_query_params().get('RestoreOriginalSpecification')

	def set_RestoreOriginalSpecification(self, RestoreOriginalSpecification):  # String
		self.add_query_param('RestoreOriginalSpecification', RestoreOriginalSpecification)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_ResourceType(self): # String
		return self.get_query_params().get('ResourceType')

	def set_ResourceType(self, ResourceType):  # String
		self.add_query_param('ResourceType', ResourceType)
	def get_AdjustDeadline(self): # String
		return self.get_query_params().get('AdjustDeadline')

	def set_AdjustDeadline(self, AdjustDeadline):  # String
		self.add_query_param('AdjustDeadline', AdjustDeadline)
	def get_TargetValue(self): # Integer
		return self.get_query_params().get('TargetValue')

	def set_TargetValue(self, TargetValue):  # Integer
		self.add_query_param('TargetValue', TargetValue)
