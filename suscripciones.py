import epaycosdk.epayco as epayco
import random

apiKey = "c40acc8a877f180bf312c79aae0503f7"
privateKey = "b13e95ea247b7cbe1f41724a1cb86d91"
lenguage = "ES"
test = True
options = {"apiKey": apiKey, "privateKey": privateKey,
           "test": test, "lenguage": lenguage}

objepayco = epayco.Epayco(options)

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
    "last_name": "Vargas Posada",  # This parameter is optional
    "email": "diego.vargas@payco.co",
    "phone": "3042462218",
    "default": False
}

customer = objepayco.customer.create(customer_info)

namePlan = 'SuscripcionPYTHON-' + str(random.randint(00, 99))

plan_info = {
    "id_plan": namePlan,
    "name": namePlan,
    "description": namePlan,
    "amount": 1,
    "currency": "cop",
    "interval": "month",
    "interval_count": 1,
    "trial_days": 7
}

plan = objepayco.plan.create(plan_info)

subscription_info = {
    "id_plan": plan['data']['id_plan'],
    "customer": customer['data']['customerId'],
    "token_card": token['id'],
    "doc_type": "CC",
    "doc_number": "1194418306",
    "url_confirmation": "http://diego.dev-plugins.info/confirmacion.php",
    "method_confirmation": "POST"
    }

sub = objepayco.subscriptions.create(subscription_info)
   
subscription_info = {
    "id_plan": plan['data']['id_plan'],
    "customer": customer['data']['customerId'],
    "token_card": token['id'],
    "doc_type": "CC",
    "doc_number": "1194418306",
    "ip": "181.134.247.50"  # This is the client's IP, it is required

}

pay = objepayco.subscriptions.charge(subscription_info)

print(pay)
