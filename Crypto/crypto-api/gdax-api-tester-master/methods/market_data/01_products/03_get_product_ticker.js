/**
 * Get Product Ticker
 *
 * https://docs.gdax.com/#get-product-ticker
 */

var publicClient = require('../../../client').publicClient;


publicClient.getProductTicker(function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});