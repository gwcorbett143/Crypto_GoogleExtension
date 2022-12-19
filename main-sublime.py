from coinbase.wallet.client import Client
from coinbase.wallet.error import AuthenticationError

cb_API_key = '5uR0RaWqzNLdqhAT'
cb_secret = 'ZvcCjLlDEuscoPl9JLak2NAIxoy5meSV'

client = Client(cb_API_key, cb_secret)

total = 0
message = []

try:
    accounts = client.get_accounts()
    for wallet in accounts.data:
        value = str(wallet['native_balance']).replace('USD ', '')
        if '0.00' in value:
            value = '0'
        else:
            message.append(str(wallet['name']) + ' ' + str(wallet['native_balance']))
        total += float(value)
    message.append('Total Balance: ' + 'USD ' + str(total))
    print('\n'.join(message))

except AuthenticationError:
    print('Could not authenticate with your coinbase API.')



