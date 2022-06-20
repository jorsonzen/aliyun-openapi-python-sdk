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
from aliyunsdksas.endpoint import endpoint_data

class ExportWarningRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ExportWarning')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IsCleartextPwd(self): # Integer
		return self.get_query_params().get('IsCleartextPwd')

	def set_IsCleartextPwd(self, IsCleartextPwd):  # Integer
		self.add_query_param('IsCleartextPwd', IsCleartextPwd)
	def get_StatusList(self): # String
		return self.get_query_params().get('StatusList')

	def set_StatusList(self, StatusList):  # String
		self.add_query_param('StatusList', StatusList)
	def get_RiskLevels(self): # String
		return self.get_query_params().get('RiskLevels')

	def set_RiskLevels(self, RiskLevels):  # String
		self.add_query_param('RiskLevels', RiskLevels)
	def get_RiskName(self): # String
		return self.get_query_params().get('RiskName')

	def set_RiskName(self, RiskName):  # String
		self.add_query_param('RiskName', RiskName)
	def get_SourceIp(self): # String
		return self.get_query_params().get('SourceIp')

	def set_SourceIp(self, SourceIp):  # String
		self.add_query_param('SourceIp', SourceIp)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
	def get_ExportType(self): # String
		return self.get_query_params().get('ExportType')

	def set_ExportType(self, ExportType):  # String
		self.add_query_param('ExportType', ExportType)
	def get_Dealed(self): # String
		return self.get_query_params().get('Dealed')

	def set_Dealed(self, Dealed):  # String
		self.add_query_param('Dealed', Dealed)
	def get_TypeNames(self): # String
		return self.get_query_params().get('TypeNames')

	def set_TypeNames(self, TypeNames):  # String
		self.add_query_param('TypeNames', TypeNames)
	def get_IsSummaryExport(self): # Integer
		return self.get_query_params().get('IsSummaryExport')

	def set_IsSummaryExport(self, IsSummaryExport):  # Integer
		self.add_query_param('IsSummaryExport', IsSummaryExport)
	def get_RiskIds(self): # String
		return self.get_query_params().get('RiskIds')

	def set_RiskIds(self, RiskIds):  # String
		self.add_query_param('RiskIds', RiskIds)
	def get_StrategyId(self): # Long
		return self.get_query_params().get('StrategyId')

	def set_StrategyId(self, StrategyId):  # Long
		self.add_query_param('StrategyId', StrategyId)
	def get_TypeName(self): # String
		return self.get_query_params().get('TypeName')

	def set_TypeName(self, TypeName):  # String
		self.add_query_param('TypeName', TypeName)
	def get_SubTypeNames(self): # String
		return self.get_query_params().get('SubTypeNames')

	def set_SubTypeNames(self, SubTypeNames):  # String
		self.add_query_param('SubTypeNames', SubTypeNames)
	def get_Uuids(self): # String
		return self.get_query_params().get('Uuids')

	def set_Uuids(self, Uuids):  # String
		self.add_query_param('Uuids', Uuids)
