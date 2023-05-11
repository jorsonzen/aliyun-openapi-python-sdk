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

class QueryDevicePictureFileRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Linkvisual', '2018-01-20', 'QueryDevicePictureFile','Linkvisual')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PictureType(self): # Integer
		return self.get_query_params().get('PictureType')

	def set_PictureType(self, PictureType):  # Integer
		self.add_query_param('PictureType', PictureType)
	def get_ThumbWidth(self): # Integer
		return self.get_query_params().get('ThumbWidth')

	def set_ThumbWidth(self, ThumbWidth):  # Integer
		self.add_query_param('ThumbWidth', ThumbWidth)
	def get_IotId(self): # String
		return self.get_query_params().get('IotId')

	def set_IotId(self, IotId):  # String
		self.add_query_param('IotId', IotId)
	def get_IotInstanceId(self): # String
		return self.get_query_params().get('IotInstanceId')

	def set_IotInstanceId(self, IotInstanceId):  # String
		self.add_query_param('IotInstanceId', IotInstanceId)
	def get_ExpireTime(self): # Integer
		return self.get_query_params().get('ExpireTime')

	def set_ExpireTime(self, ExpireTime):  # Integer
		self.add_query_param('ExpireTime', ExpireTime)
	def get_ProductKey(self): # String
		return self.get_query_params().get('ProductKey')

	def set_ProductKey(self, ProductKey):  # String
		self.add_query_param('ProductKey', ProductKey)
	def get_DeviceName(self): # String
		return self.get_query_params().get('DeviceName')

	def set_DeviceName(self, DeviceName):  # String
		self.add_query_param('DeviceName', DeviceName)
	def get_CaptureId(self): # String
		return self.get_query_params().get('CaptureId')

	def set_CaptureId(self, CaptureId):  # String
		self.add_query_param('CaptureId', CaptureId)
