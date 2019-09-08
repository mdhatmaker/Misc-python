# GDAX API Tester

This repo provides examples of how to use the official [GDAX NodeJS client library](https://github.com/coinbase/gdax-node) and allows for quick and easy testing of GDAX API endpoints.

**_Please use only with the [GDAX Sandbox](https://public.sandbox.gdax.com/). These files are intended as examples only and may contain undesirable actions such as buys and sells at undesirable prices!_**

## Instructions

1. git clone https://github.com/jborseth/gdax-api-tester.git
2. cd gdax-api-tester
3. npm install
4. Create an new API key, secret, and passphrase at https://public.sandbox.gdax.com/settings/api
2. Edit client.js to add your new API key, secret, and passphrase
3. Change into the `methods` directory and run the file for the method you want
to call. The response will be logged to the console. For example:

  ```
  cd methods
  node market_data/products/01_get_products.js
  ```

## License & Disclaimer

The code is released under the MIT License. It may be subtly broken or buggy. Please take the following message to heart:

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.