# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ApplyComputeQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ApplyComputeQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyComputeQuotaPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyComputeQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateComputeQuotaPlanRequestQuotaParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
    ):
        # The value of elastic Reserved CUs in the level-1 quota.
        # > The default value is 0. The maximum value of this parameter must be equal to the number of subscription-based reserved CUs and cannot exceed 10,000 CUs.
        # 
        # This parameter is required.
        self.elastic_reserved_cu = elastic_reserved_cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        return self


class CreateComputeQuotaPlanRequestQuotaSubQuotaInfoListParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        max_cu: int = None,
        min_cu: int = None,
    ):
        # The value of elastic Reserved CUs.
        # > The total number of elastically reserved CUs in all the level-2 quotas is equal to the number of elastically reserved CUs in the level-1 quota.
        # 
        # This parameter is required.
        self.elastic_reserved_cu = elastic_reserved_cu
        # The value of maxCU in Reserved CUs.
        # > The value of maxCU must be less than or equal to the value of maxCU in the level-1 quota that you purchased.
        # 
        # This parameter is required.
        self.max_cu = max_cu
        # The value of minCU in Reserved CUs.
        # > 
        # >- The total value of minCU in all the level-2 quotas is equal to the value of minCU in the level-1 quota.
        # >- The value of minCU must be less than or equal to the value of maxCU in the level-2 quota and less than or equal to the value of minCU in the level-1 quota that you purchased.
        # 
        # This parameter is required.
        self.min_cu = min_cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        if self.max_cu is not None:
            result['maxCU'] = self.max_cu
        if self.min_cu is not None:
            result['minCU'] = self.min_cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')
        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')
        return self


class CreateComputeQuotaPlanRequestQuotaSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        parameter: CreateComputeQuotaPlanRequestQuotaSubQuotaInfoListParameter = None,
    ):
        # The nickname of the level-2 quota.
        # 
        # This parameter is required.
        self.nick_name = nick_name
        # The parameters of the level-2 quota.
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            temp_model = CreateComputeQuotaPlanRequestQuotaSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        return self


class CreateComputeQuotaPlanRequestQuota(TeaModel):
    def __init__(
        self,
        parameter: CreateComputeQuotaPlanRequestQuotaParameter = None,
        sub_quota_info_list: List[CreateComputeQuotaPlanRequestQuotaSubQuotaInfoList] = None,
    ):
        # The parameters of level-1 quota.
        self.parameter = parameter
        # The list of level-2 quotas.
        self.sub_quota_info_list = sub_quota_info_list

    def validate(self):
        if self.parameter:
            self.parameter.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameter') is not None:
            temp_model = CreateComputeQuotaPlanRequestQuotaParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = CreateComputeQuotaPlanRequestQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        return self


class CreateComputeQuotaPlanRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        quota: CreateComputeQuotaPlanRequestQuota = None,
    ):
        # The name of quota plan.
        # 
        # This parameter is required.
        self.name = name
        # The parameters of quota plan.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = CreateComputeQuotaPlanRequestQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class CreateComputeQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateComputeQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateComputeQuotaPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateComputeQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMmsDataSourceRequest(TeaModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        name: str = None,
        networklink: str = None,
        type: str = None,
    ):
        self.config = config
        self.name = name
        self.networklink = networklink
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.name is not None:
            result['name'] = self.name
        if self.networklink is not None:
            result['networklink'] = self.networklink
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networklink') is not None:
            self.networklink = m.get('networklink')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateMmsDataSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        data_source_id: int = None,
    ):
        self.data_source_id = data_source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        return self


class CreateMmsDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateMmsDataSourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateMmsDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateMmsDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMmsDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMmsDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMmsFetchMetadataJobResponseBodyData(TeaModel):
    def __init__(
        self,
        scan_id: int = None,
    ):
        self.scan_id = scan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scan_id is not None:
            result['scanId'] = self.scan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scanId') is not None:
            self.scan_id = m.get('scanId')
        return self


class CreateMmsFetchMetadataJobResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateMmsFetchMetadataJobResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateMmsFetchMetadataJobResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateMmsFetchMetadataJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMmsFetchMetadataJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMmsFetchMetadataJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMmsJobRequest(TeaModel):
    def __init__(
        self,
        column_mapping: Dict[str, str] = None,
        dst_db_name: str = None,
        dst_schema_name: str = None,
        enable_verification: bool = None,
        eta: str = None,
        increment: bool = None,
        name: str = None,
        others: Dict[str, Any] = None,
        partition_filters: Dict[str, str] = None,
        partitions: List[int] = None,
        schema_only: bool = None,
        source_id: int = None,
        source_name: str = None,
        src_db_name: str = None,
        src_schema_name: str = None,
        table_black_list: List[str] = None,
        table_mapping: Dict[str, str] = None,
        table_white_list: List[str] = None,
        tables: List[str] = None,
        task_type: str = None,
    ):
        self.column_mapping = column_mapping
        self.dst_db_name = dst_db_name
        self.dst_schema_name = dst_schema_name
        self.enable_verification = enable_verification
        self.eta = eta
        self.increment = increment
        self.name = name
        self.others = others
        self.partition_filters = partition_filters
        self.partitions = partitions
        self.schema_only = schema_only
        self.source_id = source_id
        self.source_name = source_name
        self.src_db_name = src_db_name
        self.src_schema_name = src_schema_name
        self.table_black_list = table_black_list
        self.table_mapping = table_mapping
        self.table_white_list = table_white_list
        self.tables = tables
        # MOCK, HIVE: hive udtf task, HIVE_DATAX: hive datax task, COPY_TASK: odps Copy Task, ODPS_INSERT_OVERWRITE: odps simple insert overwrite task, MC2MC_VERIFY, OSS, HIVE_OSS
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_mapping is not None:
            result['columnMapping'] = self.column_mapping
        if self.dst_db_name is not None:
            result['dstDbName'] = self.dst_db_name
        if self.dst_schema_name is not None:
            result['dstSchemaName'] = self.dst_schema_name
        if self.enable_verification is not None:
            result['enableVerification'] = self.enable_verification
        if self.eta is not None:
            result['eta'] = self.eta
        if self.increment is not None:
            result['increment'] = self.increment
        if self.name is not None:
            result['name'] = self.name
        if self.others is not None:
            result['others'] = self.others
        if self.partition_filters is not None:
            result['partitionFilters'] = self.partition_filters
        if self.partitions is not None:
            result['partitions'] = self.partitions
        if self.schema_only is not None:
            result['schemaOnly'] = self.schema_only
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name
        if self.src_schema_name is not None:
            result['srcSchemaName'] = self.src_schema_name
        if self.table_black_list is not None:
            result['tableBlackList'] = self.table_black_list
        if self.table_mapping is not None:
            result['tableMapping'] = self.table_mapping
        if self.table_white_list is not None:
            result['tableWhiteList'] = self.table_white_list
        if self.tables is not None:
            result['tables'] = self.tables
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnMapping') is not None:
            self.column_mapping = m.get('columnMapping')
        if m.get('dstDbName') is not None:
            self.dst_db_name = m.get('dstDbName')
        if m.get('dstSchemaName') is not None:
            self.dst_schema_name = m.get('dstSchemaName')
        if m.get('enableVerification') is not None:
            self.enable_verification = m.get('enableVerification')
        if m.get('eta') is not None:
            self.eta = m.get('eta')
        if m.get('increment') is not None:
            self.increment = m.get('increment')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('others') is not None:
            self.others = m.get('others')
        if m.get('partitionFilters') is not None:
            self.partition_filters = m.get('partitionFilters')
        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')
        if m.get('schemaOnly') is not None:
            self.schema_only = m.get('schemaOnly')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')
        if m.get('srcSchemaName') is not None:
            self.src_schema_name = m.get('srcSchemaName')
        if m.get('tableBlackList') is not None:
            self.table_black_list = m.get('tableBlackList')
        if m.get('tableMapping') is not None:
            self.table_mapping = m.get('tableMapping')
        if m.get('tableWhiteList') is not None:
            self.table_white_list = m.get('tableWhiteList')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class CreateMmsJobResponseBodyData(TeaModel):
    def __init__(
        self,
        async_task_id: int = None,
    ):
        self.async_task_id = async_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['asyncTaskId'] = self.async_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncTaskId') is not None:
            self.async_task_id = m.get('asyncTaskId')
        return self


class CreateMmsJobResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateMmsJobResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateMmsJobResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateMmsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMmsJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMmsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePackageRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        is_install: bool = None,
    ):
        # The request body parameters.
        self.body = body
        # Specifies whether to install the package.
        self.is_install = is_install

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.is_install is not None:
            result['isInstall'] = self.is_install
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('isInstall') is not None:
            self.is_install = m.get('isInstall')
        return self


class CreatePackageResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreatePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The request body parameters.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQuotaPlanRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class CreateQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateQuotaPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoleRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The request body parameters. For valid values, see [MaxCompute permissions](https://help.aliyun.com/document_detail/27935.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateRoleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteComputeQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteComputeQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteComputeQuotaPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteComputeQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMmsDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteMmsDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMmsDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteMmsDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMmsJobResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteMmsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMmsJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteMmsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQuotaPlanRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        tenant_id: str = None,
    ):
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class DeleteQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteQuotaPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComputeEffectivePlanResponseBodyDataQuotaSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        region_id: str = None,
        status: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The nickname of the level-2 quota.
        self.nick_name = nick_name
        # The description of the level-2 quota.
        self.parameter = parameter
        # The region ID.
        self.region_id = region_id
        # Resource status.
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of quota.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetComputeEffectivePlanResponseBodyDataQuota(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        region_id: str = None,
        status: str = None,
        sub_quota_info_list: List[GetComputeEffectivePlanResponseBodyDataQuotaSubQuotaInfoList] = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the level-1 quota was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-1 quota.
        self.id = id
        # The name of the level-1 quota.
        self.name = name
        # The nickname of the level-1 quota.
        self.nick_name = nick_name
        # The description of the level-2 quota.
        self.parameter = parameter
        # The region ID.
        self.region_id = region_id
        # The status of the resource.
        self.status = status
        # The list of subquotas.
        self.sub_quota_info_list = sub_quota_info_list
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of quota.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = GetComputeEffectivePlanResponseBodyDataQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetComputeEffectivePlanResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        is_effective: bool = None,
        name: str = None,
        quota: GetComputeEffectivePlanResponseBodyDataQuota = None,
    ):
        # The time when the quota plan was created.
        self.create_time = create_time
        # Whether it is currently effective.
        # > A Quota plan that has taken effect cannot be deleted, i.e., isEffective=true
        self.is_effective = is_effective
        # The name of the quota plan.
        self.name = name
        # The details of the quota.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.is_effective is not None:
            result['isEffective'] = self.is_effective
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('isEffective') is not None:
            self.is_effective = m.get('isEffective')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = GetComputeEffectivePlanResponseBodyDataQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class GetComputeEffectivePlanResponseBody(TeaModel):
    def __init__(
        self,
        data: GetComputeEffectivePlanResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetComputeEffectivePlanResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetComputeEffectivePlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetComputeEffectivePlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetComputeEffectivePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComputeQuotaPlanResponseBodyDataQuotaParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        max_cu: int = None,
        min_cu: int = None,
    ):
        # The value of elastic Reserved CUs.
        self.elastic_reserved_cu = elastic_reserved_cu
        # The value of maxCU in Reserved CUs.
        self.max_cu = max_cu
        # The value of minCU in Reserved CUs.
        self.min_cu = min_cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        if self.max_cu is not None:
            result['maxCU'] = self.max_cu
        if self.min_cu is not None:
            result['minCU'] = self.min_cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')
        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')
        return self


class GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoListParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        enable_priority: bool = None,
        force_reserved_min: bool = None,
        max_cu: int = None,
        min_cu: int = None,
        scheduler_type: str = None,
        single_job_culimit: int = None,
    ):
        # The value of elastic Reserved CUs.
        self.elastic_reserved_cu = elastic_reserved_cu
        # whether to enable the priority feature.
        self.enable_priority = enable_priority
        # Whether it is exclusive.
        self.force_reserved_min = force_reserved_min
        # The value of maxCU in Reserved CUs.
        self.max_cu = max_cu
        # The value of minCU in Reserved CUs.
        self.min_cu = min_cu
        # Scheduling policy.
        self.scheduler_type = scheduler_type
        # The upper limit for CUs that can be concurrently used by a job scheduled to the quota.
        self.single_job_culimit = single_job_culimit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        if self.enable_priority is not None:
            result['enablePriority'] = self.enable_priority
        if self.force_reserved_min is not None:
            result['forceReservedMin'] = self.force_reserved_min
        if self.max_cu is not None:
            result['maxCU'] = self.max_cu
        if self.min_cu is not None:
            result['minCU'] = self.min_cu
        if self.scheduler_type is not None:
            result['schedulerType'] = self.scheduler_type
        if self.single_job_culimit is not None:
            result['singleJobCULimit'] = self.single_job_culimit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        if m.get('enablePriority') is not None:
            self.enable_priority = m.get('enablePriority')
        if m.get('forceReservedMin') is not None:
            self.force_reserved_min = m.get('forceReservedMin')
        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')
        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')
        if m.get('schedulerType') is not None:
            self.scheduler_type = m.get('schedulerType')
        if m.get('singleJobCULimit') is not None:
            self.single_job_culimit = m.get('singleJobCULimit')
        return self


class GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoListParameter = None,
        region_id: str = None,
        status: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # Cluster ID.
        self.cluster = cluster
        # Creation time.
        self.create_time = create_time
        # Creator cloud account UID.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The nickname of the level-2 quota.
        self.nick_name = nick_name
        # The parameters of the level-2 quota.
        self.parameter = parameter
        # Region ID.
        self.region_id = region_id
        # Resource status.
        self.status = status
        # Tenant ID.
        self.tenant_id = tenant_id
        # The type of quota.
        self.type = type
        # Version number.
        self.version = version

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            temp_model = GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetComputeQuotaPlanResponseBodyDataQuota(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: GetComputeQuotaPlanResponseBodyDataQuotaParameter = None,
        region_id: str = None,
        status: str = None,
        sub_quota_info_list: List[GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoList] = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # Cluster ID.
        self.cluster = cluster
        # Creation time.
        self.create_time = create_time
        # Creator\\"s cloud account UID.
        self.creator_id = creator_id
        # The ID of the level-1 quota.
        self.id = id
        # The name of the level-1 quota.
        self.name = name
        # The nickname of the level-1 quota.
        self.nick_name = nick_name
        # CU value parameters for the level-1 quota.
        self.parameter = parameter
        # Region ID.
        self.region_id = region_id
        # Resource status.
        self.status = status
        # The list of level-2 quotas.
        self.sub_quota_info_list = sub_quota_info_list
        # Tenant ID.
        self.tenant_id = tenant_id
        # Corresponds to the `resourceSystemType` field of the control cluster.
        self.type = type
        # Version number.
        self.version = version

    def validate(self):
        if self.parameter:
            self.parameter.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            temp_model = GetComputeQuotaPlanResponseBodyDataQuotaParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = GetComputeQuotaPlanResponseBodyDataQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetComputeQuotaPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        is_effective: bool = None,
        name: str = None,
        quota: GetComputeQuotaPlanResponseBodyDataQuota = None,
    ):
        # The time when the quota plan was created.
        self.create_time = create_time
        # Whether it is currently effective.
        # > 
        # > - A Quota plan that has taken effect cannot be deleted, i.e., isEffective=true
        self.is_effective = is_effective
        # The name of the quota plan.
        self.name = name
        # The details of the quota.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.is_effective is not None:
            result['isEffective'] = self.is_effective
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('isEffective') is not None:
            self.is_effective = m.get('isEffective')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = GetComputeQuotaPlanResponseBodyDataQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class GetComputeQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: GetComputeQuotaPlanResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetComputeQuotaPlanResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetComputeQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetComputeQuotaPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetComputeQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComputeQuotaScheduleRequest(TeaModel):
    def __init__(
        self,
        display_timezone: str = None,
    ):
        # Display time zone.
        self.display_timezone = display_timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_timezone is not None:
            result['displayTimezone'] = self.display_timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayTimezone') is not None:
            self.display_timezone = m.get('displayTimezone')
        return self


class GetComputeQuotaScheduleResponseBodyDataCondition(TeaModel):
    def __init__(
        self,
        at: str = None,
    ):
        # The start time when the quota plan takes effect.
        self.at = at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at is not None:
            result['at'] = self.at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('at') is not None:
            self.at = m.get('at')
        return self


