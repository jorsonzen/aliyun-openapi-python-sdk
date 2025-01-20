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
from aliyunsdkpolardbx.endpoint import endpoint_data

class CreateDBRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'polardbx', '2020-02-02', 'CreateDB','polardbx')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DBInstanceName(self): # String
		return self.get_query_params().get('DBInstanceName')

	def set_DBInstanceName(self, DBInstanceName):  # String
		self.add_query_param('DBInstanceName', DBInstanceName)
	def get_Charset(self): # String
		return self.get_query_params().get('Charset')

	def set_Charset(self, Charset):  # String
		self.add_query_param('Charset', Charset)
	def get_SecurityAccountPassword(self): # String
		return self.get_query_params().get('SecurityAccountPassword')

	def set_SecurityAccountPassword(self, SecurityAccountPassword):  # String
		self.add_query_param('SecurityAccountPassword', SecurityAccountPassword)
	def get_AccountPrivilege(self): # String
		return self.get_query_params().get('AccountPrivilege')

	def set_AccountPrivilege(self, AccountPrivilege):  # String
		self.add_query_param('AccountPrivilege', AccountPrivilege)
	def get_Mode(self): # String
		return self.get_query_params().get('Mode')

	def set_Mode(self, Mode):  # String
		self.add_query_param('Mode', Mode)
	def get_AccountName(self): # String
		return self.get_query_params().get('AccountName')

	def set_AccountName(self, AccountName):  # String
		self.add_query_param('AccountName', AccountName)
	def get_SecurityAccountName(self): # String
		return self.get_query_params().get('SecurityAccountName')

	def set_SecurityAccountName(self, SecurityAccountName):  # String
		self.add_query_param('SecurityAccountName', SecurityAccountName)
	def get_DbDescription(self): # String
		return self.get_query_params().get('DbDescription')

	def set_DbDescription(self, DbDescription):  # String
		self.add_query_param('DbDescription', DbDescription)
	def get_DbName(self): # String
		return self.get_query_params().get('DbName')

	def set_DbName(self, DbName):  # String
		self.add_query_param('DbName', DbName)
	def get_StoragePoolName(self): # String
		return self.get_query_params().get('StoragePoolName')

	def set_StoragePoolName(self, StoragePoolName):  # String
		self.add_query_param('StoragePoolName', StoragePoolName)
