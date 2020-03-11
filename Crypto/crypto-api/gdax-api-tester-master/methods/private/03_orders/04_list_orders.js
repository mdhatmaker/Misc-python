/**
 * List Orders
 *
 * https://docs.gdax.com/#list-orders
 */

var authedClient = require('../../../client').authedClient;


authedClient.getOrders(function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});

// For pagination, you can include extra page arguments
// authedClient.getOrders({after: 3000}, function(err, response, data) {
//   if (err) {
//     console.log(err);
//     return;
//   }
//
//   console.log(data);
// });