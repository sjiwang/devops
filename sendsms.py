import os
import sys

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class AliSms:

    def __init__(self):
        config = open_api_models.Config(
            access_key_id=os.getenv('ALI_CLOUD_SMS_KEY'),
            access_key_secret=os.getenv('ALI_CLOUD_SMS_SECRET')
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Dysmsapi
        config.endpoint = f'dysmsapi.aliyuncs.com'
        self.client = Dysmsapi20170525Client(config)

    def send_sms(self, m_name, p_name, phone_number):
        template_param = {}
        template_param['machine_name'] = m_name
        template_param['program_name'] = p_name
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            sign_name='应用存活',
            template_code='SMS_465421022',
            phone_numbers=phone_number,
            template_param=str(template_param)

        )
        try:
            resp = self.client.send_sms_with_options(send_sms_request, util_models.RuntimeOptions())
            print(resp)
        except Exception as err:
            print(err)
            UtilClient.assert_as_string(err)


if __name__ == '__main__':
    AliSms().send_sms('abc', '1234', '13588265347')
