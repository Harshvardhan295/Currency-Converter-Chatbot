from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    
    source_currency = data['queryResult']['parameters']['unit-currency'][0]['currency']
    amount = data['queryResult']['parameters']['unit-currency'][0]['amount']
    target_currency = data['queryResult']['parameters']['currency-name'][0]

    print("Source:", source_currency)
    print("Amount:", amount)
    print("Target:", target_currency)
#https://api.currencyapi.com/v3/latest?apikey=cur_live_RtTVIW1b3viRrJxH0nQmgPKFkEcHnQLxPdud2MQi
    # Fetch conversion rates using source_currency as base
    def fetch_conversion_factor(source, target):
        url = f"https://api.currencyapi.com/v3/latest?apikey=cur_live_RtTVIW1b3viRrJxH0nQmgPKFkEcHnQLxPdud2MQi&base_currency={source}"
        response = requests.get(url)
        response_json = response.json()
        try:
            rate = response_json['data'][target]['value']
            print(f"Conversion Rate: 1 {source} = {rate} {target}")
            return rate
        except KeyError:
            print("Error: Target currency not found in API response.")
            return None

    conversion_rate = fetch_conversion_factor(source_currency, target_currency)

    if conversion_rate is None:
        return jsonify({
            "fulfillmentText": "Sorry, I couldn't fetch the conversion rate. Please try again."
        })

    converted_amount = round(amount * conversion_rate, 2)
    
    print(f"Converted Amount: {converted_amount} {target_currency}")

    return jsonify({
        "fulfillmentText": f"{amount} {source_currency} is approximately {converted_amount} {target_currency}."
    })


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
