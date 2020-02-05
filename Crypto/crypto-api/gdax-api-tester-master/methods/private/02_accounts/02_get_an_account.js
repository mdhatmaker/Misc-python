/**
 * Get an Account
 *
 * https://docs.gdax.com/#get-an-account
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

    authedClient.getAccount(accountId, function(err, response, data) {
      if (err) {
        console.log(err);
        return;
      }

      console.log(data);
    });

  }
]);