/**
 * Get 24hr Stats
 *
 * https://docs.gdax.com/#get-24hr-stats
 */

var publicClient = require('../../../client').publicClient;


publicClient.getProduct24HrStats(function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});