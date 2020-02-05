/**
 * Websocket - connect
 *
 * https://docs.gdax.com/#websocket-feed
 */

var Gdax = require('gdax');
var websocket = new Gdax.WebsocketClient(['BTC-USD', 'ETH-USD']);
websocket.on('message', function(data) { console.log(data); });