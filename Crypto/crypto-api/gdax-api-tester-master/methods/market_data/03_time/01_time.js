/**
 * Time
 *
 * https://docs.gdax.com/#time
 */

var publicClient = require('../../../client').publicClient;


publicClient.getTime(function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});