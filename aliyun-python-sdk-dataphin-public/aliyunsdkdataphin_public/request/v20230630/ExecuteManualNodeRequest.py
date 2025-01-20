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
import json

class ExecuteManualNodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataphin-public', '2023-06-30', 'ExecuteManualNode')
		self.set_protocol_type('https')
		self.set_method('POST')

	def get_OpTenantId(self): # Long
		return self.get_query_params().get('OpTenantId')

	def set_OpTenantId(self, OpTenantId):  # Long
		self.add_query_param('OpTenantId', OpTenantId)
	def get_ExecuteCommand(self): # Struct
		return self.get_body_params().get('ExecuteCommand')

	def set_ExecuteCommand(self, ExecuteCommand):  # Struct
		self.add_body_params("ExecuteCommand", json.dumps(ExecuteCommand))
	def get_Env(self): # String
		return self.get_query_params().get('Env')

	def set_Env(self, Env):  # String
		self.add_query_param('Env', Env)
