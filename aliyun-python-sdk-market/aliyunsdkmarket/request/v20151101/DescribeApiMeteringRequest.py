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
from aliyunsdkmarket.endpoint import endpoint_data

class DescribeApiMeteringRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Market', '2015-11-01', 'DescribeApiMetering','yunmarket')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_productCode(self): # String
		return self.get_query_params().get('productCode')

	def set_productCode(self, productCode):  # String
		self.add_query_param('productCode', productCode)
	def get_type(self): # Integer
		return self.get_query_params().get('type')

	def set_type(self, type):  # Integer
		self.add_query_param('type', type)
	def get_pageNum(self): # Integer
		return self.get_query_params().get('pageNum')

	def set_pageNum(self, pageNum):  # Integer
		self.add_query_param('pageNum', pageNum)
