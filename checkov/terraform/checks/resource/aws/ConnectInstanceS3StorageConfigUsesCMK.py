from checkov.common.models.enums import CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck
from checkov.common.models.consts import ANY_VALUE


class ConnectInstanceS3StorageConfigUsesCMK(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure Connect Instance S3 Storage Config uses CMK"
        id = "CKV_AWS_270" 
        supported_resources = ['aws_connect_instance_storage_config']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'storage_config/[0]/s3_config/[0]/encryption_config/[0]/key_id'

    def get_expected_value(self):
        return ANY_VALUE


check = ConnectInstanceS3StorageConfigUsesCMK()