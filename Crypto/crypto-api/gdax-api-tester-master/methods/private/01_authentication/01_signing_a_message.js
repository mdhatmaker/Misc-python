/**
 * Signing a Message
 *
 * https://docs.gdax.com/#signing-a-message
 */

 var crypto = require('crypto');

 var secret = 'PYPd1Hv4J6/7x...';

 var timestamp = Date.now() / 1000;
 var requestPath = '/orders';

 var body = JSON.stringify({
     price: '1.0',
     size: '1.0',
     side: 'buy',
     product_id: 'BTC-USD'
 });

 var method = 'POST';

 // create the prehash string by concatenating required parts
 var what = timestamp + method + requestPath + body;

 // decode the base64 secret
 var key = Buffer(secret, 'base64');

 // create a sha256 hmac with the secret
 var hmac = crypto.createHmac('sha256', key);

 // sign the require message with the hmac
 // and finally base64 encode the result
 var result = hmac.update(what).digest('base64');

 console.log('Prehash string:', what);
 console.log('Result:', result);