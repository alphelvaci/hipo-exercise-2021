def get_amount_string(object):
    if hasattr(object, 'amount'):
        amount = object.amount
    elif hasattr(object, 'transaction'):
        amount = object.transaction.amount
    elif hasattr(object, 'card_transactions'):
        amount = object.card_transactions.transaction.amount

    if amount < 0:
        amount_string = str(amount)
    else:
        amount_string = "+" + str(amount)

    return amount_string
