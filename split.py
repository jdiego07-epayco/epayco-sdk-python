import epaycosdk.epayco as epayco
import random
import json

apiKey = "55b75fd6b1ef17eaf394fa985de6563c"
privateKey = "9327203f56866f1ed1ef4f56272ee771"
lenguage = "ES"
test = False
options = {"apiKey": apiKey, "privateKey": privateKey,
           "test": test, "lenguage": lenguage}

objepayco = epayco.Epayco(options)

# credit_info = {
#     "card[number]": "5240521756556621",
#     "card[exp_year]": "2027",
#     "card[exp_month]": "02",
#     "card[cvc]": "049"
# }

# token = objepayco.token.create(credit_info)

# customer_info = {
#     "token_card": token['id'],
#     "name": "Juan Diego",
#     "last_name": "Vargas Posada",  # This parameter is optional
#     "email": "diego.vargas@payco.co",
#     "phone": "3042462218",
#     "default": False
# }

# customer = objepayco.customer.create(customer_info)

payment_info = {
    # "token_card": token['id'],
    # "customer_id": customer['data']['customerId'],
    "token_card": "0837e22f054270493229d03",
    "customer_id": "0754200c0e6dd165e4c5344",
    "doc_type": "CC",
    "doc_number": "1194418306",
    "name": "Juan Diego",
    "last_name": "Vargas Posada",
    "email": "diego.vargas@payco.co",
    "bill": str(random.randint(100000, 999999)),
    "description": "SDK PYTHON Pruebas ePayco Split TC",
    "value": "1",
    "tax": "0",
    "tax_base": "1",
    "currency": "COP",
    "dues": "1",
    "ip": "181.134.247.50",  # This is the client's IP, it is required
    "url_response": "http://diego.dev-plugins.info/respuesta.html",
    "url_confirmation": "http://diego.dev-plugins.info/confirmacion.php",
    "method_confirmation": "POST",
    "splitpayment": "true",
    "split_app_id": "515360",
    "split_merchant_id": "515360",
    "split_type": "01",
    "split_primary_receiver": "515360",
    "split_primary_receiver_fee": "0",
    "split_rule": 'multiple',
    "split_receivers": [
        {"id": "9898", "total": "1","iva": "0", "base_iva": "1", "fee": "1"} # 1- 1
    ],
    # "split_receivers": str(json.dumps([
    #     {"id": "9898", "total": "3","iva": "0", "base_iva": "3", "fee": "1"} # Multiple
    # ])),
    "use_default_card_customer": False,
    "extra1": "",
    "extra2": "",
    "extra3": "",
    "extra4": "",
    "extra5": "",
    "extra6": "",
    "extra7": "",
    "extra8": "",
    "extra9": "",
    "extra10": ""
}

pay = objepayco.charge.create(payment_info)

print(pay)
