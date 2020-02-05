/**
 * Place a New Order
 *
 * https://docs.gdax.com/#place-a-new-order
 */

var authedClient = require('../../../client').authedClient;


// Example buy - Buy 1 BTC @ $100 USD
var args = {
  price: '100.00', // USD
  size: '0.01',  // BTC
  product_id: 'BTC-USD'
};

authedClient.buy(args, function(err, response, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});


// Example sell - Sell 1 BTC @ $100 USD
// var args = {
//   price: '100.00', // USD
//   size: '0.01',  // BTC
//   product_id: 'BTC-USD'
// };

// authedClient.sell(args, function(err, response, data) {
//   if (err) {
//     console.log(err);
//     return;
//   }

//   console.log(data);
// });