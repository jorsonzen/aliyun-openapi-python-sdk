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
from aliyunsdkiot.endpoint import endpoint_data

class CreateEdgeDriverRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Iot', '2018-01-20', 'CreateEdgeDriver')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DriverProtocol(self):
		return self.get_query_params().get('DriverProtocol')

	def set_DriverProtocol(self,DriverProtocol):
		self.add_query_param('DriverProtocol',DriverProtocol)

	def get_DriverName(self):
		return self.get_query_params().get('DriverName')

	def set_DriverName(self,DriverName):
		self.add_query_param('DriverName',DriverName)

	def get_IsBuiltIn(self):
		return self.get_query_params().get('IsBuiltIn')

	def set_IsBuiltIn(self,IsBuiltIn):
		self.add_query_param('IsBuiltIn',IsBuiltIn)

	def get_IotInstanceId(self):
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self,IotInstanceId):
		self.add_query_param('IotInstanceId',IotInstanceId)

	def get_Runtime(self):
		return self.get_query_params().get('Runtime')

	def set_Runtime(self,Runtime):
		self.add_query_param('Runtime',Runtime)

	def get_CpuArch(self):
		return self.get_query_params().get('CpuArch')

	def set_CpuArch(self,CpuArch):
		self.add_query_param('CpuArch',CpuArch)