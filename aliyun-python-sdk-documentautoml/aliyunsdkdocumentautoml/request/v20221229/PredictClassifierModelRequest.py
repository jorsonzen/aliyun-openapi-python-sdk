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

class PredictClassifierModelRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'documentAutoml', '2022-12-29', 'PredictClassifierModel','documentAutoml')
		self.set_method('POST')

	def get_body(self): # String
		return self.get_body_params().get('body')

	def set_body(self, body):  # String
		self.add_body_params('body', body)
	def get_Content(self): # String
		return self.get_query_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_query_param('Content', Content)
	def get_ClassifierId(self): # Long
		return self.get_query_params().get('ClassifierId')

	def set_ClassifierId(self, ClassifierId):  # Long
		self.add_query_param('ClassifierId', ClassifierId)
	def get_AutoPrediction(self): # Boolean
		return self.get_query_params().get('AutoPrediction')

	def set_AutoPrediction(self, AutoPrediction):  # Boolean
		self.add_query_param('AutoPrediction', AutoPrediction)
