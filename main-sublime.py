# this program scrapes data from my coinbase account using a personal API
# Note: this may not work because certain Pip packages need to be downloaded into and virtual environment for this to work

# these are the afformentioned pip packages inclding the coinbase file
from coinbase.wallet.client import Client
from coinbase.wallet.error import AuthenticationError

#these are my security keys that have access to my account (please don't steal them)
cb_API_key = '5uR0RaWqzNLdqhAT'
cb_secret = 'ZvcCjLlDEuscoPl9JLak2NAIxoy5meSV'

client = Client(cb_API_key, cb_secret) # this gets used to gain access to my account data

total = 0 # total blance is set to zero
message = [] # meesage is blank

try: # try except
    accounts = client.get_accounts() # this creates the variable from my account that will acrape the data from my coinbasea account
    for wallet in accounts.data: # enter loop that goes through every coin
        value = str(wallet['native_balance']).replace('USD ', '') # value is set to that in my wallet
        if '0.00' in value: # only prints the coins I own
            value = '0'
        else:
            message.append(str(wallet['name']) + ' ' + str(wallet['native_balance']))
        total += float(value) # adds the value of each to the total
    message.append('Total Balance: ' + 'USD ' + str(total)) # creates the total message
    print('\n'.join(message)) # prints each value

except AuthenticationError: # if my keys work this would get set off
    print('Could not authenticate with your coinbase API.')



