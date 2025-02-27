# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from abc import ABC, abstractmethod
from typing import Any

from datafusion.common import SqlTable


class BaseInputSource(ABC):
    """
    If a consuming library would like to provider their own InputSource
    this is the class they should extend to write their own. Once
    completed the Plugin InputSource can be registered with the
    SessionContext to ensure that it will be used in order
    to obtain the SqlTable information from the custom datasource.
    """

    @abstractmethod
    def is_correct_input(
        self, input_item: Any, table_name: str, **kwargs
    ) -> bool:
        pass

    @abstractmethod
    def build_table(
        self, input_item: Any, table_name: str, **kwarg
    ) -> SqlTable:
        pass
