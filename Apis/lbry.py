# Welcome to the LBRY wrapper for Python.

# https://github.com/simonstead/lbry-python


import lbry



dir(lbry)


r = lbry.claim_list("princess-bubblegum")
print(r)

#r = lbry.wallet_balance(address=<address>)
#print(r)