class GetComputeQuotaScheduleResponseBodyData(TeaModel):
    def __init__(
        self,
        condition: GetComputeQuotaScheduleResponseBodyDataCondition = None,
        id: str = None,
        plan: str = None,
        timezone: str = None,
        type: str = None,
    ):
        # The value of effective condition.
        self.condition = condition
        # The ID of the quota plan.
        self.id = id
        # The name of the quota plan.
        self.plan = plan
        # The time zone property.
        self.timezone = timezone
        # The type of the quota plan.
        self.type = type

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.plan is not None:
            result['plan'] = self.plan
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            temp_model = GetComputeQuotaScheduleResponseBodyDataCondition()
            self.condition = temp_model.from_map(m['condition'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('plan') is not None:
            self.plan = m.get('plan')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetComputeQuotaScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetComputeQuotaScheduleResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetComputeQuotaScheduleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetComputeQuotaScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetComputeQuotaScheduleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetComputeQuotaScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobInfoResponseBodyDataJobSubStatusList(TeaModel):
    def __init__(
        self,
        code: int = None,
        description: str = None,
        start_time: str = None,
    ):
        # The encoding of the substatus.
        self.code = code
        # The description of the substatus.
        self.description = description
        # The start time of the substatus.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class GetJobInfoResponseBodyDataSceneResults(TeaModel):
    def __init__(
        self,
        description: str = None,
        params: Dict[str, str] = None,
        scene: str = None,
        scene_tag: str = None,
        summary: str = None,
        type: str = None,
    ):
        # The intelligent diagnostics result description.
        self.description = description
        # Information about the nodes where data skew or data expansion is detected. This parameter is returned only when the diagnostics scenario is data skew or data expansion.
        self.params = params
        # The intelligent diagnostics result scenario.
        self.scene = scene
        # The intelligent diagnostics result tag.
        self.scene_tag = scene_tag
        # The intelligent diagnostics result summary.
        self.summary = summary
        # The intelligent diagnostics result type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.params is not None:
            result['params'] = self.params
        if self.scene is not None:
            result['scene'] = self.scene
        if self.scene_tag is not None:
            result['sceneTag'] = self.scene_tag
        if self.summary is not None:
            result['summary'] = self.summary
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sceneTag') is not None:
            self.scene_tag = m.get('sceneTag')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetJobInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        cu_usage: int = None,
        end_at_time: int = None,
        ext_node_id: str = None,
        ext_node_on_duty: str = None,
        ext_plant_from: str = None,
        input_bytes: float = None,
        instance_id: str = None,
        job_owner: str = None,
        job_sub_status_list: List[GetJobInfoResponseBodyDataJobSubStatusList] = None,
        job_type: str = None,
        memory_usage: int = None,
        priority: int = None,
        project: str = None,
        quota_nickname: str = None,
        quota_type: str = None,
        region: str = None,
        running_at_time: int = None,
        running_time: int = None,
        scene_results: List[GetJobInfoResponseBodyDataSceneResults] = None,
        signature: str = None,
        status: str = None,
        submitted_at_time: int = None,
        tenant_id: str = None,
        total_time: int = None,
        waiting_time: int = None,
    ):
        # The amount of resources consumed by the job. This parameter is returned only for jobs that are complete.Unit: 100\\*Core\\*s.
        self.cu_usage = cu_usage
        # The end time of the job.
        self.end_at_time = end_at_time
        # The ID of the ancestor node.
        self.ext_node_id = ext_node_id
        # The Alibaba Cloud account ID of the task owner.
        self.ext_node_on_duty = ext_node_on_duty
        # The upstream platform.
        self.ext_plant_from = ext_plant_from
        # The amount of data scanned by the job.
        self.input_bytes = input_bytes
        # The job ID.
        self.instance_id = instance_id
        # The owner of the job.
        self.job_owner = job_owner
        # The substatuses of the job lifecycle.
        self.job_sub_status_list = job_sub_status_list
        # The type of the job.
        self.job_type = job_type
        # The number of memory consumed by the job. This parameter is returned only for jobs that are complete.Unit: MB\\*s.
        self.memory_usage = memory_usage
        # The priority of the job.
        self.priority = priority
        # The project name.
        self.project = project
        # The nickname of the computing quota that is used by the job.
        self.quota_nickname = quota_nickname
        # The quota type.
        self.quota_type = quota_type
        # The region ID.
        self.region = region
        # The start time, which is the time when the job received the first batch of computing resources. For jobs that run for a short period of time or do not consume computing resources, such as the jobs that involve DDL statements, the job submission time is used instead.
        self.running_at_time = running_at_time
        # The execution duration, which is the duration from the start time to the end time of the job.
        self.running_time = running_time
        # The intelligent diagnostics result.
        self.scene_results = scene_results
        # The signature of the SQL job. You can use the signature to find the instances on which each time an SQL statement is executed.
        self.signature = signature
        # The job status.
        self.status = status
        # The time when the job was submitted.
        self.submitted_at_time = submitted_at_time
        # The tenant ID.
        self.tenant_id = tenant_id
        # The total duration from the time a job is submitted to the time the job is terminated.
        self.total_time = total_time
        # The wait time, which is the duration from the time the job is submitted to the time the job starts to run.
        self.waiting_time = waiting_time

    def validate(self):
        if self.job_sub_status_list:
            for k in self.job_sub_status_list:
                if k:
                    k.validate()
        if self.scene_results:
            for k in self.scene_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_usage is not None:
            result['cuUsage'] = self.cu_usage
        if self.end_at_time is not None:
            result['endAtTime'] = self.end_at_time
        if self.ext_node_id is not None:
            result['extNodeId'] = self.ext_node_id
        if self.ext_node_on_duty is not None:
            result['extNodeOnDuty'] = self.ext_node_on_duty
        if self.ext_plant_from is not None:
            result['extPlantFrom'] = self.ext_plant_from
        if self.input_bytes is not None:
            result['inputBytes'] = self.input_bytes
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner
        result['jobSubStatusList'] = []
        if self.job_sub_status_list is not None:
            for k in self.job_sub_status_list:
                result['jobSubStatusList'].append(k.to_map() if k else None)
        if self.job_type is not None:
            result['jobType'] = self.job_type
        if self.memory_usage is not None:
            result['memoryUsage'] = self.memory_usage
        if self.priority is not None:
            result['priority'] = self.priority
        if self.project is not None:
            result['project'] = self.project
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        if self.quota_type is not None:
            result['quotaType'] = self.quota_type
        if self.region is not None:
            result['region'] = self.region
        if self.running_at_time is not None:
            result['runningAtTime'] = self.running_at_time
        if self.running_time is not None:
            result['runningTime'] = self.running_time
        result['sceneResults'] = []
        if self.scene_results is not None:
            for k in self.scene_results:
                result['sceneResults'].append(k.to_map() if k else None)
        if self.signature is not None:
            result['signature'] = self.signature
        if self.status is not None:
            result['status'] = self.status
        if self.submitted_at_time is not None:
            result['submittedAtTime'] = self.submitted_at_time
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.total_time is not None:
            result['totalTime'] = self.total_time
        if self.waiting_time is not None:
            result['waitingTime'] = self.waiting_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuUsage') is not None:
            self.cu_usage = m.get('cuUsage')
        if m.get('endAtTime') is not None:
            self.end_at_time = m.get('endAtTime')
        if m.get('extNodeId') is not None:
            self.ext_node_id = m.get('extNodeId')
        if m.get('extNodeOnDuty') is not None:
            self.ext_node_on_duty = m.get('extNodeOnDuty')
        if m.get('extPlantFrom') is not None:
            self.ext_plant_from = m.get('extPlantFrom')
        if m.get('inputBytes') is not None:
            self.input_bytes = m.get('inputBytes')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')
        self.job_sub_status_list = []
        if m.get('jobSubStatusList') is not None:
            for k in m.get('jobSubStatusList'):
                temp_model = GetJobInfoResponseBodyDataJobSubStatusList()
                self.job_sub_status_list.append(temp_model.from_map(k))
        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')
        if m.get('memoryUsage') is not None:
            self.memory_usage = m.get('memoryUsage')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        if m.get('quotaType') is not None:
            self.quota_type = m.get('quotaType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('runningAtTime') is not None:
            self.running_at_time = m.get('runningAtTime')
        if m.get('runningTime') is not None:
            self.running_time = m.get('runningTime')
        self.scene_results = []
        if m.get('sceneResults') is not None:
            for k in m.get('sceneResults'):
                temp_model = GetJobInfoResponseBodyDataSceneResults()
                self.scene_results.append(temp_model.from_map(k))
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('submittedAtTime') is not None:
            self.submitted_at_time = m.get('submittedAtTime')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('totalTime') is not None:
            self.total_time = m.get('totalTime')
        if m.get('waitingTime') is not None:
            self.waiting_time = m.get('waitingTime')
        return self


class GetJobInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: GetJobInfoResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # *   1xx: informational response. The request is received and is being processed.
        # *   2xx: success. The request is successfully received, understood, and accepted by the server.
        # *   3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # *   4xx: client error. The request contains invalid request parameters and syntaxes, or specific request conditions cannot be met.
        # *   5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetJobInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetJobInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobResourceUsageRequest(TeaModel):
    def __init__(
        self,
        date: str = None,
        job_owner_list: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        quota_nickname_list: List[str] = None,
    ):
        # The date that is accurate to the day part for the query. The date must be in the yyyy-MM-dd format.
        # 
        # This parameter is required.
        self.date = date
        # The list of job executors.
        self.job_owner_list = job_owner_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The list of nicknames of quotas that are used by jobs.
        self.quota_nickname_list = quota_nickname_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.job_owner_list is not None:
            result['jobOwnerList'] = self.job_owner_list
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.quota_nickname_list is not None:
            result['quotaNicknameList'] = self.quota_nickname_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('jobOwnerList') is not None:
            self.job_owner_list = m.get('jobOwnerList')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('quotaNicknameList') is not None:
            self.quota_nickname_list = m.get('quotaNicknameList')
        return self


class GetJobResourceUsageShrinkRequest(TeaModel):
    def __init__(
        self,
        date: str = None,
        job_owner_list_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        quota_nickname_list_shrink: str = None,
    ):
        # The date that is accurate to the day part for the query. The date must be in the yyyy-MM-dd format.
        # 
        # This parameter is required.
        self.date = date
        # The list of job executors.
        self.job_owner_list_shrink = job_owner_list_shrink
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The list of nicknames of quotas that are used by jobs.
        self.quota_nickname_list_shrink = quota_nickname_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.job_owner_list_shrink is not None:
            result['jobOwnerList'] = self.job_owner_list_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.quota_nickname_list_shrink is not None:
            result['quotaNicknameList'] = self.quota_nickname_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('jobOwnerList') is not None:
            self.job_owner_list_shrink = m.get('jobOwnerList')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('quotaNicknameList') is not None:
            self.quota_nickname_list_shrink = m.get('quotaNicknameList')
        return self


class GetJobResourceUsageResponseBodyDataJobResourceUsageList(TeaModel):
    def __init__(
        self,
        cu_usage: int = None,
        date: str = None,
        job_owner: str = None,
        memory_usage: int = None,
        quota_nickname: str = None,
    ):
        # The total number of used compute units (CUs).
        self.cu_usage = cu_usage
        # The start date of the query in the format of yyyy-MM-dd.
        self.date = date
        # The job executor.
        self.job_owner = job_owner
        # The total memory usage.
        self.memory_usage = memory_usage
        # The quota nickname.
        self.quota_nickname = quota_nickname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_usage is not None:
            result['cuUsage'] = self.cu_usage
        if self.date is not None:
            result['date'] = self.date
        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner
        if self.memory_usage is not None:
            result['memoryUsage'] = self.memory_usage
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuUsage') is not None:
            self.cu_usage = m.get('cuUsage')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')
        if m.get('memoryUsage') is not None:
            self.memory_usage = m.get('memoryUsage')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        return self


class GetJobResourceUsageResponseBodyData(TeaModel):
    def __init__(
        self,
        job_resource_usage_list: List[GetJobResourceUsageResponseBodyDataJobResourceUsageList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The data list returned.
        self.job_resource_usage_list = job_resource_usage_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.job_resource_usage_list:
            for k in self.job_resource_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['jobResourceUsageList'] = []
        if self.job_resource_usage_list is not None:
            for k in self.job_resource_usage_list:
                result['jobResourceUsageList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_resource_usage_list = []
        if m.get('jobResourceUsageList') is not None:
            for k in m.get('jobResourceUsageList'):
                temp_model = GetJobResourceUsageResponseBodyDataJobResourceUsageList()
                self.job_resource_usage_list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetJobResourceUsageResponseBody(TeaModel):
    def __init__(
        self,
        data: GetJobResourceUsageResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_msg = error_msg
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetJobResourceUsageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetJobResourceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResourceUsageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobResourceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMmsAsyncTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        error_msg: str = None,
        id: int = None,
        object_id: int = None,
        progress: int = None,
        result: str = None,
        running: bool = None,
        source_id: int = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.end_time = end_time
        self.error_msg = error_msg
        self.id = id
        self.object_id = object_id
        self.progress = progress
        self.result = result
        self.running = running
        self.source_id = source_id
        self.start_time = start_time
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.id is not None:
            result['id'] = self.id
        if self.object_id is not None:
            result['objectId'] = self.object_id
        if self.progress is not None:
            result['progress'] = self.progress
        if self.result is not None:
            result['result'] = self.result
        if self.running is not None:
            result['running'] = self.running
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('running') is not None:
            self.running = m.get('running')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetMmsAsyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: GetMmsAsyncTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetMmsAsyncTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetMmsAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMmsAsyncTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMmsAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMmsDataSourceRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        with_config: bool = None,
    ):
        self.lang = lang
        self.with_config = with_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['lang'] = self.lang
        if self.with_config is not None:
            result['withConfig'] = self.with_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('withConfig') is not None:
            self.with_config = m.get('withConfig')
        return self


class GetMmsDataSourceResponseBodyDataConfig(TeaModel):
    def __init__(
        self,
        desc: str = None,
        enums: List[str] = None,
        group: str = None,
        key: str = None,
        name: str = None,
        place_holder: str = None,
        required: bool = None,
        sub_type: str = None,
        type: str = None,
        value: Any = None,
    ):
        self.desc = desc
        self.enums = enums
        self.group = group
        self.key = key
        self.name = name
        self.place_holder = place_holder
        self.required = required
        self.sub_type = sub_type
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.enums is not None:
            result['enums'] = self.enums
        if self.group is not None:
            result['group'] = self.group
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        if self.place_holder is not None:
            result['placeHolder'] = self.place_holder
        if self.required is not None:
            result['required'] = self.required
        if self.sub_type is not None:
            result['subType'] = self.sub_type
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('enums') is not None:
            self.enums = m.get('enums')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('placeHolder') is not None:
            self.place_holder = m.get('placeHolder')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('subType') is not None:
            self.sub_type = m.get('subType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetMmsDataSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        agent_is_online: bool = None,
        config: List[GetMmsDataSourceResponseBodyDataConfig] = None,
        create_time: str = None,
        db_num: int = None,
        err_msg: str = None,
        id: int = None,
        last_update_time: str = None,
        name: str = None,
        networklink: str = None,
        partition_num: int = None,
        partitions_doing_num: int = None,
        partitions_done_num: int = None,
        partitions_failed_num: int = None,
        region: str = None,
        scan_id: int = None,
        status: str = None,
        table_num: int = None,
        tables_doing_num: int = None,
        tables_done_num: int = None,
        tables_failed_num: int = None,
        tables_part_done_num: int = None,
        type: str = None,
    ):
        self.agent_is_online = agent_is_online
        self.config = config
        self.create_time = create_time
        self.db_num = db_num
        self.err_msg = err_msg
        self.id = id
        self.last_update_time = last_update_time
        self.name = name
        self.networklink = networklink
        self.partition_num = partition_num
        self.partitions_doing_num = partitions_doing_num
        self.partitions_done_num = partitions_done_num
        self.partitions_failed_num = partitions_failed_num
        self.region = region
        self.scan_id = scan_id
        self.status = status
        self.table_num = table_num
        self.tables_doing_num = tables_doing_num
        self.tables_done_num = tables_done_num
        self.tables_failed_num = tables_failed_num
        self.tables_part_done_num = tables_part_done_num
        self.type = type

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_is_online is not None:
            result['agentIsOnline'] = self.agent_is_online
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.db_num is not None:
            result['dbNum'] = self.db_num
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.id is not None:
            result['id'] = self.id
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.name is not None:
            result['name'] = self.name
        if self.networklink is not None:
            result['networklink'] = self.networklink
        if self.partition_num is not None:
            result['partitionNum'] = self.partition_num
        if self.partitions_doing_num is not None:
            result['partitionsDoingNum'] = self.partitions_doing_num
        if self.partitions_done_num is not None:
            result['partitionsDoneNum'] = self.partitions_done_num
        if self.partitions_failed_num is not None:
            result['partitionsFailedNum'] = self.partitions_failed_num
        if self.region is not None:
            result['region'] = self.region
        if self.scan_id is not None:
            result['scanId'] = self.scan_id
        if self.status is not None:
            result['status'] = self.status
        if self.table_num is not None:
            result['tableNum'] = self.table_num
        if self.tables_doing_num is not None:
            result['tablesDoingNum'] = self.tables_doing_num
        if self.tables_done_num is not None:
            result['tablesDoneNum'] = self.tables_done_num
        if self.tables_failed_num is not None:
            result['tablesFailedNum'] = self.tables_failed_num
        if self.tables_part_done_num is not None:
            result['tablesPartDoneNum'] = self.tables_part_done_num
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentIsOnline') is not None:
            self.agent_is_online = m.get('agentIsOnline')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = GetMmsDataSourceResponseBodyDataConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dbNum') is not None:
            self.db_num = m.get('dbNum')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networklink') is not None:
            self.networklink = m.get('networklink')
        if m.get('partitionNum') is not None:
            self.partition_num = m.get('partitionNum')
        if m.get('partitionsDoingNum') is not None:
            self.partitions_doing_num = m.get('partitionsDoingNum')
        if m.get('partitionsDoneNum') is not None:
            self.partitions_done_num = m.get('partitionsDoneNum')
        if m.get('partitionsFailedNum') is not None:
            self.partitions_failed_num = m.get('partitionsFailedNum')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('scanId') is not None:
            self.scan_id = m.get('scanId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tableNum') is not None:
            self.table_num = m.get('tableNum')
        if m.get('tablesDoingNum') is not None:
            self.tables_doing_num = m.get('tablesDoingNum')
        if m.get('tablesDoneNum') is not None:
            self.tables_done_num = m.get('tablesDoneNum')
        if m.get('tablesFailedNum') is not None:
            self.tables_failed_num = m.get('tablesFailedNum')
        if m.get('tablesPartDoneNum') is not None:
            self.tables_part_done_num = m.get('tablesPartDoneNum')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetMmsDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        data: GetMmsDataSourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetMmsDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetMmsDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMmsDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMmsDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMmsDbResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        extra: str = None,
        id: int = None,
        last_ddl_time: str = None,
        location: str = None,
        name: str = None,
        num_rows: int = None,
        owner: str = None,
        partitions: int = None,
        partitions_doing: int = None,
        partitions_done: int = None,
        partitions_failed: int = None,
        size: int = None,
        source_id: int = None,
        source_name: str = None,
        status: str = None,
        tables: int = None,
        tables_doing: int = None,
        tables_done: int = None,
        tables_failed: int = None,
        tables_part_done: int = None,
        updated: bool = None,
    ):
        self.description = description
        self.extra = extra
        self.id = id
        # last ddl time
        self.last_ddl_time = last_ddl_time
        self.location = location
        self.name = name
        self.num_rows = num_rows
        self.owner = owner
        self.partitions = partitions
        self.partitions_doing = partitions_doing
        self.partitions_done = partitions_done
        self.partitions_failed = partitions_failed
        self.size = size
        self.source_id = source_id
        self.source_name = source_name
        self.status = status
        self.tables = tables
        self.tables_doing = tables_doing
        self.tables_done = tables_done
        self.tables_failed = tables_failed
        self.tables_part_done = tables_part_done
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.extra is not None:
            result['extra'] = self.extra
        if self.id is not None:
            result['id'] = self.id
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.num_rows is not None:
            result['numRows'] = self.num_rows
        if self.owner is not None:
            result['owner'] = self.owner
        if self.partitions is not None:
            result['partitions'] = self.partitions
        if self.partitions_doing is not None:
            result['partitionsDoing'] = self.partitions_doing
        if self.partitions_done is not None:
            result['partitionsDone'] = self.partitions_done
        if self.partitions_failed is not None:
            result['partitionsFailed'] = self.partitions_failed
        if self.size is not None:
            result['size'] = self.size
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.status is not None:
            result['status'] = self.status
        if self.tables is not None:
            result['tables'] = self.tables
        if self.tables_doing is not None:
            result['tablesDoing'] = self.tables_doing
        if self.tables_done is not None:
            result['tablesDone'] = self.tables_done
        if self.tables_failed is not None:
            result['tablesFailed'] = self.tables_failed
        if self.tables_part_done is not None:
            result['tablesPartDone'] = self.tables_part_done
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')
        if m.get('partitionsDoing') is not None:
            self.partitions_doing = m.get('partitionsDoing')
        if m.get('partitionsDone') is not None:
            self.partitions_done = m.get('partitionsDone')
        if m.get('partitionsFailed') is not None:
            self.partitions_failed = m.get('partitionsFailed')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('tablesDoing') is not None:
            self.tables_doing = m.get('tablesDoing')
        if m.get('tablesDone') is not None:
            self.tables_done = m.get('tablesDone')
        if m.get('tablesFailed') is not None:
            self.tables_failed = m.get('tablesFailed')
        if m.get('tablesPartDone') is not None:
            self.tables_part_done = m.get('tablesPartDone')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class GetMmsDbResponseBody(TeaModel):
    def __init__(
        self,
        data: GetMmsDbResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetMmsDbResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetMmsDbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMmsDbResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMmsDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMmsFetchMetadataJobResponseBodyData(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        error_msg: str = None,
        id: int = None,
        progress: float = None,
        result: str = None,
        source_id: int = None,
        start_time: str = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.error_msg = error_msg
        self.id = id
        self.progress = progress
        self.result = result
        self.source_id = source_id
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.id is not None:
            result['id'] = self.id
        if self.progress is not None:
            result['progress'] = self.progress
        if self.result is not None:
            result['result'] = self.result
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetMmsFetchMetadataJobResponseBody(TeaModel):
    def __init__(
        self,
        data: GetMmsFetchMetadataJobResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetMmsFetchMetadataJobResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetMmsFetchMetadataJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMmsFetchMetadataJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMmsFetchMetadataJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMmsJobResponseBodyDataConfig(TeaModel):
    def __init__(
        self,
        column_mapping: Dict[str, str] = None,
        enable_verification: bool = None,
        increment: bool = None,
        others: Dict[str, Any] = None,
        partition_filters: Dict[str, str] = None,
        partitions: List[int] = None,
        schema_only: bool = None,
        table_black_list: List[str] = None,
        table_mapping: Dict[str, str] = None,
        table_white_list: List[str] = None,
        tables: List[str] = None,
        task_type: str = None,
        tunnel_quota: str = None,
    ):
        self.column_mapping = column_mapping
        self.enable_verification = enable_verification
        self.increment = increment
        self.others = others
        self.partition_filters = partition_filters
        self.partitions = partitions
        self.schema_only = schema_only
        self.table_black_list = table_black_list
        self.table_mapping = table_mapping
        self.table_white_list = table_white_list
        self.tables = tables
        self.task_type = task_type
        self.tunnel_quota = tunnel_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_mapping is not None:
            result['columnMapping'] = self.column_mapping
        if self.enable_verification is not None:
            result['enableVerification'] = self.enable_verification
        if self.increment is not None:
            result['increment'] = self.increment
        if self.others is not None:
            result['others'] = self.others
        if self.partition_filters is not None:
            result['partitionFilters'] = self.partition_filters
        if self.partitions is not None:
            result['partitions'] = self.partitions
        if self.schema_only is not None:
            result['schemaOnly'] = self.schema_only
        if self.table_black_list is not None:
            result['tableBlackList'] = self.table_black_list
        if self.table_mapping is not None:
            result['tableMapping'] = self.table_mapping
        if self.table_white_list is not None:
            result['tableWhiteList'] = self.table_white_list
        if self.tables is not None:
            result['tables'] = self.tables
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnMapping') is not None:
            self.column_mapping = m.get('columnMapping')
        if m.get('enableVerification') is not None:
            self.enable_verification = m.get('enableVerification')
        if m.get('increment') is not None:
            self.increment = m.get('increment')
        if m.get('others') is not None:
            self.others = m.get('others')
        if m.get('partitionFilters') is not None:
            self.partition_filters = m.get('partitionFilters')
        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')
        if m.get('schemaOnly') is not None:
            self.schema_only = m.get('schemaOnly')
        if m.get('tableBlackList') is not None:
            self.table_black_list = m.get('tableBlackList')
        if m.get('tableMapping') is not None:
            self.table_mapping = m.get('tableMapping')
        if m.get('tableWhiteList') is not None:
            self.table_white_list = m.get('tableWhiteList')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')
        return self


class GetMmsJobResponseBodyData(TeaModel):
    def __init__(
        self,
        config: GetMmsJobResponseBodyDataConfig = None,
        create_time: str = None,
        db_id: int = None,
        dst_db_name: str = None,
        dst_schema_name: str = None,
        eta: str = None,
        id: int = None,
        name: str = None,
        source_id: int = None,
        source_name: str = None,
        src_db_name: str = None,
        src_schema_name: str = None,
        status: str = None,
        stopped: bool = None,
        task_done: int = None,
        task_num: int = None,
        type: str = None,
    ):
        self.config = config
        self.create_time = create_time
        self.db_id = db_id
        self.dst_db_name = dst_db_name
        self.dst_schema_name = dst_schema_name
        self.eta = eta
        self.id = id
        self.name = name
        self.source_id = source_id
        self.source_name = source_name
        self.src_db_name = src_db_name
        self.src_schema_name = src_schema_name
        self.status = status
        self.stopped = stopped
        self.task_done = task_done
        self.task_num = task_num
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.db_id is not None:
            result['dbId'] = self.db_id
        if self.dst_db_name is not None:
            result['dstDbName'] = self.dst_db_name
        if self.dst_schema_name is not None:
            result['dstSchemaName'] = self.dst_schema_name
        if self.eta is not None:
            result['eta'] = self.eta
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name
        if self.src_schema_name is not None:
            result['srcSchemaName'] = self.src_schema_name
        if self.status is not None:
            result['status'] = self.status
        if self.stopped is not None:
            result['stopped'] = self.stopped
        if self.task_done is not None:
            result['taskDone'] = self.task_done
        if self.task_num is not None:
            result['taskNum'] = self.task_num
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = GetMmsJobResponseBodyDataConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')
        if m.get('dstDbName') is not None:
            self.dst_db_name = m.get('dstDbName')
        if m.get('dstSchemaName') is not None:
            self.dst_schema_name = m.get('dstSchemaName')
        if m.get('eta') is not None:
            self.eta = m.get('eta')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')
        if m.get('srcSchemaName') is not None:
            self.src_schema_name = m.get('srcSchemaName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')
        if m.get('taskDone') is not None:
            self.task_done = m.get('taskDone')
        if m.get('taskNum') is not None:
            self.task_num = m.get('taskNum')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetMmsJobResponseBody(TeaModel):
    def __init__(
        self,
        data: GetMmsJobResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetMmsJobResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetMmsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMmsJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMmsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMmsPartitionResponseBodyData(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_name: str = None,
        id: int = None,
        last_ddl_time: str = None,
        num_rows: int = None,
        size: int = None,
        source_id: int = None,
        source_name: str = None,
        status: str = None,
        table_id: int = None,
        table_name: str = None,
        updated: bool = None,
        value: str = None,
    ):
        self.db_id = db_id
        self.db_name = db_name
        self.id = id
        # lastDdlTime
        self.last_ddl_time = last_ddl_time
        self.num_rows = num_rows
        self.size = size
        self.source_id = source_id
        self.source_name = source_name
        self.status = status
        self.table_id = table_id
        self.table_name = table_name
        self.updated = updated
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.id is not None:
            result['id'] = self.id
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time
        if self.num_rows is not None:
            result['numRows'] = self.num_rows
        if self.size is not None:
            result['size'] = self.size
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.status is not None:
            result['status'] = self.status
        if self.table_id is not None:
            result['tableId'] = self.table_id
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.updated is not None:
            result['updated'] = self.updated
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetMmsPartitionResponseBody(TeaModel):
    def __init__(
        self,
        data: GetMmsPartitionResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetMmsPartitionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetMmsPartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMmsPartitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMmsPartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMmsTableResponseBodyDataSchemaColumns(TeaModel):
    def __init__(
        self,
        comment: str = None,
        default_value: str = None,
        name: str = None,
        nullable: bool = None,
        type: str = None,
    ):
        self.comment = comment
        self.default_value = default_value
        self.name = name
        self.nullable = nullable
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.name is not None:
            result['name'] = self.name
        if self.nullable is not None:
            result['nullable'] = self.nullable
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetMmsTableResponseBodyDataSchemaPartitions(TeaModel):
    def __init__(
        self,
        comment: str = None,
        default_value: str = None,
        name: str = None,
        nullable: bool = None,
        type: str = None,
    ):
        self.comment = comment
        self.default_value = default_value
        self.name = name
        self.nullable = nullable
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.name is not None:
            result['name'] = self.name
        if self.nullable is not None:
            result['nullable'] = self.nullable
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetMmsTableResponseBodyDataSchema(TeaModel):
    def __init__(
        self,
        columns: List[GetMmsTableResponseBodyDataSchemaColumns] = None,
        comment: str = None,
        name: str = None,
        partitions: List[GetMmsTableResponseBodyDataSchemaPartitions] = None,
    ):
        self.columns = columns
        self.comment = comment
        self.name = name
        self.partitions = partitions

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()
        if self.partitions:
            for k in self.partitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['columns'].append(k.to_map() if k else None)
        if self.comment is not None:
            result['comment'] = self.comment
        if self.name is not None:
            result['name'] = self.name
        result['partitions'] = []
        if self.partitions is not None:
            for k in self.partitions:
                result['partitions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('columns') is not None:
            for k in m.get('columns'):
                temp_model = GetMmsTableResponseBodyDataSchemaColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.partitions = []
        if m.get('partitions') is not None:
            for k in m.get('partitions'):
                temp_model = GetMmsTableResponseBodyDataSchemaPartitions()
                self.partitions.append(temp_model.from_map(k))
        return self


class GetMmsTableResponseBodyData(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_name: str = None,
        extra: str = None,
        has_partitions: bool = None,
        id: int = None,
        input_format: str = None,
        last_ddl_time: str = None,
        location: str = None,
        name: str = None,
        num_rows: int = None,
        output_format: str = None,
        owner: str = None,
        partitions: int = None,
        partitions_doing: int = None,
        partitions_done: int = None,
        partitions_failed: int = None,
        schema: GetMmsTableResponseBodyDataSchema = None,
        serde: str = None,
        size: int = None,
        source_id: int = None,
        source_name: str = None,
        status: str = None,
        type: str = None,
        updated: bool = None,
    ):
        self.db_id = db_id
        self.db_name = db_name
        self.extra = extra
        self.has_partitions = has_partitions
        # table ID
        self.id = id
        # inputFormat
        self.input_format = input_format
        # lastDdlTime
        self.last_ddl_time = last_ddl_time
        self.location = location
        self.name = name
        self.num_rows = num_rows
        # outputFormat
        self.output_format = output_format
        self.owner = owner
        self.partitions = partitions
        self.partitions_doing = partitions_doing
        self.partitions_done = partitions_done
        self.partitions_failed = partitions_failed
        self.schema = schema
        # serde
        self.serde = serde
        self.size = size
        self.source_id = source_id
        self.source_name = source_name
        self.status = status
        self.type = type
        self.updated = updated

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['dbId'] = self.db_id
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.extra is not None:
            result['extra'] = self.extra
        if self.has_partitions is not None:
            result['hasPartitions'] = self.has_partitions
        if self.id is not None:
            result['id'] = self.id
        if self.input_format is not None:
            result['inputFormat'] = self.input_format
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.num_rows is not None:
            result['numRows'] = self.num_rows
        if self.output_format is not None:
            result['outputFormat'] = self.output_format
        if self.owner is not None:
            result['owner'] = self.owner
        if self.partitions is not None:
            result['partitions'] = self.partitions
        if self.partitions_doing is not None:
            result['partitionsDoing'] = self.partitions_doing
        if self.partitions_done is not None:
            result['partitionsDone'] = self.partitions_done
        if self.partitions_failed is not None:
            result['partitionsFailed'] = self.partitions_failed
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        if self.serde is not None:
            result['serde'] = self.serde
        if self.size is not None:
            result['size'] = self.size
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('hasPartitions') is not None:
            self.has_partitions = m.get('hasPartitions')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('inputFormat') is not None:
            self.input_format = m.get('inputFormat')
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')
        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')
        if m.get('partitionsDoing') is not None:
            self.partitions_doing = m.get('partitionsDoing')
        if m.get('partitionsDone') is not None:
            self.partitions_done = m.get('partitionsDone')
        if m.get('partitionsFailed') is not None:
            self.partitions_failed = m.get('partitionsFailed')
        if m.get('schema') is not None:
            temp_model = GetMmsTableResponseBodyDataSchema()
            self.schema = temp_model.from_map(m['schema'])
        if m.get('serde') is not None:
            self.serde = m.get('serde')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class GetMmsTableResponseBody(TeaModel):
    def __init__(
        self,
        data: GetMmsTableResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetMmsTableResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetMmsTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMmsTableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMmsTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMmsTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        db_id: int = None,
        dst_db_name: str = None,
        dst_schema_name: str = None,
        dst_table_name: str = None,
        end_time: str = None,
        id: int = None,
        job_id: int = None,
        job_name: str = None,
        retried_times: int = None,
        running: bool = None,
        source_id: int = None,
        source_name: str = None,
        src_db_name: str = None,
        src_schema_name: str = None,
        src_table_name: str = None,
        start_time: str = None,
        status: str = None,
        stopped: bool = None,
        table_id: int = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.db_id = db_id
        self.dst_db_name = dst_db_name
        self.dst_schema_name = dst_schema_name
        self.dst_table_name = dst_table_name
        self.end_time = end_time
        self.id = id
        self.job_id = job_id
        self.job_name = job_name
        self.retried_times = retried_times
        self.running = running
        self.source_id = source_id
        self.source_name = source_name
        self.src_db_name = src_db_name
        self.src_schema_name = src_schema_name
        self.src_table_name = src_table_name
        self.start_time = start_time
        self.status = status
        self.stopped = stopped
        self.table_id = table_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.db_id is not None:
            result['dbId'] = self.db_id
        if self.dst_db_name is not None:
            result['dstDbName'] = self.dst_db_name
        if self.dst_schema_name is not None:
            result['dstSchemaName'] = self.dst_schema_name
        if self.dst_table_name is not None:
            result['dstTableName'] = self.dst_table_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.id is not None:
            result['id'] = self.id
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.job_name is not None:
            result['jobName'] = self.job_name
        if self.retried_times is not None:
            result['retriedTimes'] = self.retried_times
        if self.running is not None:
            result['running'] = self.running
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name
        if self.src_schema_name is not None:
            result['srcSchemaName'] = self.src_schema_name
        if self.src_table_name is not None:
            result['srcTableName'] = self.src_table_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.stopped is not None:
            result['stopped'] = self.stopped
        if self.table_id is not None:
            result['tableId'] = self.table_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')
        if m.get('dstDbName') is not None:
            self.dst_db_name = m.get('dstDbName')
        if m.get('dstSchemaName') is not None:
            self.dst_schema_name = m.get('dstSchemaName')
        if m.get('dstTableName') is not None:
            self.dst_table_name = m.get('dstTableName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')
        if m.get('retriedTimes') is not None:
            self.retried_times = m.get('retriedTimes')
        if m.get('running') is not None:
            self.running = m.get('running')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')
        if m.get('srcSchemaName') is not None:
            self.src_schema_name = m.get('srcSchemaName')
        if m.get('srcTableName') is not None:
            self.src_table_name = m.get('srcTableName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')
        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetMmsTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: GetMmsTaskResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetMmsTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetMmsTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMmsTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMmsTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPackageRequest(TeaModel):
    def __init__(
        self,
        source_project: str = None,
    ):
        # The project to which the package belongs. This parameter is required if the package is installed in the MaxCompute project.
        self.source_project = source_project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_project is not None:
            result['sourceProject'] = self.source_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceProject') is not None:
            self.source_project = m.get('sourceProject')
        return self


class GetPackageResponseBodyDataAllowedProjectList(TeaModel):
    def __init__(
        self,
        label: str = None,
        project: str = None,
    ):
        # The security level for sensitive data.
        self.label = label
        # The name of the MaxCompute project.
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.project is not None:
            result['project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('project') is not None:
            self.project = m.get('project')
        return self


class GetPackageResponseBodyDataResourceListFunction(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the function.
        self.actions = actions
        # The name of the function.
        self.name = name
        # The name of schema.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetPackageResponseBodyDataResourceListResource(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the resource.
        self.actions = actions
        # The name of the resource.
        self.name = name
        # The name of schema.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetPackageResponseBodyDataResourceListTable(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the table.
        self.actions = actions
        # The name of the table.
        self.name = name
        # The name of schema.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetPackageResponseBodyDataResourceList(TeaModel):
    def __init__(
        self,
        function: List[GetPackageResponseBodyDataResourceListFunction] = None,
        resource: List[GetPackageResponseBodyDataResourceListResource] = None,
        table: List[GetPackageResponseBodyDataResourceListTable] = None,
    ):
        # The functions.
        self.function = function
        # The resources.
        self.resource = resource
        # The tables.
        self.table = table

    def validate(self):
        if self.function:
            for k in self.function:
                if k:
                    k.validate()
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['function'] = []
        if self.function is not None:
            for k in self.function:
                result['function'].append(k.to_map() if k else None)
        result['resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['resource'].append(k.to_map() if k else None)
        result['table'] = []
        if self.table is not None:
            for k in self.table:
                result['table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function = []
        if m.get('function') is not None:
            for k in m.get('function'):
                temp_model = GetPackageResponseBodyDataResourceListFunction()
                self.function.append(temp_model.from_map(k))
        self.resource = []
        if m.get('resource') is not None:
            for k in m.get('resource'):
                temp_model = GetPackageResponseBodyDataResourceListResource()
                self.resource.append(temp_model.from_map(k))
        self.table = []
        if m.get('table') is not None:
            for k in m.get('table'):
                temp_model = GetPackageResponseBodyDataResourceListTable()
                self.table.append(temp_model.from_map(k))
        return self


class GetPackageResponseBodyData(TeaModel):
    def __init__(
        self,
        allowed_project_list: List[GetPackageResponseBodyDataAllowedProjectList] = None,
        resource_list: GetPackageResponseBodyDataResourceList = None,
    ):
        # The projects in which the package is installed.
        self.allowed_project_list = allowed_project_list
        # The details of the resources that are included in the package.
        self.resource_list = resource_list

    def validate(self):
        if self.allowed_project_list:
            for k in self.allowed_project_list:
                if k:
                    k.validate()
        if self.resource_list:
            self.resource_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['allowedProjectList'] = []
        if self.allowed_project_list is not None:
            for k in self.allowed_project_list:
                result['allowedProjectList'].append(k.to_map() if k else None)
        if self.resource_list is not None:
            result['resourceList'] = self.resource_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.allowed_project_list = []
        if m.get('allowedProjectList') is not None:
            for k in m.get('allowedProjectList'):
                temp_model = GetPackageResponseBodyDataAllowedProjectList()
                self.allowed_project_list.append(temp_model.from_map(k))
        if m.get('resourceList') is not None:
            temp_model = GetPackageResponseBodyDataResourceList()
            self.resource_list = temp_model.from_map(m['resourceList'])
        return self


class GetPackageResponseBody(TeaModel):
    def __init__(
        self,
        data: GetPackageResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetPackageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(
        self,
        verbose: bool = None,
    ):
        # Specifies whether to use additional information.
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verbose is not None:
            result['verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('verbose') is not None:
            self.verbose = m.get('verbose')
        return self


class GetProjectResponseBodyDataIpWhiteList(TeaModel):
    def __init__(
        self,
        ip_list: str = None,
        vpc_ip_list: str = None,
    ):
        # The IP address whitelist for access over the Internet or the network for interconnecting with other Alibaba Cloud services.
        # 
        # >  If you configure only the IP address whitelist for access over the Internet or the network for interconnecting with other Alibaba Cloud services, the access over the Internet or the network for interconnecting with other Alibaba Cloud services is subject to configurations, and access over a virtual private cloud (VPC) is not allowed.
        self.ip_list = ip_list
        # The IP address whitelist for access over a VPC.
        # 
        # >  If you configure only the IP address whitelist for access over a VPC, the access over a VPC is subject to configurations, and the access over the Internet or the network for interconnecting with other Alibaba Cloud services is not allowed.
        self.vpc_ip_list = vpc_ip_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        if self.vpc_ip_list is not None:
            result['vpcIpList'] = self.vpc_ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        if m.get('vpcIpList') is not None:
            self.vpc_ip_list = m.get('vpcIpList')
        return self


class GetProjectResponseBodyDataPropertiesEncryption(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        enable: bool = None,
        key: str = None,
    ):
        # The data encryption algorithm that is supported by the key. Valid values: AES256, AESCTR, and RC4.
        self.algorithm = algorithm
        # Indicates whether the data encryption feature needs to be enabled for the project. For more information about data encryption, see
        # 
        # [Storage encryption](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/storage-encryption).
        self.enable = enable
        # The type of key that is used for data encryption. You can select MaxCompute Default Key or Bring Your Own Key (BYOK) as the key type. If you select MaxCompute Default Key, the default key that is created by MaxCompute is used.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.enable is not None:
            result['enable'] = self.enable
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class GetProjectResponseBodyDataPropertiesExternalProjectProperties(TeaModel):
    def __init__(
        self,
        is_external_catalog_bound: str = None,
    ):
        # Indicates whether the external project is an external project for [data lakehouse solution 2.0](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/lake-warehouse-integrated-2-0-use-guide).
        self.is_external_catalog_bound = is_external_catalog_bound

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_external_catalog_bound is not None:
            result['isExternalCatalogBound'] = self.is_external_catalog_bound
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isExternalCatalogBound') is not None:
            self.is_external_catalog_bound = m.get('isExternalCatalogBound')
        return self


class GetProjectResponseBodyDataPropertiesStorageTierInfoStorageTierSize(TeaModel):
    def __init__(
        self,
        long_term_size: int = None,
        low_frequency_size: int = None,
        standard_size: int = None,
    ):
        # The storage usage at the long-term storage tier.
        self.long_term_size = long_term_size
        # The storage usage at the Infrequent Access (IA) layer.
        self.low_frequency_size = low_frequency_size
        # The storage usage at the standard storage tier.
        self.standard_size = standard_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.long_term_size is not None:
            result['longTermSize'] = self.long_term_size
        if self.low_frequency_size is not None:
            result['lowFrequencySize'] = self.low_frequency_size
        if self.standard_size is not None:
            result['standardSize'] = self.standard_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('longTermSize') is not None:
            self.long_term_size = m.get('longTermSize')
        if m.get('lowFrequencySize') is not None:
            self.low_frequency_size = m.get('lowFrequencySize')
        if m.get('standardSize') is not None:
            self.standard_size = m.get('standardSize')
        return self


class GetProjectResponseBodyDataPropertiesStorageTierInfo(TeaModel):
    def __init__(
        self,
        project_backup_size: int = None,
        project_total_size: int = None,
        storage_tier_size: GetProjectResponseBodyDataPropertiesStorageTierInfoStorageTierSize = None,
    ):
        # The backup storage usage.
        self.project_backup_size = project_backup_size
        # The total storage usage.
        self.project_total_size = project_total_size
        # The [storage tier](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/tiered-storage) information.
        self.storage_tier_size = storage_tier_size

    def validate(self):
        if self.storage_tier_size:
            self.storage_tier_size.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_backup_size is not None:
            result['projectBackupSize'] = self.project_backup_size
        if self.project_total_size is not None:
            result['projectTotalSize'] = self.project_total_size
        if self.storage_tier_size is not None:
            result['storageTierSize'] = self.storage_tier_size.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectBackupSize') is not None:
            self.project_backup_size = m.get('projectBackupSize')
        if m.get('projectTotalSize') is not None:
            self.project_total_size = m.get('projectTotalSize')
        if m.get('storageTierSize') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesStorageTierInfoStorageTierSize()
            self.storage_tier_size = temp_model.from_map(m['storageTierSize'])
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycle(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The lifecycle type. Valid values:
        # 
        # *   **mandatory**: The lifecycle clause is required in a table creation statement.
        # *   **optional**: The lifecycle clause is optional in a table creation statement. If you do not configure a lifecycle for a table, the table does not expire.
        # *   **inherit**: If you do not configure a lifecycle for a table when you create the table, the value of the odps.table.lifecycle.value parameter is used as the table lifecycle by default.
        self.type = type
        # The table lifecycle. Unit: days. Valid values: 1 to 37231. Default value: 37231.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongterm(TeaModel):
    def __init__(
        self,
        days_after_last_access_greater_than: int = None,
        days_after_last_modification_greater_than: int = None,
        days_after_last_tier_modification_greater_than: int = None,
    ):
        # The system triggers an automatic storage tier change N days after the last access time of data. N is specified by this parameter and corresponds to `LastAccessTime` that is configured for the table or partition.
        # 
        # >  If LastAccessTime of a table or partition is left empty, the following rules are applied:
        # 
        # *   For tables or partitions that you created before October 1, 2023, 2023.10.01 00:00:00 in UTC+0 is considered as the last access time.
        # 
        # *   For tables or partitions that you created on or after October 1, 2023, if no data is accessed, the table or partition creation time is considered as the last access time.
        self.days_after_last_access_greater_than = days_after_last_access_greater_than
        # The system triggers an automatic storage tier change N days after the last modification time of data. N is specified by this parameter and corresponds to `LastModifiedTime` that is configured for the table or partition.
        self.days_after_last_modification_greater_than = days_after_last_modification_greater_than
        # The period after the previous storage tier change time.
        self.days_after_last_tier_modification_greater_than = days_after_last_tier_modification_greater_than

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_after_last_access_greater_than is not None:
            result['DaysAfterLastAccessGreaterThan'] = self.days_after_last_access_greater_than
        if self.days_after_last_modification_greater_than is not None:
            result['DaysAfterLastModificationGreaterThan'] = self.days_after_last_modification_greater_than
        if self.days_after_last_tier_modification_greater_than is not None:
            result['DaysAfterLastTierModificationGreaterThan'] = self.days_after_last_tier_modification_greater_than
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysAfterLastAccessGreaterThan') is not None:
            self.days_after_last_access_greater_than = m.get('DaysAfterLastAccessGreaterThan')
        if m.get('DaysAfterLastModificationGreaterThan') is not None:
            self.days_after_last_modification_greater_than = m.get('DaysAfterLastModificationGreaterThan')
        if m.get('DaysAfterLastTierModificationGreaterThan') is not None:
            self.days_after_last_tier_modification_greater_than = m.get('DaysAfterLastTierModificationGreaterThan')
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequency(TeaModel):
    def __init__(
        self,
        days_after_last_access_greater_than: int = None,
        days_after_last_modification_greater_than: int = None,
        days_after_last_tier_modification_greater_than: int = None,
    ):
        # The system triggers an automatic storage tier change N days after the last access time of data. N is specified by this parameter and corresponds to `LastAccessTime` that is configured for the table or partition.
        # 
        # >  If LastAccessTime of a table or partition is left empty, the following rules are applied:
        # 
        # *   For tables or partitions that you created before October 1, 2023, 2023.10.01 00:00:00 in UTC+0 is considered as the last access time.
        # 
        # *   For tables or partitions that you created on or after October 1, 2023, if no data is accessed, the table or partition creation time is considered as the last access time.
        self.days_after_last_access_greater_than = days_after_last_access_greater_than
        # The system triggers an automatic storage tier change N days after the last modification time of data. N is specified by this parameter and corresponds to `LastModifiedTime` that is configured for the table or partition.
        self.days_after_last_modification_greater_than = days_after_last_modification_greater_than
        # The period after the previous storage tier change time.
        self.days_after_last_tier_modification_greater_than = days_after_last_tier_modification_greater_than

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_after_last_access_greater_than is not None:
            result['DaysAfterLastAccessGreaterThan'] = self.days_after_last_access_greater_than
        if self.days_after_last_modification_greater_than is not None:
            result['DaysAfterLastModificationGreaterThan'] = self.days_after_last_modification_greater_than
        if self.days_after_last_tier_modification_greater_than is not None:
            result['DaysAfterLastTierModificationGreaterThan'] = self.days_after_last_tier_modification_greater_than
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysAfterLastAccessGreaterThan') is not None:
            self.days_after_last_access_greater_than = m.get('DaysAfterLastAccessGreaterThan')
        if m.get('DaysAfterLastModificationGreaterThan') is not None:
            self.days_after_last_modification_greater_than = m.get('DaysAfterLastModificationGreaterThan')
        if m.get('DaysAfterLastTierModificationGreaterThan') is not None:
            self.days_after_last_tier_modification_greater_than = m.get('DaysAfterLastTierModificationGreaterThan')
        return self


class GetProjectResponseBodyDataPropertiesTableLifecycleConfig(TeaModel):
    def __init__(
        self,
        tier_to_longterm: GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongterm = None,
        tier_to_low_frequency: GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequency = None,
    ):
        # The information about the long-term storage tier.
        self.tier_to_longterm = tier_to_longterm
        # The information about the IA storage tier.
        self.tier_to_low_frequency = tier_to_low_frequency

    def validate(self):
        if self.tier_to_longterm:
            self.tier_to_longterm.validate()
        if self.tier_to_low_frequency:
            self.tier_to_low_frequency.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tier_to_longterm is not None:
            result['TierToLongterm'] = self.tier_to_longterm.to_map()
        if self.tier_to_low_frequency is not None:
            result['TierToLowFrequency'] = self.tier_to_low_frequency.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TierToLongterm') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongterm()
            self.tier_to_longterm = temp_model.from_map(m['TierToLongterm'])
        if m.get('TierToLowFrequency') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequency()
            self.tier_to_low_frequency = temp_model.from_map(m['TierToLowFrequency'])
        return self


class GetProjectResponseBodyDataProperties(TeaModel):
    def __init__(
        self,
        allow_full_scan: bool = None,
        auto_mv_quota_gb: int = None,
        elder_tunnel_quota: str = None,
        enable_auto_mv: bool = None,
        enable_decimal_2: bool = None,
        enable_dr: bool = None,
        enable_fdc_cache_force: bool = None,
        enable_tiered_storage: bool = None,
        enable_tunnel_quota_route: bool = None,
        encryption: GetProjectResponseBodyDataPropertiesEncryption = None,
        external_project_properties: GetProjectResponseBodyDataPropertiesExternalProjectProperties = None,
        fdc_quota: str = None,
        retention_days: int = None,
        sql_metering_max: str = None,
        storage_tier_info: GetProjectResponseBodyDataPropertiesStorageTierInfo = None,
        table_lifecycle: GetProjectResponseBodyDataPropertiesTableLifecycle = None,
        table_lifecycle_config: GetProjectResponseBodyDataPropertiesTableLifecycleConfig = None,
        timezone: str = None,
        tunnel_quota: str = None,
        type_system: str = None,
    ):
        # Indicates whether a full table scan is allowed in the project. A full table scan occupies a large number of resources, which reduces data processing efficiency. By default, the full table scan feature is disabled.
        self.allow_full_scan = allow_full_scan
        self.auto_mv_quota_gb = auto_mv_quota_gb
        # The Tunnel parent resource group that is bound to the project. You do not need to pay attention to this group.
        self.elder_tunnel_quota = elder_tunnel_quota
        self.enable_auto_mv = enable_auto_mv
        # Indicates whether the DECIMAL type of the MaxCompute V2.0 data type edition is enabled.
        self.enable_decimal_2 = enable_decimal_2
        self.enable_dr = enable_dr
        # Indicates whether external table caching is forcefully enabled.
        self.enable_fdc_cache_force = enable_fdc_cache_force
        # Indicates whether [tiered storage](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/tiered-storage) is enabled.
        self.enable_tiered_storage = enable_tiered_storage
        # Indicates whether the routing of the Tunnel resource group is enabled.
        # 
        # *   true: The data transfer tasks that are submitted by the project by default use the Tunnel resource group that is bound to the project.
        # *   false: The data transfer tasks that are submitted by the project by default use the Tunnel shared resource group.
        self.enable_tunnel_quota_route = enable_tunnel_quota_route
        # The storage encryption properties.
        self.encryption = encryption
        # The properties of the external project.
        self.external_project_properties = external_project_properties
        # The quota for external table caching.
        self.fdc_quota = fdc_quota
        # The retention period for backup data. Unit: days. During the retention period, you can restore data of the version in use to the backup data of any version. Valid values: [0,30]. Default value: 1. The value 0 indicates that the backup feature is disabled.
        self.retention_days = retention_days
        # The maximum consumption threshold of a single SQL statement. Formula: Amount of scanned data (GB) × Complexity.
        self.sql_metering_max = sql_metering_max
        # The [storage tier](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/tiered-storage) information.
        self.storage_tier_info = storage_tier_info
        # The table lifecycle properties.
        self.table_lifecycle = table_lifecycle
        # The [properties of tiered storage lifecycle rules](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/tiered-storage#f61fc9db76nna). After you configure the properties, the system triggers automatic switching of storage tiers based on the rules.
        self.table_lifecycle_config = table_lifecycle_config
        # The time zone that is used by your project. The time zone is the same as the time zone specified by `odps.sql.timezone`.
        self.timezone = timezone
        # The [Tunnel](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/overview-of-dts) resource group that is bound to the project.
        # 
        # *   Default resource group: The Tunnel shared resource group is used. You cannot use the subscription-based Tunnel resource group for the project. The default resource group is automatically used by the Tunnel service of your project, regardless of the parameter setting.
        # *   Subscription-based Tunnel resource group: You can use the subscription-based Tunnel resource group for the project.
        self.tunnel_quota = tunnel_quota
        # The data type edition. Valid values:
        # 
        # *   **1**: MaxCompute V1.0 data type edition
        # *   **2**: MaxCompute V2.0 data type edition
        # *   **hive**: Hive-compatible data type edition
        # 
        # For more information about the differences among the three data type editions, see [Data type editions](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/data-type-editions).
        self.type_system = type_system

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.external_project_properties:
            self.external_project_properties.validate()
        if self.storage_tier_info:
            self.storage_tier_info.validate()
        if self.table_lifecycle:
            self.table_lifecycle.validate()
        if self.table_lifecycle_config:
            self.table_lifecycle_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_full_scan is not None:
            result['allowFullScan'] = self.allow_full_scan
        if self.auto_mv_quota_gb is not None:
            result['autoMvQuotaGb'] = self.auto_mv_quota_gb
        if self.elder_tunnel_quota is not None:
            result['elderTunnelQuota'] = self.elder_tunnel_quota
        if self.enable_auto_mv is not None:
            result['enableAutoMv'] = self.enable_auto_mv
        if self.enable_decimal_2 is not None:
            result['enableDecimal2'] = self.enable_decimal_2
        if self.enable_dr is not None:
            result['enableDr'] = self.enable_dr
        if self.enable_fdc_cache_force is not None:
            result['enableFdcCacheForce'] = self.enable_fdc_cache_force
        if self.enable_tiered_storage is not None:
            result['enableTieredStorage'] = self.enable_tiered_storage
        if self.enable_tunnel_quota_route is not None:
            result['enableTunnelQuotaRoute'] = self.enable_tunnel_quota_route
        if self.encryption is not None:
            result['encryption'] = self.encryption.to_map()
        if self.external_project_properties is not None:
            result['externalProjectProperties'] = self.external_project_properties.to_map()
        if self.fdc_quota is not None:
            result['fdcQuota'] = self.fdc_quota
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        if self.sql_metering_max is not None:
            result['sqlMeteringMax'] = self.sql_metering_max
        if self.storage_tier_info is not None:
            result['storageTierInfo'] = self.storage_tier_info.to_map()
        if self.table_lifecycle is not None:
            result['tableLifecycle'] = self.table_lifecycle.to_map()
        if self.table_lifecycle_config is not None:
            result['tableLifecycleConfig'] = self.table_lifecycle_config.to_map()
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota
        if self.type_system is not None:
            result['typeSystem'] = self.type_system
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowFullScan') is not None:
            self.allow_full_scan = m.get('allowFullScan')
        if m.get('autoMvQuotaGb') is not None:
            self.auto_mv_quota_gb = m.get('autoMvQuotaGb')
        if m.get('elderTunnelQuota') is not None:
            self.elder_tunnel_quota = m.get('elderTunnelQuota')
        if m.get('enableAutoMv') is not None:
            self.enable_auto_mv = m.get('enableAutoMv')
        if m.get('enableDecimal2') is not None:
            self.enable_decimal_2 = m.get('enableDecimal2')
        if m.get('enableDr') is not None:
            self.enable_dr = m.get('enableDr')
        if m.get('enableFdcCacheForce') is not None:
            self.enable_fdc_cache_force = m.get('enableFdcCacheForce')
        if m.get('enableTieredStorage') is not None:
            self.enable_tiered_storage = m.get('enableTieredStorage')
        if m.get('enableTunnelQuotaRoute') is not None:
            self.enable_tunnel_quota_route = m.get('enableTunnelQuotaRoute')
        if m.get('encryption') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesEncryption()
            self.encryption = temp_model.from_map(m['encryption'])
        if m.get('externalProjectProperties') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesExternalProjectProperties()
            self.external_project_properties = temp_model.from_map(m['externalProjectProperties'])
        if m.get('fdcQuota') is not None:
            self.fdc_quota = m.get('fdcQuota')
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        if m.get('sqlMeteringMax') is not None:
            self.sql_metering_max = m.get('sqlMeteringMax')
        if m.get('storageTierInfo') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesStorageTierInfo()
            self.storage_tier_info = temp_model.from_map(m['storageTierInfo'])
        if m.get('tableLifecycle') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycle()
            self.table_lifecycle = temp_model.from_map(m['tableLifecycle'])
        if m.get('tableLifecycleConfig') is not None:
            temp_model = GetProjectResponseBodyDataPropertiesTableLifecycleConfig()
            self.table_lifecycle_config = temp_model.from_map(m['tableLifecycleConfig'])
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')
        if m.get('typeSystem') is not None:
            self.type_system = m.get('typeSystem')
        return self


class GetProjectResponseBodyDataSaleTag(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The instance ID of the default computing quota.
        self.resource_id = resource_id
        # The billing method of the default computing quota.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetProjectResponseBodyDataSecurityPropertiesProjectProtection(TeaModel):
    def __init__(
        self,
        exception_policy: str = None,
        protected: bool = None,
    ):
        # If you enable the project data protection mechanism, you can configure exception or trusted projects. This allows specified users to transfer data of a specified object to a specified project. The project data protection mechanism does not take effect in all the situations that are specified in the exception policy.
        self.exception_policy = exception_policy
        # Indicates whether the [data protection mechanism](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/project-data-protection) is enabled for the project. This allows or denies data transfer across projects. By default, the data protection mechanism is disabled.
        self.protected = protected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_policy is not None:
            result['exceptionPolicy'] = self.exception_policy
        if self.protected is not None:
            result['protected'] = self.protected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exceptionPolicy') is not None:
            self.exception_policy = m.get('exceptionPolicy')
        if m.get('protected') is not None:
            self.protected = m.get('protected')
        return self


class GetProjectResponseBodyDataSecurityProperties(TeaModel):
    def __init__(
        self,
        enable_download_privilege: bool = None,
        label_security: bool = None,
        object_creator_has_access_permission: bool = None,
        object_creator_has_grant_permission: bool = None,
        project_protection: GetProjectResponseBodyDataSecurityPropertiesProjectProtection = None,
        using_acl: bool = None,
        using_policy: bool = None,
    ):
        # Indicates whether the [download control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/label-based-access-control) feature is enabled. By default, this feature is disabled.
        self.enable_download_privilege = enable_download_privilege
        # Indicates whether the [label-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/label-based-access-control) feature is enabled. By default, this feature is disabled.
        self.label_security = label_security
        # Indicates whether to allow the object creator to have the access permissions on the object. The default value is true, which indicates that the object creator has the access permissions on the object.
        self.object_creator_has_access_permission = object_creator_has_access_permission
        # Indicates whether the object creator has the authorization permissions on the object. The default value is true, which indicates that the object creator has the authorization permissions on the object.
        self.object_creator_has_grant_permission = object_creator_has_grant_permission
        # The properties of the [data protection mechanism](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/project-data-protection).
        self.project_protection = project_protection
        # Indicates whether the [ACL-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/acl-based-access-control) feature is enabled. By default, this feature is enabled.
        self.using_acl = using_acl
        # Indicates whether the [policy-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/policy-based-access-control-1) feature is enabled. By default, this feature is enabled.
        self.using_policy = using_policy

    def validate(self):
        if self.project_protection:
            self.project_protection.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_download_privilege is not None:
            result['enableDownloadPrivilege'] = self.enable_download_privilege
        if self.label_security is not None:
            result['labelSecurity'] = self.label_security
        if self.object_creator_has_access_permission is not None:
            result['objectCreatorHasAccessPermission'] = self.object_creator_has_access_permission
        if self.object_creator_has_grant_permission is not None:
            result['objectCreatorHasGrantPermission'] = self.object_creator_has_grant_permission
        if self.project_protection is not None:
            result['projectProtection'] = self.project_protection.to_map()
        if self.using_acl is not None:
            result['usingAcl'] = self.using_acl
        if self.using_policy is not None:
            result['usingPolicy'] = self.using_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableDownloadPrivilege') is not None:
            self.enable_download_privilege = m.get('enableDownloadPrivilege')
        if m.get('labelSecurity') is not None:
            self.label_security = m.get('labelSecurity')
        if m.get('objectCreatorHasAccessPermission') is not None:
            self.object_creator_has_access_permission = m.get('objectCreatorHasAccessPermission')
        if m.get('objectCreatorHasGrantPermission') is not None:
            self.object_creator_has_grant_permission = m.get('objectCreatorHasGrantPermission')
        if m.get('projectProtection') is not None:
            temp_model = GetProjectResponseBodyDataSecurityPropertiesProjectProtection()
            self.project_protection = temp_model.from_map(m['projectProtection'])
        if m.get('usingAcl') is not None:
            self.using_acl = m.get('usingAcl')
        if m.get('usingPolicy') is not None:
            self.using_policy = m.get('usingPolicy')
        return self


class GetProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        comment: str = None,
        cost_storage: str = None,
        created_time: int = None,
        default_quota: str = None,
        ip_white_list: GetProjectResponseBodyDataIpWhiteList = None,
        name: str = None,
        owner: str = None,
        product_type: str = None,
        properties: GetProjectResponseBodyDataProperties = None,
        region_id: str = None,
        sale_tag: GetProjectResponseBodyDataSaleTag = None,
        security_properties: GetProjectResponseBodyDataSecurityProperties = None,
        status: str = None,
        super_admins: List[str] = None,
        three_tier_model: bool = None,
        type: str = None,
    ):
        # The project description.
        self.comment = comment
        # The total storage usage. The storage space that is occupied by your project, which is the logical storage space after your project data is collected and compressed.
        self.cost_storage = cost_storage
        # The creation time.
        self.created_time = created_time
        # The default computing quota that is used to allocate computing resources. If you do not specify a computing quota for your project, the jobs that are initiated by your project consume the computing resources in the default quota. For more information about how to use computing resources, see [Use quota groups for computing resources](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/use-of-computing-resources).
        self.default_quota = default_quota
        # The information about the IP address whitelist.
        self.ip_white_list = ip_white_list
        # The project name.
        self.name = name
        # The account information of the project owner.
        self.owner = owner
        # The billing method of the default computing quota.
        self.product_type = product_type
        # The basic properties of the project.
        self.properties = properties
        # The region ID.
        self.region_id = region_id
        # The instance ID and billing method of the default computing quota.
        self.sale_tag = sale_tag
        # The permission properties.
        self.security_properties = security_properties
        # The project status. Valid values:
        # 
        # *   **AVAILABLE**\
        # *   **READONLY**\
        # *   **FROZEN**\
        # *   **DELETING**\
        self.status = status
        # The list of `Super_Administrator` role members of the project.
        self.super_admins = super_admins
        # Indicates whether data storage by schema is supported. MaxCompute supports the schema feature. This feature allows you to classify objects such as tables, resources, and user-defined functions (UDFs) in a project by schema. You can create multiple schemas in a project. For more information, see [Schema-related operations](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/schema-related-operations).
        self.three_tier_model = three_tier_model
        # The project type. Valid values:
        # 
        # *   **managed**: internal project
        # *   **external**: external project
        self.type = type

    def validate(self):
        if self.ip_white_list:
            self.ip_white_list.validate()
        if self.properties:
            self.properties.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.security_properties:
            self.security_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.cost_storage is not None:
            result['costStorage'] = self.cost_storage
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.default_quota is not None:
            result['defaultQuota'] = self.default_quota
        if self.ip_white_list is not None:
            result['ipWhiteList'] = self.ip_white_list.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.product_type is not None:
            result['productType'] = self.product_type
        if self.properties is not None:
            result['properties'] = self.properties.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.security_properties is not None:
            result['securityProperties'] = self.security_properties.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.super_admins is not None:
            result['superAdmins'] = self.super_admins
        if self.three_tier_model is not None:
            result['threeTierModel'] = self.three_tier_model
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('costStorage') is not None:
            self.cost_storage = m.get('costStorage')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('defaultQuota') is not None:
            self.default_quota = m.get('defaultQuota')
        if m.get('ipWhiteList') is not None:
            temp_model = GetProjectResponseBodyDataIpWhiteList()
            self.ip_white_list = temp_model.from_map(m['ipWhiteList'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('productType') is not None:
            self.product_type = m.get('productType')
        if m.get('properties') is not None:
            temp_model = GetProjectResponseBodyDataProperties()
            self.properties = temp_model.from_map(m['properties'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = GetProjectResponseBodyDataSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('securityProperties') is not None:
            temp_model = GetProjectResponseBodyDataSecurityProperties()
            self.security_properties = temp_model.from_map(m['securityProperties'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('superAdmins') is not None:
            self.super_admins = m.get('superAdmins')
        if m.get('threeTierModel') is not None:
            self.three_tier_model = m.get('threeTierModel')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        data: GetProjectResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # *   1xx: informational response. The request is received and is being processed.
        # *   2xx: success. The request is successfully received, understood, and accepted by the server.
        # *   3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # *   4xx: client error. The request contains invalid request parameters and syntaxes, or specific request conditions cannot be met.
        # *   5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetProjectResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaRequest(TeaModel):
    def __init__(
        self,
        ak_proven: str = None,
        mock: bool = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The trusted AccessKey pairs.
        self.ak_proven = ak_proven
        # Specifies whether to include submodules. Valid values: -true: The request includes submodules. -false: The request does not include submodules. This is the default value.
        self.mock = mock
        # The region ID.
        self.region = region
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak_proven is not None:
            result['AkProven'] = self.ak_proven
        if self.mock is not None:
            result['mock'] = self.mock
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProven') is not None:
            self.ak_proven = m.get('AkProven')
        if m.get('mock') is not None:
            self.mock = m.get('mock')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetQuotaResponseBodyBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodyDataBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodyDataSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodyDataScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoListParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        enable_priority: bool = None,
        force_reserved_min: bool = None,
        max_cu: int = None,
        min_cu: int = None,
        scheduler_type: str = None,
        single_job_culimit: int = None,
    ):
        self.elastic_reserved_cu = elastic_reserved_cu
        self.enable_priority = enable_priority
        self.force_reserved_min = force_reserved_min
        # This parameter is required.
        self.max_cu = max_cu
        # This parameter is required.
        self.min_cu = min_cu
        self.scheduler_type = scheduler_type
        self.single_job_culimit = single_job_culimit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        if self.enable_priority is not None:
            result['enablePriority'] = self.enable_priority
        if self.force_reserved_min is not None:
            result['forceReservedMin'] = self.force_reserved_min
        if self.max_cu is not None:
            result['maxCU'] = self.max_cu
        if self.min_cu is not None:
            result['minCU'] = self.min_cu
        if self.scheduler_type is not None:
            result['schedulerType'] = self.scheduler_type
        if self.single_job_culimit is not None:
            result['singleJobCULimit'] = self.single_job_culimit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        if m.get('enablePriority') is not None:
            self.enable_priority = m.get('enablePriority')
        if m.get('forceReservedMin') is not None:
            self.force_reserved_min = m.get('forceReservedMin')
        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')
        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')
        if m.get('schedulerType') is not None:
            self.scheduler_type = m.get('schedulerType')
        if m.get('singleJobCULimit') is not None:
            self.single_job_culimit = m.get('singleJobCULimit')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class GetQuotaResponseBodyDataSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaResponseBodyDataSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: GetQuotaResponseBodyDataSubQuotaInfoListParameter = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: GetQuotaResponseBodyDataSubQuotaInfoListSaleTag = None,
        schedule_info: GetQuotaResponseBodyDataSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information about the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The nickname of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information about the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.parameter:
            self.parameter.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodyDataSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            temp_model = GetQuotaResponseBodyDataSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodyDataSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodyDataSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponseBodyData(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaResponseBodyDataBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: GetQuotaResponseBodyDataSaleTag = None,
        schedule_info: GetQuotaResponseBodyDataScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[GetQuotaResponseBodyDataSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information about the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The quota ID.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information about the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The information about the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodyDataBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodyDataSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodyDataScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = GetQuotaResponseBodyDataSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponseBodySaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodyScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class GetQuotaResponseBodySubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaResponseBodySubQuotaInfoListParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        enable_priority: bool = None,
        force_reserved_min: bool = None,
        max_cu: int = None,
        min_cu: int = None,
        scheduler_type: str = None,
        single_job_culimit: int = None,
    ):
        self.elastic_reserved_cu = elastic_reserved_cu
        self.enable_priority = enable_priority
        self.force_reserved_min = force_reserved_min
        # This parameter is required.
        self.max_cu = max_cu
        # This parameter is required.
        self.min_cu = min_cu
        self.scheduler_type = scheduler_type
        self.single_job_culimit = single_job_culimit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        if self.enable_priority is not None:
            result['enablePriority'] = self.enable_priority
        if self.force_reserved_min is not None:
            result['forceReservedMin'] = self.force_reserved_min
        if self.max_cu is not None:
            result['maxCU'] = self.max_cu
        if self.min_cu is not None:
            result['minCU'] = self.min_cu
        if self.scheduler_type is not None:
            result['schedulerType'] = self.scheduler_type
        if self.single_job_culimit is not None:
            result['singleJobCULimit'] = self.single_job_culimit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        if m.get('enablePriority') is not None:
            self.enable_priority = m.get('enablePriority')
        if m.get('forceReservedMin') is not None:
            self.force_reserved_min = m.get('forceReservedMin')
        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')
        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')
        if m.get('schedulerType') is not None:
            self.scheduler_type = m.get('schedulerType')
        if m.get('singleJobCULimit') is not None:
            self.single_job_culimit = m.get('singleJobCULimit')
        return self


class GetQuotaResponseBodySubQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetQuotaResponseBodySubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class GetQuotaResponseBodySubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaResponseBodySubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: GetQuotaResponseBodySubQuotaInfoListParameter = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: GetQuotaResponseBodySubQuotaInfoListSaleTag = None,
        schedule_info: GetQuotaResponseBodySubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information about the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The alias of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information about the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.parameter:
            self.parameter.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodySubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            temp_model = GetQuotaResponseBodySubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodySubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodySubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponseBody(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaResponseBodyBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        data: GetQuotaResponseBodyData = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        request_id: str = None,
        sale_tag: GetQuotaResponseBodySaleTag = None,
        schedule_info: GetQuotaResponseBodyScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[GetQuotaResponseBodySubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information about the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The returned data.
        self.data = data
        # The quota ID.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information about the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The information about the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.data:
            self.data.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaResponseBodyBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('data') is not None:
            temp_model = GetQuotaResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('saleTag') is not None:
            temp_model = GetQuotaResponseBodySaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaResponseBodyScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = GetQuotaResponseBodySubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaPlanRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        tenant_id: str = None,
    ):
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetQuotaPlanResponseBodyDataQuotaBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaPlanResponseBodyDataQuotaScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        schedule_info: GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the user who created the quota plan.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The alias of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaPlanResponseBodyDataQuota(TeaModel):
    def __init__(
        self,
        billing_policy: GetQuotaPlanResponseBodyDataQuotaBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        schedule_info: GetQuotaPlanResponseBodyDataQuotaScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the quota plan was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the quota.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The information of the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuotaScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = GetQuotaPlanResponseBodyDataQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetQuotaPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        name: str = None,
        quota: GetQuotaPlanResponseBodyDataQuota = None,
    ):
        # The time when the quota plan was created.
        self.create_time = create_time
        # The name of the quota plan.
        self.name = name
        # The details of the quota.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = GetQuotaPlanResponseBodyDataQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class GetQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: GetQuotaPlanResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetQuotaPlanResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaScheduleRequest(TeaModel):
    def __init__(
        self,
        display_timezone: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The time zone.
        self.display_timezone = display_timezone
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_timezone is not None:
            result['displayTimezone'] = self.display_timezone
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayTimezone') is not None:
            self.display_timezone = m.get('displayTimezone')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetQuotaScheduleResponseBodyDataCondition(TeaModel):
    def __init__(
        self,
        after: str = None,
        at: str = None,
    ):
        # The start time when the quota plan takes effect.
        self.after = after
        # The time when the quota plan takes effect.
        self.at = at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.after is not None:
            result['after'] = self.after
        if self.at is not None:
            result['at'] = self.at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('after') is not None:
            self.after = m.get('after')
        if m.get('at') is not None:
            self.at = m.get('at')
        return self


class GetQuotaScheduleResponseBodyData(TeaModel):
    def __init__(
        self,
        condition: GetQuotaScheduleResponseBodyDataCondition = None,
        id: str = None,
        operator: str = None,
        plan: str = None,
        timezone: str = None,
        type: str = None,
    ):
        # The condition value.
        self.condition = condition
        # The ID of the quota plan.
        self.id = id
        # The name of the operator.
        self.operator = operator
        # The name of the quota plan.
        self.plan = plan
        # The time zone.
        self.timezone = timezone
        # The type of the quota plan.
        self.type = type

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition.to_map()
        if self.id is not None:
            result['id'] = self.id
        if self.operator is not None:
            result['operator'] = self.operator
        if self.plan is not None:
            result['plan'] = self.plan
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            temp_model = GetQuotaScheduleResponseBodyDataCondition()
            self.condition = temp_model.from_map(m['condition'])
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('plan') is not None:
            self.plan = m.get('plan')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetQuotaScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: List[GetQuotaScheduleResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetQuotaScheduleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetQuotaScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaScheduleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQuotaScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaUsageRequest(TeaModel):
    def __init__(
        self,
        agg_method: str = None,
        from_: int = None,
        plot_types: List[str] = None,
        product_id: str = None,
        region: str = None,
        sub_quota_nickname: str = None,
        tenant_id: str = None,
        to: int = None,
        y_axis_types: List[str] = None,
    ):
        # The aggregation algorithm. For a better page experience, up to 60 points can be displayed for each metric. If you select a time range longer than 1 hour, the chart uses the average value within the range (minutes of the selected time range/60) to aggregate data by default. You can change the aggregation algorithm based on your business requirements.
        self.agg_method = agg_method
        # The time when the query starts. The value is the log time that is specified when log data is written.
        # 
        # *   The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the **from** parameter, but does not include the end time specified by the **to** parameter. If you set the **from** and **to** parameters to the same value, the time range is invalid and an error message is returned.
        # *   This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # The types of the charts.
        self.plot_types = plot_types
        # The quota type. Default value: ODPS.
        # 
        # *   ODPS: computing quota
        # *   TUNNEL: Tunnel quota
        self.product_id = product_id
        # The region ID.
        self.region = region
        # The alias of the level-2 quota.
        self.sub_quota_nickname = sub_quota_nickname
        # The ID of the tenant. You can log on to the MaxCompute console, and choose Tenants > Tenant Property from the left-side navigation pane to view the tenant ID.
        self.tenant_id = tenant_id
        # The time when the query ends. The value is the log time that is specified when log data is written.
        # 
        # *   The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the **from** parameter, but does not include the end time specified by the **to** parameter. If you set the **from** and **to** parameters to the same value, the time range is invalid and an error message is returned.
        # *   This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to
        # The data metric fields.
        self.y_axis_types = y_axis_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agg_method is not None:
            result['aggMethod'] = self.agg_method
        if self.from_ is not None:
            result['from'] = self.from_
        if self.plot_types is not None:
            result['plotTypes'] = self.plot_types
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.region is not None:
            result['region'] = self.region
        if self.sub_quota_nickname is not None:
            result['subQuotaNickname'] = self.sub_quota_nickname
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.to is not None:
            result['to'] = self.to
        if self.y_axis_types is not None:
            result['yAxisTypes'] = self.y_axis_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggMethod') is not None:
            self.agg_method = m.get('aggMethod')
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('plotTypes') is not None:
            self.plot_types = m.get('plotTypes')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('subQuotaNickname') is not None:
            self.sub_quota_nickname = m.get('subQuotaNickname')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('yAxisTypes') is not None:
            self.y_axis_types = m.get('yAxisTypes')
        return self


class GetQuotaUsageShrinkRequest(TeaModel):
    def __init__(
        self,
        agg_method: str = None,
        from_: int = None,
        plot_types_shrink: str = None,
        product_id: str = None,
        region: str = None,
        sub_quota_nickname: str = None,
        tenant_id: str = None,
        to: int = None,
        y_axis_types_shrink: str = None,
    ):
        # The aggregation algorithm. For a better page experience, up to 60 points can be displayed for each metric. If you select a time range longer than 1 hour, the chart uses the average value within the range (minutes of the selected time range/60) to aggregate data by default. You can change the aggregation algorithm based on your business requirements.
        self.agg_method = agg_method
        # The time when the query starts. The value is the log time that is specified when log data is written.
        # 
        # *   The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the **from** parameter, but does not include the end time specified by the **to** parameter. If you set the **from** and **to** parameters to the same value, the time range is invalid and an error message is returned.
        # *   This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # The types of the charts.
        self.plot_types_shrink = plot_types_shrink
        # The quota type. Default value: ODPS.
        # 
        # *   ODPS: computing quota
        # *   TUNNEL: Tunnel quota
        self.product_id = product_id
        # The region ID.
        self.region = region
        # The alias of the level-2 quota.
        self.sub_quota_nickname = sub_quota_nickname
        # The ID of the tenant. You can log on to the MaxCompute console, and choose Tenants > Tenant Property from the left-side navigation pane to view the tenant ID.
        self.tenant_id = tenant_id
        # The time when the query ends. The value is the log time that is specified when log data is written.
        # 
        # *   The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the **from** parameter, but does not include the end time specified by the **to** parameter. If you set the **from** and **to** parameters to the same value, the time range is invalid and an error message is returned.
        # *   This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to
        # The data metric fields.
        self.y_axis_types_shrink = y_axis_types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agg_method is not None:
            result['aggMethod'] = self.agg_method
        if self.from_ is not None:
            result['from'] = self.from_
        if self.plot_types_shrink is not None:
            result['plotTypes'] = self.plot_types_shrink
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.region is not None:
            result['region'] = self.region
        if self.sub_quota_nickname is not None:
            result['subQuotaNickname'] = self.sub_quota_nickname
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.to is not None:
            result['to'] = self.to
        if self.y_axis_types_shrink is not None:
            result['yAxisTypes'] = self.y_axis_types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggMethod') is not None:
            self.agg_method = m.get('aggMethod')
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('plotTypes') is not None:
            self.plot_types_shrink = m.get('plotTypes')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('subQuotaNickname') is not None:
            self.sub_quota_nickname = m.get('subQuotaNickname')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('yAxisTypes') is not None:
            self.y_axis_types_shrink = m.get('yAxisTypes')
        return self


class GetQuotaUsageResponseBodyDataPlot(TeaModel):
    def __init__(
        self,
        title: str = None,
        type: str = None,
        y_axis: List[str] = None,
    ):
        # The title of the chart.
        self.title = title
        # The type of the chart.
        self.type = type
        # The data metric field.
        self.y_axis = y_axis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        if self.y_axis is not None:
            result['yAxis'] = self.y_axis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('yAxis') is not None:
            self.y_axis = m.get('yAxis')
        return self


class GetQuotaUsageResponseBodyData(TeaModel):
    def __init__(
        self,
        metrics: Dict[str, Any] = None,
        plot: List[GetQuotaUsageResponseBodyDataPlot] = None,
    ):
        # The metric results.
        self.metrics = metrics
        # The information about the chart.
        self.plot = plot

    def validate(self):
        if self.plot:
            for k in self.plot:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metrics is not None:
            result['metrics'] = self.metrics
        result['plot'] = []
        if self.plot is not None:
            for k in self.plot:
                result['plot'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metrics') is not None:
            self.metrics = m.get('metrics')
        self.plot = []
        if m.get('plot') is not None:
            for k in m.get('plot'):
                temp_model = GetQuotaUsageResponseBodyDataPlot()
                self.plot.append(temp_model.from_map(k))
        return self


class GetQuotaUsageResponseBody(TeaModel):
    def __init__(
        self,
        data: GetQuotaUsageResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # *   1xx: informational response. The request is received and is being processed.
        # *   2xx: success. The request is successfully received, understood, and accepted by the server.
        # *   3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # *   4xx: client error. The request contains invalid request parameters and syntaxes, or specific request conditions cannot be met.
        # *   5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetQuotaUsageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetQuotaUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaUsageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetQuotaUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleAclResponseBodyDataFunction(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the function.
        self.actions = actions
        # The name of the function.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyDataInstance(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the instance.
        self.actions = actions
        # The name of the instance.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyDataPackage(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the package.
        self.actions = actions
        # The name of the package.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyDataProject(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the project.
        self.actions = actions
        # The name of the MaxCompute project.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyDataResource(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the resource.
        self.actions = actions
        # The name of the resource.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyDataTable(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
        schema_name: str = None,
    ):
        # The operations that were performed on the table.
        self.actions = actions
        # The name of the table.
        self.name = name
        # The Schema name.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class GetRoleAclResponseBodyData(TeaModel):
    def __init__(
        self,
        function: List[GetRoleAclResponseBodyDataFunction] = None,
        instance: List[GetRoleAclResponseBodyDataInstance] = None,
        package: List[GetRoleAclResponseBodyDataPackage] = None,
        project: List[GetRoleAclResponseBodyDataProject] = None,
        resource: List[GetRoleAclResponseBodyDataResource] = None,
        table: List[GetRoleAclResponseBodyDataTable] = None,
    ):
        # The function.
        self.function = function
        # The instance.
        self.instance = instance
        # The package.
        self.package = package
        # The project.
        self.project = project
        # The resource.
        self.resource = resource
        # The table.
        self.table = table

    def validate(self):
        if self.function:
            for k in self.function:
                if k:
                    k.validate()
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()
        if self.package:
            for k in self.package:
                if k:
                    k.validate()
        if self.project:
            for k in self.project:
                if k:
                    k.validate()
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['function'] = []
        if self.function is not None:
            for k in self.function:
                result['function'].append(k.to_map() if k else None)
        result['instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['instance'].append(k.to_map() if k else None)
        result['package'] = []
        if self.package is not None:
            for k in self.package:
                result['package'].append(k.to_map() if k else None)
        result['project'] = []
        if self.project is not None:
            for k in self.project:
                result['project'].append(k.to_map() if k else None)
        result['resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['resource'].append(k.to_map() if k else None)
        result['table'] = []
        if self.table is not None:
            for k in self.table:
                result['table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function = []
        if m.get('function') is not None:
            for k in m.get('function'):
                temp_model = GetRoleAclResponseBodyDataFunction()
                self.function.append(temp_model.from_map(k))
        self.instance = []
        if m.get('instance') is not None:
            for k in m.get('instance'):
                temp_model = GetRoleAclResponseBodyDataInstance()
                self.instance.append(temp_model.from_map(k))
        self.package = []
        if m.get('package') is not None:
            for k in m.get('package'):
                temp_model = GetRoleAclResponseBodyDataPackage()
                self.package.append(temp_model.from_map(k))
        self.project = []
        if m.get('project') is not None:
            for k in m.get('project'):
                temp_model = GetRoleAclResponseBodyDataProject()
                self.project.append(temp_model.from_map(k))
        self.resource = []
        if m.get('resource') is not None:
            for k in m.get('resource'):
                temp_model = GetRoleAclResponseBodyDataResource()
                self.resource.append(temp_model.from_map(k))
        self.table = []
        if m.get('table') is not None:
            for k in m.get('table'):
                temp_model = GetRoleAclResponseBodyDataTable()
                self.table.append(temp_model.from_map(k))
        return self


class GetRoleAclResponseBody(TeaModel):
    def __init__(
        self,
        data: GetRoleAclResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetRoleAclResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRoleAclResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoleAclResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRoleAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoleAclOnObjectRequest(TeaModel):
    def __init__(
        self,
        object_name: str = None,
        object_type: str = None,
    ):
        # The name of the object.
        # 
        # This parameter is required.
        self.object_name = object_name
        # The type of the object.
        # 
        # This parameter is required.
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.object_name is not None:
            result['objectName'] = self.object_name
        if self.object_type is not None:
            result['objectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectName') is not None:
            self.object_name = m.get('objectName')
        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')
        return self


class GetRoleAclOnObjectResponseBodyData(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
    ):
        # The operations that were performed on the object.
        self.actions = actions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        return self


class GetRoleAclOnObjectResponseBody(TeaModel):
    def __init__(
        self,
        data: GetRoleAclOnObjectResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetRoleAclOnObjectResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRoleAclOnObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoleAclOnObjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRoleAclOnObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRolePolicyResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRolePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRolePolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRolePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunningJobsRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        job_owner_list: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        quota_nickname_list: List[str] = None,
        to: int = None,
    ):
        # The time when the query starts. This parameter specifies the time when a job is submitted.
        # 
        # *   The time range that is specified by the **from** and **to** request parameters is a closed interval. The start time and end time are included in the range. If the value of **from** is the same as the value of **to**, the time range is invalid, and a null value is returned.
        # *   The value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # The list of job executors.
        self.job_owner_list = job_owner_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 20.
        self.page_size = page_size
        # The list of nicknames of quotas that are used by jobs.
        self.quota_nickname_list = quota_nickname_list
        # The time when the query ends. This parameter specifies the time when a job is submitted.
        # 
        # *   The time interval that is specified by the **from** and **to** request parameters is a closed interval. The start time and end time are included in the interval. If the value of **from** is the same as the value of **to**, the interval is invalid, and a null value is returned.
        # *   The value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.job_owner_list is not None:
            result['jobOwnerList'] = self.job_owner_list
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.quota_nickname_list is not None:
            result['quotaNicknameList'] = self.quota_nickname_list
        if self.to is not None:
            result['to'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('jobOwnerList') is not None:
            self.job_owner_list = m.get('jobOwnerList')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('quotaNicknameList') is not None:
            self.quota_nickname_list = m.get('quotaNicknameList')
        if m.get('to') is not None:
            self.to = m.get('to')
        return self


class GetRunningJobsShrinkRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        job_owner_list_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        quota_nickname_list_shrink: str = None,
        to: int = None,
    ):
        # The time when the query starts. This parameter specifies the time when a job is submitted.
        # 
        # *   The time range that is specified by the **from** and **to** request parameters is a closed interval. The start time and end time are included in the range. If the value of **from** is the same as the value of **to**, the time range is invalid, and a null value is returned.
        # *   The value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # The list of job executors.
        self.job_owner_list_shrink = job_owner_list_shrink
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 20.
        self.page_size = page_size
        # The list of nicknames of quotas that are used by jobs.
        self.quota_nickname_list_shrink = quota_nickname_list_shrink
        # The time when the query ends. This parameter specifies the time when a job is submitted.
        # 
        # *   The time interval that is specified by the **from** and **to** request parameters is a closed interval. The start time and end time are included in the interval. If the value of **from** is the same as the value of **to**, the interval is invalid, and a null value is returned.
        # *   The value is a UNIX timestamp that represents the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.job_owner_list_shrink is not None:
            result['jobOwnerList'] = self.job_owner_list_shrink
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.quota_nickname_list_shrink is not None:
            result['quotaNicknameList'] = self.quota_nickname_list_shrink
        if self.to is not None:
            result['to'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('jobOwnerList') is not None:
            self.job_owner_list_shrink = m.get('jobOwnerList')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('quotaNicknameList') is not None:
            self.quota_nickname_list_shrink = m.get('quotaNicknameList')
        if m.get('to') is not None:
            self.to = m.get('to')
        return self


class GetRunningJobsResponseBodyDataRunningJobInfoList(TeaModel):
    def __init__(
        self,
        cu_snapshot: float = None,
        instance_id: str = None,
        job_owner: str = None,
        memory_snapshot: float = None,
        progress: float = None,
        project: str = None,
        quota_nickname: str = None,
        running_at_time: int = None,
        submitted_at_time: int = None,
    ):
        # The compute unit (CU) snapshot proportion of the job.
        self.cu_snapshot = cu_snapshot
        # The instance ID.
        self.instance_id = instance_id
        # The account that submits the job.
        self.job_owner = job_owner
        # The memory snapshot proportion of the job.
        self.memory_snapshot = memory_snapshot
        # The progress of the job.
        self.progress = progress
        # The name of the MaxCompute project.
        self.project = project
        # The nickname of the quota that is used by the job.
        self.quota_nickname = quota_nickname
        # The time when the job starts to run.
        self.running_at_time = running_at_time
        # The time when the job is submitted.
        self.submitted_at_time = submitted_at_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_snapshot is not None:
            result['cuSnapshot'] = self.cu_snapshot
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner
        if self.memory_snapshot is not None:
            result['memorySnapshot'] = self.memory_snapshot
        if self.progress is not None:
            result['progress'] = self.progress
        if self.project is not None:
            result['project'] = self.project
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        if self.running_at_time is not None:
            result['runningAtTime'] = self.running_at_time
        if self.submitted_at_time is not None:
            result['submittedAtTime'] = self.submitted_at_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuSnapshot') is not None:
            self.cu_snapshot = m.get('cuSnapshot')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')
        if m.get('memorySnapshot') is not None:
            self.memory_snapshot = m.get('memorySnapshot')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        if m.get('runningAtTime') is not None:
            self.running_at_time = m.get('runningAtTime')
        if m.get('submittedAtTime') is not None:
            self.submitted_at_time = m.get('submittedAtTime')
        return self


class GetRunningJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        running_job_info_list: List[GetRunningJobsResponseBodyDataRunningJobInfoList] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The list of jobs in the running state.
        self.running_job_info_list = running_job_info_list
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.running_job_info_list:
            for k in self.running_job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['runningJobInfoList'] = []
        if self.running_job_info_list is not None:
            for k in self.running_job_info_list:
                result['runningJobInfoList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.running_job_info_list = []
        if m.get('runningJobInfoList') is not None:
            for k in m.get('runningJobInfoList'):
                temp_model = GetRunningJobsResponseBodyDataRunningJobInfoList()
                self.running_job_info_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class GetRunningJobsResponseBody(TeaModel):
    def __init__(
        self,
        data: GetRunningJobsResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetRunningJobsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRunningJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRunningJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRunningJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStorageAmountSummaryRequest(TeaModel):
    def __init__(
        self,
        date: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        self.date = date
        self.region = region
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetStorageAmountSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        date: str = None,
        timestamp: int = None,
        unit: Dict[str, str] = None,
        value: Dict[str, int] = None,
    ):
        self.date = date
        self.timestamp = timestamp
        self.unit = unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.unit is not None:
            result['unit'] = self.unit
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetStorageAmountSummaryResponseBody(TeaModel):
    def __init__(
        self,
        data: GetStorageAmountSummaryResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetStorageAmountSummaryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetStorageAmountSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStorageAmountSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetStorageAmountSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStorageSizeSummaryRequest(TeaModel):
    def __init__(
        self,
        date: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        self.date = date
        self.region = region
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetStorageSizeSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        date: str = None,
        timestamp: int = None,
        unit: Dict[str, str] = None,
        value: Dict[str, float] = None,
    ):
        self.date = date
        self.timestamp = timestamp
        self.unit = unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.unit is not None:
            result['unit'] = self.unit
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetStorageSizeSummaryResponseBody(TeaModel):
    def __init__(
        self,
        data: GetStorageSizeSummaryResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetStorageSizeSummaryResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetStorageSizeSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStorageSizeSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetStorageSizeSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStorageSummaryComparedRequest(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        projects: List[str] = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # This parameter is required.
        self.begin_date = begin_date
        # This parameter is required.
        self.end_date = end_date
        self.projects = projects
        self.region = region
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['beginDate'] = self.begin_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.projects is not None:
            result['projects'] = self.projects
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginDate') is not None:
            self.begin_date = m.get('beginDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('projects') is not None:
            self.projects = m.get('projects')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetStorageSummaryComparedShrinkRequest(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        projects_shrink: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # This parameter is required.
        self.begin_date = begin_date
        # This parameter is required.
        self.end_date = end_date
        self.projects_shrink = projects_shrink
        self.region = region
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['beginDate'] = self.begin_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.projects_shrink is not None:
            result['projects'] = self.projects_shrink
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginDate') is not None:
            self.begin_date = m.get('beginDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('projects') is not None:
            self.projects_shrink = m.get('projects')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class GetStorageSummaryComparedResponseBodyData(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        rate: Dict[str, float] = None,
        unit: Dict[str, str] = None,
        value: Dict[str, float] = None,
    ):
        self.begin_date = begin_date
        self.end_date = end_date
        self.rate = rate
        self.unit = unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['beginDate'] = self.begin_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.rate is not None:
            result['rate'] = self.rate
        if self.unit is not None:
            result['unit'] = self.unit
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginDate') is not None:
            self.begin_date = m.get('beginDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetStorageSummaryComparedResponseBody(TeaModel):
    def __init__(
        self,
        data: GetStorageSummaryComparedResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetStorageSummaryComparedResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetStorageSummaryComparedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStorageSummaryComparedResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetStorageSummaryComparedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableInfoRequest(TeaModel):
    def __init__(
        self,
        schema_name: str = None,
        type: str = None,
    ):
        # The name of the schema to which the table or view belongs.
        self.schema_name = schema_name
        # The type of the table or view that you want to view. Valid values:
        # 
        # *   **internal**: internal table
        # *   **external**: external table
        # *   **view**: view
        # *   **materializedView**: [materialize view](https://www.alibabacloud.com/help/maxcompute/user-guide/materialized-view-operations)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTableInfoResponseBodyDataClusterInfoSortCols(TeaModel):
    def __init__(
        self,
        name: str = None,
        order: str = None,
    ):
        # The name of the sorting field.
        self.name = name
        # The sorting order.
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.order is not None:
            result['order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('order') is not None:
            self.order = m.get('order')
        return self


class GetTableInfoResponseBodyDataClusterInfo(TeaModel):
    def __init__(
        self,
        bucket_num: int = None,
        cluster_cols: List[str] = None,
        cluster_type: str = None,
        sort_cols: List[GetTableInfoResponseBodyDataClusterInfoSortCols] = None,
    ):
        # Optional. The number of buckets in the clustered table. The value 0 indicates that the number of buckets dynamically changes when a job is running.
        self.bucket_num = bucket_num
        # The cluster keys.
        self.cluster_cols = cluster_cols
        # The clustering type of the table. MaxCompute supports [hash clustering](https://www.alibabacloud.com/help/maxcompute/use-cases/hash-clustering) and
        # 
        # [range clustering](https://www.alibabacloud.com/help/maxcompute/use-cases/range-clustering).
        self.cluster_type = cluster_type
        # The condition by which the results are sorted.
        self.sort_cols = sort_cols

    def validate(self):
        if self.sort_cols:
            for k in self.sort_cols:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_num is not None:
            result['bucketNum'] = self.bucket_num
        if self.cluster_cols is not None:
            result['clusterCols'] = self.cluster_cols
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        result['sortCols'] = []
        if self.sort_cols is not None:
            for k in self.sort_cols:
                result['sortCols'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketNum') is not None:
            self.bucket_num = m.get('bucketNum')
        if m.get('clusterCols') is not None:
            self.cluster_cols = m.get('clusterCols')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        self.sort_cols = []
        if m.get('sortCols') is not None:
            for k in m.get('sortCols'):
                temp_model = GetTableInfoResponseBodyDataClusterInfoSortCols()
                self.sort_cols.append(temp_model.from_map(k))
        return self


class GetTableInfoResponseBodyDataNativeColumns(TeaModel):
    def __init__(
        self,
        comment: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
    ):
        # The column comments.
        self.comment = comment
        # The sensitivity-level label of the column. For more information, see [Label-based access control](https://www.alibabacloud.com/help/maxcompute/user-guide/label-based-access-control).
        self.label = label
        # The column name.
        self.name = name
        # The column type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.label is not None:
            result['label'] = self.label
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTableInfoResponseBodyDataPartitionColumns(TeaModel):
    def __init__(
        self,
        comment: str = None,
        label: str = None,
        name: str = None,
        type: str = None,
    ):
        # The comments of the partition key column.
        self.comment = comment
        # The sensitivity-level label of the column. For more information, see [Label-based access control](https://www.alibabacloud.com/help/maxcompute/user-guide/label-based-access-control).
        self.label = label
        # The partition name.
        self.name = name
        # The partition column type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.label is not None:
            result['label'] = self.label
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetTableInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_refresh_enabled: bool = None,
        cluster_info: GetTableInfoResponseBodyDataClusterInfo = None,
        comment: str = None,
        create_table_ddl: str = None,
        creation_time: int = None,
        display_name: str = None,
        file_num: int = None,
        is_external_table: bool = None,
        is_outdated: bool = None,
        last_access_time: int = None,
        last_ddltime: int = None,
        last_modified_time: int = None,
        lifecycle: str = None,
        location: str = None,
        materialized_view: bool = None,
        name: str = None,
        native_columns: List[GetTableInfoResponseBodyDataNativeColumns] = None,
        odps_properties_rolearn: str = None,
        odps_sql_text_option_flush_header: bool = None,
        odps_text_option_header_lines_count: int = None,
        owner: str = None,
        partition_columns: List[GetTableInfoResponseBodyDataPartitionColumns] = None,
        physical_size: int = None,
        project_name: str = None,
        rewrite_enabled: bool = None,
        schema: str = None,
        size: int = None,
        storage_handler: str = None,
        table_label: str = None,
        tablesotre_table_name: str = None,
        tablestore_columns_mapping: str = None,
        type: str = None,
        view_text: str = None,
    ):
        # Indicates whether the materialized view is automatically refreshed. This response parameter is returned when type is set to materializedView.
        self.auto_refresh_enabled = auto_refresh_enabled
        # The clustering attribute. This response parameter is returned when the table is a clustered table.
        self.cluster_info = cluster_info
        # The comments of the table.
        self.comment = comment
        # DDL statement to create a table.
        self.create_table_ddl = create_table_ddl
        # The creation time.
        self.creation_time = creation_time
        # The display name.
        self.display_name = display_name
        # The number of file of the table.
        self.file_num = file_num
        # Indicates whether the table is an external table. This response parameter is returned when type is set to external.
        self.is_external_table = is_external_table
        # Indicates whether data of the materialized view is invalid due to changes in the data of the source table. This response parameter is returned when type is set to materializedView.
        self.is_outdated = is_outdated
        # The time when data of the table or view was last accessed.
        self.last_access_time = last_access_time
        # The time when the data definition language (DDL) statement of the table or view was last modified.
        self.last_ddltime = last_ddltime
        # The time when data of the table or view was last modified.
        self.last_modified_time = last_modified_time
        # The lifecycle. Unit: days.
        self.lifecycle = lifecycle
        # The path of the external table. This response parameter is returned when type is set to external.
        self.location = location
        # Indicates whether the table or view is a [materialize view](https://www.alibabacloud.com/help/maxcompute/user-guide/materialized-view-operations).
        self.materialized_view = materialized_view
        # The name of the table or view.
        self.name = name
        # The field information.
        self.native_columns = native_columns
        # The Alibaba Cloud Resource Name (ARN) of the role AliyunODPSDefaultRole in Resource Access Management (RAM). This response parameter is returned when type is set to external.
        self.odps_properties_rolearn = odps_properties_rolearn
        # Indicates whether the table header is ignored. This response parameter is returned when type is set to external.
        self.odps_sql_text_option_flush_header = odps_sql_text_option_flush_header
        # The first N rows that were ignored in the table header. This response parameter is returned when type is set to external.
        self.odps_text_option_header_lines_count = odps_text_option_header_lines_count
        # The account information of the table or view owner.
        self.owner = owner
        # The information about partition key columns. This response parameter is returned only for partitioned tables.
        self.partition_columns = partition_columns
        # The physical size of the table.
        self.physical_size = physical_size
        # The name of the project to which the table or view belongs.
        self.project_name = project_name
        # Indicates whether the query rewrite operation can be performed by using the materialized view. This response parameter is returned when type is set to materializedView.
        self.rewrite_enabled = rewrite_enabled
        # The name of the schema to which the table or the view belongs.
        self.schema = schema
        # The data size of the non-partitioned table. If the table is a partitioned table, the system does not calculate the data size of the table. In this case, the value of this parameter is NULL. The PARTITIONS view includes the data size of each partition in a partitioned table. Unit: bytes.
        self.size = size
        # The storage handler of the external table. This response parameter is returned when type is set to external.
        self.storage_handler = storage_handler
        # The sensitivity-level label of the table. For more information, see [Label-based access control](https://www.alibabacloud.com/help/maxcompute/user-guide/label-based-access-control).
        self.table_label = table_label
        # The name of the Tablestore table to be accessed. This response parameter is returned when type is set to external.
        self.tablesotre_table_name = tablesotre_table_name
        # The columns of the Tablestore table to be accessed, including the primary key column and attribute column. This response parameter is returned when type is set to external.
        self.tablestore_columns_mapping = tablestore_columns_mapping
        # The type of the table or view. Valid values:
        # 
        # *   **internal**: internal table
        # *   **external**: external table
        # *   **view**: view
        # *   **materializedView**: [materialize view](https://www.alibabacloud.com/help/maxcompute/user-guide/materialized-view-operations)
        self.type = type
        # The statement that generates the view. This response parameter is returned when type is set to view.
        self.view_text = view_text

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()
        if self.native_columns:
            for k in self.native_columns:
                if k:
                    k.validate()
        if self.partition_columns:
            for k in self.partition_columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_refresh_enabled is not None:
            result['autoRefreshEnabled'] = self.auto_refresh_enabled
        if self.cluster_info is not None:
            result['clusterInfo'] = self.cluster_info.to_map()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.create_table_ddl is not None:
            result['createTableDDL'] = self.create_table_ddl
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.file_num is not None:
            result['fileNum'] = self.file_num
        if self.is_external_table is not None:
            result['isExternalTable'] = self.is_external_table
        if self.is_outdated is not None:
            result['isOutdated'] = self.is_outdated
        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time
        if self.last_ddltime is not None:
            result['lastDDLTime'] = self.last_ddltime
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.lifecycle is not None:
            result['lifecycle'] = self.lifecycle
        if self.location is not None:
            result['location'] = self.location
        if self.materialized_view is not None:
            result['materializedView'] = self.materialized_view
        if self.name is not None:
            result['name'] = self.name
        result['nativeColumns'] = []
        if self.native_columns is not None:
            for k in self.native_columns:
                result['nativeColumns'].append(k.to_map() if k else None)
        if self.odps_properties_rolearn is not None:
            result['odpsPropertiesRolearn'] = self.odps_properties_rolearn
        if self.odps_sql_text_option_flush_header is not None:
            result['odpsSqlTextOptionFlushHeader'] = self.odps_sql_text_option_flush_header
        if self.odps_text_option_header_lines_count is not None:
            result['odpsTextOptionHeaderLinesCount'] = self.odps_text_option_header_lines_count
        if self.owner is not None:
            result['owner'] = self.owner
        result['partitionColumns'] = []
        if self.partition_columns is not None:
            for k in self.partition_columns:
                result['partitionColumns'].append(k.to_map() if k else None)
        if self.physical_size is not None:
            result['physicalSize'] = self.physical_size
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.rewrite_enabled is not None:
            result['rewriteEnabled'] = self.rewrite_enabled
        if self.schema is not None:
            result['schema'] = self.schema
        if self.size is not None:
            result['size'] = self.size
        if self.storage_handler is not None:
            result['storageHandler'] = self.storage_handler
        if self.table_label is not None:
            result['tableLabel'] = self.table_label
        if self.tablesotre_table_name is not None:
            result['tablesotreTableName'] = self.tablesotre_table_name
        if self.tablestore_columns_mapping is not None:
            result['tablestoreColumnsMapping'] = self.tablestore_columns_mapping
        if self.type is not None:
            result['type'] = self.type
        if self.view_text is not None:
            result['viewText'] = self.view_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRefreshEnabled') is not None:
            self.auto_refresh_enabled = m.get('autoRefreshEnabled')
        if m.get('clusterInfo') is not None:
            temp_model = GetTableInfoResponseBodyDataClusterInfo()
            self.cluster_info = temp_model.from_map(m['clusterInfo'])
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('createTableDDL') is not None:
            self.create_table_ddl = m.get('createTableDDL')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('fileNum') is not None:
            self.file_num = m.get('fileNum')
        if m.get('isExternalTable') is not None:
            self.is_external_table = m.get('isExternalTable')
        if m.get('isOutdated') is not None:
            self.is_outdated = m.get('isOutdated')
        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')
        if m.get('lastDDLTime') is not None:
            self.last_ddltime = m.get('lastDDLTime')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('lifecycle') is not None:
            self.lifecycle = m.get('lifecycle')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('materializedView') is not None:
            self.materialized_view = m.get('materializedView')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.native_columns = []
        if m.get('nativeColumns') is not None:
            for k in m.get('nativeColumns'):
                temp_model = GetTableInfoResponseBodyDataNativeColumns()
                self.native_columns.append(temp_model.from_map(k))
        if m.get('odpsPropertiesRolearn') is not None:
            self.odps_properties_rolearn = m.get('odpsPropertiesRolearn')
        if m.get('odpsSqlTextOptionFlushHeader') is not None:
            self.odps_sql_text_option_flush_header = m.get('odpsSqlTextOptionFlushHeader')
        if m.get('odpsTextOptionHeaderLinesCount') is not None:
            self.odps_text_option_header_lines_count = m.get('odpsTextOptionHeaderLinesCount')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        self.partition_columns = []
        if m.get('partitionColumns') is not None:
            for k in m.get('partitionColumns'):
                temp_model = GetTableInfoResponseBodyDataPartitionColumns()
                self.partition_columns.append(temp_model.from_map(k))
        if m.get('physicalSize') is not None:
            self.physical_size = m.get('physicalSize')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('rewriteEnabled') is not None:
            self.rewrite_enabled = m.get('rewriteEnabled')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('storageHandler') is not None:
            self.storage_handler = m.get('storageHandler')
        if m.get('tableLabel') is not None:
            self.table_label = m.get('tableLabel')
        if m.get('tablesotreTableName') is not None:
            self.tablesotre_table_name = m.get('tablesotreTableName')
        if m.get('tablestoreColumnsMapping') is not None:
            self.tablestore_columns_mapping = m.get('tablestoreColumnsMapping')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('viewText') is not None:
            self.view_text = m.get('viewText')
        return self


class GetTableInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTableInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetTableInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetTableInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTableInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrustedProjectsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetTrustedProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrustedProjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTrustedProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillJobsRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The ID of the region in which the instance resides.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class KillJobsResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class KillJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KillJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = KillJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComputeMetricsByInstanceRequest(TeaModel):
    def __init__(
        self,
        end_date: int = None,
        instance_id: str = None,
        job_owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_names: List[str] = None,
        region: str = None,
        signature: str = None,
        spec_codes: List[str] = None,
        start_date: int = None,
        types: List[str] = None,
    ):
        # The end time for the period.
        self.end_date = end_date
        # The job(instance) ID.
        self.instance_id = instance_id
        # The Alibaba Cloud account that is used to run the MaxCompute job.
        self.job_owner = job_owner
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The name of MaxCompute project.
        self.project_names = project_names
        # The region ID.
        self.region = region
        # The signature of the SQL job.
        self.signature = signature
        # Specification types.
        self.spec_codes = spec_codes
        # The start time for the period.
        self.start_date = start_date
        # Metering types.
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_names is not None:
            result['projectNames'] = self.project_names
        if self.region is not None:
            result['region'] = self.region
        if self.signature is not None:
            result['signature'] = self.signature
        if self.spec_codes is not None:
            result['specCodes'] = self.spec_codes
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectNames') is not None:
            self.project_names = m.get('projectNames')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('specCodes') is not None:
            self.spec_codes = m.get('specCodes')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class ListComputeMetricsByInstanceResponseBodyDataInstanceComputeMetrics(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        job_owner: str = None,
        project_name: str = None,
        signature: str = None,
        spec_code: str = None,
        submit_time: int = None,
        type: str = None,
        unit: str = None,
        usage: float = None,
    ):
        # The end time of the job execution.
        self.end_time = end_time
        # The job(instance) ID.
        self.instance_id = instance_id
        # The owner of the job.
        self.job_owner = job_owner
        # The name of the project.
        self.project_name = project_name
        # The signature of the SQL job.
        self.signature = signature
        # Specifications Type, specifies the resource package that you select when you purchase the MaxCompute service.
        # - OdpsStandard: the pay-as-you-go resource package.
        # 
        # - OdpsSpot: the pay-as-you-go spot resource package.
        self.spec_code = spec_code
        # The submission time of the job.
        self.submit_time = submit_time
        # Metering types.
        # - ComputationSql: the metering data of SQL jobs that involve internal tables.
        # 
        # - ComputationSqlOTS: the metering data of SQL jobs that involve Tablestore external tables.
        # 
        # - ComputationSqlOSS: the metering data of SQL jobs that involve OSS external tables.
        # 
        # - MapReduce: the metering data of MapReduce jobs.
        # 
        # - spark: the metering data of Spark jobs.
        # 
        # - mars: the metering data of Mars jobs.
        self.type = type
        # The unit of computing resource usage
        self.unit = unit
        # The computing resource usage is calculated based on the following items:
        # 
        # - Amount of scanned data in the unit of GB. For the jobs whose metering types are ComputationSql, ComputationSqlOTS, or ComputationSqlOSS, they are billed based on the amount of scanned data. The computing resource usage of such a job is calculated by using the following formula: Amount of scanned data × Complexity. The complexity is fixed at 1 for the jobs whose metering types are ComputationSqlOTS or ComputationSqlOSS.
        # 
        # - CU-hours. For the jobs whose metering types are MapReduce, spark, or mars, they are billed based on CU-hours.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.signature is not None:
            result['signature'] = self.signature
        if self.spec_code is not None:
            result['specCode'] = self.spec_code
        if self.submit_time is not None:
            result['submitTime'] = self.submit_time
        if self.type is not None:
            result['type'] = self.type
        if self.unit is not None:
            result['unit'] = self.unit
        if self.usage is not None:
            result['usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('specCode') is not None:
            self.spec_code = m.get('specCode')
        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('usage') is not None:
            self.usage = m.get('usage')
        return self


class ListComputeMetricsByInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_compute_metrics: List[ListComputeMetricsByInstanceResponseBodyDataInstanceComputeMetrics] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # List of pay-as-you-go job compute usage.
        self.instance_compute_metrics = instance_compute_metrics
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of results returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_compute_metrics:
            for k in self.instance_compute_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['instanceComputeMetrics'] = []
        if self.instance_compute_metrics is not None:
            for k in self.instance_compute_metrics:
                result['instanceComputeMetrics'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_compute_metrics = []
        if m.get('instanceComputeMetrics') is not None:
            for k in m.get('instanceComputeMetrics'):
                temp_model = ListComputeMetricsByInstanceResponseBodyDataInstanceComputeMetrics()
                self.instance_compute_metrics.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListComputeMetricsByInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: ListComputeMetricsByInstanceResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListComputeMetricsByInstanceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListComputeMetricsByInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListComputeMetricsByInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListComputeMetricsByInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComputeQuotaPlanResponseBodyDataPlanListQuotaParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        max_cu: int = None,
        min_cu: int = None,
    ):
        self.elastic_reserved_cu = elastic_reserved_cu
        self.max_cu = max_cu
        self.min_cu = min_cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        if self.max_cu is not None:
            result['maxCU'] = self.max_cu
        if self.min_cu is not None:
            result['minCU'] = self.min_cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')
        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')
        return self


class ListComputeQuotaPlanResponseBodyDataPlanListQuotaSubQuotaInfoListParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        max_cu: int = None,
        min_cu: int = None,
    ):
        self.elastic_reserved_cu = elastic_reserved_cu
        self.max_cu = max_cu
        self.min_cu = min_cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        if self.max_cu is not None:
            result['maxCU'] = self.max_cu
        if self.min_cu is not None:
            result['minCU'] = self.min_cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')
        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')
        return self


class ListComputeQuotaPlanResponseBodyDataPlanListQuotaSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: ListComputeQuotaPlanResponseBodyDataPlanListQuotaSubQuotaInfoListParameter = None,
        region_id: str = None,
        status: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # Cluster ID.
        self.cluster = cluster
        # The creation time.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The nickname of the level-2 quota.
        self.nick_name = nick_name
        # The description of the level-2 quota.
        self.parameter = parameter
        # Region ID.
        self.region_id = region_id
        # Resource status.
        self.status = status
        # Tenant ID.
        self.tenant_id = tenant_id
        # The type of quota.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            temp_model = ListComputeQuotaPlanResponseBodyDataPlanListQuotaSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListComputeQuotaPlanResponseBodyDataPlanListQuota(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: ListComputeQuotaPlanResponseBodyDataPlanListQuotaParameter = None,
        region_id: str = None,
        status: str = None,
        sub_quota_info_list: List[ListComputeQuotaPlanResponseBodyDataPlanListQuotaSubQuotaInfoList] = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # Cluster ID.
        self.cluster = cluster
        # The time when the level-1 quota was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-1 quota.
        self.id = id
        # The name of the level-1 quota.
        self.name = name
        # The nickname of the level-1 quota.
        self.nick_name = nick_name
        # The description of the level-1 quota.
        self.parameter = parameter
        # Region ID.
        self.region_id = region_id
        # Resource status.
        self.status = status
        # The list of subquotas.
        self.sub_quota_info_list = sub_quota_info_list
        # Tenant ID.
        self.tenant_id = tenant_id
        # The type of quota.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.parameter:
            self.parameter.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            temp_model = ListComputeQuotaPlanResponseBodyDataPlanListQuotaParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = ListComputeQuotaPlanResponseBodyDataPlanListQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListComputeQuotaPlanResponseBodyDataPlanList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        name: str = None,
        quota: ListComputeQuotaPlanResponseBodyDataPlanListQuota = None,
    ):
        # The time when the quota plan was created.
        self.create_time = create_time
        # The name of the quota plan.
        self.name = name
        # The details of the quota.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = ListComputeQuotaPlanResponseBodyDataPlanListQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class ListComputeQuotaPlanResponseBodyData(TeaModel):
    def __init__(
        self,
        plan_list: List[ListComputeQuotaPlanResponseBodyDataPlanList] = None,
    ):
        # The list of quota plan.
        self.plan_list = plan_list

    def validate(self):
        if self.plan_list:
            for k in self.plan_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['planList'] = []
        if self.plan_list is not None:
            for k in self.plan_list:
                result['planList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plan_list = []
        if m.get('planList') is not None:
            for k in m.get('planList'):
                temp_model = ListComputeQuotaPlanResponseBodyDataPlanList()
                self.plan_list.append(temp_model.from_map(k))
        return self


class ListComputeQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: ListComputeQuotaPlanResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListComputeQuotaPlanResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListComputeQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListComputeQuotaPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListComputeQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionsRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        prefix: str = None,
        schema_name: str = None,
    ):
        # Specifies the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries to return on each page.
        self.max_item = max_item
        # The names of the returned resources. The names must start with the value specified by the prefix parameter. If the prefix parameter is set to a, the names of the returned resources must start with a.
        self.prefix = prefix
        # the name of schema.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class ListFunctionsResponseBodyDataFunctions(TeaModel):
    def __init__(
        self,
        class_: str = None,
        creation_time: int = None,
        display_name: str = None,
        name: str = None,
        owner: str = None,
        resources: str = None,
        schema: str = None,
    ):
        # The class in which the function was defined.
        self.class_ = class_
        # The time when the function was created. Unit: milliseconds.
        self.creation_time = creation_time
        # The display name of the function.
        self.display_name = display_name
        # The name of the function.
        self.name = name
        # The owner of the function.
        self.owner = owner
        # The name of the resource that was associated with the function.
        self.resources = resources
        # The schema of the function.
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['class'] = self.class_
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.resources is not None:
            result['resources'] = self.resources
        if self.schema is not None:
            result['schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('class') is not None:
            self.class_ = m.get('class')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('resources') is not None:
            self.resources = m.get('resources')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        return self


class ListFunctionsResponseBodyData(TeaModel):
    def __init__(
        self,
        functions: List[ListFunctionsResponseBodyDataFunctions] = None,
        marker: str = None,
        max_item: int = None,
    ):
        # The information about each function.
        self.functions = functions
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['functions'] = []
        if self.functions is not None:
            for k in self.functions:
                result['functions'].append(k.to_map() if k else None)
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('functions') is not None:
            for k in m.get('functions'):
                temp_model = ListFunctionsResponseBodyDataFunctions()
                self.functions.append(temp_model.from_map(k))
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        return self


class ListFunctionsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListFunctionsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListFunctionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListFunctionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobInfosRequest(TeaModel):
    def __init__(
        self,
        asc_order: bool = None,
        ext_node_id_list: List[str] = None,
        from_: int = None,
        instance_id_list: List[str] = None,
        job_owner_list: List[str] = None,
        priority_list: List[int] = None,
        project_list: List[str] = None,
        quota_nickname: str = None,
        scene_tag_list: List[str] = None,
        signature_list: List[str] = None,
        sort_by_list: List[str] = None,
        sort_order_list: List[str] = None,
        status_list: List[str] = None,
        to: int = None,
        type_list: List[str] = None,
        order_column: str = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # Specifies whether to sort query results in ascending or descending order.
        self.asc_order = asc_order
        # The ancestor node IDs.
        self.ext_node_id_list = ext_node_id_list
        # The start timestamp.
        # 
        # This parameter is required.
        self.from_ = from_
        # The job instance IDs.
        self.instance_id_list = instance_id_list
        # The job owners.
        self.job_owner_list = job_owner_list
        # The job priorities.
        self.priority_list = priority_list
        # The project names.
        self.project_list = project_list
        # The quota nickname.
        self.quota_nickname = quota_nickname
        # The intelligent diagnostics tags.
        self.scene_tag_list = scene_tag_list
        # The job signatures.
        self.signature_list = signature_list
        # The sorting columns.
        self.sort_by_list = sort_by_list
        # The orders for the sorting columns.
        self.sort_order_list = sort_order_list
        # The job states.
        self.status_list = status_list
        # The end timestamp.
        # 
        # This parameter is required.
        self.to = to
        # The job types.
        self.type_list = type_list
        # The column based on which you want to sort query results.
        self.order_column = order_column
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        self.region = region
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order
        if self.ext_node_id_list is not None:
            result['extNodeIdList'] = self.ext_node_id_list
        if self.from_ is not None:
            result['from'] = self.from_
        if self.instance_id_list is not None:
            result['instanceIdList'] = self.instance_id_list
        if self.job_owner_list is not None:
            result['jobOwnerList'] = self.job_owner_list
        if self.priority_list is not None:
            result['priorityList'] = self.priority_list
        if self.project_list is not None:
            result['projectList'] = self.project_list
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        if self.scene_tag_list is not None:
            result['sceneTagList'] = self.scene_tag_list
        if self.signature_list is not None:
            result['signatureList'] = self.signature_list
        if self.sort_by_list is not None:
            result['sortByList'] = self.sort_by_list
        if self.sort_order_list is not None:
            result['sortOrderList'] = self.sort_order_list
        if self.status_list is not None:
            result['statusList'] = self.status_list
        if self.to is not None:
            result['to'] = self.to
        if self.type_list is not None:
            result['typeList'] = self.type_list
        if self.order_column is not None:
            result['orderColumn'] = self.order_column
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')
        if m.get('extNodeIdList') is not None:
            self.ext_node_id_list = m.get('extNodeIdList')
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('instanceIdList') is not None:
            self.instance_id_list = m.get('instanceIdList')
        if m.get('jobOwnerList') is not None:
            self.job_owner_list = m.get('jobOwnerList')
        if m.get('priorityList') is not None:
            self.priority_list = m.get('priorityList')
        if m.get('projectList') is not None:
            self.project_list = m.get('projectList')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        if m.get('sceneTagList') is not None:
            self.scene_tag_list = m.get('sceneTagList')
        if m.get('signatureList') is not None:
            self.signature_list = m.get('signatureList')
        if m.get('sortByList') is not None:
            self.sort_by_list = m.get('sortByList')
        if m.get('sortOrderList') is not None:
            self.sort_order_list = m.get('sortOrderList')
        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('typeList') is not None:
            self.type_list = m.get('typeList')
        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListJobInfosResponseBodyDataJobInfoListSceneResults(TeaModel):
    def __init__(
        self,
        description: str = None,
        params: Dict[str, str] = None,
        scene: str = None,
        scene_tag: str = None,
        summary: str = None,
        type: str = None,
    ):
        # The intelligent diagnostics result description.
        self.description = description
        # Information about the nodes where data skew or data expansion is detected. This parameter is returned only when the diagnostics scenario is data skew or data expansion.
        self.params = params
        # The intelligent diagnostics result scenario.
        self.scene = scene
        # The intelligent diagnostics result tag.
        self.scene_tag = scene_tag
        # The intelligent diagnostics result summary.
        self.summary = summary
        # The intelligent diagnostics result type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.params is not None:
            result['params'] = self.params
        if self.scene is not None:
            result['scene'] = self.scene
        if self.scene_tag is not None:
            result['sceneTag'] = self.scene_tag
        if self.summary is not None:
            result['summary'] = self.summary
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('sceneTag') is not None:
            self.scene_tag = m.get('sceneTag')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListJobInfosResponseBodyDataJobInfoList(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        cu_snapshot: float = None,
        cu_usage: int = None,
        end_at_time: int = None,
        ext_node_id: str = None,
        ext_node_on_duty: str = None,
        ext_plant_from: str = None,
        input_bytes: float = None,
        instance_id: str = None,
        job_owner: str = None,
        job_type: str = None,
        memory_snapshot: float = None,
        memory_usage: int = None,
        priority: int = None,
        project: str = None,
        quota_nickname: str = None,
        quota_type: str = None,
        region: str = None,
        running_at_time: int = None,
        running_time: int = None,
        scene_results: List[ListJobInfosResponseBodyDataJobInfoListSceneResults] = None,
        signature: str = None,
        status: str = None,
        status_snapshot: str = None,
        submitted_at_time: int = None,
        tags: str = None,
        tenant_id: str = None,
        total_time: int = None,
        waiting_time: int = None,
    ):
        # The cluster ID.
        self.cluster = cluster
        # The CU snapshot proportion of the job.
        self.cu_snapshot = cu_snapshot
        # The amount of resources consumed by the job. This parameter is returned only for jobs that are complete.Unit: 100\\*Core\\*s.
        self.cu_usage = cu_usage
        # The time when the job stops running.
        self.end_at_time = end_at_time
        # The node ID of DataWorks.
        self.ext_node_id = ext_node_id
        # The account of the node owner.
        self.ext_node_on_duty = ext_node_on_duty
        # The upstream platform.
        self.ext_plant_from = ext_plant_from
        # The amount of scanned data for the job. Unit: byte.
        self.input_bytes = input_bytes
        # The instance ID.
        self.instance_id = instance_id
        # The account that commits the job.
        self.job_owner = job_owner
        # The type of the job.
        self.job_type = job_type
        # The memory snapshot proportion of the job.
        self.memory_snapshot = memory_snapshot
        # The number of memory consumed by the job. This parameter is returned only for jobs that are complete.Unit: MB\\*s.
        self.memory_usage = memory_usage
        # The priority of the job.
        self.priority = priority
        # The name of the MaxCompute project.
        self.project = project
        # The nickname of the quota that is used by the job.
        self.quota_nickname = quota_nickname
        # The type of the quota.
        self.quota_type = quota_type
        # The region ID.
        self.region = region
        # The time when the job starts to run.
        self.running_at_time = running_at_time
        # The period for which the job runs.
        self.running_time = running_time
        # The intelligent diagnostics results.
        self.scene_results = scene_results
        # The signature of the SQL job.
        self.signature = signature
        # The status of the job.
        self.status = status
        # The status of the snapshot.
        self.status_snapshot = status_snapshot
        # The time when the job was committed.
        self.submitted_at_time = submitted_at_time
        # The tags.
        self.tags = tags
        # The tenant ID.
        self.tenant_id = tenant_id
        # The total period for which the job runs.
        self.total_time = total_time
        # The duration for which the job waits to start.
        self.waiting_time = waiting_time

    def validate(self):
        if self.scene_results:
            for k in self.scene_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.cu_snapshot is not None:
            result['cuSnapshot'] = self.cu_snapshot
        if self.cu_usage is not None:
            result['cuUsage'] = self.cu_usage
        if self.end_at_time is not None:
            result['endAtTime'] = self.end_at_time
        if self.ext_node_id is not None:
            result['extNodeId'] = self.ext_node_id
        if self.ext_node_on_duty is not None:
            result['extNodeOnDuty'] = self.ext_node_on_duty
        if self.ext_plant_from is not None:
            result['extPlantFrom'] = self.ext_plant_from
        if self.input_bytes is not None:
            result['inputBytes'] = self.input_bytes
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner
        if self.job_type is not None:
            result['jobType'] = self.job_type
        if self.memory_snapshot is not None:
            result['memorySnapshot'] = self.memory_snapshot
        if self.memory_usage is not None:
            result['memoryUsage'] = self.memory_usage
        if self.priority is not None:
            result['priority'] = self.priority
        if self.project is not None:
            result['project'] = self.project
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        if self.quota_type is not None:
            result['quotaType'] = self.quota_type
        if self.region is not None:
            result['region'] = self.region
        if self.running_at_time is not None:
            result['runningAtTime'] = self.running_at_time
        if self.running_time is not None:
            result['runningTime'] = self.running_time
        result['sceneResults'] = []
        if self.scene_results is not None:
            for k in self.scene_results:
                result['sceneResults'].append(k.to_map() if k else None)
        if self.signature is not None:
            result['signature'] = self.signature
        if self.status is not None:
            result['status'] = self.status
        if self.status_snapshot is not None:
            result['statusSnapshot'] = self.status_snapshot
        if self.submitted_at_time is not None:
            result['submittedAtTime'] = self.submitted_at_time
        if self.tags is not None:
            result['tags'] = self.tags
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.total_time is not None:
            result['totalTime'] = self.total_time
        if self.waiting_time is not None:
            result['waitingTime'] = self.waiting_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('cuSnapshot') is not None:
            self.cu_snapshot = m.get('cuSnapshot')
        if m.get('cuUsage') is not None:
            self.cu_usage = m.get('cuUsage')
        if m.get('endAtTime') is not None:
            self.end_at_time = m.get('endAtTime')
        if m.get('extNodeId') is not None:
            self.ext_node_id = m.get('extNodeId')
        if m.get('extNodeOnDuty') is not None:
            self.ext_node_on_duty = m.get('extNodeOnDuty')
        if m.get('extPlantFrom') is not None:
            self.ext_plant_from = m.get('extPlantFrom')
        if m.get('inputBytes') is not None:
            self.input_bytes = m.get('inputBytes')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')
        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')
        if m.get('memorySnapshot') is not None:
            self.memory_snapshot = m.get('memorySnapshot')
        if m.get('memoryUsage') is not None:
            self.memory_usage = m.get('memoryUsage')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        if m.get('quotaType') is not None:
            self.quota_type = m.get('quotaType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('runningAtTime') is not None:
            self.running_at_time = m.get('runningAtTime')
        if m.get('runningTime') is not None:
            self.running_time = m.get('runningTime')
        self.scene_results = []
        if m.get('sceneResults') is not None:
            for k in m.get('sceneResults'):
                temp_model = ListJobInfosResponseBodyDataJobInfoListSceneResults()
                self.scene_results.append(temp_model.from_map(k))
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusSnapshot') is not None:
            self.status_snapshot = m.get('statusSnapshot')
        if m.get('submittedAtTime') is not None:
            self.submitted_at_time = m.get('submittedAtTime')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('totalTime') is not None:
            self.total_time = m.get('totalTime')
        if m.get('waitingTime') is not None:
            self.waiting_time = m.get('waitingTime')
        return self


class ListJobInfosResponseBodyData(TeaModel):
    def __init__(
        self,
        job_info_list: List[ListJobInfosResponseBodyDataJobInfoList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The information about the jobs.
        self.job_info_list = job_info_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.job_info_list:
            for k in self.job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['jobInfoList'] = []
        if self.job_info_list is not None:
            for k in self.job_info_list:
                result['jobInfoList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_info_list = []
        if m.get('jobInfoList') is not None:
            for k in m.get('jobInfoList'):
                temp_model = ListJobInfosResponseBodyDataJobInfoList()
                self.job_info_list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListJobInfosResponseBody(TeaModel):
    def __init__(
        self,
        data: ListJobInfosResponseBodyData = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # Indicates whether the request was successful. If this parameter was not empty and the value of this parameter was not 200, the request failed.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListJobInfosResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListJobInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobInfosResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobMetricRequest(TeaModel):
    def __init__(
        self,
        group: str = None,
        metric: str = None,
        period: int = None,
        project: List[str] = None,
        quota: List[str] = None,
        type: str = None,
        end_time: int = None,
        start_time: int = None,
    ):
        # Grouping basis.
        # 
        # > Available values: project, quota, type, status. Meanings:
        # >- project: Group and aggregate by project;
        # >- quota: Group and aggregate by quota;
        # >- type: Group and aggregate by job type;
        # >- status: Group and aggregate by job status.
        self.group = group
        # The name of observation metric.
        self.metric = metric
        # The monitoring statistical period.Unit:Second(s).
        self.period = period
        # The name of MaxCompute projects (for filtering).
        self.project = project
        # The nickname of computing Quota nickname used by the job (for filtering).
        self.quota = quota
        # The type of observation metric.
        self.type = type
        # The end time for the observation interval.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The start time for the observation interval.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.metric is not None:
            result['metric'] = self.metric
        if self.period is not None:
            result['period'] = self.period
        if self.project is not None:
            result['project'] = self.project
        if self.quota is not None:
            result['quota'] = self.quota
        if self.type is not None:
            result['type'] = self.type
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('metric') is not None:
            self.metric = m.get('metric')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('quota') is not None:
            self.quota = m.get('quota')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListJobMetricResponseBodyDataMetrics(TeaModel):
    def __init__(
        self,
        metric: Dict[str, str] = None,
        values: List[List[float]] = None,
    ):
        # Metric related information.
        self.metric = metric
        # Metric values information.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            self.metric = m.get('metric')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListJobMetricResponseBodyData(TeaModel):
    def __init__(
        self,
        category: str = None,
        metrics: List[ListJobMetricResponseBodyDataMetrics] = None,
        name: str = None,
        period: int = None,
    ):
        # The category of the metrics.
        self.category = category
        # Metric details.
        self.metrics = metrics
        # The name of observation metric.
        self.name = name
        # The monitoring statistical period.Unit:Second(s).
        self.period = period

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.period is not None:
            result['period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.metrics = []
        if m.get('metrics') is not None:
            for k in m.get('metrics'):
                temp_model = ListJobMetricResponseBodyDataMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('period') is not None:
            self.period = m.get('period')
        return self


class ListJobMetricResponseBody(TeaModel):
    def __init__(
        self,
        data: ListJobMetricResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # HTTP status code.
        # - 1xx: Informational response - Request received, processing continues.
        # - 2xx: Success - The request has been successfully received, understood, and accepted by the server.
        # - 3xx: Redirection - Further action must be taken to complete the request.
        # - 4xx: Client error - The request contains bad syntax or cannot be fulfilled.
        # - 5xx: Server error - The server failed to fulfill an apparently valid request.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListJobMetricResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListJobMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobMetricResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobSnapshotInfosRequest(TeaModel):
    def __init__(
        self,
        asc_order: bool = None,
        ext_node_id_list: List[str] = None,
        from_: int = None,
        instance_id_list: List[str] = None,
        job_owner_list: List[str] = None,
        priority_list: List[int] = None,
        project_list: List[str] = None,
        quota_nickname: str = None,
        signature_list: List[str] = None,
        sort_by_list: List[str] = None,
        sort_order_list: List[str] = None,
        status_list: List[str] = None,
        to: int = None,
        type_list: List[str] = None,
        order_column: str = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # Specifies whether to sort data in ascending order.
        self.asc_order = asc_order
        # The ID of the upstream node.
        self.ext_node_id_list = ext_node_id_list
        # Start timestamp.
        # > This parameter is invalid. The end timestamp should be the time point for the snapshot you want to view.
        self.from_ = from_
        # The instance ID.
        self.instance_id_list = instance_id_list
        # The account that commits the job.
        self.job_owner_list = job_owner_list
        # The priority of the job.
        self.priority_list = priority_list
        # The name of project.
        self.project_list = project_list
        # The nickname of the compute Quota used by the job.
        self.quota_nickname = quota_nickname
        # The signature of the SQL job.
        self.signature_list = signature_list
        # The sorting columns.
        self.sort_by_list = sort_by_list
        # The orders for the sorting columns.
        self.sort_order_list = sort_order_list
        # The status of jobs.
        self.status_list = status_list
        # End timestamp.
        # 
        # This parameter is required.
        self.to = to
        # The type of the job.
        self.type_list = type_list
        # The sorting column.
        self.order_column = order_column
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        self.region = region
        # The ID of the tenant. You can log on to the MaxCompute console, and choose Tenants > Tenant Property from the left-side navigation pane to view the tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order
        if self.ext_node_id_list is not None:
            result['extNodeIdList'] = self.ext_node_id_list
        if self.from_ is not None:
            result['from'] = self.from_
        if self.instance_id_list is not None:
            result['instanceIdList'] = self.instance_id_list
        if self.job_owner_list is not None:
            result['jobOwnerList'] = self.job_owner_list
        if self.priority_list is not None:
            result['priorityList'] = self.priority_list
        if self.project_list is not None:
            result['projectList'] = self.project_list
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        if self.signature_list is not None:
            result['signatureList'] = self.signature_list
        if self.sort_by_list is not None:
            result['sortByList'] = self.sort_by_list
        if self.sort_order_list is not None:
            result['sortOrderList'] = self.sort_order_list
        if self.status_list is not None:
            result['statusList'] = self.status_list
        if self.to is not None:
            result['to'] = self.to
        if self.type_list is not None:
            result['typeList'] = self.type_list
        if self.order_column is not None:
            result['orderColumn'] = self.order_column
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')
        if m.get('extNodeIdList') is not None:
            self.ext_node_id_list = m.get('extNodeIdList')
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('instanceIdList') is not None:
            self.instance_id_list = m.get('instanceIdList')
        if m.get('jobOwnerList') is not None:
            self.job_owner_list = m.get('jobOwnerList')
        if m.get('priorityList') is not None:
            self.priority_list = m.get('priorityList')
        if m.get('projectList') is not None:
            self.project_list = m.get('projectList')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        if m.get('signatureList') is not None:
            self.signature_list = m.get('signatureList')
        if m.get('sortByList') is not None:
            self.sort_by_list = m.get('sortByList')
        if m.get('sortOrderList') is not None:
            self.sort_order_list = m.get('sortOrderList')
        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')
        if m.get('to') is not None:
            self.to = m.get('to')
        if m.get('typeList') is not None:
            self.type_list = m.get('typeList')
        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListJobSnapshotInfosResponseBodyDataJobInfoList(TeaModel):
    def __init__(
        self,
        cpu_request: int = None,
        cpu_usage: int = None,
        cpu_usage_to_request_ratio: float = None,
        ext_node_id: str = None,
        ext_node_on_duty: str = None,
        ext_plant_from: str = None,
        instance_id: str = None,
        job_owner: str = None,
        job_type: str = None,
        max_cpu_pct: float = None,
        max_memory_pct: float = None,
        memory_request: int = None,
        memory_usage: int = None,
        memory_usage_to_request_ratio: float = None,
        min_cpu_pct: float = None,
        min_memory_pct: float = None,
        priority: int = None,
        project: str = None,
        quota_nickname: str = None,
        quota_type: str = None,
        region: str = None,
        running_at_time: int = None,
        running_time: int = None,
        signature: str = None,
        snapshot_time: int = None,
        status: str = None,
        submitted_at_time: int = None,
        tenant_id: str = None,
        total_time: int = None,
        waiting_time: int = None,
    ):
        # The CPU request amount of the job at the snapshot time point. Unit: Core.
        self.cpu_request = cpu_request
        # CPU usage of the job at the snapshot time. Unit: Core.
        self.cpu_usage = cpu_usage
        # The CPU satisfaction ratio of the job at the snapshot time point (cpuUsage/cpuRequest).
        self.cpu_usage_to_request_ratio = cpu_usage_to_request_ratio
        # The ID of the upstream node.
        self.ext_node_id = ext_node_id
        # The account ID of the task owner.
        self.ext_node_on_duty = ext_node_on_duty
        # The upstream platform.
        self.ext_plant_from = ext_plant_from
        # The instance ID.
        self.instance_id = instance_id
        # The account that commits the job.
        self.job_owner = job_owner
        # The type of the job.
        self.job_type = job_type
        # Not applicable.
        self.max_cpu_pct = max_cpu_pct
        # Not applicable.
        self.max_memory_pct = max_memory_pct
        # The Memory request amount of the job at the snapshot time point. Unit: MB.
        self.memory_request = memory_request
        # Memory usage of the job at the snapshot time. Unit: MB.
        self.memory_usage = memory_usage
        # The Memory satisfaction ratio of the job at the snapshot time point (memoryUsage/memoryRequest).
        self.memory_usage_to_request_ratio = memory_usage_to_request_ratio
        # The CPU usage ratio of the annual or monthly subscription job at the snapshot time (CPU usage / (reserved CPU guarantee + elastic reserved CPU)). This parameter is not available for pay-as-you-go jobs.
        self.min_cpu_pct = min_cpu_pct
        # The memory usage ratio of the annual or monthly subscription job at the observation time (memory usage / (reserved memory guarantee + elastic reserved memory)). This parameter is not available for pay-as-you-go jobs.
        self.min_memory_pct = min_memory_pct
        # The priority of the job.
        self.priority = priority
        # The name of the MaxCompute project.
        self.project = project
        # The nickname of the computing Quota used by the job.
        self.quota_nickname = quota_nickname
        # The type of the quota.
        self.quota_type = quota_type
        # The region ID.
        self.region = region
        # The start time of the job.
        # > The time when the job received the first batch of computing resources.
        self.running_at_time = running_at_time
        # The running duration, which is the duration from the runningAtTime to the snapshotTime of the job.  Unit: seconds (s).
        self.running_time = running_time
        # The signature of the SQL job.
        self.signature = signature
        # The snapshot time.
        self.snapshot_time = snapshot_time
        # The snapshot status of the job.
        # 
        # > The snapshot status is only running.
        self.status = status
        # The time when the job was committed.
        self.submitted_at_time = submitted_at_time
        # The tenant ID.
        self.tenant_id = tenant_id
        # The interval from the time when the job was submitted to the snapshotTime .Unit: seconds (s).
        self.total_time = total_time
        # The duration from the time the job is submitted to the time the job starts to run. Unit: seconds (s).
        self.waiting_time = waiting_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_request is not None:
            result['cpuRequest'] = self.cpu_request
        if self.cpu_usage is not None:
            result['cpuUsage'] = self.cpu_usage
        if self.cpu_usage_to_request_ratio is not None:
            result['cpuUsageToRequestRatio'] = self.cpu_usage_to_request_ratio
        if self.ext_node_id is not None:
            result['extNodeId'] = self.ext_node_id
        if self.ext_node_on_duty is not None:
            result['extNodeOnDuty'] = self.ext_node_on_duty
        if self.ext_plant_from is not None:
            result['extPlantFrom'] = self.ext_plant_from
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.job_owner is not None:
            result['jobOwner'] = self.job_owner
        if self.job_type is not None:
            result['jobType'] = self.job_type
        if self.max_cpu_pct is not None:
            result['maxCpuPct'] = self.max_cpu_pct
        if self.max_memory_pct is not None:
            result['maxMemoryPct'] = self.max_memory_pct
        if self.memory_request is not None:
            result['memoryRequest'] = self.memory_request
        if self.memory_usage is not None:
            result['memoryUsage'] = self.memory_usage
        if self.memory_usage_to_request_ratio is not None:
            result['memoryUsageToRequestRatio'] = self.memory_usage_to_request_ratio
        if self.min_cpu_pct is not None:
            result['minCpuPct'] = self.min_cpu_pct
        if self.min_memory_pct is not None:
            result['minMemoryPct'] = self.min_memory_pct
        if self.priority is not None:
            result['priority'] = self.priority
        if self.project is not None:
            result['project'] = self.project
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        if self.quota_type is not None:
            result['quotaType'] = self.quota_type
        if self.region is not None:
            result['region'] = self.region
        if self.running_at_time is not None:
            result['runningAtTime'] = self.running_at_time
        if self.running_time is not None:
            result['runningTime'] = self.running_time
        if self.signature is not None:
            result['signature'] = self.signature
        if self.snapshot_time is not None:
            result['snapshotTime'] = self.snapshot_time
        if self.status is not None:
            result['status'] = self.status
        if self.submitted_at_time is not None:
            result['submittedAtTime'] = self.submitted_at_time
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.total_time is not None:
            result['totalTime'] = self.total_time
        if self.waiting_time is not None:
            result['waitingTime'] = self.waiting_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuRequest') is not None:
            self.cpu_request = m.get('cpuRequest')
        if m.get('cpuUsage') is not None:
            self.cpu_usage = m.get('cpuUsage')
        if m.get('cpuUsageToRequestRatio') is not None:
            self.cpu_usage_to_request_ratio = m.get('cpuUsageToRequestRatio')
        if m.get('extNodeId') is not None:
            self.ext_node_id = m.get('extNodeId')
        if m.get('extNodeOnDuty') is not None:
            self.ext_node_on_duty = m.get('extNodeOnDuty')
        if m.get('extPlantFrom') is not None:
            self.ext_plant_from = m.get('extPlantFrom')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('jobOwner') is not None:
            self.job_owner = m.get('jobOwner')
        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')
        if m.get('maxCpuPct') is not None:
            self.max_cpu_pct = m.get('maxCpuPct')
        if m.get('maxMemoryPct') is not None:
            self.max_memory_pct = m.get('maxMemoryPct')
        if m.get('memoryRequest') is not None:
            self.memory_request = m.get('memoryRequest')
        if m.get('memoryUsage') is not None:
            self.memory_usage = m.get('memoryUsage')
        if m.get('memoryUsageToRequestRatio') is not None:
            self.memory_usage_to_request_ratio = m.get('memoryUsageToRequestRatio')
        if m.get('minCpuPct') is not None:
            self.min_cpu_pct = m.get('minCpuPct')
        if m.get('minMemoryPct') is not None:
            self.min_memory_pct = m.get('minMemoryPct')
        if m.get('priority') is not None:
            self.priority = m.get('priority')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        if m.get('quotaType') is not None:
            self.quota_type = m.get('quotaType')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('runningAtTime') is not None:
            self.running_at_time = m.get('runningAtTime')
        if m.get('runningTime') is not None:
            self.running_time = m.get('runningTime')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('snapshotTime') is not None:
            self.snapshot_time = m.get('snapshotTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('submittedAtTime') is not None:
            self.submitted_at_time = m.get('submittedAtTime')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('totalTime') is not None:
            self.total_time = m.get('totalTime')
        if m.get('waitingTime') is not None:
            self.waiting_time = m.get('waitingTime')
        return self


class ListJobSnapshotInfosResponseBodyData(TeaModel):
    def __init__(
        self,
        job_info_list: List[ListJobSnapshotInfosResponseBodyDataJobInfoList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The job snapshots.
        self.job_info_list = job_info_list
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of returned results.
        self.total_count = total_count

    def validate(self):
        if self.job_info_list:
            for k in self.job_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['jobInfoList'] = []
        if self.job_info_list is not None:
            for k in self.job_info_list:
                result['jobInfoList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_info_list = []
        if m.get('jobInfoList') is not None:
            for k in m.get('jobInfoList'):
                temp_model = ListJobSnapshotInfosResponseBodyDataJobInfoList()
                self.job_info_list.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListJobSnapshotInfosResponseBody(TeaModel):
    def __init__(
        self,
        data: ListJobSnapshotInfosResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListJobSnapshotInfosResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListJobSnapshotInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobSnapshotInfosResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobSnapshotInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMmsDataSourcesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        region: str = None,
        type: str = None,
    ):
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.region = region
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region is not None:
            result['region'] = self.region
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListMmsDataSourcesResponseBodyDataObjectListConfig(TeaModel):
    def __init__(
        self,
        desc: str = None,
        enums: List[str] = None,
        group: str = None,
        key: str = None,
        name: str = None,
        place_holder: str = None,
        required: bool = None,
        sub_type: str = None,
        type: str = None,
        value: Any = None,
    ):
        self.desc = desc
        self.enums = enums
        self.group = group
        self.key = key
        self.name = name
        self.place_holder = place_holder
        self.required = required
        self.sub_type = sub_type
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['desc'] = self.desc
        if self.enums is not None:
            result['enums'] = self.enums
        if self.group is not None:
            result['group'] = self.group
        if self.key is not None:
            result['key'] = self.key
        if self.name is not None:
            result['name'] = self.name
        if self.place_holder is not None:
            result['placeHolder'] = self.place_holder
        if self.required is not None:
            result['required'] = self.required
        if self.sub_type is not None:
            result['subType'] = self.sub_type
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('enums') is not None:
            self.enums = m.get('enums')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('placeHolder') is not None:
            self.place_holder = m.get('placeHolder')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('subType') is not None:
            self.sub_type = m.get('subType')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListMmsDataSourcesResponseBodyDataObjectList(TeaModel):
    def __init__(
        self,
        agent_is_online: bool = None,
        config: List[ListMmsDataSourcesResponseBodyDataObjectListConfig] = None,
        create_time: str = None,
        db_num: int = None,
        err_msg: str = None,
        id: int = None,
        last_update_time: str = None,
        name: str = None,
        networklink: str = None,
        partition_num: int = None,
        partitions_doing_num: int = None,
        partitions_done_num: int = None,
        partitions_failed_num: int = None,
        region: str = None,
        scan_id: int = None,
        status: str = None,
        table_num: int = None,
        tables_doing_num: int = None,
        tables_done_num: int = None,
        tables_failed_num: int = None,
        tables_part_done_num: int = None,
        type: str = None,
    ):
        self.agent_is_online = agent_is_online
        self.config = config
        self.create_time = create_time
        self.db_num = db_num
        self.err_msg = err_msg
        self.id = id
        self.last_update_time = last_update_time
        self.name = name
        self.networklink = networklink
        self.partition_num = partition_num
        self.partitions_doing_num = partitions_doing_num
        self.partitions_done_num = partitions_done_num
        self.partitions_failed_num = partitions_failed_num
        self.region = region
        self.scan_id = scan_id
        self.status = status
        self.table_num = table_num
        self.tables_doing_num = tables_doing_num
        self.tables_done_num = tables_done_num
        self.tables_failed_num = tables_failed_num
        self.tables_part_done_num = tables_part_done_num
        self.type = type

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_is_online is not None:
            result['agentIsOnline'] = self.agent_is_online
        result['config'] = []
        if self.config is not None:
            for k in self.config:
                result['config'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.db_num is not None:
            result['dbNum'] = self.db_num
        if self.err_msg is not None:
            result['errMsg'] = self.err_msg
        if self.id is not None:
            result['id'] = self.id
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.name is not None:
            result['name'] = self.name
        if self.networklink is not None:
            result['networklink'] = self.networklink
        if self.partition_num is not None:
            result['partitionNum'] = self.partition_num
        if self.partitions_doing_num is not None:
            result['partitionsDoingNum'] = self.partitions_doing_num
        if self.partitions_done_num is not None:
            result['partitionsDoneNum'] = self.partitions_done_num
        if self.partitions_failed_num is not None:
            result['partitionsFailedNum'] = self.partitions_failed_num
        if self.region is not None:
            result['region'] = self.region
        if self.scan_id is not None:
            result['scanId'] = self.scan_id
        if self.status is not None:
            result['status'] = self.status
        if self.table_num is not None:
            result['tableNum'] = self.table_num
        if self.tables_doing_num is not None:
            result['tablesDoingNum'] = self.tables_doing_num
        if self.tables_done_num is not None:
            result['tablesDoneNum'] = self.tables_done_num
        if self.tables_failed_num is not None:
            result['tablesFailedNum'] = self.tables_failed_num
        if self.tables_part_done_num is not None:
            result['tablesPartDoneNum'] = self.tables_part_done_num
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentIsOnline') is not None:
            self.agent_is_online = m.get('agentIsOnline')
        self.config = []
        if m.get('config') is not None:
            for k in m.get('config'):
                temp_model = ListMmsDataSourcesResponseBodyDataObjectListConfig()
                self.config.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dbNum') is not None:
            self.db_num = m.get('dbNum')
        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networklink') is not None:
            self.networklink = m.get('networklink')
        if m.get('partitionNum') is not None:
            self.partition_num = m.get('partitionNum')
        if m.get('partitionsDoingNum') is not None:
            self.partitions_doing_num = m.get('partitionsDoingNum')
        if m.get('partitionsDoneNum') is not None:
            self.partitions_done_num = m.get('partitionsDoneNum')
        if m.get('partitionsFailedNum') is not None:
            self.partitions_failed_num = m.get('partitionsFailedNum')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('scanId') is not None:
            self.scan_id = m.get('scanId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tableNum') is not None:
            self.table_num = m.get('tableNum')
        if m.get('tablesDoingNum') is not None:
            self.tables_doing_num = m.get('tablesDoingNum')
        if m.get('tablesDoneNum') is not None:
            self.tables_done_num = m.get('tablesDoneNum')
        if m.get('tablesFailedNum') is not None:
            self.tables_failed_num = m.get('tablesFailedNum')
        if m.get('tablesPartDoneNum') is not None:
            self.tables_part_done_num = m.get('tablesPartDoneNum')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListMmsDataSourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        object_list: List[ListMmsDataSourcesResponseBodyDataObjectList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.object_list = object_list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.object_list:
            for k in self.object_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['objectList'] = []
        if self.object_list is not None:
            for k in self.object_list:
                result['objectList'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_list = []
        if m.get('objectList') is not None:
            for k in m.get('objectList'):
                temp_model = ListMmsDataSourcesResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListMmsDataSourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListMmsDataSourcesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListMmsDataSourcesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListMmsDataSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMmsDataSourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMmsDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMmsDbsRequestSorter(TeaModel):
    def __init__(
        self,
        num_rows: str = None,
        size: str = None,
        update_time: str = None,
    ):
        self.num_rows = num_rows
        self.size = size
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.num_rows is not None:
            result['numRows'] = self.num_rows
        if self.size is not None:
            result['size'] = self.size
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListMmsDbsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        sorter: ListMmsDbsRequestSorter = None,
        status: str = None,
    ):
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.sorter = sorter
        self.status = status

    def validate(self):
        if self.sorter:
            self.sorter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.sorter is not None:
            result['sorter'] = self.sorter.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sorter') is not None:
            temp_model = ListMmsDbsRequestSorter()
            self.sorter = temp_model.from_map(m['sorter'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListMmsDbsShrinkRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        sorter_shrink: str = None,
        status: str = None,
    ):
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.sorter_shrink = sorter_shrink
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.sorter_shrink is not None:
            result['sorter'] = self.sorter_shrink
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sorter') is not None:
            self.sorter_shrink = m.get('sorter')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListMmsDbsResponseBodyDataObjectList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deleted: bool = None,
        description: str = None,
        extra: str = None,
        id: int = None,
        last_ddl_time: str = None,
        location: str = None,
        name: str = None,
        num_rows: int = None,
        owner: str = None,
        partitions: int = None,
        partitions_doing: int = None,
        partitions_done: int = None,
        partitions_failed: int = None,
        size: int = None,
        source_id: int = None,
        source_name: str = None,
        status: str = None,
        tables: int = None,
        tables_doing: int = None,
        tables_done: int = None,
        tables_failed: int = None,
        tables_part_done: int = None,
        update_time: str = None,
        updated: bool = None,
    ):
        self.create_time = create_time
        self.deleted = deleted
        self.description = description
        self.extra = extra
        self.id = id
        # Last DDL Time
        self.last_ddl_time = last_ddl_time
        self.location = location
        self.name = name
        self.num_rows = num_rows
        self.owner = owner
        self.partitions = partitions
        self.partitions_doing = partitions_doing
        self.partitions_done = partitions_done
        self.partitions_failed = partitions_failed
        self.size = size
        self.source_id = source_id
        self.source_name = source_name
        self.status = status
        self.tables = tables
        self.tables_doing = tables_doing
        self.tables_done = tables_done
        self.tables_failed = tables_failed
        self.tables_part_done = tables_part_done
        self.update_time = update_time
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.deleted is not None:
            result['deleted'] = self.deleted
        if self.description is not None:
            result['description'] = self.description
        if self.extra is not None:
            result['extra'] = self.extra
        if self.id is not None:
            result['id'] = self.id
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.num_rows is not None:
            result['numRows'] = self.num_rows
        if self.owner is not None:
            result['owner'] = self.owner
        if self.partitions is not None:
            result['partitions'] = self.partitions
        if self.partitions_doing is not None:
            result['partitionsDoing'] = self.partitions_doing
        if self.partitions_done is not None:
            result['partitionsDone'] = self.partitions_done
        if self.partitions_failed is not None:
            result['partitionsFailed'] = self.partitions_failed
        if self.size is not None:
            result['size'] = self.size
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.status is not None:
            result['status'] = self.status
        if self.tables is not None:
            result['tables'] = self.tables
        if self.tables_doing is not None:
            result['tablesDoing'] = self.tables_doing
        if self.tables_done is not None:
            result['tablesDone'] = self.tables_done
        if self.tables_failed is not None:
            result['tablesFailed'] = self.tables_failed
        if self.tables_part_done is not None:
            result['tablesPartDone'] = self.tables_part_done
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')
        if m.get('partitionsDoing') is not None:
            self.partitions_doing = m.get('partitionsDoing')
        if m.get('partitionsDone') is not None:
            self.partitions_done = m.get('partitionsDone')
        if m.get('partitionsFailed') is not None:
            self.partitions_failed = m.get('partitionsFailed')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('tablesDoing') is not None:
            self.tables_doing = m.get('tablesDoing')
        if m.get('tablesDone') is not None:
            self.tables_done = m.get('tablesDone')
        if m.get('tablesFailed') is not None:
            self.tables_failed = m.get('tablesFailed')
        if m.get('tablesPartDone') is not None:
            self.tables_part_done = m.get('tablesPartDone')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListMmsDbsResponseBodyData(TeaModel):
    def __init__(
        self,
        object_list: List[ListMmsDbsResponseBodyDataObjectList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.object_list = object_list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.object_list:
            for k in self.object_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['objectList'] = []
        if self.object_list is not None:
            for k in self.object_list:
                result['objectList'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_list = []
        if m.get('objectList') is not None:
            for k in m.get('objectList'):
                temp_model = ListMmsDbsResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListMmsDbsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListMmsDbsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListMmsDbsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListMmsDbsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMmsDbsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMmsDbsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMmsJobsRequestSorter(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListMmsJobsRequest(TeaModel):
    def __init__(
        self,
        sorter: ListMmsJobsRequestSorter = None,
        dst_db_name: str = None,
        dst_table_name: str = None,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        src_db_name: str = None,
        src_table_name: str = None,
        status: str = None,
        stopped: int = None,
    ):
        self.sorter = sorter
        self.dst_db_name = dst_db_name
        self.dst_table_name = dst_table_name
        self.name = name
        self.page_num = page_num
        self.page_size = page_size
        self.src_db_name = src_db_name
        self.src_table_name = src_table_name
        self.status = status
        self.stopped = stopped

    def validate(self):
        if self.sorter:
            self.sorter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sorter is not None:
            result['sorter'] = self.sorter.to_map()
        if self.dst_db_name is not None:
            result['dstDbName'] = self.dst_db_name
        if self.dst_table_name is not None:
            result['dstTableName'] = self.dst_table_name
        if self.name is not None:
            result['name'] = self.name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name
        if self.src_table_name is not None:
            result['srcTableName'] = self.src_table_name
        if self.status is not None:
            result['status'] = self.status
        if self.stopped is not None:
            result['stopped'] = self.stopped
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sorter') is not None:
            temp_model = ListMmsJobsRequestSorter()
            self.sorter = temp_model.from_map(m['sorter'])
        if m.get('dstDbName') is not None:
            self.dst_db_name = m.get('dstDbName')
        if m.get('dstTableName') is not None:
            self.dst_table_name = m.get('dstTableName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')
        if m.get('srcTableName') is not None:
            self.src_table_name = m.get('srcTableName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')
        return self


class ListMmsJobsResponseBodyDataObjectListConfig(TeaModel):
    def __init__(
        self,
        column_mapping: Dict[str, str] = None,
        enable_verification: bool = None,
        increment: bool = None,
        others: Dict[str, Any] = None,
        partition_filters: Dict[str, str] = None,
        partitions: List[int] = None,
        schema_only: bool = None,
        table_black_list: List[str] = None,
        table_mapping: Dict[str, str] = None,
        table_white_list: List[str] = None,
        tables: List[str] = None,
        task_type: str = None,
        tunnel_quota: str = None,
    ):
        self.column_mapping = column_mapping
        self.enable_verification = enable_verification
        self.increment = increment
        self.others = others
        self.partition_filters = partition_filters
        self.partitions = partitions
        self.schema_only = schema_only
        self.table_black_list = table_black_list
        self.table_mapping = table_mapping
        self.table_white_list = table_white_list
        self.tables = tables
        self.task_type = task_type
        self.tunnel_quota = tunnel_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_mapping is not None:
            result['columnMapping'] = self.column_mapping
        if self.enable_verification is not None:
            result['enableVerification'] = self.enable_verification
        if self.increment is not None:
            result['increment'] = self.increment
        if self.others is not None:
            result['others'] = self.others
        if self.partition_filters is not None:
            result['partitionFilters'] = self.partition_filters
        if self.partitions is not None:
            result['partitions'] = self.partitions
        if self.schema_only is not None:
            result['schemaOnly'] = self.schema_only
        if self.table_black_list is not None:
            result['tableBlackList'] = self.table_black_list
        if self.table_mapping is not None:
            result['tableMapping'] = self.table_mapping
        if self.table_white_list is not None:
            result['tableWhiteList'] = self.table_white_list
        if self.tables is not None:
            result['tables'] = self.tables
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnMapping') is not None:
            self.column_mapping = m.get('columnMapping')
        if m.get('enableVerification') is not None:
            self.enable_verification = m.get('enableVerification')
        if m.get('increment') is not None:
            self.increment = m.get('increment')
        if m.get('others') is not None:
            self.others = m.get('others')
        if m.get('partitionFilters') is not None:
            self.partition_filters = m.get('partitionFilters')
        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')
        if m.get('schemaOnly') is not None:
            self.schema_only = m.get('schemaOnly')
        if m.get('tableBlackList') is not None:
            self.table_black_list = m.get('tableBlackList')
        if m.get('tableMapping') is not None:
            self.table_mapping = m.get('tableMapping')
        if m.get('tableWhiteList') is not None:
            self.table_white_list = m.get('tableWhiteList')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')
        return self


class ListMmsJobsResponseBodyDataObjectList(TeaModel):
    def __init__(
        self,
        config: ListMmsJobsResponseBodyDataObjectListConfig = None,
        create_time: str = None,
        db_id: int = None,
        dst_db_name: str = None,
        dst_schema_name: str = None,
        eta: str = None,
        id: int = None,
        name: str = None,
        source_id: int = None,
        source_name: str = None,
        src_db_name: str = None,
        src_schema_name: str = None,
        status: str = None,
        stopped: bool = None,
        task_done: int = None,
        task_num: int = None,
        type: str = None,
    ):
        self.config = config
        self.create_time = create_time
        self.db_id = db_id
        self.dst_db_name = dst_db_name
        self.dst_schema_name = dst_schema_name
        self.eta = eta
        self.id = id
        self.name = name
        self.source_id = source_id
        self.source_name = source_name
        self.src_db_name = src_db_name
        self.src_schema_name = src_schema_name
        self.status = status
        self.stopped = stopped
        self.task_done = task_done
        self.task_num = task_num
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.db_id is not None:
            result['dbId'] = self.db_id
        if self.dst_db_name is not None:
            result['dstDbName'] = self.dst_db_name
        if self.dst_schema_name is not None:
            result['dstSchemaName'] = self.dst_schema_name
        if self.eta is not None:
            result['eta'] = self.eta
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name
        if self.src_schema_name is not None:
            result['srcSchemaName'] = self.src_schema_name
        if self.status is not None:
            result['status'] = self.status
        if self.stopped is not None:
            result['stopped'] = self.stopped
        if self.task_done is not None:
            result['taskDone'] = self.task_done
        if self.task_num is not None:
            result['taskNum'] = self.task_num
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = ListMmsJobsResponseBodyDataObjectListConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')
        if m.get('dstDbName') is not None:
            self.dst_db_name = m.get('dstDbName')
        if m.get('dstSchemaName') is not None:
            self.dst_schema_name = m.get('dstSchemaName')
        if m.get('eta') is not None:
            self.eta = m.get('eta')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')
        if m.get('srcSchemaName') is not None:
            self.src_schema_name = m.get('srcSchemaName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')
        if m.get('taskDone') is not None:
            self.task_done = m.get('taskDone')
        if m.get('taskNum') is not None:
            self.task_num = m.get('taskNum')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListMmsJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        object_list: List[ListMmsJobsResponseBodyDataObjectList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.object_list = object_list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.object_list:
            for k in self.object_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['objectList'] = []
        if self.object_list is not None:
            for k in self.object_list:
                result['objectList'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_list = []
        if m.get('objectList') is not None:
            for k in m.get('objectList'):
                temp_model = ListMmsJobsResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListMmsJobsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListMmsJobsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListMmsJobsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListMmsJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMmsJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMmsJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMmsPartitionsRequestSorter(TeaModel):
    def __init__(
        self,
        last_ddl_time: str = None,
        num_rows: str = None,
        size: str = None,
    ):
        self.last_ddl_time = last_ddl_time
        self.num_rows = num_rows
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time
        if self.num_rows is not None:
            result['numRows'] = self.num_rows
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListMmsPartitionsRequest(TeaModel):
    def __init__(
        self,
        sorter: ListMmsPartitionsRequestSorter = None,
        db_id: int = None,
        db_name: str = None,
        last_ddl_time_end: str = None,
        last_ddl_time_start: str = None,
        page_num: int = None,
        page_size: int = None,
        status: List[str] = None,
        table_name: str = None,
        updated: bool = None,
        value: str = None,
    ):
        self.sorter = sorter
        self.db_id = db_id
        self.db_name = db_name
        self.last_ddl_time_end = last_ddl_time_end
        self.last_ddl_time_start = last_ddl_time_start
        self.page_num = page_num
        self.page_size = page_size
        self.status = status
        self.table_name = table_name
        self.updated = updated
        self.value = value

    def validate(self):
        if self.sorter:
            self.sorter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sorter is not None:
            result['sorter'] = self.sorter.to_map()
        if self.db_id is not None:
            result['dbId'] = self.db_id
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.last_ddl_time_end is not None:
            result['lastDdlTimeEnd'] = self.last_ddl_time_end
        if self.last_ddl_time_start is not None:
            result['lastDdlTimeStart'] = self.last_ddl_time_start
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.updated is not None:
            result['updated'] = self.updated
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sorter') is not None:
            temp_model = ListMmsPartitionsRequestSorter()
            self.sorter = temp_model.from_map(m['sorter'])
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('lastDdlTimeEnd') is not None:
            self.last_ddl_time_end = m.get('lastDdlTimeEnd')
        if m.get('lastDdlTimeStart') is not None:
            self.last_ddl_time_start = m.get('lastDdlTimeStart')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListMmsPartitionsShrinkRequestSorter(TeaModel):
    def __init__(
        self,
        last_ddl_time: str = None,
        num_rows: str = None,
        size: str = None,
    ):
        self.last_ddl_time = last_ddl_time
        self.num_rows = num_rows
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time
        if self.num_rows is not None:
            result['numRows'] = self.num_rows
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListMmsPartitionsShrinkRequest(TeaModel):
    def __init__(
        self,
        sorter: ListMmsPartitionsShrinkRequestSorter = None,
        db_id: int = None,
        db_name: str = None,
        last_ddl_time_end: str = None,
        last_ddl_time_start: str = None,
        page_num: int = None,
        page_size: int = None,
        status_shrink: str = None,
        table_name: str = None,
        updated: bool = None,
        value: str = None,
    ):
        self.sorter = sorter
        self.db_id = db_id
        self.db_name = db_name
        self.last_ddl_time_end = last_ddl_time_end
        self.last_ddl_time_start = last_ddl_time_start
        self.page_num = page_num
        self.page_size = page_size
        self.status_shrink = status_shrink
        self.table_name = table_name
        self.updated = updated
        self.value = value

    def validate(self):
        if self.sorter:
            self.sorter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sorter is not None:
            result['sorter'] = self.sorter.to_map()
        if self.db_id is not None:
            result['dbId'] = self.db_id
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.last_ddl_time_end is not None:
            result['lastDdlTimeEnd'] = self.last_ddl_time_end
        if self.last_ddl_time_start is not None:
            result['lastDdlTimeStart'] = self.last_ddl_time_start
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status_shrink is not None:
            result['status'] = self.status_shrink
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.updated is not None:
            result['updated'] = self.updated
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sorter') is not None:
            temp_model = ListMmsPartitionsShrinkRequestSorter()
            self.sorter = temp_model.from_map(m['sorter'])
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('lastDdlTimeEnd') is not None:
            self.last_ddl_time_end = m.get('lastDdlTimeEnd')
        if m.get('lastDdlTimeStart') is not None:
            self.last_ddl_time_start = m.get('lastDdlTimeStart')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status_shrink = m.get('status')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListMmsPartitionsResponseBodyDataObjectList(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_name: str = None,
        id: int = None,
        last_ddl_time: str = None,
        num_rows: int = None,
        size: int = None,
        source_id: int = None,
        source_name: str = None,
        status: str = None,
        table_id: int = None,
        table_name: str = None,
        updated: bool = None,
        value: str = None,
    ):
        self.db_id = db_id
        self.db_name = db_name
        self.id = id
        # lastDdlTime
        self.last_ddl_time = last_ddl_time
        self.num_rows = num_rows
        self.size = size
        self.source_id = source_id
        self.source_name = source_name
        self.status = status
        self.table_id = table_id
        self.table_name = table_name
        self.updated = updated
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.id is not None:
            result['id'] = self.id
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time
        if self.num_rows is not None:
            result['numRows'] = self.num_rows
        if self.size is not None:
            result['size'] = self.size
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.status is not None:
            result['status'] = self.status
        if self.table_id is not None:
            result['tableId'] = self.table_id
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.updated is not None:
            result['updated'] = self.updated
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListMmsPartitionsResponseBodyData(TeaModel):
    def __init__(
        self,
        object_list: List[ListMmsPartitionsResponseBodyDataObjectList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.object_list = object_list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.object_list:
            for k in self.object_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['objectList'] = []
        if self.object_list is not None:
            for k in self.object_list:
                result['objectList'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_list = []
        if m.get('objectList') is not None:
            for k in m.get('objectList'):
                temp_model = ListMmsPartitionsResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListMmsPartitionsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListMmsPartitionsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListMmsPartitionsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListMmsPartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMmsPartitionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMmsPartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMmsTablesRequestSorter(TeaModel):
    def __init__(
        self,
        last_ddl_time: str = None,
        num_rows: str = None,
        size: str = None,
    ):
        self.last_ddl_time = last_ddl_time
        self.num_rows = num_rows
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time
        if self.num_rows is not None:
            result['numRows'] = self.num_rows
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListMmsTablesRequest(TeaModel):
    def __init__(
        self,
        sorter: ListMmsTablesRequestSorter = None,
        db_id: int = None,
        db_name: str = None,
        has_partitions: bool = None,
        last_ddl_time_end: str = None,
        last_ddl_time_start: str = None,
        name: str = None,
        only_name: bool = None,
        page_num: int = None,
        page_size: int = None,
        status: List[str] = None,
        type: str = None,
    ):
        self.sorter = sorter
        self.db_id = db_id
        self.db_name = db_name
        self.has_partitions = has_partitions
        self.last_ddl_time_end = last_ddl_time_end
        self.last_ddl_time_start = last_ddl_time_start
        self.name = name
        self.only_name = only_name
        self.page_num = page_num
        self.page_size = page_size
        self.status = status
        self.type = type

    def validate(self):
        if self.sorter:
            self.sorter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sorter is not None:
            result['sorter'] = self.sorter.to_map()
        if self.db_id is not None:
            result['dbId'] = self.db_id
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.has_partitions is not None:
            result['hasPartitions'] = self.has_partitions
        if self.last_ddl_time_end is not None:
            result['lastDdlTimeEnd'] = self.last_ddl_time_end
        if self.last_ddl_time_start is not None:
            result['lastDdlTimeStart'] = self.last_ddl_time_start
        if self.name is not None:
            result['name'] = self.name
        if self.only_name is not None:
            result['onlyName'] = self.only_name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sorter') is not None:
            temp_model = ListMmsTablesRequestSorter()
            self.sorter = temp_model.from_map(m['sorter'])
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('hasPartitions') is not None:
            self.has_partitions = m.get('hasPartitions')
        if m.get('lastDdlTimeEnd') is not None:
            self.last_ddl_time_end = m.get('lastDdlTimeEnd')
        if m.get('lastDdlTimeStart') is not None:
            self.last_ddl_time_start = m.get('lastDdlTimeStart')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('onlyName') is not None:
            self.only_name = m.get('onlyName')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListMmsTablesShrinkRequestSorter(TeaModel):
    def __init__(
        self,
        last_ddl_time: str = None,
        num_rows: str = None,
        size: str = None,
    ):
        self.last_ddl_time = last_ddl_time
        self.num_rows = num_rows
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time
        if self.num_rows is not None:
            result['numRows'] = self.num_rows
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListMmsTablesShrinkRequest(TeaModel):
    def __init__(
        self,
        sorter: ListMmsTablesShrinkRequestSorter = None,
        db_id: int = None,
        db_name: str = None,
        has_partitions: bool = None,
        last_ddl_time_end: str = None,
        last_ddl_time_start: str = None,
        name: str = None,
        only_name: bool = None,
        page_num: int = None,
        page_size: int = None,
        status_shrink: str = None,
        type: str = None,
    ):
        self.sorter = sorter
        self.db_id = db_id
        self.db_name = db_name
        self.has_partitions = has_partitions
        self.last_ddl_time_end = last_ddl_time_end
        self.last_ddl_time_start = last_ddl_time_start
        self.name = name
        self.only_name = only_name
        self.page_num = page_num
        self.page_size = page_size
        self.status_shrink = status_shrink
        self.type = type

    def validate(self):
        if self.sorter:
            self.sorter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sorter is not None:
            result['sorter'] = self.sorter.to_map()
        if self.db_id is not None:
            result['dbId'] = self.db_id
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.has_partitions is not None:
            result['hasPartitions'] = self.has_partitions
        if self.last_ddl_time_end is not None:
            result['lastDdlTimeEnd'] = self.last_ddl_time_end
        if self.last_ddl_time_start is not None:
            result['lastDdlTimeStart'] = self.last_ddl_time_start
        if self.name is not None:
            result['name'] = self.name
        if self.only_name is not None:
            result['onlyName'] = self.only_name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status_shrink is not None:
            result['status'] = self.status_shrink
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sorter') is not None:
            temp_model = ListMmsTablesShrinkRequestSorter()
            self.sorter = temp_model.from_map(m['sorter'])
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('hasPartitions') is not None:
            self.has_partitions = m.get('hasPartitions')
        if m.get('lastDdlTimeEnd') is not None:
            self.last_ddl_time_end = m.get('lastDdlTimeEnd')
        if m.get('lastDdlTimeStart') is not None:
            self.last_ddl_time_start = m.get('lastDdlTimeStart')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('onlyName') is not None:
            self.only_name = m.get('onlyName')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status_shrink = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListMmsTablesResponseBodyDataObjectListSchemaColumns(TeaModel):
    def __init__(
        self,
        comment: str = None,
        default_value: str = None,
        name: str = None,
        nullable: bool = None,
        type: str = None,
    ):
        self.comment = comment
        self.default_value = default_value
        self.name = name
        self.nullable = nullable
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.name is not None:
            result['name'] = self.name
        if self.nullable is not None:
            result['nullable'] = self.nullable
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListMmsTablesResponseBodyDataObjectListSchemaPartitions(TeaModel):
    def __init__(
        self,
        comment: str = None,
        default_value: str = None,
        name: str = None,
        nullable: bool = None,
        type: str = None,
    ):
        self.comment = comment
        self.default_value = default_value
        self.name = name
        self.nullable = nullable
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.name is not None:
            result['name'] = self.name
        if self.nullable is not None:
            result['nullable'] = self.nullable
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListMmsTablesResponseBodyDataObjectListSchema(TeaModel):
    def __init__(
        self,
        columns: List[ListMmsTablesResponseBodyDataObjectListSchemaColumns] = None,
        comment: str = None,
        name: str = None,
        partitions: List[ListMmsTablesResponseBodyDataObjectListSchemaPartitions] = None,
    ):
        self.columns = columns
        self.comment = comment
        self.name = name
        self.partitions = partitions

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()
        if self.partitions:
            for k in self.partitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['columns'].append(k.to_map() if k else None)
        if self.comment is not None:
            result['comment'] = self.comment
        if self.name is not None:
            result['name'] = self.name
        result['partitions'] = []
        if self.partitions is not None:
            for k in self.partitions:
                result['partitions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('columns') is not None:
            for k in m.get('columns'):
                temp_model = ListMmsTablesResponseBodyDataObjectListSchemaColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.partitions = []
        if m.get('partitions') is not None:
            for k in m.get('partitions'):
                temp_model = ListMmsTablesResponseBodyDataObjectListSchemaPartitions()
                self.partitions.append(temp_model.from_map(k))
        return self


class ListMmsTablesResponseBodyDataObjectList(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        db_name: str = None,
        extra: str = None,
        has_partitions: bool = None,
        id: int = None,
        input_format: str = None,
        last_ddl_time: str = None,
        location: str = None,
        name: str = None,
        num_rows: int = None,
        output_format: str = None,
        owner: str = None,
        partitions: int = None,
        partitions_doing: int = None,
        partitions_done: int = None,
        partitions_failed: int = None,
        schema: ListMmsTablesResponseBodyDataObjectListSchema = None,
        serde: str = None,
        size: int = None,
        source_id: int = None,
        source_name: str = None,
        status: str = None,
        type: str = None,
        updated: bool = None,
    ):
        self.db_id = db_id
        self.db_name = db_name
        self.extra = extra
        self.has_partitions = has_partitions
        # table ID
        self.id = id
        # inputFormat
        self.input_format = input_format
        # lastDdlTime
        self.last_ddl_time = last_ddl_time
        self.location = location
        self.name = name
        self.num_rows = num_rows
        # outFormat
        self.output_format = output_format
        self.owner = owner
        self.partitions = partitions
        self.partitions_doing = partitions_doing
        self.partitions_done = partitions_done
        self.partitions_failed = partitions_failed
        self.schema = schema
        # serde
        self.serde = serde
        self.size = size
        self.source_id = source_id
        self.source_name = source_name
        self.status = status
        self.type = type
        self.updated = updated

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['dbId'] = self.db_id
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.extra is not None:
            result['extra'] = self.extra
        if self.has_partitions is not None:
            result['hasPartitions'] = self.has_partitions
        if self.id is not None:
            result['id'] = self.id
        if self.input_format is not None:
            result['inputFormat'] = self.input_format
        if self.last_ddl_time is not None:
            result['lastDdlTime'] = self.last_ddl_time
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        if self.num_rows is not None:
            result['numRows'] = self.num_rows
        if self.output_format is not None:
            result['outputFormat'] = self.output_format
        if self.owner is not None:
            result['owner'] = self.owner
        if self.partitions is not None:
            result['partitions'] = self.partitions
        if self.partitions_doing is not None:
            result['partitionsDoing'] = self.partitions_doing
        if self.partitions_done is not None:
            result['partitionsDone'] = self.partitions_done
        if self.partitions_failed is not None:
            result['partitionsFailed'] = self.partitions_failed
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        if self.serde is not None:
            result['serde'] = self.serde
        if self.size is not None:
            result['size'] = self.size
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('hasPartitions') is not None:
            self.has_partitions = m.get('hasPartitions')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('inputFormat') is not None:
            self.input_format = m.get('inputFormat')
        if m.get('lastDdlTime') is not None:
            self.last_ddl_time = m.get('lastDdlTime')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('numRows') is not None:
            self.num_rows = m.get('numRows')
        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('partitions') is not None:
            self.partitions = m.get('partitions')
        if m.get('partitionsDoing') is not None:
            self.partitions_doing = m.get('partitionsDoing')
        if m.get('partitionsDone') is not None:
            self.partitions_done = m.get('partitionsDone')
        if m.get('partitionsFailed') is not None:
            self.partitions_failed = m.get('partitionsFailed')
        if m.get('schema') is not None:
            temp_model = ListMmsTablesResponseBodyDataObjectListSchema()
            self.schema = temp_model.from_map(m['schema'])
        if m.get('serde') is not None:
            self.serde = m.get('serde')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListMmsTablesResponseBodyData(TeaModel):
    def __init__(
        self,
        object_list: List[ListMmsTablesResponseBodyDataObjectList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.object_list = object_list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.object_list:
            for k in self.object_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['objectList'] = []
        if self.object_list is not None:
            for k in self.object_list:
                result['objectList'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_list = []
        if m.get('objectList') is not None:
            for k in m.get('objectList'):
                temp_model = ListMmsTablesResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListMmsTablesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListMmsTablesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListMmsTablesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListMmsTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMmsTablesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMmsTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMmsTaskLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        action: str = None,
        create_time: str = None,
        id: int = None,
        msg: str = None,
        source_id: int = None,
        status: str = None,
        task_id: int = None,
    ):
        self.action = action
        self.create_time = create_time
        self.id = id
        self.msg = msg
        self.source_id = source_id
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.msg is not None:
            result['msg'] = self.msg
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListMmsTaskLogsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListMmsTaskLogsResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListMmsTaskLogsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListMmsTaskLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMmsTaskLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMmsTaskLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMmsTasksRequestSorter(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        status: str = None,
    ):
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListMmsTasksRequest(TeaModel):
    def __init__(
        self,
        sorter: ListMmsTasksRequestSorter = None,
        dst_db_name: str = None,
        dst_table_name: str = None,
        job_id: int = None,
        job_name: str = None,
        page_num: int = None,
        page_size: int = None,
        partition: str = None,
        src_db_name: str = None,
        src_table_name: str = None,
        status: str = None,
    ):
        self.sorter = sorter
        self.dst_db_name = dst_db_name
        self.dst_table_name = dst_table_name
        self.job_id = job_id
        self.job_name = job_name
        self.page_num = page_num
        self.page_size = page_size
        self.partition = partition
        self.src_db_name = src_db_name
        self.src_table_name = src_table_name
        self.status = status

    def validate(self):
        if self.sorter:
            self.sorter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sorter is not None:
            result['sorter'] = self.sorter.to_map()
        if self.dst_db_name is not None:
            result['dstDbName'] = self.dst_db_name
        if self.dst_table_name is not None:
            result['dstTableName'] = self.dst_table_name
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.job_name is not None:
            result['jobName'] = self.job_name
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.partition is not None:
            result['partition'] = self.partition
        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name
        if self.src_table_name is not None:
            result['srcTableName'] = self.src_table_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sorter') is not None:
            temp_model = ListMmsTasksRequestSorter()
            self.sorter = temp_model.from_map(m['sorter'])
        if m.get('dstDbName') is not None:
            self.dst_db_name = m.get('dstDbName')
        if m.get('dstTableName') is not None:
            self.dst_table_name = m.get('dstTableName')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')
        if m.get('srcTableName') is not None:
            self.src_table_name = m.get('srcTableName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListMmsTasksResponseBodyDataObjectList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        db_id: int = None,
        dst_db_name: str = None,
        dst_schema_name: str = None,
        dst_table_name: str = None,
        end_time: str = None,
        id: int = None,
        job_id: int = None,
        job_name: str = None,
        retried_times: int = None,
        running: bool = None,
        source_id: int = None,
        source_name: str = None,
        src_db_name: str = None,
        src_schema_name: str = None,
        src_table_name: str = None,
        start_time: str = None,
        status: str = None,
        stopped: bool = None,
        table_id: int = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.db_id = db_id
        self.dst_db_name = dst_db_name
        self.dst_schema_name = dst_schema_name
        self.dst_table_name = dst_table_name
        self.end_time = end_time
        self.id = id
        self.job_id = job_id
        self.job_name = job_name
        self.retried_times = retried_times
        self.running = running
        self.source_id = source_id
        self.source_name = source_name
        self.src_db_name = src_db_name
        self.src_schema_name = src_schema_name
        self.src_table_name = src_table_name
        self.start_time = start_time
        self.status = status
        self.stopped = stopped
        self.table_id = table_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.db_id is not None:
            result['dbId'] = self.db_id
        if self.dst_db_name is not None:
            result['dstDbName'] = self.dst_db_name
        if self.dst_schema_name is not None:
            result['dstSchemaName'] = self.dst_schema_name
        if self.dst_table_name is not None:
            result['dstTableName'] = self.dst_table_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.id is not None:
            result['id'] = self.id
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.job_name is not None:
            result['jobName'] = self.job_name
        if self.retried_times is not None:
            result['retriedTimes'] = self.retried_times
        if self.running is not None:
            result['running'] = self.running
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.src_db_name is not None:
            result['srcDbName'] = self.src_db_name
        if self.src_schema_name is not None:
            result['srcSchemaName'] = self.src_schema_name
        if self.src_table_name is not None:
            result['srcTableName'] = self.src_table_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.stopped is not None:
            result['stopped'] = self.stopped
        if self.table_id is not None:
            result['tableId'] = self.table_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dbId') is not None:
            self.db_id = m.get('dbId')
        if m.get('dstDbName') is not None:
            self.dst_db_name = m.get('dstDbName')
        if m.get('dstSchemaName') is not None:
            self.dst_schema_name = m.get('dstSchemaName')
        if m.get('dstTableName') is not None:
            self.dst_table_name = m.get('dstTableName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('jobName') is not None:
            self.job_name = m.get('jobName')
        if m.get('retriedTimes') is not None:
            self.retried_times = m.get('retriedTimes')
        if m.get('running') is not None:
            self.running = m.get('running')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('srcDbName') is not None:
            self.src_db_name = m.get('srcDbName')
        if m.get('srcSchemaName') is not None:
            self.src_schema_name = m.get('srcSchemaName')
        if m.get('srcTableName') is not None:
            self.src_table_name = m.get('srcTableName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')
        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListMmsTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        object_list: List[ListMmsTasksResponseBodyDataObjectList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.object_list = object_list
        self.page_num = page_num
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.object_list:
            for k in self.object_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['objectList'] = []
        if self.object_list is not None:
            for k in self.object_list:
                result['objectList'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_list = []
        if m.get('objectList') is not None:
            for k in m.get('objectList'):
                temp_model = ListMmsTasksResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k))
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListMmsTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: ListMmsTasksResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListMmsTasksResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListMmsTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMmsTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMmsTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPackagesResponseBodyDataCreatedPackages(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        name: str = None,
    ):
        # The time when the package was created.
        self.create_time = create_time
        # The name of the package.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListPackagesResponseBodyDataInstalledPackages(TeaModel):
    def __init__(
        self,
        install_time: int = None,
        name: str = None,
        source_project: str = None,
        status: str = None,
    ):
        # The time when the package was installed.
        self.install_time = install_time
        # The name of the package.
        self.name = name
        # The project to which the package belongs. This parameter is required if the package is installed in the MaxCompute project.
        self.source_project = source_project
        # The status of the package.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.install_time is not None:
            result['installTime'] = self.install_time
        if self.name is not None:
            result['name'] = self.name
        if self.source_project is not None:
            result['sourceProject'] = self.source_project
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('installTime') is not None:
            self.install_time = m.get('installTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourceProject') is not None:
            self.source_project = m.get('sourceProject')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListPackagesResponseBodyData(TeaModel):
    def __init__(
        self,
        created_packages: List[ListPackagesResponseBodyDataCreatedPackages] = None,
        installed_packages: List[ListPackagesResponseBodyDataInstalledPackages] = None,
    ):
        # The packages that were created.
        self.created_packages = created_packages
        # The packages that were installed.
        self.installed_packages = installed_packages

    def validate(self):
        if self.created_packages:
            for k in self.created_packages:
                if k:
                    k.validate()
        if self.installed_packages:
            for k in self.installed_packages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['createdPackages'] = []
        if self.created_packages is not None:
            for k in self.created_packages:
                result['createdPackages'].append(k.to_map() if k else None)
        result['installedPackages'] = []
        if self.installed_packages is not None:
            for k in self.installed_packages:
                result['installedPackages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.created_packages = []
        if m.get('createdPackages') is not None:
            for k in m.get('createdPackages'):
                temp_model = ListPackagesResponseBodyDataCreatedPackages()
                self.created_packages.append(temp_model.from_map(k))
        self.installed_packages = []
        if m.get('installedPackages') is not None:
            for k in m.get('installedPackages'):
                temp_model = ListPackagesResponseBodyDataInstalledPackages()
                self.installed_packages.append(temp_model.from_map(k))
        return self


class ListPackagesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListPackagesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListPackagesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPackagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectUsersResponseBodyDataUsers(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the user.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListProjectUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        users: List[ListProjectUsersResponseBodyDataUsers] = None,
    ):
        # An array that contains users.
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = ListProjectUsersResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListProjectUsersResponseBody(TeaModel):
    def __init__(
        self,
        data: ListProjectUsersResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListProjectUsersResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProjectUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        list_system_catalog: bool = None,
        marker: str = None,
        max_item: int = None,
        prefix: str = None,
        quota_name: str = None,
        quota_nick_name: str = None,
        region: str = None,
        sale_tags: str = None,
        tenant_id: str = None,
        type: str = None,
    ):
        # Specifies whether to list the built-in **SYSTEM_CATALOG** projects that are used to provide data such as project metadata and historical usage data. For more information, see [Tenant-level Information Schema](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/tenant-level-information-schema).
        # 
        # Valid values:
        # 
        # *   true: The built-in SYSTEM_CATALOG projects are listed.
        # *   false: The built-in SYSTEM_CATALOG projects are not listed.
        self.list_system_catalog = list_system_catalog
        # The maximum number of entries to return on each page.
        self.marker = marker
        # The maximum number of entries per page. Default value: 10.
        self.max_item = max_item
        # Specifies the marker after which the returned list begins.
        self.prefix = prefix
        # The quota name that is automatically generated. You can log on to the [MaxCompute console](https://maxcompute.console.aliyun.com), choose **Workspace** > **Quotas** from the left-side navigation pane, and then view the quota name on the **Quotas** page.
        self.quota_name = quota_name
        # The quota nickname. You can log on to the [MaxCompute console](https://maxcompute.console.aliyun.com), choose **Workspace** > **Quotas** from the left-side navigation pane, and then view the quota nickname on the **Quotas** page.
        self.quota_nick_name = quota_nick_name
        # The region ID.
        self.region = region
        # The instance ID and billing method of the default computing quota.
        self.sale_tags = sale_tags
        # The tenant ID. You can log on to the [MaxCompute console](https://maxcompute.console.aliyun.com), and choose **Tenants** > **Tenant Property** from the left-side navigation pane to view the tenant ID.
        self.tenant_id = tenant_id
        # The project type. Valid values:
        # 
        # *   **managed**: internal project
        # *   **external**: external project
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_system_catalog is not None:
            result['listSystemCatalog'] = self.list_system_catalog
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.quota_name is not None:
            result['quotaName'] = self.quota_name
        if self.quota_nick_name is not None:
            result['quotaNickName'] = self.quota_nick_name
        if self.region is not None:
            result['region'] = self.region
        if self.sale_tags is not None:
            result['saleTags'] = self.sale_tags
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('listSystemCatalog') is not None:
            self.list_system_catalog = m.get('listSystemCatalog')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('quotaName') is not None:
            self.quota_name = m.get('quotaName')
        if m.get('quotaNickName') is not None:
            self.quota_nick_name = m.get('quotaNickName')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('saleTags') is not None:
            self.sale_tags = m.get('saleTags')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListProjectsResponseBodyDataProjectsIpWhiteList(TeaModel):
    def __init__(
        self,
        ip_list: str = None,
        vpc_ip_list: str = None,
    ):
        # The IP address whitelist for access over the Internet or the network for interconnecting with other Alibaba Cloud services.
        # 
        # >  If you configure only the IP address whitelist for access over the Internet or the network for interconnecting with other Alibaba Cloud services, the access over the Internet or the network for interconnecting with other Alibaba Cloud services is subject to configurations, and access over a virtual private cloud (VPC) is not allowed.
        self.ip_list = ip_list
        # The IP address whitelist for access over a VPC.
        # 
        # >  If you configure only the IP address whitelist for access over a VPC, the access over a VPC is subject to configurations, and the access over the Internet or the network for interconnecting with other Alibaba Cloud services is not allowed.
        self.vpc_ip_list = vpc_ip_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_list is not None:
            result['ipList'] = self.ip_list
        if self.vpc_ip_list is not None:
            result['vpcIpList'] = self.vpc_ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')
        if m.get('vpcIpList') is not None:
            self.vpc_ip_list = m.get('vpcIpList')
        return self


class ListProjectsResponseBodyDataProjectsPropertiesEncryption(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        enable: bool = None,
        key: str = None,
    ):
        # The data encryption algorithm that is supported by the key. Valid values: AES256, AESCTR, and RC4.
        self.algorithm = algorithm
        # Indicates whether the data encryption feature needs to be enabled for the project. For more information about data encryption, see
        # 
        # [Storage encryption](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/storage-encryption).
        self.enable = enable
        # The type of key that is used for data encryption. You can select MaxCompute Default Key or Bring Your Own Key (BYOK) as the key type. If you select MaxCompute Default Key, the default key that is created by MaxCompute is used.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.enable is not None:
            result['enable'] = self.enable
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class ListProjectsResponseBodyDataProjectsPropertiesExternalProjectProperties(TeaModel):
    def __init__(
        self,
        is_external_catalog_bound: str = None,
    ):
        # Indicates whether the external project is an external project for [data lakehouse solution 2.0](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/lake-warehouse-integrated-2-0-use-guide).
        self.is_external_catalog_bound = is_external_catalog_bound

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_external_catalog_bound is not None:
            result['isExternalCatalogBound'] = self.is_external_catalog_bound
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isExternalCatalogBound') is not None:
            self.is_external_catalog_bound = m.get('isExternalCatalogBound')
        return self


class ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The lifecycle type. Valid values:
        # 
        # *   **mandatory**: The lifecycle clause is required in a table creation statement.
        # *   **optional**: The lifecycle clause is optional in a table creation statement. If you do not configure a lifecycle for a table, the table does not expire.
        # *   **inherit**: If you do not configure a lifecycle for a table when you create the table, the value of the odps.table.lifecycle.value parameter is used as the table lifecycle by default.
        self.type = type
        # The table lifecycle. Unit: days. Valid values: 1 to 37231. Default value: 37231.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListProjectsResponseBodyDataProjectsProperties(TeaModel):
    def __init__(
        self,
        allow_full_scan: bool = None,
        enable_decimal_2: bool = None,
        enable_tunnel_quota_route: bool = None,
        encryption: ListProjectsResponseBodyDataProjectsPropertiesEncryption = None,
        external_project_properties: ListProjectsResponseBodyDataProjectsPropertiesExternalProjectProperties = None,
        retention_days: int = None,
        sql_metering_max: str = None,
        table_lifecycle: ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle = None,
        timezone: str = None,
        tunnel_quota: str = None,
        type_system: str = None,
    ):
        # Indicates whether a full table scan is allowed in the project. A full table scan occupies a large number of resources, which reduces data processing efficiency. By default, the full table scan feature is disabled.
        self.allow_full_scan = allow_full_scan
        # Indicates whether the DECIMAL type of the MaxCompute V2.0 data type edition is enabled.
        self.enable_decimal_2 = enable_decimal_2
        # Indicates whether the routing of the Tunnel resource group is enabled.
        # 
        # *   true: The data transfer tasks that are submitted by the project by default use the Tunnel resource group that is bound to the project.
        # *   false: The data transfer tasks that are submitted by the project by default use the Tunnel shared resource group.
        self.enable_tunnel_quota_route = enable_tunnel_quota_route
        # The storage encryption properties.
        self.encryption = encryption
        # The properties of the external project.
        self.external_project_properties = external_project_properties
        # The retention period for backup data. Unit: days. During the retention period, you can restore data of the version in use to the backup data of any version. Valid values: [0,30]. Default value: 1. The value 0 indicates that the backup feature is disabled.
        self.retention_days = retention_days
        # The maximum consumption threshold of a single SQL statement. Formula: Amount of scanned data (GB) × Complexity.
        self.sql_metering_max = sql_metering_max
        # The table lifecycle properties.
        self.table_lifecycle = table_lifecycle
        # The time zone that is used by your project. The time zone is the same as the time zone specified by `odps.sql.timezone`.
        self.timezone = timezone
        # The [Tunnel](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/overview-of-dts) resource group that is bound to the project.
        # 
        # *   Default resource group: The Tunnel shared resource group is used. You cannot use the subscription-based Tunnel resource group for the project. The default resource group is automatically used by the Tunnel service of your project, regardless of the parameter setting.
        # *   Subscription-based Tunnel resource group: You can use the subscription-based Tunnel resource group for the project.
        self.tunnel_quota = tunnel_quota
        # The data type edition. Valid values:
        # 
        # *   **1**: MaxCompute V1.0 data type edition
        # *   **2**: MaxCompute V2.0 data type edition
        # *   **hive**: Hive-compatible data type edition
        # 
        # For more information about the differences among the three data type editions, see [Data type editions](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/data-type-editions).
        self.type_system = type_system

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.external_project_properties:
            self.external_project_properties.validate()
        if self.table_lifecycle:
            self.table_lifecycle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_full_scan is not None:
            result['allowFullScan'] = self.allow_full_scan
        if self.enable_decimal_2 is not None:
            result['enableDecimal2'] = self.enable_decimal_2
        if self.enable_tunnel_quota_route is not None:
            result['enableTunnelQuotaRoute'] = self.enable_tunnel_quota_route
        if self.encryption is not None:
            result['encryption'] = self.encryption.to_map()
        if self.external_project_properties is not None:
            result['externalProjectProperties'] = self.external_project_properties.to_map()
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        if self.sql_metering_max is not None:
            result['sqlMeteringMax'] = self.sql_metering_max
        if self.table_lifecycle is not None:
            result['tableLifecycle'] = self.table_lifecycle.to_map()
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota
        if self.type_system is not None:
            result['typeSystem'] = self.type_system
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowFullScan') is not None:
            self.allow_full_scan = m.get('allowFullScan')
        if m.get('enableDecimal2') is not None:
            self.enable_decimal_2 = m.get('enableDecimal2')
        if m.get('enableTunnelQuotaRoute') is not None:
            self.enable_tunnel_quota_route = m.get('enableTunnelQuotaRoute')
        if m.get('encryption') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsPropertiesEncryption()
            self.encryption = temp_model.from_map(m['encryption'])
        if m.get('externalProjectProperties') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsPropertiesExternalProjectProperties()
            self.external_project_properties = temp_model.from_map(m['externalProjectProperties'])
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        if m.get('sqlMeteringMax') is not None:
            self.sql_metering_max = m.get('sqlMeteringMax')
        if m.get('tableLifecycle') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle()
            self.table_lifecycle = temp_model.from_map(m['tableLifecycle'])
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')
        if m.get('typeSystem') is not None:
            self.type_system = m.get('typeSystem')
        return self


class ListProjectsResponseBodyDataProjectsSaleTag(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The instance ID of the default computing quota.
        self.resource_id = resource_id
        # The billing method of the default computing quota.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection(TeaModel):
    def __init__(
        self,
        exception_policy: str = None,
        protected: bool = None,
    ):
        # If you enable the project data protection mechanism, you can configure exception or trusted projects. This allows specified users to transfer data of a specified object to a specified project. The project data protection mechanism does not take effect in all the situations that are specified in the exception policy.
        self.exception_policy = exception_policy
        # Indicates whether the [data protection mechanism](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/project-data-protection) is enabled for the project. This allows or denies data transfer across projects. By default, the data protection mechanism is disabled.
        self.protected = protected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exception_policy is not None:
            result['exceptionPolicy'] = self.exception_policy
        if self.protected is not None:
            result['protected'] = self.protected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exceptionPolicy') is not None:
            self.exception_policy = m.get('exceptionPolicy')
        if m.get('protected') is not None:
            self.protected = m.get('protected')
        return self


class ListProjectsResponseBodyDataProjectsSecurityProperties(TeaModel):
    def __init__(
        self,
        enable_download_privilege: bool = None,
        label_security: bool = None,
        object_creator_has_access_permission: bool = None,
        object_creator_has_grant_permission: bool = None,
        project_protection: ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection = None,
        using_acl: bool = None,
        using_policy: bool = None,
    ):
        # Indicates whether the [download control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/label-based-access-control) feature is enabled. By default, this feature is disabled.
        self.enable_download_privilege = enable_download_privilege
        # Indicates whether the [label-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/label-based-access-control) feature is enabled. By default, this feature is disabled.
        self.label_security = label_security
        # Indicates whether to allow the object creator to have the access permissions on the object. The default value is true, which indicates that the object creator has the access permissions on the object.
        self.object_creator_has_access_permission = object_creator_has_access_permission
        # Indicates whether the object creator has the authorization permissions on the object. The default value is true, which indicates that the object creator has the authorization permissions on the object.
        self.object_creator_has_grant_permission = object_creator_has_grant_permission
        # The properties of the [data protection mechanism](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/project-data-protection).
        self.project_protection = project_protection
        # Indicates whether the [ACL-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/acl-based-access-control) feature is enabled. By default, this feature is enabled.
        self.using_acl = using_acl
        # Indicates whether the [policy-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/policy-based-access-control-1) feature is enabled. By default, this feature is enabled.
        self.using_policy = using_policy

    def validate(self):
        if self.project_protection:
            self.project_protection.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_download_privilege is not None:
            result['enableDownloadPrivilege'] = self.enable_download_privilege
        if self.label_security is not None:
            result['labelSecurity'] = self.label_security
        if self.object_creator_has_access_permission is not None:
            result['objectCreatorHasAccessPermission'] = self.object_creator_has_access_permission
        if self.object_creator_has_grant_permission is not None:
            result['objectCreatorHasGrantPermission'] = self.object_creator_has_grant_permission
        if self.project_protection is not None:
            result['projectProtection'] = self.project_protection.to_map()
        if self.using_acl is not None:
            result['usingAcl'] = self.using_acl
        if self.using_policy is not None:
            result['usingPolicy'] = self.using_policy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableDownloadPrivilege') is not None:
            self.enable_download_privilege = m.get('enableDownloadPrivilege')
        if m.get('labelSecurity') is not None:
            self.label_security = m.get('labelSecurity')
        if m.get('objectCreatorHasAccessPermission') is not None:
            self.object_creator_has_access_permission = m.get('objectCreatorHasAccessPermission')
        if m.get('objectCreatorHasGrantPermission') is not None:
            self.object_creator_has_grant_permission = m.get('objectCreatorHasGrantPermission')
        if m.get('projectProtection') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection()
            self.project_protection = temp_model.from_map(m['projectProtection'])
        if m.get('usingAcl') is not None:
            self.using_acl = m.get('usingAcl')
        if m.get('usingPolicy') is not None:
            self.using_policy = m.get('usingPolicy')
        return self


class ListProjectsResponseBodyDataProjects(TeaModel):
    def __init__(
        self,
        comment: str = None,
        cost_storage: str = None,
        created_time: int = None,
        default_quota: str = None,
        ip_white_list: ListProjectsResponseBodyDataProjectsIpWhiteList = None,
        name: str = None,
        owner: str = None,
        properties: ListProjectsResponseBodyDataProjectsProperties = None,
        region_id: str = None,
        sale_tag: ListProjectsResponseBodyDataProjectsSaleTag = None,
        security_properties: ListProjectsResponseBodyDataProjectsSecurityProperties = None,
        status: str = None,
        three_tier_model: bool = None,
        type: str = None,
    ):
        # The project description.
        self.comment = comment
        # The total storage usage. The storage space that is occupied by your project, which is the logical storage space after your project data is collected and compressed.
        self.cost_storage = cost_storage
        # The creation time.
        self.created_time = created_time
        # The default computing quota that is used to allocate computing resources. If you do not specify a computing quota for your project, the jobs that are initiated by your project consume the computing resources in the default quota. For more information about how to use computing resources, see [Use quota groups for computing resources](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/use-of-computing-resources)
        self.default_quota = default_quota
        # The information about the IP address whitelist.
        self.ip_white_list = ip_white_list
        # The name of the project.
        self.name = name
        # The account information of the project owner.
        self.owner = owner
        # The basic properties of the project.
        self.properties = properties
        # The region ID.
        self.region_id = region_id
        # The instance ID and billing method of the default computing quota.
        self.sale_tag = sale_tag
        # The permission properties.
        self.security_properties = security_properties
        # The project status. Valid values:
        # 
        # *   **AVAILABLE**\
        # *   **READONLY**\
        # *   **FROZEN**\
        # *   **DELETING**\
        self.status = status
        # Indicates whether data storage by schema is supported. MaxCompute supports the schema feature. This feature allows you to classify objects such as tables, resources, and user-defined functions (UDFs) in a project by schema. You can create multiple schemas in a project. For more information, see [Schema-related operations](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/schema-related-operations).
        # 
        # Valid values:
        # 
        # *   true: supported
        # *   false: not supported
        self.three_tier_model = three_tier_model
        # The project type. Valid values:
        # 
        # *   **managed**: internal project
        # *   **external**: external project
        self.type = type

    def validate(self):
        if self.ip_white_list:
            self.ip_white_list.validate()
        if self.properties:
            self.properties.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.security_properties:
            self.security_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.cost_storage is not None:
            result['costStorage'] = self.cost_storage
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.default_quota is not None:
            result['defaultQuota'] = self.default_quota
        if self.ip_white_list is not None:
            result['ipWhiteList'] = self.ip_white_list.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.properties is not None:
            result['properties'] = self.properties.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.security_properties is not None:
            result['securityProperties'] = self.security_properties.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.three_tier_model is not None:
            result['threeTierModel'] = self.three_tier_model
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('costStorage') is not None:
            self.cost_storage = m.get('costStorage')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('defaultQuota') is not None:
            self.default_quota = m.get('defaultQuota')
        if m.get('ipWhiteList') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsIpWhiteList()
            self.ip_white_list = temp_model.from_map(m['ipWhiteList'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('properties') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsProperties()
            self.properties = temp_model.from_map(m['properties'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('securityProperties') is not None:
            temp_model = ListProjectsResponseBodyDataProjectsSecurityProperties()
            self.security_properties = temp_model.from_map(m['securityProperties'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('threeTierModel') is not None:
            self.three_tier_model = m.get('threeTierModel')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListProjectsResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        marker: str = None,
        max_item: int = None,
        projects: List[ListProjectsResponseBodyDataProjects] = None,
    ):
        # A pagination token. Only continuous page turning is supported. If NextToken is not empty, the next page exists. The value of NextToken can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # The list of projects.
        self.projects = projects

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['projects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.projects = []
        if m.get('projects') is not None:
            for k in m.get('projects'):
                temp_model = ListProjectsResponseBodyDataProjects()
                self.projects.append(temp_model.from_map(k))
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListProjectsResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListProjectsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotasRequest(TeaModel):
    def __init__(
        self,
        billing_type: str = None,
        marker: str = None,
        max_item: int = None,
        product_id: str = None,
        region: str = None,
        sale_tags: str = None,
        tenant_id: str = None,
    ):
        # The billing method of the quota.
        self.billing_type = billing_type
        # Specifies the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries to return on each page.
        self.max_item = max_item
        # The service ID.
        self.product_id = product_id
        # The ID of the region.
        self.region = region
        # The cost tag. You can filter out quota objects based on the cost tag. The cost tag is created when you tag a service.
        self.sale_tags = sale_tags
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_type is not None:
            result['billingType'] = self.billing_type
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.product_id is not None:
            result['productId'] = self.product_id
        if self.region is not None:
            result['region'] = self.region
        if self.sale_tags is not None:
            result['saleTags'] = self.sale_tags
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingType') is not None:
            self.billing_type = m.get('billingType')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('productId') is not None:
            self.product_id = m.get('productId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('saleTags') is not None:
            self.sale_tags = m.get('saleTags')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListQuotasResponseBodyDataQuotaInfoListTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListQuotasResponseBodyDataQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyDataQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        enable_priority: bool = None,
        force_reserved_min: bool = None,
        max_cu: int = None,
        min_cu: int = None,
        scheduler_type: str = None,
        single_job_culimit: int = None,
    ):
        self.elastic_reserved_cu = elastic_reserved_cu
        self.enable_priority = enable_priority
        self.force_reserved_min = force_reserved_min
        # This parameter is required.
        self.max_cu = max_cu
        # This parameter is required.
        self.min_cu = min_cu
        self.scheduler_type = scheduler_type
        self.single_job_culimit = single_job_culimit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        if self.enable_priority is not None:
            result['enablePriority'] = self.enable_priority
        if self.force_reserved_min is not None:
            result['forceReservedMin'] = self.force_reserved_min
        if self.max_cu is not None:
            result['maxCU'] = self.max_cu
        if self.min_cu is not None:
            result['minCU'] = self.min_cu
        if self.scheduler_type is not None:
            result['schedulerType'] = self.scheduler_type
        if self.single_job_culimit is not None:
            result['singleJobCULimit'] = self.single_job_culimit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        if m.get('enablePriority') is not None:
            self.enable_priority = m.get('enablePriority')
        if m.get('forceReservedMin') is not None:
            self.force_reserved_min = m.get('forceReservedMin')
        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')
        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')
        if m.get('schedulerType') is not None:
            self.scheduler_type = m.get('schedulerType')
        if m.get('singleJobCULimit') is not None:
            self.single_job_culimit = m.get('singleJobCULimit')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListParameter = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag = None,
        schedule_info: ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The nickname of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the endpoint group.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version of the algorithm image.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.parameter:
            self.parameter.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBodyDataQuotaInfoList(TeaModel):
    def __init__(
        self,
        tags: List[ListQuotasResponseBodyDataQuotaInfoListTags] = None,
        billing_policy: ListQuotasResponseBodyDataQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: ListQuotasResponseBodyDataQuotaInfoListSaleTag = None,
        schedule_info: ListQuotasResponseBodyDataQuotaInfoListScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The tags.
        self.tags = tags
        # The information of the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The quota ID.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the endpoint group.
        self.status = status
        # The information of the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListQuotasResponseBodyDataQuotaInfoListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyDataQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = ListQuotasResponseBodyDataQuotaInfoListSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        marker: str = None,
        max_item: int = None,
        quota_info_list: List[ListQuotasResponseBodyDataQuotaInfoList] = None,
    ):
        # A pagination token. Only continuous page turning is supported. If NextToken is not empty, the next page exists. The value of NextToken can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # The list of quotas.
        self.quota_info_list = quota_info_list

    def validate(self):
        if self.quota_info_list:
            for k in self.quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['quotaInfoList'] = []
        if self.quota_info_list is not None:
            for k in self.quota_info_list:
                result['quotaInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.quota_info_list = []
        if m.get('quotaInfoList') is not None:
            for k in m.get('quotaInfoList'):
                temp_model = ListQuotasResponseBodyDataQuotaInfoList()
                self.quota_info_list.append(temp_model.from_map(k))
        return self


class ListQuotasResponseBodyQuotaInfoListTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListQuotasResponseBodyQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        enable_priority: bool = None,
        force_reserved_min: bool = None,
        max_cu: int = None,
        min_cu: int = None,
        scheduler_type: str = None,
        single_job_culimit: int = None,
    ):
        self.elastic_reserved_cu = elastic_reserved_cu
        self.enable_priority = enable_priority
        self.force_reserved_min = force_reserved_min
        # This parameter is required.
        self.max_cu = max_cu
        # This parameter is required.
        self.min_cu = min_cu
        self.scheduler_type = scheduler_type
        self.single_job_culimit = single_job_culimit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        if self.enable_priority is not None:
            result['enablePriority'] = self.enable_priority
        if self.force_reserved_min is not None:
            result['forceReservedMin'] = self.force_reserved_min
        if self.max_cu is not None:
            result['maxCU'] = self.max_cu
        if self.min_cu is not None:
            result['minCU'] = self.min_cu
        if self.scheduler_type is not None:
            result['schedulerType'] = self.scheduler_type
        if self.single_job_culimit is not None:
            result['singleJobCULimit'] = self.single_job_culimit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        if m.get('enablePriority') is not None:
            self.enable_priority = m.get('enablePriority')
        if m.get('forceReservedMin') is not None:
            self.force_reserved_min = m.get('forceReservedMin')
        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')
        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')
        if m.get('schedulerType') is not None:
            self.scheduler_type = m.get('schedulerType')
        if m.get('singleJobCULimit') is not None:
            self.single_job_culimit = m.get('singleJobCULimit')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of an object in a MaxCompute quota. This identifier exists in the sales bill of Alibaba Cloud. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The type of the object. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListParameter = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag = None,
        schedule_info: ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The alias of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the endpoint group.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.parameter:
            self.parameter.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBodyQuotaInfoList(TeaModel):
    def __init__(
        self,
        tags: List[ListQuotasResponseBodyQuotaInfoListTags] = None,
        billing_policy: ListQuotasResponseBodyQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: ListQuotasResponseBodyQuotaInfoListSaleTag = None,
        schedule_info: ListQuotasResponseBodyQuotaInfoListScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The tags.
        self.tags = tags
        # The information of the order.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The quota ID.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifier of an object in a MaxCompute quota. This identifier is the same as the identifier in the sales bill of Alibaba Cloud. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the endpoint group.
        self.status = status
        # The information of the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version.
        self.version = version

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListQuotasResponseBodyQuotaInfoListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasResponseBodyQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = ListQuotasResponseBodyQuotaInfoListSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        data: ListQuotasResponseBodyData = None,
        marker: str = None,
        max_item: int = None,
        quota_info_list: List[ListQuotasResponseBodyQuotaInfoList] = None,
        request_id: str = None,
    ):
        # A pagination token. Only continuous page turning is supported. If NextToken is not empty, the next page exists. The value of NextToken can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The returned data.
        self.data = data
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # The list of quotas.
        self.quota_info_list = quota_info_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()
        if self.quota_info_list:
            for k in self.quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['quotaInfoList'] = []
        if self.quota_info_list is not None:
            for k in self.quota_info_list:
                result['quotaInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('data') is not None:
            temp_model = ListQuotasResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.quota_info_list = []
        if m.get('quotaInfoList') is not None:
            for k in m.get('quotaInfoList'):
                temp_model = ListQuotasResponseBodyQuotaInfoList()
                self.quota_info_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListQuotasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQuotasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQuotasPlansRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        tenant_id: str = None,
    ):
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method of the quota. Valid values:
        # 
        # *   subscription: a subscription quota.
        # *   payasyougo: a pay-as-you-go quota.
        self.billing_method = billing_method
        # The specifications of the order.
        self.odps_spec_code = odps_spec_code
        # The ID of the order.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
    ):
        # The quota plan that takes effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the current quota plan is scheduled.
        self.curr_time = curr_time
        # The next quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the next quota plan is scheduled.
        self.next_time = next_time
        # If the quota plan that immediately takes effect is different from the current quota plan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan immediately takes effect.
        self.once_time = once_time
        # The name of the operator.
        self.operator_name = operator_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        schedule_info: ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the quota plan was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The nickname of the level-2 quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The tag of the resource for the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasPlansResponseBodyDataPlanListQuota(TeaModel):
    def __init__(
        self,
        billing_policy: ListQuotasPlansResponseBodyDataPlanListQuotaBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        schedule_info: ListQuotasPlansResponseBodyDataPlanListQuotaScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The information of the order.
        self.billing_policy = billing_policy
        # The ID of the cluster.
        self.cluster = cluster
        # The time when the quota plan was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the resource.
        self.creator_id = creator_id
        # The ID of the quota.
        self.id = id
        # The name of the quota.
        self.name = name
        # The alias of the quota.
        self.nick_name = nick_name
        # The description of the quota.
        self.parameter = parameter
        # The ID of the parent resource.
        self.parent_id = parent_id
        # The ID of the region.
        self.region_id = region_id
        # The information of the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The information of the level-2 quota.
        self.sub_quota_info_list = sub_quota_info_list
        # The tag of the resource for the quota.
        self.tag = tag
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The type of the resource system. This parameter corresponds to the resourceSystemType parameter of the cluster.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('scheduleInfo') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = ListQuotasPlansResponseBodyDataPlanListQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListQuotasPlansResponseBodyDataPlanList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        name: str = None,
        quota: ListQuotasPlansResponseBodyDataPlanListQuota = None,
    ):
        # The time when the quota plan was created.
        self.create_time = create_time
        # The name of the quota plan.
        self.name = name
        # The details of the quota.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = ListQuotasPlansResponseBodyDataPlanListQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class ListQuotasPlansResponseBodyData(TeaModel):
    def __init__(
        self,
        plan_list: List[ListQuotasPlansResponseBodyDataPlanList] = None,
    ):
        # The list of quota plans.
        self.plan_list = plan_list

    def validate(self):
        if self.plan_list:
            for k in self.plan_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['planList'] = []
        if self.plan_list is not None:
            for k in self.plan_list:
                result['planList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plan_list = []
        if m.get('planList') is not None:
            for k in m.get('planList'):
                temp_model = ListQuotasPlansResponseBodyDataPlanList()
                self.plan_list.append(temp_model.from_map(k))
        return self


class ListQuotasPlansResponseBody(TeaModel):
    def __init__(
        self,
        data: ListQuotasPlansResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListQuotasPlansResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListQuotasPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQuotasPlansResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQuotasPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        name: str = None,
        schema_name: str = None,
    ):
        # Specifies the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries to return on each page.
        self.max_item = max_item
        # The name of the resource.
        self.name = name
        # The name of the schema.
        self.schema_name = schema_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.name is not None:
            result['name'] = self.name
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        return self


class ListResourcesResponseBodyDataResources(TeaModel):
    def __init__(
        self,
        comment: str = None,
        content_md5: str = None,
        creation_time: int = None,
        display_name: str = None,
        last_modified_time: int = None,
        last_updator: str = None,
        name: str = None,
        owner: str = None,
        schema: str = None,
        size: int = None,
        type: str = None,
    ):
        # The remarks.
        self.comment = comment
        # The Base64-encoded 128-bit MD5 hash value of the HTTP request body.
        self.content_md5 = content_md5
        # The time when the resource was created.
        self.creation_time = creation_time
        # The display name.
        self.display_name = display_name
        # The time when the resource was modified.
        self.last_modified_time = last_modified_time
        # The user who updated the resource.
        self.last_updator = last_updator
        # The name of the resource.
        self.name = name
        # The owner of the resource.
        self.owner = owner
        # The schema to which the resource belongs.
        self.schema = schema
        # The size of the resource.
        self.size = size
        # The resource type.
        # 
        # Valid values:
        # 
        # *   file
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   py
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   jar
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   volumefile
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   table
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.content_md5 is not None:
            result['contentMD5'] = self.content_md5
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time
        if self.last_updator is not None:
            result['lastUpdator'] = self.last_updator
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.schema is not None:
            result['schema'] = self.schema
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('contentMD5') is not None:
            self.content_md5 = m.get('contentMD5')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')
        if m.get('lastUpdator') is not None:
            self.last_updator = m.get('lastUpdator')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        resources: List[ListResourcesResponseBodyDataResources] = None,
    ):
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # The list of resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.resources = []
        if m.get('resources') is not None:
            for k in m.get('resources'):
                temp_model = ListResourcesResponseBodyDataResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListResourcesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListResourcesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesResponseBodyDataRolesAclFunction(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the function.
        self.actions = actions
        # The name of the function.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclInstance(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the instance.
        self.actions = actions
        # The name of the instance.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclPackage(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the package.
        self.actions = actions
        # The name of the package.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclProject(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the project.
        self.actions = actions
        # The name of the MaxCompute project.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclResource(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the resource.
        self.actions = actions
        # The name of the resource.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAclTable(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the table.
        self.actions = actions
        # The name of the table.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListRolesResponseBodyDataRolesAcl(TeaModel):
    def __init__(
        self,
        function: List[ListRolesResponseBodyDataRolesAclFunction] = None,
        instance: List[ListRolesResponseBodyDataRolesAclInstance] = None,
        package: List[ListRolesResponseBodyDataRolesAclPackage] = None,
        project: List[ListRolesResponseBodyDataRolesAclProject] = None,
        resource: List[ListRolesResponseBodyDataRolesAclResource] = None,
        table: List[ListRolesResponseBodyDataRolesAclTable] = None,
    ):
        # The function.
        self.function = function
        # The instance.
        self.instance = instance
        # The package.
        self.package = package
        # The project.
        self.project = project
        # The resource.
        self.resource = resource
        # The table.
        self.table = table

    def validate(self):
        if self.function:
            for k in self.function:
                if k:
                    k.validate()
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()
        if self.package:
            for k in self.package:
                if k:
                    k.validate()
        if self.project:
            for k in self.project:
                if k:
                    k.validate()
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        if self.table:
            for k in self.table:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['function'] = []
        if self.function is not None:
            for k in self.function:
                result['function'].append(k.to_map() if k else None)
        result['instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['instance'].append(k.to_map() if k else None)
        result['package'] = []
        if self.package is not None:
            for k in self.package:
                result['package'].append(k.to_map() if k else None)
        result['project'] = []
        if self.project is not None:
            for k in self.project:
                result['project'].append(k.to_map() if k else None)
        result['resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['resource'].append(k.to_map() if k else None)
        result['table'] = []
        if self.table is not None:
            for k in self.table:
                result['table'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function = []
        if m.get('function') is not None:
            for k in m.get('function'):
                temp_model = ListRolesResponseBodyDataRolesAclFunction()
                self.function.append(temp_model.from_map(k))
        self.instance = []
        if m.get('instance') is not None:
            for k in m.get('instance'):
                temp_model = ListRolesResponseBodyDataRolesAclInstance()
                self.instance.append(temp_model.from_map(k))
        self.package = []
        if m.get('package') is not None:
            for k in m.get('package'):
                temp_model = ListRolesResponseBodyDataRolesAclPackage()
                self.package.append(temp_model.from_map(k))
        self.project = []
        if m.get('project') is not None:
            for k in m.get('project'):
                temp_model = ListRolesResponseBodyDataRolesAclProject()
                self.project.append(temp_model.from_map(k))
        self.resource = []
        if m.get('resource') is not None:
            for k in m.get('resource'):
                temp_model = ListRolesResponseBodyDataRolesAclResource()
                self.resource.append(temp_model.from_map(k))
        self.table = []
        if m.get('table') is not None:
            for k in m.get('table'):
                temp_model = ListRolesResponseBodyDataRolesAclTable()
                self.table.append(temp_model.from_map(k))
        return self


class ListRolesResponseBodyDataRoles(TeaModel):
    def __init__(
        self,
        acl: ListRolesResponseBodyDataRolesAcl = None,
        name: str = None,
        policy: str = None,
        type: str = None,
    ):
        # The ACL-based permissions that are granted to the role.
        self.acl = acl
        # The name of the role.
        self.name = name
        # The policy that is attached to the role.
        self.policy = policy
        # The type of the role.
        self.type = type

    def validate(self):
        if self.acl:
            self.acl.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.policy is not None:
            result['policy'] = self.policy
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            temp_model = ListRolesResponseBodyDataRolesAcl()
            self.acl = temp_model.from_map(m['acl'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListRolesResponseBodyData(TeaModel):
    def __init__(
        self,
        roles: List[ListRolesResponseBodyDataRoles] = None,
    ):
        # The MaxCompute project-level roles.
        self.roles = roles

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['roles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.roles = []
        if m.get('roles') is not None:
            for k in m.get('roles'):
                temp_model = ListRolesResponseBodyDataRoles()
                self.roles.append(temp_model.from_map(k))
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListRolesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListRolesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRolesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStoragePartitionsInfoRequest(TeaModel):
    def __init__(
        self,
        asc_order: bool = None,
        date: str = None,
        order_column: str = None,
        page_number: int = None,
        page_size: int = None,
        partition_prefix: str = None,
        region: str = None,
        schema: str = None,
        tenant_id: str = None,
        types: List[str] = None,
    ):
        # Specifies whether to sort data in ascending order.
        self.asc_order = asc_order
        # The date on which the statistics are collected, in days. Set this parameter to a value in the YYYYMMdd format.
        # 
        # This parameter is required.
        self.date = date
        # The sorting column.
        self.order_column = order_column
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The name of the partition that you want to use for fuzzy match.
        self.partition_prefix = partition_prefix
        # The region ID.
        self.region = region
        # The name of the schema.
        self.schema = schema
        # The ID of the tenant. You can log on to the MaxCompute console, and choose **Tenants** > **Tenant Property** from the left-side navigation pane to view the tenant ID.
        self.tenant_id = tenant_id
        # The storage types.
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order
        if self.date is not None:
            result['date'] = self.date
        if self.order_column is not None:
            result['orderColumn'] = self.order_column
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.partition_prefix is not None:
            result['partitionPrefix'] = self.partition_prefix
        if self.region is not None:
            result['region'] = self.region
        if self.schema is not None:
            result['schema'] = self.schema
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('partitionPrefix') is not None:
            self.partition_prefix = m.get('partitionPrefix')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class ListStoragePartitionsInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        asc_order: bool = None,
        date: str = None,
        order_column: str = None,
        page_number: int = None,
        page_size: int = None,
        partition_prefix: str = None,
        region: str = None,
        schema: str = None,
        tenant_id: str = None,
        types_shrink: str = None,
    ):
        # Specifies whether to sort data in ascending order.
        self.asc_order = asc_order
        # The date on which the statistics are collected, in days. Set this parameter to a value in the YYYYMMdd format.
        # 
        # This parameter is required.
        self.date = date
        # The sorting column.
        self.order_column = order_column
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The name of the partition that you want to use for fuzzy match.
        self.partition_prefix = partition_prefix
        # The region ID.
        self.region = region
        # The name of the schema.
        self.schema = schema
        # The ID of the tenant. You can log on to the MaxCompute console, and choose **Tenants** > **Tenant Property** from the left-side navigation pane to view the tenant ID.
        self.tenant_id = tenant_id
        # The storage types.
        self.types_shrink = types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order
        if self.date is not None:
            result['date'] = self.date
        if self.order_column is not None:
            result['orderColumn'] = self.order_column
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.partition_prefix is not None:
            result['partitionPrefix'] = self.partition_prefix
        if self.region is not None:
            result['region'] = self.region
        if self.schema is not None:
            result['schema'] = self.schema
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.types_shrink is not None:
            result['types'] = self.types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('partitionPrefix') is not None:
            self.partition_prefix = m.get('partitionPrefix')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('types') is not None:
            self.types_shrink = m.get('types')
        return self


class ListStoragePartitionsInfoResponseBodyDataStoragePartitionInfoList(TeaModel):
    def __init__(
        self,
        file_count: int = None,
        file_size: float = None,
        file_size_unit: str = None,
        is_partitioned: bool = None,
        last_access_time: int = None,
        partition: str = None,
        project_name: str = None,
        rate: float = None,
        schema_name: str = None,
        storage_type: str = None,
        table_name: str = None,
        total_frequency: int = None,
        total_input_amount: float = None,
        total_input_amount_unit: str = None,
        type: str = None,
    ):
        # The number of files.
        self.file_count = file_count
        # The storage size.
        self.file_size = file_size
        # The unit of the storage size.
        self.file_size_unit = file_size_unit
        # Indicates whether the table is a partitioned table. This operation returns the partition information. You do not need to take note of this parameter.
        self.is_partitioned = is_partitioned
        # The time when the partition data was last accessed.
        # 
        # >  The data collection method is upgraded from July 2023. If the data is not accessed after the upgrade or is accessed by using ALGO jobs or the direct read method of Hologres, the last access time cannot be collected.
        self.last_access_time = last_access_time
        # The partition name.
        self.partition = partition
        # The project name.
        self.project_name = project_name
        # The change rate of the total storage usage compared with that of the recent {$recentDays} days. No value is returned.
        self.rate = rate
        # The schema name.
        self.schema_name = schema_name
        # The storage type.
        # 
        # *   standard
        # *   lowfrequency
        # *   longterm
        self.storage_type = storage_type
        # The table name.
        self.table_name = table_name
        # The access frequency.
        # 
        # > 
        # 
        # *   Access behaviors include:
        # 
        # *   The table is used as the input table of an SQL task.
        # *   The table is downloaded by Tunnel.
        # *   The table is read by calling the Storage API. The partition granularity of the partitioned table is not available. Each time an access operation is performed, the access frequency is incremented by 1.
        # 
        # *   The data collection method is upgraded from July 2023. If the data is not accessed after the upgrade or is accessed by using ALGO jobs or the direct read method of Hologres, the access frequency cannot be collected.
        self.total_frequency = total_frequency
        # The total amount of accessed data.
        # 
        # >  The amount of data that is read by all access behaviors.
        self.total_input_amount = total_input_amount
        # The unit of the total amount of accessed data.
        self.total_input_amount_unit = total_input_amount_unit
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_count is not None:
            result['fileCount'] = self.file_count
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.file_size_unit is not None:
            result['fileSizeUnit'] = self.file_size_unit
        if self.is_partitioned is not None:
            result['isPartitioned'] = self.is_partitioned
        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time
        if self.partition is not None:
            result['partition'] = self.partition
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.rate is not None:
            result['rate'] = self.rate
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.total_frequency is not None:
            result['totalFrequency'] = self.total_frequency
        if self.total_input_amount is not None:
            result['totalInputAmount'] = self.total_input_amount
        if self.total_input_amount_unit is not None:
            result['totalInputAmountUnit'] = self.total_input_amount_unit
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileCount') is not None:
            self.file_count = m.get('fileCount')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('fileSizeUnit') is not None:
            self.file_size_unit = m.get('fileSizeUnit')
        if m.get('isPartitioned') is not None:
            self.is_partitioned = m.get('isPartitioned')
        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')
        if m.get('partition') is not None:
            self.partition = m.get('partition')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('totalFrequency') is not None:
            self.total_frequency = m.get('totalFrequency')
        if m.get('totalInputAmount') is not None:
            self.total_input_amount = m.get('totalInputAmount')
        if m.get('totalInputAmountUnit') is not None:
            self.total_input_amount_unit = m.get('totalInputAmountUnit')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListStoragePartitionsInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        date: str = None,
        page_number: int = None,
        page_size: int = None,
        storage_partition_info_list: List[ListStoragePartitionsInfoResponseBodyDataStoragePartitionInfoList] = None,
        total_count: int = None,
    ):
        # The date on which the statistics are collected.
        self.date = date
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The partition storage information.
        self.storage_partition_info_list = storage_partition_info_list
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.storage_partition_info_list:
            for k in self.storage_partition_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['storagePartitionInfoList'] = []
        if self.storage_partition_info_list is not None:
            for k in self.storage_partition_info_list:
                result['storagePartitionInfoList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.storage_partition_info_list = []
        if m.get('storagePartitionInfoList') is not None:
            for k in m.get('storagePartitionInfoList'):
                temp_model = ListStoragePartitionsInfoResponseBodyDataStoragePartitionInfoList()
                self.storage_partition_info_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListStoragePartitionsInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: ListStoragePartitionsInfoResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # *   1xx: informational response. The request is received and is being processed.
        # *   2xx: success. The request is successfully received, understood, and accepted by the server.
        # *   3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # *   4xx: client error. The request contains invalid request parameters and syntaxes, or specific request conditions cannot be met.
        # *   5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListStoragePartitionsInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListStoragePartitionsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStoragePartitionsInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListStoragePartitionsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStorageProjectsInfoRequest(TeaModel):
    def __init__(
        self,
        asc_order: bool = None,
        date: str = None,
        order_column: str = None,
        page_number: int = None,
        page_size: int = None,
        project_prefix: str = None,
        recent_days: int = None,
        region: str = None,
        tenant_id: str = None,
    ):
        self.asc_order = asc_order
        # This parameter is required.
        self.date = date
        self.order_column = order_column
        self.page_number = page_number
        self.page_size = page_size
        self.project_prefix = project_prefix
        self.recent_days = recent_days
        self.region = region
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order
        if self.date is not None:
            result['date'] = self.date
        if self.order_column is not None:
            result['orderColumn'] = self.order_column
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_prefix is not None:
            result['projectPrefix'] = self.project_prefix
        if self.recent_days is not None:
            result['recentDays'] = self.recent_days
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectPrefix') is not None:
            self.project_prefix = m.get('projectPrefix')
        if m.get('recentDays') is not None:
            self.recent_days = m.get('recentDays')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListStorageProjectsInfoResponseBodyDataStorageProjectInfoList(TeaModel):
    def __init__(
        self,
        date: str = None,
        long_term_storage: float = None,
        long_term_storage_unit: str = None,
        low_freq_storage: float = None,
        low_freq_storage_unit: str = None,
        project_name: str = None,
        rate: float = None,
        recycle_bin_storage: float = None,
        recycle_bin_storage_unit: str = None,
        standard_storage: float = None,
        standard_storage_unit: str = None,
        timestamp: int = None,
        total_storage: float = None,
        total_storage_unit: str = None,
    ):
        self.date = date
        self.long_term_storage = long_term_storage
        self.long_term_storage_unit = long_term_storage_unit
        self.low_freq_storage = low_freq_storage
        self.low_freq_storage_unit = low_freq_storage_unit
        self.project_name = project_name
        self.rate = rate
        self.recycle_bin_storage = recycle_bin_storage
        self.recycle_bin_storage_unit = recycle_bin_storage_unit
        self.standard_storage = standard_storage
        self.standard_storage_unit = standard_storage_unit
        self.timestamp = timestamp
        self.total_storage = total_storage
        self.total_storage_unit = total_storage_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.long_term_storage is not None:
            result['longTermStorage'] = self.long_term_storage
        if self.long_term_storage_unit is not None:
            result['longTermStorageUnit'] = self.long_term_storage_unit
        if self.low_freq_storage is not None:
            result['lowFreqStorage'] = self.low_freq_storage
        if self.low_freq_storage_unit is not None:
            result['lowFreqStorageUnit'] = self.low_freq_storage_unit
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.rate is not None:
            result['rate'] = self.rate
        if self.recycle_bin_storage is not None:
            result['recycleBinStorage'] = self.recycle_bin_storage
        if self.recycle_bin_storage_unit is not None:
            result['recycleBinStorageUnit'] = self.recycle_bin_storage_unit
        if self.standard_storage is not None:
            result['standardStorage'] = self.standard_storage
        if self.standard_storage_unit is not None:
            result['standardStorageUnit'] = self.standard_storage_unit
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.total_storage is not None:
            result['totalStorage'] = self.total_storage
        if self.total_storage_unit is not None:
            result['totalStorageUnit'] = self.total_storage_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('longTermStorage') is not None:
            self.long_term_storage = m.get('longTermStorage')
        if m.get('longTermStorageUnit') is not None:
            self.long_term_storage_unit = m.get('longTermStorageUnit')
        if m.get('lowFreqStorage') is not None:
            self.low_freq_storage = m.get('lowFreqStorage')
        if m.get('lowFreqStorageUnit') is not None:
            self.low_freq_storage_unit = m.get('lowFreqStorageUnit')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('recycleBinStorage') is not None:
            self.recycle_bin_storage = m.get('recycleBinStorage')
        if m.get('recycleBinStorageUnit') is not None:
            self.recycle_bin_storage_unit = m.get('recycleBinStorageUnit')
        if m.get('standardStorage') is not None:
            self.standard_storage = m.get('standardStorage')
        if m.get('standardStorageUnit') is not None:
            self.standard_storage_unit = m.get('standardStorageUnit')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('totalStorage') is not None:
            self.total_storage = m.get('totalStorage')
        if m.get('totalStorageUnit') is not None:
            self.total_storage_unit = m.get('totalStorageUnit')
        return self


class ListStorageProjectsInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        date: str = None,
        page_number: int = None,
        page_size: int = None,
        storage_project_info_list: List[ListStorageProjectsInfoResponseBodyDataStorageProjectInfoList] = None,
        total_count: int = None,
    ):
        self.date = date
        self.page_number = page_number
        self.page_size = page_size
        self.storage_project_info_list = storage_project_info_list
        self.total_count = total_count

    def validate(self):
        if self.storage_project_info_list:
            for k in self.storage_project_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['storageProjectInfoList'] = []
        if self.storage_project_info_list is not None:
            for k in self.storage_project_info_list:
                result['storageProjectInfoList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.storage_project_info_list = []
        if m.get('storageProjectInfoList') is not None:
            for k in m.get('storageProjectInfoList'):
                temp_model = ListStorageProjectsInfoResponseBodyDataStorageProjectInfoList()
                self.storage_project_info_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListStorageProjectsInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: ListStorageProjectsInfoResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListStorageProjectsInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListStorageProjectsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStorageProjectsInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListStorageProjectsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStorageTablesInfoRequest(TeaModel):
    def __init__(
        self,
        asc_order: bool = None,
        date: str = None,
        order_column: str = None,
        page_number: int = None,
        page_size: int = None,
        recent_days: int = None,
        region: str = None,
        schema: str = None,
        table_prefix: str = None,
        tenant_id: str = None,
        types: List[str] = None,
    ):
        # Specifies whether to sort data in ascending order.
        self.asc_order = asc_order
        # The date on which the statistics are collected, in days. Set this parameter to a value in the `YYYYMMdd` format.
        # 
        # This parameter is required.
        self.date = date
        # The sorting column.
        self.order_column = order_column
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The number of recent days for comparison.
        self.recent_days = recent_days
        # The region ID.
        self.region = region
        # The name of the schema.
        self.schema = schema
        # The name of the table that you want to use for fuzzy match.
        self.table_prefix = table_prefix
        # The ID of the tenant. You can log on to the MaxCompute console, and choose **Tenants** > **Tenant Property** from the left-side navigation pane to view the tenant ID.
        self.tenant_id = tenant_id
        # The storage types.
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order
        if self.date is not None:
            result['date'] = self.date
        if self.order_column is not None:
            result['orderColumn'] = self.order_column
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.recent_days is not None:
            result['recentDays'] = self.recent_days
        if self.region is not None:
            result['region'] = self.region
        if self.schema is not None:
            result['schema'] = self.schema
        if self.table_prefix is not None:
            result['tablePrefix'] = self.table_prefix
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.types is not None:
            result['types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('recentDays') is not None:
            self.recent_days = m.get('recentDays')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('tablePrefix') is not None:
            self.table_prefix = m.get('tablePrefix')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('types') is not None:
            self.types = m.get('types')
        return self


class ListStorageTablesInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        asc_order: bool = None,
        date: str = None,
        order_column: str = None,
        page_number: int = None,
        page_size: int = None,
        recent_days: int = None,
        region: str = None,
        schema: str = None,
        table_prefix: str = None,
        tenant_id: str = None,
        types_shrink: str = None,
    ):
        # Specifies whether to sort data in ascending order.
        self.asc_order = asc_order
        # The date on which the statistics are collected, in days. Set this parameter to a value in the `YYYYMMdd` format.
        # 
        # This parameter is required.
        self.date = date
        # The sorting column.
        self.order_column = order_column
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The number of recent days for comparison.
        self.recent_days = recent_days
        # The region ID.
        self.region = region
        # The name of the schema.
        self.schema = schema
        # The name of the table that you want to use for fuzzy match.
        self.table_prefix = table_prefix
        # The ID of the tenant. You can log on to the MaxCompute console, and choose **Tenants** > **Tenant Property** from the left-side navigation pane to view the tenant ID.
        self.tenant_id = tenant_id
        # The storage types.
        self.types_shrink = types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order
        if self.date is not None:
            result['date'] = self.date
        if self.order_column is not None:
            result['orderColumn'] = self.order_column
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.recent_days is not None:
            result['recentDays'] = self.recent_days
        if self.region is not None:
            result['region'] = self.region
        if self.schema is not None:
            result['schema'] = self.schema
        if self.table_prefix is not None:
            result['tablePrefix'] = self.table_prefix
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.types_shrink is not None:
            result['types'] = self.types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('recentDays') is not None:
            self.recent_days = m.get('recentDays')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('tablePrefix') is not None:
            self.table_prefix = m.get('tablePrefix')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('types') is not None:
            self.types_shrink = m.get('types')
        return self


class ListStorageTablesInfoResponseBodyDataStorageTableInfoList(TeaModel):
    def __init__(
        self,
        date: str = None,
        is_partitioned: bool = None,
        last_access_time: int = None,
        long_term_storage: float = None,
        long_term_storage_file_count: int = None,
        long_term_storage_unit: str = None,
        low_freq_storage: float = None,
        low_freq_storage_file_count: int = None,
        low_freq_storage_unit: str = None,
        project_name: str = None,
        rate: float = None,
        schema_name: str = None,
        standard_storage: float = None,
        standard_storage_file_count: int = None,
        standard_storage_unit: str = None,
        storage_type: str = None,
        table_name: str = None,
        total_frequency: int = None,
        total_input_amount: float = None,
        total_input_amount_unit: str = None,
        total_storage: float = None,
        total_storage_file_count: int = None,
        total_storage_unit: str = None,
    ):
        # The date on which the statistics are collected. This value is not returned.
        self.date = date
        # Indicates whether the table is a partitioned table.
        self.is_partitioned = is_partitioned
        # The time when the table was last accessed. This value is returned when the table is a non-partitioned table.
        # 
        # >  The data collection method is upgraded from July 2023. If the data is not accessed after the upgrade or is accessed by using ALGO jobs or the direct read method of Hologres, the last access time cannot be collected.
        self.last_access_time = last_access_time
        # The storage usage at the long-term storage tier.
        self.long_term_storage = long_term_storage
        # The number of long-term storage files.
        self.long_term_storage_file_count = long_term_storage_file_count
        # The unit of the storage usage at the long-term storage tier.
        self.long_term_storage_unit = long_term_storage_unit
        # The storage usage at the low-frequency tier.
        self.low_freq_storage = low_freq_storage
        # The number of low-frequency storage files.
        self.low_freq_storage_file_count = low_freq_storage_file_count
        # The unit of the storage usage at the low-frequency storage tier.
        self.low_freq_storage_unit = low_freq_storage_unit
        # The project name.
        self.project_name = project_name
        # The change rate of the total storage usage compared with that of the recent {$recentDays} days.
        self.rate = rate
        # The schema name.
        self.schema_name = schema_name
        # The storage usage at the standard storage tier.
        self.standard_storage = standard_storage
        # The number of standard storage files.
        self.standard_storage_file_count = standard_storage_file_count
        # The unit of the storage usage at the standard storage tier.
        self.standard_storage_unit = standard_storage_unit
        # The table storage type.
        # 
        # *   standard
        # *   lowfrequency
        # *   longterm
        # *   unknown: This value is returned when the table is a partitioned table. You can call the ListStoragePartitionsInfo operation to query the storage type of each partition.
        self.storage_type = storage_type
        # The table name.
        self.table_name = table_name
        # The access frequency.
        # 
        # > 
        # 
        # *   Access behaviors include:
        # 
        # *   The table is used as the input table of an SQL task.
        # *   The table is downloaded by Tunnel.
        # *   The table is read by calling the Storage API. The partition granularity of the partitioned table is not available. Each time an access operation is performed, the access frequency is incremented by 1.
        # 
        # *   The data collection method is upgraded from July 2023. If the data is not accessed after the upgrade or is accessed by using ALGO jobs or the direct read method of Hologres, the access frequency cannot be collected.
        self.total_frequency = total_frequency
        # The total amount of accessed data.
        # 
        # >  The amount of data that is read by all access behaviors.
        self.total_input_amount = total_input_amount
        # The unit of the total amount of accessed data.
        self.total_input_amount_unit = total_input_amount_unit
        # The total storage usage. For a partitioned table, this parameter indicates the sum of the storage usage of all partitions. If the storage types of partitions are different, the value is the sum of the storage usage of each storage type.
        self.total_storage = total_storage
        # The total number of files.
        self.total_storage_file_count = total_storage_file_count
        # The unit of storage usage.
        self.total_storage_unit = total_storage_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.is_partitioned is not None:
            result['isPartitioned'] = self.is_partitioned
        if self.last_access_time is not None:
            result['lastAccessTime'] = self.last_access_time
        if self.long_term_storage is not None:
            result['longTermStorage'] = self.long_term_storage
        if self.long_term_storage_file_count is not None:
            result['longTermStorageFileCount'] = self.long_term_storage_file_count
        if self.long_term_storage_unit is not None:
            result['longTermStorageUnit'] = self.long_term_storage_unit
        if self.low_freq_storage is not None:
            result['lowFreqStorage'] = self.low_freq_storage
        if self.low_freq_storage_file_count is not None:
            result['lowFreqStorageFileCount'] = self.low_freq_storage_file_count
        if self.low_freq_storage_unit is not None:
            result['lowFreqStorageUnit'] = self.low_freq_storage_unit
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.rate is not None:
            result['rate'] = self.rate
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.standard_storage is not None:
            result['standardStorage'] = self.standard_storage
        if self.standard_storage_file_count is not None:
            result['standardStorageFileCount'] = self.standard_storage_file_count
        if self.standard_storage_unit is not None:
            result['standardStorageUnit'] = self.standard_storage_unit
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.total_frequency is not None:
            result['totalFrequency'] = self.total_frequency
        if self.total_input_amount is not None:
            result['totalInputAmount'] = self.total_input_amount
        if self.total_input_amount_unit is not None:
            result['totalInputAmountUnit'] = self.total_input_amount_unit
        if self.total_storage is not None:
            result['totalStorage'] = self.total_storage
        if self.total_storage_file_count is not None:
            result['totalStorageFileCount'] = self.total_storage_file_count
        if self.total_storage_unit is not None:
            result['totalStorageUnit'] = self.total_storage_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('isPartitioned') is not None:
            self.is_partitioned = m.get('isPartitioned')
        if m.get('lastAccessTime') is not None:
            self.last_access_time = m.get('lastAccessTime')
        if m.get('longTermStorage') is not None:
            self.long_term_storage = m.get('longTermStorage')
        if m.get('longTermStorageFileCount') is not None:
            self.long_term_storage_file_count = m.get('longTermStorageFileCount')
        if m.get('longTermStorageUnit') is not None:
            self.long_term_storage_unit = m.get('longTermStorageUnit')
        if m.get('lowFreqStorage') is not None:
            self.low_freq_storage = m.get('lowFreqStorage')
        if m.get('lowFreqStorageFileCount') is not None:
            self.low_freq_storage_file_count = m.get('lowFreqStorageFileCount')
        if m.get('lowFreqStorageUnit') is not None:
            self.low_freq_storage_unit = m.get('lowFreqStorageUnit')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('standardStorage') is not None:
            self.standard_storage = m.get('standardStorage')
        if m.get('standardStorageFileCount') is not None:
            self.standard_storage_file_count = m.get('standardStorageFileCount')
        if m.get('standardStorageUnit') is not None:
            self.standard_storage_unit = m.get('standardStorageUnit')
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('totalFrequency') is not None:
            self.total_frequency = m.get('totalFrequency')
        if m.get('totalInputAmount') is not None:
            self.total_input_amount = m.get('totalInputAmount')
        if m.get('totalInputAmountUnit') is not None:
            self.total_input_amount_unit = m.get('totalInputAmountUnit')
        if m.get('totalStorage') is not None:
            self.total_storage = m.get('totalStorage')
        if m.get('totalStorageFileCount') is not None:
            self.total_storage_file_count = m.get('totalStorageFileCount')
        if m.get('totalStorageUnit') is not None:
            self.total_storage_unit = m.get('totalStorageUnit')
        return self


class ListStorageTablesInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        date: str = None,
        page_number: int = None,
        page_size: int = None,
        storage_table_info_list: List[ListStorageTablesInfoResponseBodyDataStorageTableInfoList] = None,
        total_count: int = None,
    ):
        # The date on which the statistics are collected.
        self.date = date
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The table storage information.
        self.storage_table_info_list = storage_table_info_list
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.storage_table_info_list:
            for k in self.storage_table_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['storageTableInfoList'] = []
        if self.storage_table_info_list is not None:
            for k in self.storage_table_info_list:
                result['storageTableInfoList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.storage_table_info_list = []
        if m.get('storageTableInfoList') is not None:
            for k in m.get('storageTableInfoList'):
                temp_model = ListStorageTablesInfoResponseBodyDataStorageTableInfoList()
                self.storage_table_info_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListStorageTablesInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: ListStorageTablesInfoResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # *   1xx: informational response. The request is received and is being processed.
        # *   2xx: success. The request is successfully received, understood, and accepted by the server.
        # *   3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # *   4xx: client error. The request contains invalid request parameters and syntaxes, or specific request conditions cannot be met.
        # *   5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListStorageTablesInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListStorageTablesInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStorageTablesInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListStorageTablesInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTablesRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        prefix: str = None,
        schema_name: str = None,
        type: str = None,
    ):
        # Specifies the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries to return on each page.
        self.max_item = max_item
        # The names of the returned resources. The names must start with the value specified by the prefix parameter. If the prefix parameter is set to a, the names of the returned resources must start with a.
        self.prefix = prefix
        # The name of the schema.
        self.schema_name = schema_name
        # The type of the table.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        if self.prefix is not None:
            result['prefix'] = self.prefix
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListTablesResponseBodyDataTables(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        display_name: str = None,
        name: str = None,
        owner: str = None,
        schema: str = None,
        type: str = None,
    ):
        # The time when the table was created.
        self.creation_time = creation_time
        # The display name of the table.
        self.display_name = display_name
        # The name of the table.
        self.name = name
        # The owner of the table.
        self.owner = owner
        # The schema to which the table belongs.
        self.schema = schema
        # The type of the table.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.schema is not None:
            result['schema'] = self.schema
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListTablesResponseBodyData(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        tables: List[ListTablesResponseBodyDataTables] = None,
    ):
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item
        # The information about tables.
        self.tables = tables

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_item is not None:
            result['maxItem'] = self.max_item
        result['tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['tables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')
        self.tables = []
        if m.get('tables') is not None:
            for k in m.get('tables'):
                temp_model = ListTablesResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k))
        return self


class ListTablesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListTablesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListTablesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTablesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTunnelQuotaTimerResponseBodyDataTunnelQuotaParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_slot_num: int = None,
        slot_num: int = None,
    ):
        # The number of elastically reserved slots.
        self.elastic_reserved_slot_num = elastic_reserved_slot_num
        # The number of reserved slots.
        self.slot_num = slot_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_slot_num is not None:
            result['elasticReservedSlotNum'] = self.elastic_reserved_slot_num
        if self.slot_num is not None:
            result['slotNum'] = self.slot_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedSlotNum') is not None:
            self.elastic_reserved_slot_num = m.get('elasticReservedSlotNum')
        if m.get('slotNum') is not None:
            self.slot_num = m.get('slotNum')
        return self


class ListTunnelQuotaTimerResponseBodyData(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        timezone: str = None,
        tunnel_quota_parameter: ListTunnelQuotaTimerResponseBodyDataTunnelQuotaParameter = None,
    ):
        # The start time of the time-specific configuration.
        self.begin_time = begin_time
        # The end time of the time-specific configuration.
        self.end_time = end_time
        # The time zone property for the time-specific configuration.
        self.timezone = timezone
        # The parameters for the time-specific configuration.
        self.tunnel_quota_parameter = tunnel_quota_parameter

    def validate(self):
        if self.tunnel_quota_parameter:
            self.tunnel_quota_parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.tunnel_quota_parameter is not None:
            result['tunnelQuotaParameter'] = self.tunnel_quota_parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('tunnelQuotaParameter') is not None:
            temp_model = ListTunnelQuotaTimerResponseBodyDataTunnelQuotaParameter()
            self.tunnel_quota_parameter = temp_model.from_map(m['tunnelQuotaParameter'])
        return self


class ListTunnelQuotaTimerResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListTunnelQuotaTimerResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # *   1xx: informational response. The request is received and is being processed.
        # *   2xx: success. The request is successfully received, understood, and accepted by the server.
        # *   3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # *   4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # *   5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListTunnelQuotaTimerResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListTunnelQuotaTimerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTunnelQuotaTimerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTunnelQuotaTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListUsersResponseBodyDataUsers(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        account_type: str = None,
        display_name: str = None,
        tenant_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The username of the account.
        self.account_name = account_name
        # The type of the account.
        self.account_type = account_type
        # The display name.
        self.display_name = display_name
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.account_name is not None:
            result['accountName'] = self.account_name
        if self.account_type is not None:
            result['accountType'] = self.account_type
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')
        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class ListUsersResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        users: List[ListUsersResponseBodyDataUsers] = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count
        # The users.
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = ListUsersResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        data: ListUsersResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListUsersResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersByRoleResponseBodyDataUsers(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the user.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListUsersByRoleResponseBodyData(TeaModel):
    def __init__(
        self,
        users: List[ListUsersByRoleResponseBodyDataUsers] = None,
    ):
        # The users.
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['users'] = []
        if self.users is not None:
            for k in self.users:
                result['users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.users = []
        if m.get('users') is not None:
            for k in m.get('users'):
                temp_model = ListUsersByRoleResponseBodyDataUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersByRoleResponseBody(TeaModel):
    def __init__(
        self,
        data: ListUsersByRoleResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListUsersByRoleResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListUsersByRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersByRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUsersByRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryQuotaRequest(TeaModel):
    def __init__(
        self,
        ak_proven: str = None,
        mock: bool = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The trusted AccessKey pairs.
        self.ak_proven = ak_proven
        # Specifies whether to include submodules. Valid values: true and false. -true: The request includes submodules. -false (default): The request does not include submodules.
        self.mock = mock
        # The region ID.
        self.region = region
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ak_proven is not None:
            result['AkProven'] = self.ak_proven
        if self.mock is not None:
            result['mock'] = self.mock
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProven') is not None:
            self.ak_proven = m.get('AkProven')
        if m.get('mock') is not None:
            self.mock = m.get('mock')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class QueryQuotaResponseBodyDataBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        instance_id: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method. Valid values:
        # 
        # *   subscription: the subscription quota.
        # *   payasyougo: the pay-as-you-go quota.
        self.billing_method = billing_method
        # In MaxCompute, instanceId and orderId are considered the same.
        self.instance_id = instance_id
        # The order specifications.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class QueryQuotaResponseBodyDataSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of a MaxCompute quota object. This identifier exists in the Alibaba Cloud sales bill. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The object type. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class QueryQuotaResponseBodyDataScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The current quota plan that has taken effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the plan specified by currPlan is scheduled.
        self.curr_time = curr_time
        # The quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the plan specified by nextPlan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan specified by this parameter is triggered and the plan is different from the plan specified by currPlan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan specified by oncePlan is scheduled.
        self.once_time = once_time
        # The operator name.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class QueryQuotaResponseBodyDataSubQuotaInfoListBillingPolicy(TeaModel):
    def __init__(
        self,
        billing_method: str = None,
        instance_id: str = None,
        odps_spec_code: str = None,
        order_id: str = None,
    ):
        # The billing method. Valid values:
        # 
        # *   subscription: the subscription quota.
        # *   payasyougo: the pay-as-you-go quota.
        self.billing_method = billing_method
        # In MaxCompute, instanceId and orderId are considered the same.
        self.instance_id = instance_id
        # The order specifications.
        self.odps_spec_code = odps_spec_code
        # The order ID.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.odps_spec_code is not None:
            result['odpsSpecCode'] = self.odps_spec_code
        if self.order_id is not None:
            result['orderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('odpsSpecCode') is not None:
            self.odps_spec_code = m.get('odpsSpecCode')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        return self


class QueryQuotaResponseBodyDataSubQuotaInfoListSaleTag(TeaModel):
    def __init__(
        self,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The identifier of a MaxCompute quota object. This identifier exists in the Alibaba Cloud sales bill. You can use this identifier to associate the cost of a quota object with a tag.
        self.resource_ids = resource_ids
        # The object type. Valid values: quota and project.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class QueryQuotaResponseBodyDataSubQuotaInfoListScheduleInfo(TeaModel):
    def __init__(
        self,
        curr_plan: str = None,
        curr_time: str = None,
        next_plan: str = None,
        next_time: str = None,
        once_plan: str = None,
        once_time: str = None,
        operator_name: str = None,
        timezone: str = None,
    ):
        # The current quota plan that has taken effect based on the scheduling plan.
        self.curr_plan = curr_plan
        # The time when the plan specified by currPlan is scheduled.
        self.curr_time = curr_time
        # The quota plan that will take effect based on the scheduling plan.
        self.next_plan = next_plan
        # The time when the plan specified by nextPlan is scheduled.
        self.next_time = next_time
        # The quota plan that immediately takes effect. If the quota plan specified by this parameter is triggered and the plan is different from the plan specified by currPlan, this parameter is not empty.
        self.once_plan = once_plan
        # The time when the quota plan specified by oncePlan is scheduled.
        self.once_time = once_time
        # The operator name.
        self.operator_name = operator_name
        # The time zone of the project.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_plan is not None:
            result['currPlan'] = self.curr_plan
        if self.curr_time is not None:
            result['currTime'] = self.curr_time
        if self.next_plan is not None:
            result['nextPlan'] = self.next_plan
        if self.next_time is not None:
            result['nextTime'] = self.next_time
        if self.once_plan is not None:
            result['oncePlan'] = self.once_plan
        if self.once_time is not None:
            result['onceTime'] = self.once_time
        if self.operator_name is not None:
            result['operatorName'] = self.operator_name
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currPlan') is not None:
            self.curr_plan = m.get('currPlan')
        if m.get('currTime') is not None:
            self.curr_time = m.get('currTime')
        if m.get('nextPlan') is not None:
            self.next_plan = m.get('nextPlan')
        if m.get('nextTime') is not None:
            self.next_time = m.get('nextTime')
        if m.get('oncePlan') is not None:
            self.once_plan = m.get('oncePlan')
        if m.get('onceTime') is not None:
            self.once_time = m.get('onceTime')
        if m.get('operatorName') is not None:
            self.operator_name = m.get('operatorName')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class QueryQuotaResponseBodyDataSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        billing_policy: QueryQuotaResponseBodyDataSubQuotaInfoListBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        group_name: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: QueryQuotaResponseBodyDataSubQuotaInfoListSaleTag = None,
        schedule_info: QueryQuotaResponseBodyDataSubQuotaInfoListScheduleInfo = None,
        status: str = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The order information.
        self.billing_policy = billing_policy
        # The cluster ID.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the quota plan.
        self.creator_id = creator_id
        # The role group name.
        self.group_name = group_name
        # The ID of the level-2 quota.
        self.id = id
        # The name of the level-2 quota.
        self.name = name
        # The nickname of the level-2 quota.
        self.nick_name = nick_name
        # The quota description.
        self.parameter = parameter
        # The parent resource ID.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifiers of MaxCompute quota objects. The identifiers are the same as those in the Alibaba Cloud sales bill. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information about the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The resource tag of a quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # This parameter corresponds to the resourceSystemType field.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = QueryQuotaResponseBodyDataSubQuotaInfoListBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = QueryQuotaResponseBodyDataSubQuotaInfoListSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = QueryQuotaResponseBodyDataSubQuotaInfoListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class QueryQuotaResponseBodyData(TeaModel):
    def __init__(
        self,
        billing_policy: QueryQuotaResponseBodyDataBillingPolicy = None,
        cluster: str = None,
        create_time: int = None,
        creator_id: str = None,
        group_name: str = None,
        id: str = None,
        name: str = None,
        nick_name: str = None,
        parameter: Dict[str, Any] = None,
        parent_id: str = None,
        region_id: str = None,
        sale_tag: QueryQuotaResponseBodyDataSaleTag = None,
        schedule_info: QueryQuotaResponseBodyDataScheduleInfo = None,
        status: str = None,
        sub_quota_info_list: List[QueryQuotaResponseBodyDataSubQuotaInfoList] = None,
        tag: str = None,
        tenant_id: str = None,
        type: str = None,
        version: str = None,
    ):
        # The order information.
        self.billing_policy = billing_policy
        # The ID of the Managed Service for Prometheus cluster.
        self.cluster = cluster
        # The time when the resource was created.
        self.create_time = create_time
        # The ID of the Alibaba Cloud account that is used to create the quota plan.
        self.creator_id = creator_id
        # The group name.
        self.group_name = group_name
        # The quota ID.
        self.id = id
        # The quota name.
        self.name = name
        # The quota alias.
        self.nick_name = nick_name
        # The quota description.
        self.parameter = parameter
        # The parent resource ID.
        self.parent_id = parent_id
        # The region ID.
        self.region_id = region_id
        # The identifiers of MaxCompute quota objects. The identifiers are the same as those in the Alibaba Cloud sales bill. This parameter is used for tags.
        self.sale_tag = sale_tag
        # The information about the scheduling plan.
        self.schedule_info = schedule_info
        # The status of the resource.
        self.status = status
        # The level-2 quotas.
        self.sub_quota_info_list = sub_quota_info_list
        # The resource tag of a quota.
        self.tag = tag
        # The tenant ID.
        self.tenant_id = tenant_id
        # This parameter corresponds to the resourceSystemType field.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.billing_policy:
            self.billing_policy.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.schedule_info:
            self.schedule_info.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_policy is not None:
            result['billingPolicy'] = self.billing_policy.to_map()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator_id is not None:
            result['creatorId'] = self.creator_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()
        if self.schedule_info is not None:
            result['scheduleInfo'] = self.schedule_info.to_map()
        if self.status is not None:
            result['status'] = self.status
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['tag'] = self.tag
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billingPolicy') is not None:
            temp_model = QueryQuotaResponseBodyDataBillingPolicy()
            self.billing_policy = temp_model.from_map(m['billingPolicy'])
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creatorId') is not None:
            self.creator_id = m.get('creatorId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('saleTag') is not None:
            temp_model = QueryQuotaResponseBodyDataSaleTag()
            self.sale_tag = temp_model.from_map(m['saleTag'])
        if m.get('scheduleInfo') is not None:
            temp_model = QueryQuotaResponseBodyDataScheduleInfo()
            self.schedule_info = temp_model.from_map(m['scheduleInfo'])
        if m.get('status') is not None:
            self.status = m.get('status')
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = QueryQuotaResponseBodyDataSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class QueryQuotaResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryQuotaResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = QueryQuotaResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStorageMetricRequest(TeaModel):
    def __init__(
        self,
        project_list: List[str] = None,
        type_list: List[str] = None,
        end_time: int = None,
        start_time: int = None,
    ):
        self.project_list = project_list
        self.type_list = type_list
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_list is not None:
            result['projectList'] = self.project_list
        if self.type_list is not None:
            result['typeList'] = self.type_list
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectList') is not None:
            self.project_list = m.get('projectList')
        if m.get('typeList') is not None:
            self.type_list = m.get('typeList')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class QueryStorageMetricResponseBodyDataMetrics(TeaModel):
    def __init__(
        self,
        metric: Dict[str, str] = None,
        values: List[List[float]] = None,
    ):
        self.metric = metric
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            self.metric = m.get('metric')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class QueryStorageMetricResponseBodyData(TeaModel):
    def __init__(
        self,
        category: str = None,
        metrics: List[QueryStorageMetricResponseBodyDataMetrics] = None,
        name: str = None,
        period: int = None,
    ):
        self.category = category
        self.metrics = metrics
        self.name = name
        self.period = period

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.period is not None:
            result['period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.metrics = []
        if m.get('metrics') is not None:
            for k in m.get('metrics'):
                temp_model = QueryStorageMetricResponseBodyDataMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('period') is not None:
            self.period = m.get('period')
        return self


class QueryStorageMetricResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryStorageMetricResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = QueryStorageMetricResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryStorageMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryStorageMetricResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryStorageMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTunnelMetricRequest(TeaModel):
    def __init__(
        self,
        code_list: List[int] = None,
        group_list: List[str] = None,
        operation_list: List[str] = None,
        project: str = None,
        quota_nickname: str = None,
        table_list: List[str] = None,
        top_n: int = None,
        end_time: int = None,
        start_time: int = None,
        strategy: str = None,
    ):
        self.code_list = code_list
        self.group_list = group_list
        self.operation_list = operation_list
        self.project = project
        self.quota_nickname = quota_nickname
        self.table_list = table_list
        self.top_n = top_n
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.start_time = start_time
        self.strategy = strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_list is not None:
            result['codeList'] = self.code_list
        if self.group_list is not None:
            result['groupList'] = self.group_list
        if self.operation_list is not None:
            result['operationList'] = self.operation_list
        if self.project is not None:
            result['project'] = self.project
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        if self.table_list is not None:
            result['tableList'] = self.table_list
        if self.top_n is not None:
            result['topN'] = self.top_n
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.strategy is not None:
            result['strategy'] = self.strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeList') is not None:
            self.code_list = m.get('codeList')
        if m.get('groupList') is not None:
            self.group_list = m.get('groupList')
        if m.get('operationList') is not None:
            self.operation_list = m.get('operationList')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        if m.get('tableList') is not None:
            self.table_list = m.get('tableList')
        if m.get('topN') is not None:
            self.top_n = m.get('topN')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')
        return self


class QueryTunnelMetricResponseBodyDataMetrics(TeaModel):
    def __init__(
        self,
        metric: Dict[str, str] = None,
        values: List[List[float]] = None,
    ):
        self.metric = metric
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            self.metric = m.get('metric')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class QueryTunnelMetricResponseBodyData(TeaModel):
    def __init__(
        self,
        category: str = None,
        metrics: List[QueryTunnelMetricResponseBodyDataMetrics] = None,
        name: str = None,
        period: int = None,
    ):
        self.category = category
        self.metrics = metrics
        self.name = name
        self.period = period

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.period is not None:
            result['period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.metrics = []
        if m.get('metrics') is not None:
            for k in m.get('metrics'):
                temp_model = QueryTunnelMetricResponseBodyDataMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('period') is not None:
            self.period = m.get('period')
        return self


class QueryTunnelMetricResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryTunnelMetricResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = QueryTunnelMetricResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryTunnelMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTunnelMetricResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTunnelMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTunnelMetricDetailRequest(TeaModel):
    def __init__(
        self,
        asc_order: bool = None,
        group_list: List[str] = None,
        limit: int = None,
        operation_list: List[str] = None,
        order_column: str = None,
        project: str = None,
        quota_nickname: str = None,
        table_list: List[str] = None,
        end_time: int = None,
        start_time: int = None,
    ):
        self.asc_order = asc_order
        self.group_list = group_list
        self.limit = limit
        self.operation_list = operation_list
        self.order_column = order_column
        self.project = project
        self.quota_nickname = quota_nickname
        self.table_list = table_list
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order
        if self.group_list is not None:
            result['groupList'] = self.group_list
        if self.limit is not None:
            result['limit'] = self.limit
        if self.operation_list is not None:
            result['operationList'] = self.operation_list
        if self.order_column is not None:
            result['orderColumn'] = self.order_column
        if self.project is not None:
            result['project'] = self.project
        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname
        if self.table_list is not None:
            result['tableList'] = self.table_list
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')
        if m.get('groupList') is not None:
            self.group_list = m.get('groupList')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('operationList') is not None:
            self.operation_list = m.get('operationList')
        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')
        if m.get('tableList') is not None:
            self.table_list = m.get('tableList')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class QueryTunnelMetricDetailResponseBodyDataMetrics(TeaModel):
    def __init__(
        self,
        metric: Dict[str, str] = None,
        value: Dict[str, Any] = None,
    ):
        self.metric = metric
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            self.metric = m.get('metric')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class QueryTunnelMetricDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        metrics: List[QueryTunnelMetricDetailResponseBodyDataMetrics] = None,
        name: str = None,
    ):
        self.metrics = metrics
        self.name = name

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('metrics') is not None:
            for k in m.get('metrics'):
                temp_model = QueryTunnelMetricDetailResponseBodyDataMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class QueryTunnelMetricDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryTunnelMetricDetailResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = QueryTunnelMetricDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryTunnelMetricDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTunnelMetricDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTunnelMetricDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryMmsJobResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RetryMmsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RetryMmsJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RetryMmsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartMmsJobResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class StartMmsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartMmsJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartMmsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMmsJobResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class StopMmsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopMmsJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopMmsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateComputeQuotaPlanRequestQuotaParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
    ):
        # The value of elastic Reserved CUs in the level-1 quota.
        # > The default value is 0. The maximum value of this parameter must be equal to the number of subscription-based reserved CUs and cannot exceed 10,000 CUs.
        # 
        # This parameter is required.
        self.elastic_reserved_cu = elastic_reserved_cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        return self


class UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoListParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_cu: int = None,
        max_cu: int = None,
        min_cu: int = None,
    ):
        # The value of elastic Reserved CUs.
        # > The total number of elastically reserved CUs in all the level-2 quotas is equal to the number of elastically reserved CUs in the level-1 quota.
        # 
        # This parameter is required.
        self.elastic_reserved_cu = elastic_reserved_cu
        # The value of maxCU in Reserved CUs.
        # > The value of maxCU must be less than or equal to the value of maxCU in the level-1 quota that you purchased.
        # 
        # This parameter is required.
        self.max_cu = max_cu
        # The value of minCU in Reserved CUs.
        # > 
        # >- The total value of minCU in all the level-2 quotas is equal to the value of minCU in the level-1 quota.
        # >- The value of minCU must be less than or equal to the value of maxCU in the level-2 quota and less than or equal to the value of minCU in the level-1 quota that you purchased.
        # 
        # This parameter is required.
        self.min_cu = min_cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_cu is not None:
            result['elasticReservedCU'] = self.elastic_reserved_cu
        if self.max_cu is not None:
            result['maxCU'] = self.max_cu
        if self.min_cu is not None:
            result['minCU'] = self.min_cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedCU') is not None:
            self.elastic_reserved_cu = m.get('elasticReservedCU')
        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')
        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')
        return self


class UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        parameter: UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoListParameter = None,
    ):
        # The nickname of the level-2 quota.
        # 
        # This parameter is required.
        self.nick_name = nick_name
        # The parameters of the level-2 quota.
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            temp_model = UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        return self


class UpdateComputeQuotaPlanRequestQuota(TeaModel):
    def __init__(
        self,
        parameter: UpdateComputeQuotaPlanRequestQuotaParameter = None,
        sub_quota_info_list: List[UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoList] = None,
    ):
        # The parameters of level-1 quota.
        self.parameter = parameter
        # The list of level-2 quotas.
        self.sub_quota_info_list = sub_quota_info_list

    def validate(self):
        if self.parameter:
            self.parameter.validate()
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parameter') is not None:
            temp_model = UpdateComputeQuotaPlanRequestQuotaParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = UpdateComputeQuotaPlanRequestQuotaSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        return self


class UpdateComputeQuotaPlanRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        quota: UpdateComputeQuotaPlanRequestQuota = None,
    ):
        # The name of quota plan.
        # 
        # This parameter is required.
        self.name = name
        # The parameters of quota plan.
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('quota') is not None:
            temp_model = UpdateComputeQuotaPlanRequestQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class UpdateComputeQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateComputeQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateComputeQuotaPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateComputeQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateComputeQuotaScheduleRequestBodyCondition(TeaModel):
    def __init__(
        self,
        at: str = None,
    ):
        # The start time when the quota plan takes effect.
        # 
        # This parameter is required.
        self.at = at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at is not None:
            result['at'] = self.at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('at') is not None:
            self.at = m.get('at')
        return self


class UpdateComputeQuotaScheduleRequestBody(TeaModel):
    def __init__(
        self,
        condition: UpdateComputeQuotaScheduleRequestBodyCondition = None,
        plan: str = None,
        type: str = None,
    ):
        # The value of effective condition.
        self.condition = condition
        # The name of the quota plan.
        # 
        # This parameter is required.
        self.plan = plan
        # The type of the quota plan.
        # 
        # >Notice: Currently, only daily is supported.</notice>
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition.to_map()
        if self.plan is not None:
            result['plan'] = self.plan
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            temp_model = UpdateComputeQuotaScheduleRequestBodyCondition()
            self.condition = temp_model.from_map(m['condition'])
        if m.get('plan') is not None:
            self.plan = m.get('plan')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateComputeQuotaScheduleRequest(TeaModel):
    def __init__(
        self,
        body: List[UpdateComputeQuotaScheduleRequestBody] = None,
        schedule_timezone: str = None,
    ):
        # The request body parameters.
        self.body = body
        self.schedule_timezone = schedule_timezone

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        if self.schedule_timezone is not None:
            result['scheduleTimezone'] = self.schedule_timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = UpdateComputeQuotaScheduleRequestBody()
                self.body.append(temp_model.from_map(k))
        if m.get('scheduleTimezone') is not None:
            self.schedule_timezone = m.get('scheduleTimezone')
        return self


class UpdateComputeQuotaScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # HTTP status code.
        # - 1xx: Informational - The request has been received and is being processed.
        # - 2xx: Success - The request action was successfully received, understood, and accepted by the server.
        # - 3xx: Redirection - Further action must be taken to complete the request.
        # - 4xx: Client Error - The request contains an error in the request parameters, syntax, or specific request conditions cannot be met.
        # - 5xx: Server Error - The server could not fulfill the request due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateComputeQuotaScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateComputeQuotaScheduleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateComputeQuotaScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateComputeSubQuotaRequestSubQuotaInfoListParameter(TeaModel):
    def __init__(
        self,
        enable_priority: bool = None,
        force_reserved_min: bool = None,
        max_cu: int = None,
        min_cu: int = None,
        scheduler_type: str = None,
        single_job_culimit: int = None,
    ):
        # Specifies whether to enable the priority feature.
        self.enable_priority = enable_priority
        # Specifies whether the quota is strongly exclusive.
        self.force_reserved_min = force_reserved_min
        # The value of minCU in Reserved CUs.
        # > The value of maxCU must be less than or equal to the value of maxCU in the level-1 quota that you purchased.
        # 
        # This parameter is required.
        self.max_cu = max_cu
        # The value of maxCU in Reserved CUs.
        # > 
        # >- The total value of minCU in all the level-2 quotas is equal to the value of minCU in the level-1 quota.
        # >- The value of minCU must be less than or equal to the value of maxCU in the level-2 quota and less than or equal to the value of minCU in the level-1 quota that you purchased.
        # 
        # This parameter is required.
        self.min_cu = min_cu
        # Scheduling policy of the quota.
        self.scheduler_type = scheduler_type
        # The upper limit for CUs that can be concurrently used by a job scheduled to the quota.
        self.single_job_culimit = single_job_culimit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_priority is not None:
            result['enablePriority'] = self.enable_priority
        if self.force_reserved_min is not None:
            result['forceReservedMin'] = self.force_reserved_min
        if self.max_cu is not None:
            result['maxCU'] = self.max_cu
        if self.min_cu is not None:
            result['minCU'] = self.min_cu
        if self.scheduler_type is not None:
            result['schedulerType'] = self.scheduler_type
        if self.single_job_culimit is not None:
            result['singleJobCULimit'] = self.single_job_culimit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enablePriority') is not None:
            self.enable_priority = m.get('enablePriority')
        if m.get('forceReservedMin') is not None:
            self.force_reserved_min = m.get('forceReservedMin')
        if m.get('maxCU') is not None:
            self.max_cu = m.get('maxCU')
        if m.get('minCU') is not None:
            self.min_cu = m.get('minCU')
        if m.get('schedulerType') is not None:
            self.scheduler_type = m.get('schedulerType')
        if m.get('singleJobCULimit') is not None:
            self.single_job_culimit = m.get('singleJobCULimit')
        return self


class UpdateComputeSubQuotaRequestSubQuotaInfoList(TeaModel):
    def __init__(
        self,
        nick_name: str = None,
        parameter: UpdateComputeSubQuotaRequestSubQuotaInfoListParameter = None,
        type: str = None,
    ):
        # The nickname of the level-2 quota.
        # 
        # This parameter is required.
        self.nick_name = nick_name
        # The parameters of the level-2 quota.
        self.parameter = parameter
        # The type of quota.
        # 
        # > 
        # > - FUXI_OFFLINE(default) : Quotas of this type are used to run batch jobs.
        self.type = type

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick_name is not None:
            result['nickName'] = self.nick_name
        if self.parameter is not None:
            result['parameter'] = self.parameter.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nickName') is not None:
            self.nick_name = m.get('nickName')
        if m.get('parameter') is not None:
            temp_model = UpdateComputeSubQuotaRequestSubQuotaInfoListParameter()
            self.parameter = temp_model.from_map(m['parameter'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateComputeSubQuotaRequest(TeaModel):
    def __init__(
        self,
        sub_quota_info_list: List[UpdateComputeSubQuotaRequestSubQuotaInfoList] = None,
    ):
        # The list of level-2 quotas.
        self.sub_quota_info_list = sub_quota_info_list

    def validate(self):
        if self.sub_quota_info_list:
            for k in self.sub_quota_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['subQuotaInfoList'] = []
        if self.sub_quota_info_list is not None:
            for k in self.sub_quota_info_list:
                result['subQuotaInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_quota_info_list = []
        if m.get('subQuotaInfoList') is not None:
            for k in m.get('subQuotaInfoList'):
                temp_model = UpdateComputeSubQuotaRequestSubQuotaInfoList()
                self.sub_quota_info_list.append(temp_model.from_map(k))
        return self


class UpdateComputeSubQuotaResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # - 4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # - 5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateComputeSubQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateComputeSubQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateComputeSubQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMmsDataSourceRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        config: Dict[str, Any] = None,
        name: str = None,
        test: bool = None,
    ):
        self.action = action
        self.config = config
        self.name = name
        self.test = test

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.config is not None:
            result['config'] = self.config
        if self.name is not None:
            result['name'] = self.name
        if self.test is not None:
            result['test'] = self.test
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('test') is not None:
            self.test = m.get('test')
        return self


class UpdateMmsDataSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        async_task_id: int = None,
        source_id: int = None,
    ):
        self.async_task_id = async_task_id
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['asyncTaskId'] = self.async_task_id
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncTaskId') is not None:
            self.async_task_id = m.get('asyncTaskId')
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        return self


class UpdateMmsDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateMmsDataSourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = UpdateMmsDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateMmsDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMmsDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateMmsDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePackageRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The request body parameters.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdatePackageResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdatePackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePackageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectBasicMetaRequestPropertiesEncryption(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        enable: bool = None,
        key: str = None,
    ):
        # The data encryption algorithm that is supported by the key. Valid values: AES256, AESCTR, and RC4.
        self.algorithm = algorithm
        # Indicates whether the data encryption feature needs to be enabled for the project. For more information about data encryption, see
        # <props="china">[Storage Encryption](https://help.aliyun.com/zh/maxcompute/security-and-compliance/storage-encryption)
        # <props="intl">[Storage Encryption](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/storage-encryption).
        self.enable = enable
        # The type of key that is used for data encryption. You can select MaxCompute Default Key or Bring Your Own Key (BYOK) as the key type. If you select MaxCompute Default Key, the default key that is created by MaxCompute is used.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm
        if self.enable is not None:
            result['enable'] = self.enable
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class UpdateProjectBasicMetaRequestPropertiesTableLifecycle(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The lifecycle type. Valid values:
        # - *mandatory*: The lifecycle clause is required in a table creation statement.
        # - *optional*: The lifecycle clause is optional in a table creation statement. If you do not configure a lifecycle for a table, the table does not expire.
        # - *inherit*: If you do not configure a lifecycle for a table when you create the table, the value of the odps.table.lifecycle.value parameter is used as the table lifecycle by default.
        self.type = type
        # The table lifecycle. Unit: days. Valid values: 1 to 37231. Default value: 37231.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateProjectBasicMetaRequestProperties(TeaModel):
    def __init__(
        self,
        allow_full_scan: bool = None,
        enable_decimal_2: bool = None,
        enable_dr: bool = None,
        enable_tunnel_quota_route: bool = None,
        encryption: UpdateProjectBasicMetaRequestPropertiesEncryption = None,
        retention_days: int = None,
        sql_metering_max: str = None,
        table_lifecycle: UpdateProjectBasicMetaRequestPropertiesTableLifecycle = None,
        timezone: str = None,
        tunnel_quota: str = None,
        type_system: str = None,
    ):
        # Indicates whether a full table scan is allowed in the project. A full table scan occupies a large number of resources, which reduces data processing efficiency. By default, the full table scan feature is disabled.
        self.allow_full_scan = allow_full_scan
        # Indicates whether the DECIMAL type of the MaxCompute V2.0 data type edition is enabled.
        self.enable_decimal_2 = enable_decimal_2
        self.enable_dr = enable_dr
        # Indicates whether the routing of the Tunnel resource group is enabled.
        # 
        # - true: The data transfer tasks that are submitted by the project by default use the Tunnel resource group that is bound to the project.
        # - false: The data transfer tasks that are submitted by the project by default use the Tunnel shared resource group.
        self.enable_tunnel_quota_route = enable_tunnel_quota_route
        # The storage encryption properties.
        self.encryption = encryption
        # The retention period for backup data. Unit: days. During the retention period, you can restore data of the version in use to the backup data of any version. Valid values: [0,30]. Default value: 1. The value 0 indicates that the backup feature is disabled.
        self.retention_days = retention_days
        # The maximum consumption threshold of a single SQL statement. Formula: Amount of scanned data (GB) × Complexity.
        self.sql_metering_max = sql_metering_max
        # The table lifecycle properties.
        self.table_lifecycle = table_lifecycle
        # The time zone that is used by your project. The time zone is the same as the time zone specified by `odps.sql.timezone` .
        self.timezone = timezone
        # The <props="china">[Data Transmission Service](https://help.aliyun.com/zh/maxcompute/user-guide/overview-of-dts)
        # <props="intl">[Data Transmission Service](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/overview-of-dts) resource group that is bound to the project.
        # 
        # - Default resource group: The Tunnel shared resource group is used. You cannot use the subscription-based Tunnel resource group for the project. The default resource group is automatically used by the Tunnel service of your project, regardless of the parameter setting.
        # - Subscription-based Tunnel resource group: You can use the subscription-based Tunnel resource group for the project.
        self.tunnel_quota = tunnel_quota
        # The data type edition. Valid values:
        # 
        # - *1*: MaxCompute V1.0 data type edition
        # - *2*: MaxCompute V2.0 data type edition
        # - *hive*: Hive-compatible data type edition
        # For more information about the differences among the three data type editions, see <props="china">[Data Type Versions](https://help.aliyun.com/zh/maxcompute/user-guide/data-type-editions)
        # <props="intl">[Data Type Versions](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/data-type-editions).
        self.type_system = type_system

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.table_lifecycle:
            self.table_lifecycle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_full_scan is not None:
            result['allowFullScan'] = self.allow_full_scan
        if self.enable_decimal_2 is not None:
            result['enableDecimal2'] = self.enable_decimal_2
        if self.enable_dr is not None:
            result['enableDr'] = self.enable_dr
        if self.enable_tunnel_quota_route is not None:
            result['enableTunnelQuotaRoute'] = self.enable_tunnel_quota_route
        if self.encryption is not None:
            result['encryption'] = self.encryption.to_map()
        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days
        if self.sql_metering_max is not None:
            result['sqlMeteringMax'] = self.sql_metering_max
        if self.table_lifecycle is not None:
            result['tableLifecycle'] = self.table_lifecycle.to_map()
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota
        if self.type_system is not None:
            result['typeSystem'] = self.type_system
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowFullScan') is not None:
            self.allow_full_scan = m.get('allowFullScan')
        if m.get('enableDecimal2') is not None:
            self.enable_decimal_2 = m.get('enableDecimal2')
        if m.get('enableDr') is not None:
            self.enable_dr = m.get('enableDr')
        if m.get('enableTunnelQuotaRoute') is not None:
            self.enable_tunnel_quota_route = m.get('enableTunnelQuotaRoute')
        if m.get('encryption') is not None:
            temp_model = UpdateProjectBasicMetaRequestPropertiesEncryption()
            self.encryption = temp_model.from_map(m['encryption'])
        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')
        if m.get('sqlMeteringMax') is not None:
            self.sql_metering_max = m.get('sqlMeteringMax')
        if m.get('tableLifecycle') is not None:
            temp_model = UpdateProjectBasicMetaRequestPropertiesTableLifecycle()
            self.table_lifecycle = temp_model.from_map(m['tableLifecycle'])
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')
        if m.get('typeSystem') is not None:
            self.type_system = m.get('typeSystem')
        return self


class UpdateProjectBasicMetaRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        properties: UpdateProjectBasicMetaRequestProperties = None,
    ):
        # The project description.
        self.comment = comment
        # The basic properties of the project.
        self.properties = properties

    def validate(self):
        if self.properties:
            self.properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.properties is not None:
            result['properties'] = self.properties.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('properties') is not None:
            temp_model = UpdateProjectBasicMetaRequestProperties()
            self.properties = temp_model.from_map(m['properties'])
        return self


class UpdateProjectBasicMetaResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: informational response. The request is received and is being processed.
        # - 2xx: success. The request is successfully received, understood, and accepted by the server.
        # - 3xx: redirection. The request is redirected, and further actions are required to complete the request.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProjectBasicMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectBasicMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProjectBasicMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectDefaultQuotaRequest(TeaModel):
    def __init__(
        self,
        quota: str = None,
    ):
        # The default computing quota that is used to allocate computing resources, the jobs that are initiated by this project consume the computing resources in the default quota.
        self.quota = quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['quota'] = self.quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('quota') is not None:
            self.quota = m.get('quota')
        return self


class UpdateProjectDefaultQuotaResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProjectDefaultQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectDefaultQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProjectDefaultQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectIpWhiteListRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The request body parameters.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdateProjectIpWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateProjectIpWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectIpWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProjectIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaPlanRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateQuotaPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateQuotaPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQuotaPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateQuotaPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaScheduleRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The request body parameters.
        self.body = body
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.region is not None:
            result['region'] = self.region
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class UpdateQuotaScheduleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned result.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateQuotaScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQuotaScheduleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateQuotaScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTunnelQuotaTimerRequestBodyTunnelQuotaParameter(TeaModel):
    def __init__(
        self,
        elastic_reserved_slot_num: int = None,
        slot_num: int = None,
    ):
        # The number of elastically reserved slots.
        self.elastic_reserved_slot_num = elastic_reserved_slot_num
        # The number of reserved slots.
        self.slot_num = slot_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_reserved_slot_num is not None:
            result['elasticReservedSlotNum'] = self.elastic_reserved_slot_num
        if self.slot_num is not None:
            result['slotNum'] = self.slot_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticReservedSlotNum') is not None:
            self.elastic_reserved_slot_num = m.get('elasticReservedSlotNum')
        if m.get('slotNum') is not None:
            self.slot_num = m.get('slotNum')
        return self


class UpdateTunnelQuotaTimerRequestBody(TeaModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
        tunnel_quota_parameter: UpdateTunnelQuotaTimerRequestBodyTunnelQuotaParameter = None,
    ):
        # The start time of the time-specific configuration.
        self.begin_time = begin_time
        # The end time of the time-specific configuration.
        self.end_time = end_time
        # The parameters for the time-specific configuration.
        self.tunnel_quota_parameter = tunnel_quota_parameter

    def validate(self):
        if self.tunnel_quota_parameter:
            self.tunnel_quota_parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['beginTime'] = self.begin_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.tunnel_quota_parameter is not None:
            result['tunnelQuotaParameter'] = self.tunnel_quota_parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginTime') is not None:
            self.begin_time = m.get('beginTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('tunnelQuotaParameter') is not None:
            temp_model = UpdateTunnelQuotaTimerRequestBodyTunnelQuotaParameter()
            self.tunnel_quota_parameter = temp_model.from_map(m['tunnelQuotaParameter'])
        return self


class UpdateTunnelQuotaTimerRequest(TeaModel):
    def __init__(
        self,
        body: List[UpdateTunnelQuotaTimerRequestBody] = None,
        timezone: str = None,
    ):
        # The request body.
        self.body = body
        self.timezone = timezone

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        if self.timezone is not None:
            result['timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = UpdateTunnelQuotaTimerRequestBody()
                self.body.append(temp_model.from_map(k))
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        return self


class UpdateTunnelQuotaTimerResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # *   1xx: informational response. The request is received and is being processed.
        # *   2xx: success. The request is successfully received, understood, and accepted by the server.
        # *   3xx: redirection. The request is redirected, and further actions are required to complete the request.
        # *   4xx: client error. The request contains invalid request parameters or syntaxes, or specific request conditions cannot be met.
        # *   5xx: server error. The server cannot meet requirements due to other reasons.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateTunnelQuotaTimerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTunnelQuotaTimerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTunnelQuotaTimerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUsersToRoleRequest(TeaModel):
    def __init__(
        self,
        add: List[str] = None,
        remove: List[str] = None,
    ):
        # The accounts.
        self.add = add
        # The accounts.
        self.remove = remove

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['add'] = self.add
        if self.remove is not None:
            result['remove'] = self.remove
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add') is not None:
            self.add = m.get('add')
        if m.get('remove') is not None:
            self.remove = m.get('remove')
        return self


class UpdateUsersToRoleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateUsersToRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUsersToRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUsersToRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


