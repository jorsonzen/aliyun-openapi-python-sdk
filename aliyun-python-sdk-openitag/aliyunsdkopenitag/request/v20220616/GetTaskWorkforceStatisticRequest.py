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

from aliyunsdkcore.request import RoaRequest

class GetTaskWorkforceStatisticRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'OpenITag', '2022-06-16', 'GetTaskWorkforceStatistic')
		self.set_uri_pattern('/openapi/api/v1/tenants/[TenantId]/tasks/[TaskId]/workforce/statistic')
		self.set_method('GET')

	def get_StatType(self): # String
		return self.get_query_params().get('StatType')

	def set_StatType(self, StatType):  # String
		self.add_query_param('StatType', StatType)
	def get_TenantId(self): # String
		return self.get_path_params().get('TenantId')

	def set_TenantId(self, TenantId):  # String
		self.add_path_param('TenantId', TenantId)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_TaskId(self): # Long
		return self.get_path_params().get('TaskId')

	def set_TaskId(self, TaskId):  # Long
		self.add_path_param('TaskId', TaskId)
	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
