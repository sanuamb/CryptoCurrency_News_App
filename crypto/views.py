from django.shortcuts import render
import requests
import json

# Create your views here.

def home(request):

    #Get crypto price data
    price_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,LTC,EOS,BCH,XLM,USDT,TRX&tsyms=USD")
    price=json.loads(price_request.content)

    # Get crypto news data
    api_request=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_request.content)
    return render(request,'home.html',{'api':api,'price':price})

def prices(request):

    if request.method=='POST':
        quote = request.POST['quote']
        quote=quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request,'prices.html',{'quote':quote,'crypto':crypto})
    else:
        return render(request,'prices.html',{})

