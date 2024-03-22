import requests

class Crypto:

    def __init__(self, name):
        self.url = f"https://api.finage.co.uk/agg/crypto/prev-close/{name}?apikey=API_KEY7eGAVOS66ZIGBJ4T1MD5FX2FF5GG0YIH"
        self.open = None
        self.close = None
        
    def get(self):
        r = requests.get(self.url)
        response = r.json()
        #check to make sure I got a question, i.e. results

        if response.get('results'):
            self.open = response['results'][0]['o']
            self.close = response['results'][0]['c']
            return response['results']
        else:
            return None

        