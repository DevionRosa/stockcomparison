import requests

class Forex:

    def __init__(self, name):
        self.url = f"https://api.polygon.io/v2/aggs/ticker/C:{name}/prev?adjusted=true&apiKey=wW_ta6la5WhHJhwOHzDFAu2T5jjAk2cD"
        self.open = None
        self.close = None
        
    def get(self):
        r = requests.get(self.url)
        #response is just a json dictonary of values after .json() call
        response = r.json()
        #check to make sure I got a question, i.e. results

        if response.get('results'):
            self.open = response['results'][0]['o']
            self.close = response['results'][0]['c']
            return response['results']
        else:
            return None