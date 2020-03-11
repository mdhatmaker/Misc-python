/**
 * List Accounts
 *
 * https://docs.gdax.com/#list-accounts
 */

var authedClient = require('../../../client').authedClient;


authedClient.getAccounts(function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});