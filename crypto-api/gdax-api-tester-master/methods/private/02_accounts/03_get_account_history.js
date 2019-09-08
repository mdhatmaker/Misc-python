/**
 * Get Account History
 *
 * https://docs.gdax.com/#get-account-history
 */

var async = require('async');
var authedClient = require('../../../client').authedClient;


async.waterfall([
  function(callback) {

    authedClient.getAccounts(function(err, response, accounts) {
      if (err) {
        console.log(err);
        return;
      }

      callback(null, accounts[0].id);
    });

  }, function(accountId) {

    authedClient.getAccountHistory(accountId, function(err, response, data) {
      if (err) {
        console.log(err);
        return;
      }

      if (data.length) {
        console.log(data);
      } else {
        console.log('No account activity');
      }
    });
  }
]);