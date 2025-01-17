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

def get_netfunding_information_for_account_or_merchant():
    startTime = "2021-01-01T00:00:00Z"
    endTime = "2021-01-02T23:59:59Z"
    organizationId = "testrest"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = NetFundingsApi(client_config)
        return_data, status, body = api_instance.get_net_funding_details(startTime, endTime, organization_id=organizationId)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling NetFundingsApi->get_net_funding_details: %s\n" % e)

if __name__ == "__main__":
    get_netfunding_information_for_account_or_merchant()
