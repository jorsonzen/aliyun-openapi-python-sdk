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
from aliyunsdklinkvisual.endpoint import endpoint_data

class QueryRecordDownloadUrlRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Linkvisual', '2018-01-20', 'QueryRecordDownloadUrl','Linkvisual')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_IotId(self): # String
		return self.get_query_params().get('IotId')

	def set_IotId(self, IotId):  # String
		self.add_query_param('IotId', IotId)
	def get_IotInstanceId(self): # String
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self, IotInstanceId):  # String
		self.add_query_param('IotInstanceId', IotInstanceId)
	def get_ProductKey(self): # String
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self, ProductKey):  # String
		self.add_query_param('ProductKey', ProductKey)
	def get_FileName(self): # String
		return self.get_query_params().get('FileName')

	def set_FileName(self, FileName):  # String
		self.add_query_param('FileName', FileName)
	def get_DeviceName(self): # String
		return self.get_query_params().get('DeviceName')

	def set_DeviceName(self, DeviceName):  # String
		self.add_query_param('DeviceName', DeviceName)
