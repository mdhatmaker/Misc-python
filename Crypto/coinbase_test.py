from coinbase.wallet.client import Client

# ---AUTHENTICATE---
client = Client(
    "amD6R28mVJeqHC2p",                         # api key
    "AtoQ9r4k8wDxboflZsXIjhqQCmNkJlZe",         # api secret
    api_version='2017-11-14')

# ---LIST WALLETS AND TRANSACTIONS---
accounts = client.get_accounts()
for account in accounts.data:
  balance = account.balance
  print "%s: %s %s" % (account.name, balance.amount, balance.currency)
  #print account.get_transactions()

# ---CREATE A NEW WALLET---
account = client.create_account(name="API Wallet")
balance = account.balance
print "%s: %s %s" % (account.name, balance.amount, balance.currency)

