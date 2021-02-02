# Import libraries
import tweepy
import requests
import json
import time
import api_data


# Authentication
auth_handler = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=SECRET_KEY)
auth_handler.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# To avoid spamming
api = tweepy.API(auth_handler, wait_on_rate_limit=True)

print("Logged In..")

def tweet_eth_price():

    # Get Ethereum Price from coingecko
    ethprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true')
    price = ethprice.json()

    # Current price
    ethusd = price['ethereum']['usd']

    # Market cap
    eth_mc = price['ethereum']['usd_market_cap']

    # 24 Hour volume
    eth_24h_vol = price['ethereum']['usd_24h_vol']

    # 24 Hour price change
    eth_24h_change = price['ethereum']['usd_24h_change']

    # Tweet message
    message = ' ETH Price:        $'+ str(ethusd) +' USD' '\n ETH Market Cap:   $'+ str(round(eth_mc, 2)) + 'USD' '\n ETH 24hr Volume:  $' + str(round(eth_24h_vol, 2)) + 'USD' '\n ETH 24hr Change:  $' + str(round(eth_24h_change,3)) + 'USD'
    print(message)

    # Tweet the message
    api.update_status(message)

    print("Tweet posted successfully!")

    # Sleep for 3 hours
    time.sleep(5*60*60)

    return print(message)

# Let the bot run forever
while True:
    tweet_eth_price()
