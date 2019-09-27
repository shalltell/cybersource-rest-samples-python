from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def download_dtd_for_report(reportDefinitionNameVersion):

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = DownloadDTDApi(client_config)
        return_data, status, body = api_instance.get_d_t_d_v2(reportDefinitionNameVersion)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)
        print("\nAPI RESPONSE : ", return_data)

        return return_data
    except Exception as e:
        print("\nException when calling DownloadDTDApi->get_d_t_d_v2: %s\n" % e)

if __name__ == "__main__":
    print("\nInput missing path parameter <reportDefinitionNameVersion>:")
    reportDefinitionNameVersion = input()

    download_dtd_for_report(reportDefinitionNameVersion)
