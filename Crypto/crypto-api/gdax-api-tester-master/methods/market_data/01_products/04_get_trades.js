/**
 * Get Trades
 *
 * https://docs.gdax.com/#get-trades
 */

var publicClient = require('../../../client').publicClient;


publicClient.getProductTrades({after: 1000}, function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});