import requests
import json


def get_newsapi_results(query):
    # Define the endpoint
    url = 'https://newsapi.org/v2/everything?'
    # Specify the query and number of returns
    # try:
    #     with open('env-config.json', 'r') as config_file:
    #         config_data = json.load(config_file)
    #         newsapi_secret_key = config_data['news_api_token']
    # except FileNotFoundError:
    #     return "File not found"

    parameters = {
        'q': query,  # query phrase
        'pageSize': 20,  # maximum is 100
        'apiKey': ""  # your own API key
    }
    # Make the request
    response = requests.get(url, params=parameters)

    return response
