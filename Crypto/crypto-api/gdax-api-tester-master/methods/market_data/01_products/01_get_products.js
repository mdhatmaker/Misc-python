/**
 * Get Products
 *
 * https://docs.gdax.com/#get-products
 */

var publicClient = require('../../../client').publicClient;


publicClient.getProducts(function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});