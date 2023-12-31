from django.shortcuts import render
from .models import Cryptocurrency
import requests


def update_list():
    all_coins = Cryptocurrency.objects.all()
    for coin in all_coins:
        url = f'https://api.bybit.com/v2/public/tickers?symbol={coin.symbols}USD'
        response = requests.get(url)
        data = response.json()
        if data['result']:
            ticker_data = data['result'][0]
            coin.symbols = ticker_data['symbol']
            coin.price = float(ticker_data['bid_price'])
            coin.volume = float(ticker_data['volume_24h'])
            coin.save()


def home(request):
    update_list()
    all_coins = Cryptocurrency.objects.order_by('-price')
    context = {
        'coins': all_coins
    }
    return render(request, 'pages/home.html', context)