/**
 * Get currencies
 *
 * https://docs.gdax.com/#get-currencies
 */

var publicClient = require('../../../client').publicClient;


publicClient.getCurrencies(function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});