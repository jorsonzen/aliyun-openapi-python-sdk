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

class CreateWmBaseImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'CreateWmBaseImage')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_Scale(self): # Integer
		return self.get_body_params().get('Scale')

	def set_Scale(self, Scale):  # Integer
		self.add_body_params('Scale', Scale)
	def get_WmInfoUint(self): # String
		return self.get_body_params().get('WmInfoUint')

	def set_WmInfoUint(self, WmInfoUint):  # String
		self.add_body_params('WmInfoUint', WmInfoUint)
	def get_WmInfoSize(self): # Long
		return self.get_body_params().get('WmInfoSize')

	def set_WmInfoSize(self, WmInfoSize):  # Long
		self.add_body_params('WmInfoSize', WmInfoSize)
	def get_WmInfoBytesB64(self): # String
		return self.get_body_params().get('WmInfoBytesB64')

	def set_WmInfoBytesB64(self, WmInfoBytesB64):  # String
		self.add_body_params('WmInfoBytesB64', WmInfoBytesB64)
	def get_WmType(self): # String
		return self.get_body_params().get('WmType')

	def set_WmType(self, WmType):  # String
		self.add_body_params('WmType', WmType)
	def get_Width(self): # Integer
		return self.get_body_params().get('Width')

	def set_Width(self, Width):  # Integer
		self.add_body_params('Width', Width)
	def get_Opacity(self): # Integer
		return self.get_body_params().get('Opacity')

	def set_Opacity(self, Opacity):  # Integer
		self.add_body_params('Opacity', Opacity)
	def get_Height(self): # Integer
		return self.get_body_params().get('Height')

	def set_Height(self, Height):  # Integer
		self.add_body_params('Height', Height)
