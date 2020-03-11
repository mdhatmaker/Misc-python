/**
 * Get Historic Rates
 *
 * https://docs.gdax.com/#get-historic-rates
 */

var publicClient = require('../../../client').publicClient;


publicClient.getProductHistoricRates(function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});


// Alternatively, you can include extra parameters if needed
// publicClient.getProductHistoricRates({granularity: 3000}, function(err, response) {
//   if (err) {
//     console.log(err);
//     return;
//   }
//
//   console.log(response.body);
// });