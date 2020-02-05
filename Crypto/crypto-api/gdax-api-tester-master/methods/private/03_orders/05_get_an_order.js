/**
 * Get an Order
 *
 * https://docs.gdax.com/#get-an-order
 */

var authedClient = require('../../../client').authedClient;
var async = require('async');


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

    authedClient.getOrder(orderId, function(err, response, order) {
      if (err) {
        console.log(err);
        return;
      }
      console.log(order);
    });
  }
]);