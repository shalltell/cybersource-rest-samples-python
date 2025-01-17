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

def authorization_with_customer_token_default_payment_instrument_and_shipping_address_creation():
    clientReferenceInformationCode = "TC50171_3"
    clientReferenceInformation = Ptsv2paymentsClientReferenceInformation(
        code = clientReferenceInformationCode
    )


    processingInformationActionList = []
    processingInformationActionList.append("TOKEN_CREATE")

    processingInformationActionTokenTypes = []
    processingInformationActionTokenTypes.append("paymentInstrument")
    processingInformationActionTokenTypes.append("shippingAddress")
    processingInformationCapture = False
    processingInformation = Ptsv2paymentsProcessingInformation(
        action_list = processingInformationActionList,
        action_token_types = processingInformationActionTokenTypes,
        capture = processingInformationCapture
    )

    paymentInformationCardNumber = "4111111111111111"
    paymentInformationCardExpirationMonth = "12"
    paymentInformationCardExpirationYear = "2031"
    paymentInformationCardSecurityCode = "123"
    paymentInformationCard = Ptsv2paymentsPaymentInformationCard(
        number = paymentInformationCardNumber,
        expiration_month = paymentInformationCardExpirationMonth,
        expiration_year = paymentInformationCardExpirationYear,
        security_code = paymentInformationCardSecurityCode
    )

    paymentInformationCustomerId = "AB695DA801DD1BB6E05341588E0A3BDC"
    paymentInformationCustomer = Ptsv2paymentsPaymentInformationCustomer(
        id = paymentInformationCustomerId
    )

    paymentInformation = Ptsv2paymentsPaymentInformation(
        card = paymentInformationCard.__dict__,
        customer = paymentInformationCustomer.__dict__
    )

    orderInformationAmountDetailsTotalAmount = "102.21"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetails = Ptsv2paymentsOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency
    )

    orderInformationBillToFirstName = "John"
    orderInformationBillToLastName = "Doe"
    orderInformationBillToAddress1 = "1 Market St"
    orderInformationBillToLocality = "san francisco"
    orderInformationBillToAdministrativeArea = "CA"
    orderInformationBillToPostalCode = "94105"
    orderInformationBillToCountry = "US"
    orderInformationBillToEmail = "test@cybs.com"
    orderInformationBillToPhoneNumber = "4158880000"
    orderInformationBillTo = Ptsv2paymentsOrderInformationBillTo(
        first_name = orderInformationBillToFirstName,
        last_name = orderInformationBillToLastName,
        address1 = orderInformationBillToAddress1,
        locality = orderInformationBillToLocality,
        administrative_area = orderInformationBillToAdministrativeArea,
        postal_code = orderInformationBillToPostalCode,
        country = orderInformationBillToCountry,
        email = orderInformationBillToEmail,
        phone_number = orderInformationBillToPhoneNumber
    )

    orderInformationShipToFirstName = "John"
    orderInformationShipToLastName = "Doe"
    orderInformationShipToAddress1 = "1 Market St"
    orderInformationShipToLocality = "san francisco"
    orderInformationShipToAdministrativeArea = "CA"
    orderInformationShipToPostalCode = "94105"
    orderInformationShipToCountry = "US"
    orderInformationShipTo = Ptsv2paymentsOrderInformationShipTo(
        first_name = orderInformationShipToFirstName,
        last_name = orderInformationShipToLastName,
        address1 = orderInformationShipToAddress1,
        locality = orderInformationShipToLocality,
        administrative_area = orderInformationShipToAdministrativeArea,
        postal_code = orderInformationShipToPostalCode,
        country = orderInformationShipToCountry
    )

    orderInformation = Ptsv2paymentsOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        bill_to = orderInformationBillTo.__dict__,
        ship_to = orderInformationShipTo.__dict__
    )

    tokenInformationPaymentInstrument_default = True
    tokenInformationPaymentInstrument = Ptsv2paymentsTokenInformationPaymentInstrument(
        default = tokenInformationPaymentInstrument_default
    )

    tokenInformationShippingAddress_default = True
    tokenInformationShippingAddress = Ptsv2paymentsTokenInformationShippingAddress(
        default = tokenInformationShippingAddress_default
    )

    tokenInformation = Ptsv2paymentsTokenInformation(
        payment_instrument = tokenInformationPaymentInstrument.__dict__,
        shipping_address = tokenInformationShippingAddress.__dict__
    )

    requestObj = CreatePaymentRequest(
        client_reference_information = clientReferenceInformation.__dict__,
        processing_information = processingInformation.__dict__,
        payment_information = paymentInformation.__dict__,
        order_information = orderInformation.__dict__,
        token_information = tokenInformation.__dict__
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)


    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = PaymentsApi(client_config)
        return_data, status, body = api_instance.create_payment(requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling PaymentsApi->create_payment: %s\n" % e)

if __name__ == "__main__":
    authorization_with_customer_token_default_payment_instrument_and_shipping_address_creation()
