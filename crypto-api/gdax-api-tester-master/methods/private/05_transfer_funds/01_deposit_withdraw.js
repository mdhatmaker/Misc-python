/**
 * Deposit/Withdraw (deprecated)
 *
 * https://docs.gdax.com/#depositwithdraw
 */

var authedClient = require('../../../client').authedClient;


var params = {
  amount: 0.008,
  currency: 'BTC',
  crypto_address: '13jGj9ApoakHwKes3DXVXKaUb9FchH9Qe5'
};

authedClient.newWithdraw(params, function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});


// When transfer was checked by "bypass 2FA" was NOT checked. Correct and safe.
// { message: 'Two factor authentication is enabled, please include `two_factor_code` in your request' }

