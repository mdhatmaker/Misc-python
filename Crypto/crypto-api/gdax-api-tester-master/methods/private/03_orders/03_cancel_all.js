/**
 * Cancel All
 *
 * https://docs.gdax.com/#cancel-all
 */

var authedClient = require('../../../client').authedClient;


authedClient.cancelOrders(function(err, response, result) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(result);
});
