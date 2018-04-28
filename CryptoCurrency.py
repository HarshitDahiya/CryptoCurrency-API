from flask import Flask, render_template
import json,requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.coinmarketcap.com/v1/ticker/?start=0&limit=100')
    print('Response Code:: %s \n \n' %(response))

    json_str=response.json()
    rows=json_str
    for currency in range(len(json_str)):
        print("\nCurrency Name : ",json_str[currency]['name'])
        print("Currency Price : ",json_str[currency]['price_usd'])
    return render_template('Index.html',rows=rows)

if __name__=='__main__':
    app.run(debug = True,port=5000)
