def convert_currency(amount_needed_inr,current_currency_name):
    current_currency_amount=0

    if(current_currency_name=="Euro"):
        per_inr=0.01417
        current_currency_amount=per_inr*amount_needed_inr
        return current_currency_amount
    elif(current_currency_name=="British Pound"):
        per_inr=0.0100
        current_currency_amount=per_inr*amount_needed_inr
        return current_currency_amount
    elif(current_currency_name=="Australian Dollar"):
        per_inr=0.02140
        current_currency_amount=per_inr*amount_needed_inr
        return current_currency_amount
    elif(current_currency_name=="Canadian Dollar"):
        per_inr=0.02027
        current_currency_amount=per_inr*amount_needed_inr
        return current_currency_amount



currency_needed=convert_currency(2000,"Euro")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
