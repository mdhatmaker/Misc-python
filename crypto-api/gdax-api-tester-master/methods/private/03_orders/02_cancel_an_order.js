/**
 * Cancel an Order
 *
 * https://docs.gdax.com/#cancel-an-order
 */

var async = require('async');
var authedClient = require('../../../client').authedClient;


async.waterfall([
  function(callback) {

    authedClient.getOrders(function(err, response, orders) {
      if (err) {
        console.log(err);
        return;
      }

      if (orders.length === 0) {
        console.log('You have no orders');
        return;
      }

      callback(null, orders[0].id);
    });

  }, function(orderId) {

    // Alternatively, you can manually specify an order ID here
    // var orderId = '';

    authedClient.cancelOrder(orderId, function(err, response, result) {
      if (err) {
        console.log(err);
        return;
      }

      console.log(result);
    });
  }
]);