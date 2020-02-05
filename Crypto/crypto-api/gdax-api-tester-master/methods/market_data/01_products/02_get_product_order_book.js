/**
 * Get Product Order Book
 *
 * https://docs.gdax.com/#get-product-order-book
 */

var publicClient = require('../../../client').publicClient;

publicClient.getProductOrderBook({level: 3}, function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});