import epaycosdk.epayco as epayco
import random

apiKey = "c40acc8a877f180bf312c79aae0503f7"
privateKey = "b13e95ea247b7cbe1f41724a1cb86d91"
lenguage = "ES"
test = True
options={"apiKey":apiKey,"privateKey":privateKey,"test":test,"lenguage":lenguage} 

objepayco=epayco.Epayco(options)

credit_info = {
  "card[number]": "5240521756556621",
  "card[exp_year]": "2027",
  "card[exp_month]": "02",
  "card[cvc]": "049"
  }

token = objepayco.token.create(credit_info)

customer_info = {
  "token_card": token['id'],
  "name": "Juan Diego",
  "last_name": "Vargas Posada", #This parameter is optional
  "email": "diego.vargas@payco.co",
  "phone": "3042462218",
  "default": False
  }

customer = objepayco.customer.create(customer_info)

payment_info = {
  "token_card": token['id'],
  "customer_id": customer['data']['customerId'],
  "doc_type": "CC",
  "doc_number": "1194418306",
  "name": "Juan Diego",
  "last_name": "Varga Posada",
  "email": "diego.vargas@payco.co",
  "bill": str(random.randint(100000, 999999)),
  "description": "SDK PYTHON Pruebas ePayco TC",
  "value": "1",
  "tax": "0",
  "tax_base": "1",
  "currency": "COP",
  "dues": "1",
  "ip": "181.134.247.50",  # This is the client's IP, it is required,
  "url_response": "http://diego.dev-plugins.info/respuesta.html",
  "url_confirmation": "http://diego.dev-plugins.info/confirmacion.php",
  "method_confirmation": "POST",
  #Extra params: These params are optional and can be used by the commerce
  "use_default_card_customer":False, # if the user wants to be charged with the card that the customer currently has as default = true
}

pay = objepayco.charge.create(payment_info)

print (pay)
