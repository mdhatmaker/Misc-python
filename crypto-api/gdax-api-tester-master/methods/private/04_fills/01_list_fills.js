/**
 * List Fills
 *
 * https://docs.gdax.com/#list-fills
 */

var authedClient  = require('../../../client.js').authedClient;


authedClient.getFills(function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});